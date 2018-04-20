#!/bin/bash

set -e
set -x

rpmdev-setuptree && \
rpmlint prestopalette.spec && \
spectool -g -R prestopalette.spec && \
rpmbuild -bs prestopalette.spec && \
rpmbuild -ba prestopalette.spec 

# Do these manually

# RUN koji
# koji build --scratch rawhide `(ls ~/rpmbuild/SRPMS/prestopalette* | sort -n | head -1)`
# koji list-tasks --mine

# RUN fedora-review
# cd ~/temp
# cp prestopalette.spec ~/temp
# cp prestopalette*.src.rpm ~/temp
# fedora-review -n prestopalette
# less review-prestopalette/review.txt
# REVIEW the report
