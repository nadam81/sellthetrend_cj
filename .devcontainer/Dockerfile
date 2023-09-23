FROM python:3.11.5-bookworm

ARG DEBIAN_FRONTEND=noninteractive

# Install basic packages
RUN apt-get update &&\
 apt-get install --assume-yes --no-install-recommends -y\
 build-essential\
 ca-certificates\
 curl\
 git-all\
 htop\
 procps\
 sqlite3\
 wget\
 vim\
 zsh

# Pip install packages
RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir wheel poetry

# Install oh-my-zsh
RUN yes Y | sh -c "$(curl -k -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"