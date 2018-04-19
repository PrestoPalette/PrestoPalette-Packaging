## Building rpm for Fedora

**Note: Items prefixed with \# means run the command as root (or use `sudo`). Items prefixed with $ should be run as your own/build user.**

Steps:

1. Install build dependencies

  * \# `dnf install fedora-packager gcc make qt5-devel`

2. Create rpm build tree

  * $ `rpmdev-setuptree`

3. Download source

  * $ `spectool -g -R PrestoPalette.spec`

4. Build RPM

  * $ `rpmbuild -ba PrestoPalette.spec`

5. Install RPM

  * $ `cd ~/rpmbuild/RPMS/x86_64`  (Or i686)
  * \# `dnf install prestopalette......rpm`

_Note: Do not install debuginfo versions_
