#!/bin/bash
# If error, exit.
set -e

# Image
IMAGE="jacob-flower"

docker build -t $IMAGE .
