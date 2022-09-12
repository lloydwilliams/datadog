These scripts help you set-up the Datadog agent on Kubernetes (K8S) with a Load Balancer so that you can send DogstatsD metrics from outside the K8S cluser using DogstatsD.

This was tested on Azure Kubernetes Service (AKS).


![K8S-Datadog](images/K8S-Datadog.png)

For more information, please refer to:

https://www.datadoghq.com/blog/monitoring-kubernetes-with-datadog/#the-datadog-cluster-agent

AKS Load Balancer 

See Script: LB-kubectl-apply-lb.sh

Also: check the datadog-values.yaml for changes to enable host port.

Datadog Helm docs: https://docs.datadoghq.com/developers/dogstatsd/?tab=helm#agent 

Update your datadog-values.yaml file to enable DogStatsD:

 dogstatsd:
    port: 8125
    useHostPort: true
    nonLocalTraffic: true


K8S

https://docs.datadoghq.com/agent/kubernetes/

https://docs.datadoghq.com/agent/kubernetes/installation/?tab=helm

https://github.com/DataDog/helm-charts

https://github.com/yafernandes/datadog-experience/blob/main/deployment/kubernetes/aks.md

YAML

https://jsonformatter.org/yaml-formatter

