#!/bin/bash
echo installing confluent operator
helm upgrade --install confluent-operator confluentinc/confluent-for-kubernetes

