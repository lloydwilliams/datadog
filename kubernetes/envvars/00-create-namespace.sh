#!/bin/sh
kubectl create namespace envars

echo setting the current context default namespace to envars 
kubectl config set-context --current --namespace envars

