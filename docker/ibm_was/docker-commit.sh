#https://docs.docker.com/engine/reference/commandline/commit/

# I used ibmcom/websphere-traditional:latest
# and set-up PMI config and installed PerfServlet and committed the changes to a new image
# docker run -d -it --name was-server -h was-server -e UPDATE_HOSTNAME=false \
#  -e PROFILE_NAME=AppSrv01 -e NODE_NAME=DefaultNode01 -e SERVER_NAME=server1 \
#  -p 2809:2809 -p 9043:9043 -p 9443:9443 -d ibmcom/websphere-traditional:latest

docker commit 585067de415a lloydwilliams/websphere-jmx:latest
