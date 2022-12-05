#!/bin/sh
kubectl config set-context --current --namespace payroll
#GKE
#kubectl expose deployment bookdetails-deployment --port=80 --target-port=8080 --type LoadBalancer

#minikube
kubectl expose deployment payroll --type=NodePort --port=8080

#kubectl describe svc bookdetails-deployment

#kubectl get svc
kubectl get service payroll

echo 'Post to localhost:8080/employees'
echo 'Example: { "name": "Samwise Gamgee", "role": "gardener" }'
kubectl port-forward $(kubectl get pod --selector="app=payroll" --output jsonpath='{.items[0].metadata.name}') 8080:8080


