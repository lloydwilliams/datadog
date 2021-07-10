#!/bin/bash
kubectl create namespace confluent

echo setting the current context default namespace to confluent 
kubectl config set-context --current --namespace confluent

