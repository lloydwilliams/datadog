#FROM openjdk:8-jdk-alpine
FROM openjdk:8u292-slim-buster
ADD https://dtdg.co/latest-java-tracer /dd-java-agent.jar
RUN apt-get update && apt-get install -y procps
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar
COPY ./target/start.sh /start.sh
RUN chmod a+rx /start.sh
CMD ["sh", "/start.sh"]