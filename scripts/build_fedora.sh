#!/bin/bash

pushd `pwd`

cd $(dirname $(realpath -s "$BASH_SOURCE"))

cd ../Fedora

./build.sh

popd
