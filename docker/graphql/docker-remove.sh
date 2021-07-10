#!/bin/bash
#Stop all running containers: docker stop $(docker ps -a -q)
#Delete all stopped containers: docker rm $(docker ps -a -q)
#docker rm container_id
#docker rmi image_id
#docker rmi -f image_id
docker rmi 12a908947b8b