#!/bin/sh
kubectl config set-context --current --namespace datadog
kubectl create secret generic datadog-secret --from-literal api-key=$DATADOG_API_KEY
kubectl create secret generic datadog-secret --from-literal app-key=$DATADOG_APP_KEY

#kubectl create secret generic datadog-auth-token --from-literal=token=<TOKEN_FROM_PREVIOUS_STEP>