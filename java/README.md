# Datadog for Java

[Oracle Java](https://www.oracle.com/java/) is the #1 programming language and development platform. 

## Java SDK

[Java SDK Downloads](https://www.oracle.com/java/technologies/downloads/) 

## Spring Boot

[Spring](https://spring.io/) is a framework by [VMWare Tanzu](https://tanzu.vmware.com/spring-app-framework).

The [Spring Boot](https://spring.io/projects/spring-boot) project makes it easy to create stand-alone, production-grade Spring based Applications that you can "just run".

The [Spring Initializr](https://start.spring.io/) can help you get started. 

This is an example of a [Spring Boot application](https://github.com/lloydwilliams/datadog/tree/main/kubernetes/payroll/eclipse-workspace/payroll) for Java 8. 

## Datadog APM

Any application packaged into a .jar file (such as a Spring Boot application) can be easily traced using the [Datadog tracing library available on GitHub](https://github.com/DataDog/dd-trace-java) by [adding the java tracer to the VM using -javaagent](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java/?tab=springboot#add-the-java-tracer-to-the-jvm). 

You can easily get the latest version of the Datadog Java Trace library by running the command:

```
wget --no-check-certificate -O dd-java-agent.jar https://dtdg.co/latest-java-tracer
```

or check the version that you have using:

```
get-new-dd-java-agent.sh
```

You might want to put this in a script that you can run periodically to get the latest version because new features of the Java Trace Library are released on a regular basis. 

For example:

```
java -javaagent:/u01/datadog/dd-java-agent.jar -XX:+UnlockCommercialFeatures -XX:+FlightRecorder \
 -Ddd.trace.methods=com.example.payroll.EmployeeController[*] \
 -Ddd.profiling.enabled=true -Ddd.logs.injection=true -Ddd.appsec.enabled=true \
 -Ddd.service=payroll -Ddd.env=dev -Ddd.version=3.0.1 -Duser.timezone=UTC -jar target/payroll-3.0.1.jar
```

There are many options that you can choose to set documented in the Datadog documenation for [Tracing Java Applications](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java/?tab=springboot).

![001-run-payroll](images/001-run-payroll.png)

This application is a microservice which opens port 8080 to accept [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) API calls.

You can run a [cURL command](https://blog.hubspot.com/website/curl-command) 

```
curl --location --request POST 'localhost:8080/employees' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Samwise Gamgee",
    "role": "gardener"
}'
```

or use a popular tool like [Postman](https://www.postman.com/downloads/) to make the API call. 

![002-postman](images/002-postman.png)

Datadog APM will trace each call to the application and automatically generate spans for [certain types of activities](https://docs.datadoghq.com/tracing/trace_collection/compatibility/java/#networking-framework-compatibility) such as JDBC calls to a database. 

Notice that you can also configure the application to [inject the trace id into the logs](https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/java). This makes it very easy to see the logs related to this one specifc call without having to switch to a different tool. 

![payroll-trace](images/003-payroll-trace.png)



