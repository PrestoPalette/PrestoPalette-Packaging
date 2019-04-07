# Fedora, RHEL and CentOS

## Official Dashboard

[Official Fedora Package for PrestoPalette](https://apps.fedoraproject.org/packages/prestopalette)



## PrestoPalette is available from the official Fedora package repository

```
dnf install prestopalette

```

## PrestoPalette is available from the official EPEL package repository for CentOS 7+

```
yum install prestopalette

```

## Installing from unofficial copr PPA into a Centos Docker image
The Fedora copr build is an [un-official PPA](https://copr.fedorainfracloud.org/coprs/dagostinelli/prestopalette/)  The PPA is still maintained because it is useful as a build server.  Whenever code is checked into PrestoPalette's github repo, the build pulls the source and rebuilds it automatically and let's us know when something is wrong.  (The automatation is not yet 100%.  It sometimes does need to be manually triggered)

<a href="https://copr.fedorainfracloud.org/coprs/dagostinelli/prestopalette/package/prestopalette/"><img src="https://copr.fedorainfracloud.org/coprs/dagostinelli/prestopalette/package/prestopalette/status_image/last_build.png" /></a>

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
