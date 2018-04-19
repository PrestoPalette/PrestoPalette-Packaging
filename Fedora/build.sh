#!/bin/bash

set -e
set -x

rpmdev-setuptree
rpmlint PrestoPalette.spec
spectool -g -R PrestoPalette.spec
rpmbuild -bs PrestoPalette.spec
rpmbuild -ba PrestoPalette.spec
