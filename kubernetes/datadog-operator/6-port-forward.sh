#!/bin/sh
gcloud container clusters get-credentials lloyd-gke-cluster2 --region northamerica-northeast1 --project datadog-sandbox \
 && kubectl port-forward --namespace datadog $(kubectl get pod --namespace datadog --selector="app.kubernetes.io/instance=my-datadog-operator,app.kubernetes.io/name=datadog-operator" --output jsonpath='{.items[0].metadata.name}') 8383:8383

echo 'my-datadog-operator metrics are exposed at http://localhost:8383/metrics'