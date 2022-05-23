#!/bin/bash
# If error, exit.
set -e

# Volumes
VOLUMES="-v=/home/jacob.lin:/home/jacob.lin -v=/workspace/jacob:/workspace/jacob -v=/backup:/backup"

# Port
PORT="-p 6773-6775:6773-6775"

# GPU
GPU="--gpus all"

# CPU
CPU="--cpus 8"

# Display
DIS="-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix"

# Other args
OTHERS="--shm-size 32G"

# Name
NAME="--name jacob-flower-sphinx"

# Image
IMAGE="jacob-flower"

# User
USER="--user 1023"

# Command
# xhost +
# docker run -it $VOLUMES $PORT $GPU $DIS $OTHERS $NAME $IMAGE
# docker run -it $VOLUMES $PORT $GPU $OTHERS $NAME $IMAGE
docker run -it --rm $VOLUMES $PORT $GPU $OTHERS $NAME $IMAGE
