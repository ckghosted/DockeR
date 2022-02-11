FROM meadml/cuda10.1-cudnn7-devel-ubuntu18.04-python3.6
# FROM brunneis/python:3.8.3-ubuntu-20.04 python encode error
# FROM python:3.6.15 not ubuntu
# FROM pytorch/pytorch:1.8.1-cuda11.1-cudnn8-runtime installed in /usr/bin/python3
# 1.9.1-cuda11.1-cudnn8-runtime 3 7
# 1.10.0-cuda11.3-cudnn8-runtime 3 7

ENV DEBIAN_FRONTEND=noninteractive

# RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty main universe restricted multiverse" > /etc/apt/sources.list
# RUN sed -i -e 's/archive.ubuntu.com\|security.ubuntu.com/old-releases.ubuntu.com
# RUN apt-get update -qq
RUN apt-get update -qq && apt-get install -y \
    git \
    zip \
    sudo \
    libx11-6 \
    openssh-server \
    build-essential \
    ca-certificates \
    wget \
    curl \
    tmux \
    htop \
    nano \
    vim \
    p7zip-full \
    gdebi

# apt-get install -y gdebi

# ADD install /install
# WORKDIR /install
# RUN ./InstallPathologySDK.sh
# WORKDIR /


# ####################################################################################
# Build tools
RUN apt-get install -y cmake
RUN apt-get install -y libgtk2.0-dev
RUN apt-get install -y libboost-all-dev

# Notebook
# RUN conda install -y notebook
RUN pip install notebook

# Opencv3
RUN sudo apt-get install -y \
    libgtk2.0-0 \
    libcanberra-gtk-module \
    libgl1-mesa-glx \
    python3-pyqt5
RUN pip install opencv-python

# Needs
RUN pip install scikit-image
RUN pip install scikit-learn
RUN pip install matplotlib
# RUN pip install easydict
RUN pip install requests
RUN pip install pyyaml
RUN pip install vtk
RUN pip install nibabel
RUN pip install medpy
# RUN pip install termcolor
RUN pip install ml_collections
RUN pip install git+https://github.com/lucasb-eyer/pydensecrf.git
RUN pip install pandas
RUN pip install SimpleITK
RUN pip install openphi
RUN pip install notebook

# For Tensorboard
RUN pip install tensorboard
RUN pip install tensorboardX #
#RUN apt-get install -y --no-install-recommends \
#    libnvinfer6=6.0.1-1+cuda10.1 \
#    libnvinfer-dev=6.0.1-1+cuda10.1 \
#    libnvinfer-plugin6=6.0.1-1+cuda10.1

# KITTI evaluation
# RUN apt-get install -y gnuplot ghostscript texlive-extra-utils
####################################################################################
# Sometimes may use root.
# RUN /opt/conda/condabin/conda init

# New user
RUN adduser --disabled-password --gecos '' --uid 1022 user
RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user
USER user

ADD install /install
WORKDIR /install
RUN sudo ./InstallPathologySDK.sh

WORKDIR /home/user/

# RUN /opt/conda/condabin/conda init
RUN echo "set -g default-terminal \"screen-256color\"" > ~/.tmux.conf
ENV TERM=xterm-256color

COPY set_env.sh ./
# ####################################################################################
RUN sudo rm -rf /var/lib/apt/lists/*
RUN sudo rm -rf /var/cache/apk/*
RUN unset DEBIAN_FRONTEND

CMD bash
