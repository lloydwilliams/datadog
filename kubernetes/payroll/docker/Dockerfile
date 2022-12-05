FROM eclipse-temurin:8u345-b01-jdk
ADD https://dtdg.co/latest-java-tracer /dd-java-agent.jar
RUN apt-get update && apt-get install -y procps
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar
COPY ./target/start.sh /start.sh
LABEL com.datadoghq.ad.logs: '[{"source": "java", "service": "payroll", "auto_multi_line_detection": true}]'
RUN mkdir /logs
RUN chmod a+rx /logs
RUN chmod a+rx /start.sh
CMD ["sh", "/start.sh"]