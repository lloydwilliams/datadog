#!/bin/sh
kubectl config set-context --current --namespace tomcat
#GKE
#kubectl expose deployment my-tomcat-deployment --port=80 --target-port=8080 --type LoadBalancer

#minikube
kubectl expose deployment my-tomcat-deployment --type=NodePort --port=8080

#kubectl describe svc my-tomcat-deployment

#kubectl get svc
kubectl get service my-tomcat-deployment

kubectl port-forward $(kubectl get pod --selector="app=my-tomcat-deployment" --output jsonpath='{.items[0].metadata.name}') 8280:8080

# echo 'go to http://localhost:8280/'
# curl http://localhost:8280/

#minikube service test-tomcat-deployment --url
# http://192.168.99.101:30822
