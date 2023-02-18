# Compile stage
FROM java:11 AS build-env

ADD . /consumer
WORKDIR /consumer

COPY .mvn/ .mvn
COPY mvnw pom.xml ./
RUN ./consumer dependency:resolve

COPY src ./src

CMD ["./consumer", "spring-boot:run"]

# Final stage
FROM debian:buster

EXPOSE 8000

WORKDIR /
COPY --from=build-env /server /

CMD ["/server"]