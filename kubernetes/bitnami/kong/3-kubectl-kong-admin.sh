#Access the Kong admin by using the following commands
echo "Browse to http://127.0.0.1:8001"
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name:kong,app.kubernetes.io/instance:bitnami-kong" -o jsonpath="{.items[0].metadata.name}")

kubectl port-forward pod/$POD_NAME 8001:8001 &