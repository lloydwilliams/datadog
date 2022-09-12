#!/bin/sh
#Download the datadog-values.yaml configuration file. Run: V-values.sh to get the file.
#Make the appropriate changes to the file.
#Deploy the Datadog Agent with:
helm install datadog-agent -f datadog-values.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog 