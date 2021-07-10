#!/bin/sh
kubectl config set-context --current --namespace graphql
kubectl delete -f bookdetails-deployment.yaml
#kubectl delete pods,services -l name=bookdetails-deployment
kubectl delete service bookdetails-deployment
