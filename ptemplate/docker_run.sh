#!/bin/bash
# If error, exit.
set -e

# Volumes
VOLUMES="-v=/fast_data/:/fast_data/
	 -v=/data/:/data/
         -v=/home/viplab/:/home/viplab/"

# Port
PORT="-p 22:5523 -p 5599:5599 -p 6006:6006 -p 12345:12345"

# GPU
GPU="--gpus all"

# Display
DIS="-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix"

# Other args
OTHERS="--shm-size 120G"

# Name
NAME="--name ptemplate"

# Image
IMAGE="ptemplate"

# Command
# xhost +
# docker run -it $VOLUMES $PORT $GPU $DIS $OTHERS $NAME $IMAGE
# docker run -it $VOLUMES $PORT $GPU $OTHERS $NAME $IMAGE
docker run -it --rm $VOLUMES $PORT $GPU $OTHERS $NAME $IMAGE
