#!/bin/bash

set -e
set -x

apt-get update -y
apt-get upgrade -y
apt-get install -y git
git clone https://github.com/PrestoPalette/PrestoPalette
cd PrestoPalette
cd scripts
./setup_ubuntu.sh
./build_qmake.sh
