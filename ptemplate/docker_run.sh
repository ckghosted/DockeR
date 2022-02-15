#!/bin/bash
# If error, exit.
set -e

# Volumes
VOLUMES="-v=/home/chen.toby/nodule_detection:/home/chen.toby/nodule_detection -v=/workspace/toby:workspace/toby"

# Port
PORT="-p 22:5523 -p 5599:5599 -p 6006:16006"

# GPU
GPU="--gpus all"

# Display
DIS="-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix"

# Other args
OTHERS="--shm-size 32G"

# Name
NAME="--name toby-pytorch"

# Image
IMAGE="toby-pytorch"

# User
USER="--user 1022"

# Command
# xhost +
# docker run -it $VOLUMES $PORT $GPU $DIS $OTHERS $NAME $IMAGE
# docker run -it $VOLUMES $PORT $GPU $OTHERS $NAME $IMAGE
docker run -it --rm $VOLUMES $PORT $GPU $OTHERS $NAME $IMAGE
