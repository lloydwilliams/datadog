#!/bin/sh

helm upgrade datadog-agent -f datadog-values.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog