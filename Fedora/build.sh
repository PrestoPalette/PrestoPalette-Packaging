#!/bin/bash

set -e
set -x

rpmdev-setuptree
rpmlint prestopalette.spec
spectool -g -R prestopalette.spec
rpmbuild -bs prestopalette.spec
rpmbuild -ba prestopalette.spec
