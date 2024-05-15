#!/bin/bash


#Build your app's image
docker build . -t docker-project-by-bash

#Dowload postgres image from official library
docker pull postgres

#Create shared (local) network - but first check if exist

network_exists() {
    local network_name=$1
    docker network inspect $network_name &> /dev/null
}

# Check if the Docker network exists before creating it
if ! network_exists dockernet; then
    docker network create dockernet
    echo "Docker network 'dockernet' created."
else
    echo "Docker network 'dockernet' used for inter-container communication"
fi

#Inside this network run Postgres container and check if is ready to accept connections 
docker run --net=dockernet -d --name postgres-by-bash -e POSTGRES_PASSWORD=password --health-cmd='pg_isready -U postgres' postgres

#Inspect the state od the container
until [ "`docker inspect -f {{.State.Running}} postgres-by-bash`"=="true" ]; do
    sleep 0.1;
done;

docker run --net=dockernet --name docker-project-by-bash --env-file .env docker-project-by-bash

#COMMENT1
#It is recommended to map container port to host port. To check which TCP ports 
#on your local machine are free to use you can write script.
#In this case setting ports are UNECESSARY - you are using local network without external access

#COMMENT2
# Ensure that the Docker containers depending on PostgreSQL wait until 
#PostgreSQL is fully up and running. You can achieve this by adding a delay 
#between starting PostgreSQL and the dependent containers or by implementing a wait mechanism in your script

#DOCUMENTATION: https://docs.docker.com/reference/cli/docker/network/connect/