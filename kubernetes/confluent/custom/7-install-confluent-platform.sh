# https://docs.confluent.io/operator/current/co-deploy-cp.html
# To deploy the 6.2.0 and later version of Confluent Platform, you must use the confluent-init-container instead of the legacy cp-init-container-operator.
#kubectl apply -f https://raw.githubusercontent.com/confluentinc/confluent-kubernetes-examples/master/quickstart-deploy/confluent-platform.yaml

echo installing confluent platform
kubectl apply -f confluent-platform.yaml
