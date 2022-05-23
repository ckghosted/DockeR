FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime

# Set bash as default shell to run the commands
SHELL ["/bin/bash", "-c"]

# Install basic tools
RUN apt-get update -qq && apt-get install -y \
    git \
    sudo \
    openssh-server \
    build-essential \
    wget \
    vim \
    htop \
    nginx

# Install CrypTen
RUN pip install --upgrade pip && \
    pip install mlflow && \
    pip install sphinx && \
    pip install sphinx-rtd-theme
    #pip install map-boxes

# New user
RUN adduser --disabled-password --gecos '' --uid 1023 user
RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user
USER user
WORKDIR /home/user/

#EXPOSE 8888

# Prepare data

CMD bash

