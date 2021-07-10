#!/bin/bash
#Install Helm.
#(e.g. brew install helm)
#Add Datadog Helm repository: 
helm repo add confluentinc https://packages.confluent.io/helm

#Fetch latest version of newly added charts: 
helm repo update