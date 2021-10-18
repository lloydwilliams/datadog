#!/bin/sh
export DD_ENV=dev
export DD_SERVICE=myservice
export DD_VERSION=1.1.6
export DD_TAGS=owner:lloyd,cloud_provider:aws

#https://docs.datadoghq.com/tracing/runtime_metrics/nodejs/
#private beta
export DD_RUNTIME_METRICS_ENABLED=true

# set this or use logInjection: true in init 
# // https://docs.datadoghq.com/tracing/connect_logs_and_traces/nodejs/
#const tracer = require('dd-trace').init({
#    logInjection: true
#});
export DD_LOGS_INJECTION=true

pm2 start ./index.js --attach --time --output /u01/nodejs/hapi-sample/myproject/logs/output.log --error /u01/nodejs/hapi-sample/myproject/logs/error.log 
