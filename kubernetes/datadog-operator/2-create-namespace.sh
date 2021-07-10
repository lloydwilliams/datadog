#!/bin/bash
kubectl create namespace datadog

echo setting the current context default namespace to datadog 
kubectl config set-context --current --namespace datadog

