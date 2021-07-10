#!/bin/sh
kubectl config set-context --current --namespace graphql
#GKE
#kubectl expose deployment bookdetails-deployment --port=80 --target-port=8080 --type LoadBalancer

#minikube
kubectl expose deployment bookdetails-deployment --type=NodePort --port=8080

#kubectl describe svc bookdetails-deployment

#kubectl get svc
kubectl get service bookdetails-deployment

echo 'use GraphQL Playground http://localhost:8180/graphql'
kubectl port-forward $(kubectl get pod --selector="app=bookdetails-deployment" --output jsonpath='{.items[0].metadata.name}') 8180:8080


