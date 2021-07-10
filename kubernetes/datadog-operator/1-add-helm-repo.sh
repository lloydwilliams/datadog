#!/bin/sh
#mac
#brew install helm

#add repos
#helm repo add stable https://charts.helm.sh/stable
helm repo add datadog https://helm.datadoghq.com
helm install my-datadog-operator datadog/datadog-operator

#helm ls # see what has been released using Helm
helm list --all --all-namespaces
