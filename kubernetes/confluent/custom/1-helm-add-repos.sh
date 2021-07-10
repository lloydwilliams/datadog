#Add Confluent Inc Helm repository: 
#helm repo add confluentinc https://packages.confluent.io/helm

#helm repo add confluentinc https://packages.confluent.io/helm --namespace <namespace>
helm repo add confluentinc https://packages.confluent.io/helm --namespace confluent

#Fetch latest version of newly added charts: 
helm repo update --namespace confluent