#!/bin/sh
#runs the graphql example that returns information about books
cd /Users/lloyd.williams/u01/eclipse-workspaces/graphql/book-details

echo 'use GraphQL Playground with http://localhost:8080/graphql'
echo 'or run test.sh to test with curl'

# if using Oracle JDK add
# -XX:+UnlockCommercialFeatures -XX:+FlightRecorder
export JAVA_HOME=/Library/Java/JavaVirtualMachines/zulu-8.jdk/Contents/Home

${JAVA_HOME}/bin/java -javaagent:/Users/lloyd.williams/u01/datadog/dd-java-agent.jar \
  -Ddd.trace.methods="com.graphqljava.tutorial.bookdetails.GraphQLDataFetchers[getBookByIdDataFetcher,getAuthorDataFetcher];com.graphqljava.tutorial.bookdetails.GraphQLProvider[buildWiring]" \
  -Ddd.env=dev \
  -Ddd.service=bookdetails \
  -Ddd.version=2.2.0 \
  -Ddd.tags=source:bookdetails,owner:lloyd,demo:graphql \
  -Ddd.agent.host=localhost \
  -Ddd.logs.injection=true \
  -jar ./target/book-details-2.2.0.jar