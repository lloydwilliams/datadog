#!/bin/bash

echo setting the current context default namespace to datadog 
kubectl config set-context --current --namespace datadog

helm upgrade datadog-agent -f datadog-values-aks.yaml --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog