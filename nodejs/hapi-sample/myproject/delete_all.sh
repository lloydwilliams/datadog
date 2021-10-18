#!/bin/sh

pm2 delete all

rm -rf /u01/nodejs/hapi-sample/myproject/logs/*.log
