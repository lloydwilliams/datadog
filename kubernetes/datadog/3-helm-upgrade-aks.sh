#!/bin/bash
helm upgrade datadog-agent -f datadog-values-aks.yaml --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog