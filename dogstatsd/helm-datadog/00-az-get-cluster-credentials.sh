#!/bin/sh

echo 'Getting Azure K8S Cluster Credentials:'
az aks get-credentials --resource-group lloyd-resource-group --name lloyd-aks-dogstatsd-udp

