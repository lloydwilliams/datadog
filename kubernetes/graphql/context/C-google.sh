#!/bin/sh
#kubectl config get-contexts                          # display list of contexts 
#kubectl config current-context                       # display the current-context
#kubectl config use-context my-cluster-name           # set the default context to my-cluster-name
kubectl config get-contexts

sleep 2

kubectl config use-context gke_datadog-sandbox_northamerica-northeast1_lloyd-gke-cluster2           

sleep 4

kubectl config get-contexts

echo 'The current context is:'

kubectl config current-context  
