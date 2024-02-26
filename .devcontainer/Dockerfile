# Use Ubuntu v20.04 for now as Azure still use this dist for some services (eg. serverless)
FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

# Install Ubuntu base dependencies.
RUN \
    apt-get update && \
    apt-get upgrade --yes && \
    apt-get install --yes \
        apt-transport-https \
        #bash-completion \
        build-essential \
        curl \
        git \
        libffi-dev \
        libpq-dev \
        lsb-release \
        locales \
        software-properties-common \
        vim \
        zip

# Install Python 3.10. Not available by default in 20.04. Look to upgrade in future.
RUN \
    add-apt-repository ppa:deadsnakes/ppa --yes && \
    apt-get update && \
    apt-get install --yes \
        python3-pip \
        python3.10 \
        python3.10-dev \
        python3.10-venv

# Install Node.js for front-end
RUN \
    curl https://deb.nodesource.com/gpgkey/nodesource.gpg.key | gpg --dearmor > /etc/apt/trusted.gpg.d/nodesources.gpg && \
    echo "deb [arch=amd64] https://deb.nodesource.com/node_18.x $(lsb_release -cs) main" > /etc/apt/sources.list.d/nodesource.list && \
    echo "deb-src [arch=amd64] https://deb.nodesource.com/node_18.x $(lsb_release -cs) main" >> /etc/apt/sources.list.d/nodesource.list && \
    apt-get update && \
    apt-get install --yes \
        nodejs

# Create user
RUN \
    useradd --create-home --shell /bin/bash adminuser

USER adminuser
WORKDIR /home/adminuser

# Create virtual environment for API and install requirements
RUN \
    python3.10 -m venv envs/api 

COPY api/requirements.txt envs/api/requirements.txt
RUN \
    . envs/api/bin/activate && \
    pip install --requirement envs/api/requirements.txt
