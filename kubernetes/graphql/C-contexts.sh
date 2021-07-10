#!/bin/sh
#kubectl config get-contexts                          # display list of contexts 
#kubectl config current-context                       # display the current-context
#kubectl config use-context my-cluster-name           # set the default context to my-cluster-name
kubectl config current-context  
kubectl config get-contexts