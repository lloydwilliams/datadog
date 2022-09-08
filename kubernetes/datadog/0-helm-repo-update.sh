#!/bin/bash
#https://app.datadoghq.com/account/settings#agent/kubernetes

#Install Helm.
#(e.g. brew install helm)
#Add Datadog Helm repository: 
# helm repo add datadog https://helm.datadoghq.com

#Add stable repository (for kube-state-metrics chart): 
#helm repo add stable https://charts.helm.sh/stable

#Fetch latest version of newly added charts: 
helm repo update