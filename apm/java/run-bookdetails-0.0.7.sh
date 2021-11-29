#!/bin/sh
# export JAVA_HOME=/Library/Java/JavaVirtualMachines/zulu-8.jdk/Contents/Home
# ${JAVA_HOME}/bin/java -javaagent:/Users/lloyd.williams/u01/datadog/dd-java-agent.jar \

java -javaagent:dd-java-agent.jar \
  -Ddd.trace.methods="com.graphqljava.tutorial.bookdetails.GraphQLDataFetchers[getBookByIdDataFetcher,getAuthorDataFetcher];com.graphqljava.tutorial.bookdetails.GraphQLProvider[buildWiring]" \
  -Ddd.tags=source:bookdetails,service:bookdetails,env:dev,version:0.0.7 \
  -Ddd.logs.injection=true \
  -Dlog4j.configurationFile=log4j.properties -jar ./book-details-0.0.7.jar

