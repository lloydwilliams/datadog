#remove the components
kubectl config set-context --current --namespace confluent
kubectl delete -f ./confluent-platform.yaml
