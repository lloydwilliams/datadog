#!/bin/sh
echo "Installing Bitnami Kong .... \n"

kubectl create namespace kong

helm install bitnami-kong bitnami/kong -f ./kong-values.yaml

#---
#    Access the Kong admin by using the following commands

 echo "Browse to http://127.0.0.1:8001"
 export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name:kong,app.kubernetes.io/instance:bitnami-kong" -o jsonpath="{.items[0].metadata.name}")

 kubectl port-forward pod/$POD_NAME 8001:8001 &

# The Kong Ingress Controller was deployed as part of the Kong pods. The following objects are available in the Kubernetes API:

#     kubectl get kongconsumers
#     kubectl get kongcredentials
#     kubectl get kongingresses
#     kubectl get kongplugins

#If you want to upgrade the installation you will need to re-set the database credentials. 
#Execute the following command
#kubectl get secret --namespace default bitnami-kong-postgresql -o jsonpath="{.data.postgresql-password}" | base64 --decode