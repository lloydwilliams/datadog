#!/bin/sh
#remove the components
kubectl config set-context --current --namespace confluent
kubectl delete -f ./producer-app-data.yaml