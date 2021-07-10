#Edit the <CFK-home>/values.yaml file to customize the CFK configuration.

helm upgrade --install confluent-operator \
  confluentinc/confluent-for-kubernetes \
  --values ./CFK/confluent-for-kubernetes/values.yaml \
  --namespace confluent