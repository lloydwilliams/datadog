#!/bin/sh
kubectl config set-context --current --namespace datadog
helm upgrade datadog-agent -f datadog-values.yaml --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog