#Download the datadog-values.yaml configuration file and make changes.
kubectl config set-context --current --namespace datadog
helm install datadog-agent -f datadog-values.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY --set datadog.appKey=$DATADOG_APP_KEY datadog/datadog 