#https://www.freecodecamp.org/news/how-to-remove-images-in-docker/
# stop all the images
docker stop $(docker ps -a -q)