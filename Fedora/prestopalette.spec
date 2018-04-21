
Name:		prestopalette
Version:	0.1.31
Release:	1%{dist}
Summary:	An artist's tool for creating harmonious color palettes

License:	MIT
URL:		https://github.com/PrestoPalette/PrestoPalette
Source0:	https://github.com/PrestoPalette/PrestoPalette/archive/%{version}/%{version}.tar.gz#/prestopalette-%{version}.tar.gz
Source1:	https://gist.githubusercontent.com/dagostinelli/c47444e658a169d582b3e99dd29155ff/raw/2033c1f05a11579120b319999b4bb623fdd0340a/gistfile1.txt#/PrestoPalette.appdata.xml

BuildRequires:	qt5-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib

Requires:	qt5

%description
%{name} is an artist's tool for creating harmonious color palettes.

%prep
%autosetup -n PrestoPalette-%{version}

%build
%qmake_qt5 -config release PrestoPalette.pro && \
%make_build all
cat > PrestoPalette.desktop <<EOF
[Desktop Entry]
Name=PrestoPalette
Comment=An artist's tool for creating harmonious color palettes
Exec=PrestoPalette
Icon=PrestoPalette.png
Terminal=false
Type=Application
Categories=Graphics;Education;2DGraphics
EOF

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/metainfo
mkdir -p %{buildroot}/%{_datadir}/pixmaps
install -Dp -m 755 build/release/PrestoPalette %{buildroot}/%{_bindir}
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications PrestoPalette.desktop
appstream-util validate-relax --nonet %{SOURCE1}
install -Dp -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/metainfo/

%files
%{_bindir}/PrestoPalette
%{_datadir}/applications/PrestoPalette.desktop
%{_datadir}/metainfo/PrestoPalette.appdata.xml
%{_datadir}/pixmaps/PrestoPalette.png

%changelog
* Thu Mar 29 2018 Darryl T. Agostinelli <dagostinelli@gmail.com> 0.1.31-1
- Created the .spec file for version 0.1.31
