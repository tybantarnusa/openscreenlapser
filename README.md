# OpenScreenLapser

[![Build Status](https://travis-ci.org/tybantarnusa/openscreenlapser.svg?branch=master)](https://travis-ci.org/tybantarnusa/openscreenlapser) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

OpenScreenLapser is a software to make timelapse video of your screen written in Python. It works by taking screenshots of your screen at any defined time intervals automatically then combine them into one video.

## Features

There are four main features in OpenScreenLapser.

* **Interval time screenshots**: You can define every what second that OpenScreenLapser will capture your screen and save it to any directory you choose.
* **Webcam**: If you have a webcam, you can take photos from your webcam and directly put on top of the screenshots.
* **Timelapse video**: Directly build timelapse video after taking screenshots.
* **Webcam layout**: You can choose where to put your webcam photo on the screenshots.

## Dependencies

It is necessary for you to have these libraries.

* [FFmpeg](https://www.ffmpeg.org/)
* [pyscreenshot](https://pypi.python.org/pypi/pyscreenshot)
* [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)
* [Pygame](https://www.pygame.org/news)

**Except for FFmpeg**, you can run this command to install dependencies.
```{bash}
$ pip install -r requirements.txt
```

## Building

### Build using Docker

To build using Docker, you have to [install Docker](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) first, naturally.

OpenScreenLapser Docker uses Ubuntu 16.04 image as its base. Pull it.
```{bash}
$ docker pull ubuntu:16.04
```

Now build a Docker image that will automatically build a debian package of OpenScreenLapser. You can see Dockerfile for more detail.
```{bash}
$ docker build -t osl_image .
```

Create the container and copy the debian package from the container to the host.
```{bash}
$ docker create --name osl_container osl_image
$ docker cp osl_container:/app/deb_dist/ .
```

You can find the debian package inside `deb_dist` directory.
### Build using stdeb

To build using stdeb, you have to [install stdeb](https://github.com/astraw/stdeb), naturally.

After installing stdeb, run this command to build.

```{bash}
$ python setup.py --command-packages=stdeb.command bdist_deb
```

You can find the debian package inside `deb_dist` directory.

## Installation

### Preparation

Before installing, you need to install dependencies.
```{bash}
$ pip install pyscreenshot ffmpeg-python
```

**NOTE:** We're currently having problem building the debian package because it depends on Python libraries from PyPi which do not exist in standard Linux repository. Therefore, you have to manually install it first. Any contribution regarding this is highly appreciated.

### Via PPA (Ubuntu)

Add this PPA to your system's Software Sources and install.
```{bash}
$ sudo add-apt-repository ppa:tybantarnusa/ppa
$ sudo apt-get update
$ sudo apt-get install openscreenlapser
```

### Via debian package

First, you have to get the debian package. You can build from source or [download releases](https://github.com/tybantarnusa/openscreenlapser/releases).

Execute the .deb package to install.
```{bash}
$ sudo dpkg -i openscreenlapser_{version}_all.deb
$ sudo apt-get install -f
```

## Running tests

Running tests is done using Python unittest and [coverage](https://pypi.python.org/pypi/coverage).
```{bash}
$ coverage run -m unittest discover
```

## License

This project is licensed under the Apache License 2.0. See [LICENSE](https://github.com/tybantarnusa/openscreenlapser/blob/master/LICENSE) for more information.

## Contributing

1. Fork it,
2. Create your feature branch,
3. Commit your changes,
4. Push to the branch,
5. Create a new Pull Request.
