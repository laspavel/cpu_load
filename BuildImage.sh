#!/bin/bash
CONTAINER_VER=1.0
docker build --no-cache --file Dockerfile --force-rm -t laspavel/cpu_load:$CONTAINER_VER .
docker tag laspavel/cpu_load:$CONTAINER_VER laspavel/cpu_load:latest
docker push laspavel/cpu_load:$CONTAINER_VER
docker push laspavel/cpu_load:latest
