#remove the components
kubectl config set-context --current --namespace default
helm uninstall datadog-agent