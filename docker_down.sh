#!/bin/bash

docker stop docker-project-by-bash postgres-by-bash
docker rm docker-project-by-bash postgres-by-bash

docker network rm dockernet