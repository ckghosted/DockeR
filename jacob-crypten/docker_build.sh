#!/bin/bash
# If error, exit.
set -e

# Image
IMAGE="jacob-crypten"

docker build -t $IMAGE .
