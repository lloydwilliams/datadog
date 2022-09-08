#!/bin/bash
echo setting the current context default namespace to datadog 
kubectl config set-context --current --namespace datadog 
 
# https://github.com/DataDog/helm-charts/tree/master/charts/datadog#all-configuration-options
 
#Download the datadog-values.yaml configuration file.
#Deploy the Datadog Agent with:

#helm install RELEASE_NAME -f datadog-values.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog 
helm install datadog-agent -f datadog-values-aks.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY --set datadog.appKey=$DATADOG_APP_KEY --create-namespace=true datadog/datadog 