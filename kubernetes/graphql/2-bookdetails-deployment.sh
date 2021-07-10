#!/bin/sh
kubectl config set-context --current --namespace graphql
kubectl apply -f bookdetails-deployment.yaml