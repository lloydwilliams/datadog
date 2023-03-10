#!/bin/sh

##java -javaagent:/Users/lloyd.williams/u01/datadog/dd-java-agent.jar \
## -Ddd.profiling.enabled=true -XX:+UnlockCommercialFeatures -XX:+FlightRecorder \
## -Ddd.trace.methods=com.example.payroll.EmployeeController[*] \
## -Ddd.logs.injection=true -Ddd.appsec.enabled=false \

#java -javaagent:/Users/lloyd.williams/u01/datadog/dd-java-agent.jar \
# -Ddd.service=gates -Ddd.env=dev -Ddd.version=1.0.1 -Duser.timezone=UTC -jar target/gates-1.0.1.jar

java -Duser.timezone=UTC -jar gates-1.0.1.jar