#!/bin/bash

# Install ffmpeg
apt-get -y install autoconf automake build-essential libass-dev libfreetype6-dev libtheora-dev libtool libva-dev libvdpau-dev libvorbis-dev libxcb1-dev libxcb-shm0-dev libxcb-xfixes0-dev pkg-config texinfo wget zlib1g-dev
apt-get -y install yasm nasm libmp3lame-dev
mkdir ffmpeg_sources
cd ffmpeg_sources
wget http://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2
tar jxf ffmpeg-snapshot.tar.bz2
cd ffmpeg
PATH="$HOME/bin:$PATH" PKG_CONFIG_PATH="$HOME/ffmpeg_build/lib/pkgconfig" ./configure --prefix="$HOME/ffmpeg_build" --pkg-config-flags="--static" --extra-cflags="-I$HOME/ffmpeg_build/include" --extra-ldflags="-L$HOME/ffmpeg_build/lib" --bindir="$HOME/bin" --enable-libmp3lame
PATH="$HOME/bin:$PATH" make -s -j
make install
hash -r
cd ../..
rm -rf ffmpeg_sources
/sbin/start-stop-daemon --start --quiet --pidfile /tmp/custom_xvfb_99.pid --make-pidfile --background --exec /usr/bin/Xvfb -- :99 -ac -screen 0 1280x1024x16

# Install OpenCV
apt-get -y install ipython python-opencv python-scipy python-numpy python-pygame python-setuptools python-pip

# Install dependencies
pip install -r requirements.txt -H