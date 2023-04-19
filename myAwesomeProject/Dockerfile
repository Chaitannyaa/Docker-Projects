# Use an OpenJDK base image with version 11
FROM openjdk:21-slim-buster

# Set the working directory to /app
WORKDIR /app
COPY . .

# Copy the Spring Boot executable JAR file into the container at /app
COPY target/myAwesomeProject-0.0.1-SNAPSHOT.jar /app

# Expose port 8080 for the container to listen on
EXPOSE 8080

# Set the entry point to run the Spring Boot executable JAR file
ENTRYPOINT ["java", "-jar", "myAwesomeProject-0.0.1-SNAPSHOT.jar"]
