#!/bin/bash

# Requirements - may need to open firewall for these URLs
#Repository	Name	
#https://helm.datadoghq.com	datadog-crds	
#https://kubernetes.github.io/kube-state-metrics	kube-state-metrics

#Download the datadog-values.yaml configuration file.
#Deploy the Datadog Agent with:
#helm install RELEASE_NAME -f datadog-values.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog 

# -----
# make sure your environment has the values for $DATADOG_API_KEY and $DATADOG_APP_KEY
#export DATADOG_API_KEY=
#export DATADOG_APP_KEY=
# -----
helm install datadog-agent -f datadog-values-gke.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY --set datadog.appKey=$DATADOG_APP_KEY --create-namespace=true datadog/datadog 
#https://helm.sh/docs/helm/helm_install/
#--insecure-skip-tls-verify     skip tls certificate checks for the chart download