#!/bin/sh
kubectl config set-context --current --namespace datadog
#helm upgrade datadog-agent -f datadog-values-gke.yaml --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog
helm upgrade datadog-agent -f datadog-values-gke.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY --set datadog.appKey=$DATADOG_APP_KEY datadog/datadog