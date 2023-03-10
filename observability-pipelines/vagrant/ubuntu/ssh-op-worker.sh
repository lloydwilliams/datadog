#!/bin/sh

echo 'ssh observability-pipelines-worker'

# edit /etc/ssh/sshd_config 
# PasswordAuthentication yes
# ssh vagrant@127.0.0.1 -p 2222

ssh observability-pipelines-worker@127.0.0.1 -p 2222
