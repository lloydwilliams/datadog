#!/bin/sh
java -javaagent:/dd-java-agent.jar -XX:FlightRecorderOptions=stackdepth=256 -jar /app.jar