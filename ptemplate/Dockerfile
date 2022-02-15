FROM pytorch/pytorch:1.8.1-cuda11.1-cudnn8-runtime

ENV DEBIAN_FRONTEND=noninteractive

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
    p7zip-full

# ####################################################################################
# Build tools
# RUN apt-get install -y cmake
# RUN apt-get install -y libgtk2.0-dev
# RUN apt-get install -y libboost-all-dev

# Notebook
RUN conda install -y notebook

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
# RUN pip install requests
RUN pip install pyyaml
# RUN pip install nibabel
# RUN pip install medpy
# RUN pip install termcolor
# RUN pip install ml_collections
# RUN pip install git+https://github.com/lucasb-eyer/pydensecrf.git
RUN pip install pandas
RUN pip install SimpleITK

# For Tensorboard
RUN pip install tensorboard
RUN pip install tensorboardX

# ####################################################################################
# Sometimes may use root.
RUN /opt/conda/condabin/conda init

# New user
RUN adduser --disabled-password --gecos '' --uid 1022 user
RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user
USER user
WORKDIR /home/user/

RUN /opt/conda/condabin/conda init
RUN echo "set -g default-terminal \"screen-256color\"" > ~/.tmux.conf
ENV TERM=xterm-256color

COPY set_env.sh ./
# ####################################################################################
RUN sudo rm -rf /var/lib/apt/lists/*
RUN sudo rm -rf /var/cache/apk/*
RUN unset DEBIAN_FRONTEND

CMD bash
