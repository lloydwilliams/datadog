#!/bin/sh
kubectl create namespace graphql

echo setting the current context default namespace to graphql 
kubectl config set-context --current --namespace graphql

