#!/bin/sh
kubectl config set-context --current --namespace tomcat
kubectl apply -f tomcat-deployment.yaml