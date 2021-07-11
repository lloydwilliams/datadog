#!/bin/bash

# Using variables from env for keys
helm install datadog-operator -f datadog-operator-values.yaml --set datadog.apiKey=$DATADOG_API_KEY --set datadog.appKey=$DATADOG_APP_KEY datadog/datadog-operator