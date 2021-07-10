FROM tomcat:9-jdk11-slim
ADD https://dtdg.co/latest-java-tracer /dd-java-agent.jar
RUN apt-get update && apt-get install -y procps
ENV DD_SERVICE="tomcat"
ENV DD_VERSION="9.0.21"
ENV CATALINA_OPTS="-javaagent:/dd-java-agent.jar -XX:FlightRecorderOptions=stackdepth=256"