#!/bin/sh
java -javaagent:/Users/lloyd.williams/u01/datadog/dd-java-agent.jar -XX:+UnlockCommercialFeatures -XX:+FlightRecorder \
 -Ddd.trace.methods=com.example.payroll.EmployeeController[*] \
 -Ddd.profiling.enabled=true -Ddd.logs.injection=true -Ddd.appsec.enabled=true \
 -Ddd.service=payroll -Ddd.env=dev -Ddd.version=3.0.1 -Duser.timezone=UTC -jar target/payroll-3.0.1.jar