package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/jackc/pgx/v4/pgxpool"
)

type Signal struct {
	Signal_id int64  `json:"signal_id"`
	Typename  string `json:"typename"`
}

type getSignalsResponse struct {
	Signals []Signal `json:"signals"`
}

func main() {
	// Set the flags for the logging package to give us the filename in the logs
	log.SetFlags(log.LstdFlags | log.Lshortfile)

	dbPool := getDBConnection(context.Background())
	defer dbPool.Close()

	log.Println("starting server...")
	http.HandleFunc("/signal", signalHandler(dbPool))
	log.Fatal(http.ListenAndServe(":8000", nil))
}

func signalHandler(db *pgxpool.Pool) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		rows, err := db.Query(context.Background(), "SELECT * FROM signal;")
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			log.Printf("error: %v\n", err.Error())
			return
		}
		defer rows.Close()

		var signals []Signal

		for rows.Next() {
			var sig Signal
			if err := rows.Scan(&sig.Signal_id, &sig.Typename); err != nil {
				w.WriteHeader(http.StatusInternalServerError)
				log.Printf("error: %v\n", err.Error())
				return
			}
			signals = append(signals, sig)
		}
		if err = rows.Err(); err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			log.Printf("error: %v\n", err.Error())
			return
		}
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)
		var response getSignalsResponse
		response.Signals = make([]Signal, len(signals))
		for i := range signals {
			response.Signals[i] = signals[i]
		}
		body, err := json.Marshal(response)
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			log.Printf("error: %v\n", err.Error())
			return
		}

		if _, err = w.Write(body); err != nil {
			log.Printf("failed to write response body")
		}
	}
}

func getDBConnection(ctx context.Context) *pgxpool.Pool {
	// Retrieve the database host address
	host := os.Getenv("DD_DB_HOST")
	if host == "" {
		host = "127.0.0.1"
	}

	const connectionString = "postgres://goland:goland@%s:5432/goland?sslmode=disable"

	// Try connecting to the database a few times before giving up
	// Retry to connect for a while
	var dbPool *pgxpool.Pool
	var err error
	for i := 1; i < 8; i++ {
		log.Printf("trying to connect to the db server (attempt %d)...\n", i)
		dbPool, err = pgxpool.Connect(ctx, fmt.Sprintf(connectionString, host))
		if err == nil {
			break
		}
		log.Printf("got error: %v\n", err)

		// Sleep a bit before trying again
		time.Sleep(time.Duration(i*i) * time.Second)
	}

	// Stop execution if the database was not initialized
	if dbPool == nil {
		log.Fatalln("could not connect to the database")
	}

	// Get a connection from the pool and check if the database connection is active and working
	db, err := dbPool.Acquire(ctx)
	if err != nil {
		log.Fatalf("failed to get connection on startup: %v\n", err)
	}
	if err := db.Conn().Ping(ctx); err != nil {
		log.Fatalln(err)
	}

	// Add the connection back to the pool
	db.Release()

	return dbPool
}
