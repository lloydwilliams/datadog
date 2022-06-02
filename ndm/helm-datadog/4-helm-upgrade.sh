#!/bin/sh

helm upgrade datadog-agent -f datadog-values-1.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog