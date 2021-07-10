#!/bin/bash
helm upgrade datadog-agent -f datadog-values-gke.yaml --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog