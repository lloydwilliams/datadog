#!/bin/sh
java -javaagent:./dd-java-agent.jar -Ddd.profiling.enabled=false -Ddd.logs.injection=true -Ddd.service=payroll -Ddd.env=dev -Ddd.version=0.0.2 -jar target/payroll-0.0.2.jar