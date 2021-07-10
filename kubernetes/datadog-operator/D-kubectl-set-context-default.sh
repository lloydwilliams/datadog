#!/bin/sh
#kubectl create namespace datadog

echo setting the current context default namespace to default 
kubectl config set-context --current --namespace default
