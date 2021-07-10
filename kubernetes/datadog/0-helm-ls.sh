#!/bin/sh
#mac
#brew install helm

#add repos
#helm repo add stable https://charts.helm.sh/stable

#helm ls              # see what has been released using Helm

#gcloud container clusters get-credentials lloyd-cluster --region=northamerica-northeast1
#
#helm list -n datadog
#helm list -n kafka

helm list --all --all-namespaces

# helm delete datadogn -n datadog
