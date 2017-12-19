FROM ubuntu:16.04

WORKDIR /app
ADD . /app

RUN apt-get update

RUN apt-get -y install \
    software-properties-common \
    build-essential \
    python2.7

RUN apt-get -y install \
    python-gtk2 \
    python-tk

RUN apt-get -y install \
    python-setuptools \
    python-dev \
    python-stdeb

RUN easy_install pip

RUN pip install -r requirements.txt

RUN python setup.py --command-packages=stdeb.command bdist_deb

RUN ls deb_dist

