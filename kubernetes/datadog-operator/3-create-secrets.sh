#!/bin/sh
## make sure your environment has the values for $DATADOG_API_KEY and $DATADOG_APP_KEY before running this command
#kubectl create secret generic datadog-secret --from-literal api-key=${DATADOG_API_KEY} --from-literal app-key=${DATADOG_APP_KEY}
kubectl config set-context --current --namespace datadog
kubectl create secret generic datadog-secret --from-literal=api-key=${DATADOG_API_KEY} --from-literal=app-key=${DATADOG_APP_KEY} --namespace="datadog"
