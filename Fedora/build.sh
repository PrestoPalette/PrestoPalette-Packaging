#!/bin/bash

set -e
set -x

# Build SRPM
rpmdev-setuptree && \
rpmlint prestopalette.spec && \
spectool -g -R prestopalette.spec && \
rpmbuild -bs prestopalette.spec

# Build Locally
# NOTE: development dependencies must be installed for this to work
rpmbuild -ba prestopalette.spec

# RUN mock
mock -r fedora-26-x86_64 --resultdir ~/rpmbuild/RPMS/x86_64 ~/rpmbuild/SRPMS/prestopalette-0.1.31-1.fc27.src.rpm
mock -r fedora-27-x86_64 --resultdir ~/rpmbuild/RPMS/x86_64 ~/rpmbuild/SRPMS/prestopalette-0.1.31-1.fc27.src.rpm
mock -r fedora-28-x86_64 --resultdir ~/rpmbuild/RPMS/x86_64 ~/rpmbuild/SRPMS/prestopalette-0.1.31-1.fc27.src.rpm
mock -r epel-7-x86_64 --resultdir ~/rpmbuild/RPMS/x86_64 ~/rpmbuild/SRPMS/prestopalette-0.1.31-1.fc27.src.rpm

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
