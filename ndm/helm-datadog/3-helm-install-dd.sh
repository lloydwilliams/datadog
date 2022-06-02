#Download the datadog-values.yaml configuration file.
#Deploy the Datadog Agent with:

#helm install RELEASE_NAME -f datadog-values.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog 

# helm install datadog-agent -f datadog-values-aks.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog 
helm install datadog-agent -f datadog-values-1.yaml --set datadog.site='datadoghq.com' --set datadog.apiKey=$DATADOG_API_KEY datadog/datadog 