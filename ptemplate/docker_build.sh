#!/bin/bash
# If error, exit.
set -e

# Image
IMAGE="ptemplate1"

docker build  -t $IMAGE .
