#!/bin/sh
wget --no-check-certificate -O dd-java-agent.jar https://dtdg.co/latest-java-tracer

sleep 10

java -jar dd-java-agent.jar