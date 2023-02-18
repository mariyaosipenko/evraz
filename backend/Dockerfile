# Compile stage
FROM golang:1.19 AS build-env

ADD . /backend
WORKDIR /backend

RUN go build -o /server

# Final stage
FROM debian:buster

EXPOSE 8000

WORKDIR /
COPY --from=build-env /server /

CMD ["/server"]