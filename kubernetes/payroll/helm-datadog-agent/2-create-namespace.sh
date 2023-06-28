#!/bin/bash
kubectl create namespace datadog

echo setting the namespace to datadog 
kubectl config set-context --current --namespace datadog
