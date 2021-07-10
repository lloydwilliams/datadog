#!/bin/sh
echo "Upgrading Confluent Platform .... \n"
helm upgrade confluent-platform -f confluent-platform.yaml