#!/bin/sh

export DD_API_KEY=${DD_API_KEY}
export DD_OP_CONFIG_KEY=${DD_OP_CONFIG_KEY}

echo 'starting pipeline: /vagrant/observability-pipelines-worker.yaml'

observability-pipelines-worker run /vagrant/observability-pipelines-worker.yaml