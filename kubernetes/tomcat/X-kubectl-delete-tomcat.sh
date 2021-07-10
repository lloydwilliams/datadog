#!/bin/sh
kubectl config set-context --current --namespace tomcat
kubectl delete -f tomcat-deployment.yaml
#kubectl delete pods,services -l name=my-tomcat-deployment

kubectl delete service my-tomcat-deployment
#kubectl delete service test-tomcat-deployment