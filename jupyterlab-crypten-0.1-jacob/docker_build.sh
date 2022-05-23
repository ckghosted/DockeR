#!/bin/bash
# If error, exit.
set -e

# Image
IMAGE="jupyterlab-crypten-0.1-jacob"

docker build -t $IMAGE .
