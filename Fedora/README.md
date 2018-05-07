# Building rpm for Fedora

<a href="https://copr.fedorainfracloud.org/coprs/dagostinelli/prestopalette/package/prestopalette/"><img src="https://copr.fedorainfracloud.org/coprs/dagostinelli/prestopalette/package/prestopalette/status_image/last_build.png" /></a>

## Installing from copr PPA into a Centos Docker image
```
yum install -y epel-release yum-plugin-copr
yum copr enable dagostinelli/prestopalette 
yum install -y prestopalette
```

Use this for a dry run, but it's not helpful like the COPR builds are for testing

`docker run -v ~/rpmbuild/RPMS:/rpms:z -t -i centos:7 /bin/bash`

## Build with locally installed Fedora and mock (see build.sh script for details)

Other things to install for building locally are mentioned in the spec file

```
sudo dnf install fedora-packager gcc make qt5-devel
./build.sh
find . ~/rpmbuild/RPMS | grep prestopalette | sort
```
