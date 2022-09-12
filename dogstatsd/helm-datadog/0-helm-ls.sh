#!/bin/sh
#mac
#brew install helm

#add repos
#helm repo add stable https://charts.helm.sh/stable

#helm ls              # see what has been released using Helm

#helm list -n datadog
#helm list -n kafka

helm list --all --all-namespaces
