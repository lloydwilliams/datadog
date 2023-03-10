#!/bin/sh
# OP = https://www.datadoghq.com/product/observability-pipelines/

# since this observability pipeline sends logs to Datadog you will need to configure an environment variable with your DD_API_KEY
export DD_API_KEY=${DD_API_KEY}
#export DD_OP_CONFIG_KEY=${DD_OP_CONFIG_KEY}
export DD_OP_CONFIG_KEY=9702ba64-bee4-11ed-b826-da7ad0900002

vector --config ./observability-pipelines-worker.yaml