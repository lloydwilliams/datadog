#!/bin/sh
#Download the datadog-values.yaml configuration file.
#Deploy the Datadog Agent with:

#helm install RELEASE_NAME -f datadog-values.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog 
kubectl config set-context --current --namespace datadog
helm install datadog-agent -f datadog-values.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog 