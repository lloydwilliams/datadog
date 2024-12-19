#!/bin/sh

export JAVA_HOME=/Library/Java/JavaVirtualMachines/zulu-17.jdk/Contents/Home

#$JAVA_HOME/bin/java -jar dogstatsd17-1.0.1.jar

$JAVA_HOME/bin/java -jar dogstatsd17-1.0.1-jar-with-dependencies.jar
