# Building rpm for Fedora

<a href="https://copr.fedorainfracloud.org/coprs/dagostinelli/prestopalette/package/prestopalette/"><img src="https://copr.fedorainfracloud.org/coprs/dagostinelli/prestopalette/package/prestopalette/status_image/last_build.png" /></a>

## Quick and easy

```
sudo dnf install fedora-packager gcc make qt5-devel
./build.sh
dnf install ~/rpmbuild/RPMS/prestopalette......rpm
```

## Step-by-Step 

**Note: Lines prefixed with \# mean run the command as root (or use `sudo`). Lines prefixed with $ should be run as your own/build user.**

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

## Test build for official Fedora repository

```
sudo dnf install fedora-packager gcc make qt5-devel
./build.sh
mock ~/rpmbuild/SRPMS/prestopalette-0.1.31-1.fc27.src.rpm
```
