#!/bin/sh
kubectl create namespace tomcat

echo setting the current context default namespace to tomcat 
kubectl config set-context --current --namespace tomcat

