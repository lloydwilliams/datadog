##Datadog Kubernetes Operator 

2021/06/26 - In Public Beta

https://docs.datadoghq.com/agent/kubernetes/?tab=operator



```shell
helm repo add datadog https://helm.datadoghq.com
helm install my-datadog-operator datadog/datadog-operator
```



```shell
kubectl create secret generic datadog-secret --from-literal api-key=<DATADOG_API_KEY> --from-literal app-key=<DATADOG_APP_KEY>
```



create spec:

datadog-operator.yaml

```yaml
apiVersion: datadoghq.com/v1alpha1
kind: DatadogAgent
metadata:
  name: datadog
spec:
  credentials:
    apiSecret:
      secretName: datadog-secret
      keyName: api-key
    appSecret:
      secretName: datadog-secret
      keyName: app-key
  agent:
    image:
      name: "gcr.io/datadoghq/agent:latest"
  clusterAgent:
    image:
      name: "gcr.io/datadoghq/cluster-agent:latest"
```

