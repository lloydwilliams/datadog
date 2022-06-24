#!/bin/bash
kubectl create namespace datadog

echo setting the context to lloyd-k8s-ndm and default namespace to datadog 
kubectl config set-context --current --namespace datadog
