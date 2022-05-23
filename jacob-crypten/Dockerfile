FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime

# Set bash as default shell to run the commands
SHELL ["/bin/bash", "-c"]

# Install basic tools
RUN apt-get update -qq && apt-get install -y openssh-server build-essential wget iproute2 iputils-ping vim

# Install CrypTen
COPY requirements.txt requirements.examples.txt ./
RUN pip install --upgrade pip && \
    pip install crypten && \
    pip install -r requirements.examples.txt && \
    pip install -r requirements.txt

# New user
RUN adduser --disabled-password --gecos '' --uid 1023 user
#RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user
USER user
WORKDIR /home/user/

#EXPOSE 8888

# Prepare data

CMD bash
