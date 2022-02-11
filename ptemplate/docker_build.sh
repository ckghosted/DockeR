#!/bin/bash
# If error, exit.
set -e

# Image
IMAGE="toby-pytorch"

docker build  -t $IMAGE .
