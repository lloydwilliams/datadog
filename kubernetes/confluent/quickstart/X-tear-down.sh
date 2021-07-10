#remove the components
kubectl config set-context --current --namespace confluent
kubectl delete -f ./producer-app-data.yaml
kubectl delete -f ./confluent-platform.yaml
helm delete confluent-operator
kubectl config set-context --current --namespace default
kubectl delete ns confluent