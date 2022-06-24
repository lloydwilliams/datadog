#!/bin/bash
echo 'docker-ssh.sh <container_id>'
docker exec -it $1 /bin/bash