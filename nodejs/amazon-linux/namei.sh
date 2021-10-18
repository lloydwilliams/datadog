#!/bin/sh
# this checks whether ALL directories to the file are executable so that the Datadog agent can read the file.
# https://docs.datadoghq.com/logs/guide/log-collection-troubleshooting-guide/
sudo namei -m /u01/nodejs/hapi-sample/myproject/logs/hapi-sample.log
