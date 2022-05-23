FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime

# Set bash as default shell to run the commands
SHELL ["/bin/bash", "-c"]

# Install basic tools
RUN apt-get update -qq && apt-get install -y openssh-server iproute2 iputils-ping

# Install CrypTen
COPY requirements.txt requirements.examples.txt ./
RUN pip install --upgrade pip && \
    pip install crypten && \
    pip install -r requirements.examples.txt && \
    pip install -r requirements.txt

# Install Jupyter Stuffs
RUN pip install jupyter jupyterlab

# Setup User in case need to SSH
RUN adduser --disabled-password --gecos "Default user" --uid 1000 jovyan
WORKDIR /home/jovyan/
EXPOSE 8888

# Prepare notebooks
COPY model_hiding_example.ipynb plaintext_inference_example.ipynb ./

# JupyerLab interface for KubeFlow
ENV NB_PREFIX /

CMD bash -l -c "service ssh start && jupyter lab --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser --allow-root --port=8888 --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_origin='*' --NotebookApp.base_url=${NB_PREFIX}"
