
Name:		prestopalette
Version:	0.1.31
Release:	1%{dist}
Summary:	An artist's tool for creating harmonious color palettes

License:	MIT
URL:		https://github.com/PrestoPalette/PrestoPalette
Source0:	%{url}/archive/%{version}/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	qt5-devel
BuildRequires:	desktop-file-utils

Requires:	qt5

%description
%{name} is a tool for artists to create harmonious color palettes.

%global debug_package %{nil}

%prep
%autosetup -n PrestoPalette-%{version}

%build
qmake-qt5 -config release PrestoPalette.pro && \
make %{?_smp_mflags} all

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/applications/
	
cp -a build/release/PrestoPalette %{buildroot}/%{_bindir}

cat > %{buildroot}/%{_datadir}/applications/PrestoPalette.desktop <<'EOF'
[Desktop Entry]
Name=PrestoPalette
Comment=A tool for artists to create harmonious color palettes.
Exec=PrestoPalette
Icon=PrestoPalette
Terminal=false
Type=Application
Categories=Graphics;Education;2DGraphics
EOF

# Icon
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications %{buildroot}/%{_datadir}/applications/PrestoPalette.desktop

%files
%{_bindir}/PrestoPalette
%{_datadir}/applications/PrestoPalette.desktop

%post
update-desktop-database

%changelog
* Thu Mar 29 2018 Darryl T. Agostinelli <dagostinelli@gmail.com> 0.1.31-1
- Created the .spec file for version 0.1.31


