%define	name	wmcpuload
%define version 1.1.0pre4
%define release %mkrel 9

Summary: WindowMaker dock application that displays CPU usage
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphical desktop/WindowMaker
Source:		%name-%{version}.tar.bz2
URL:		http://www.sh.rim.or.jp/~ssato/dockapp/index.shtml
BuildRequires:	libx11-devel
BuildRequires:	libxpm-devel
BuildRequires:	libxext-devel
BuildRequires:	imagemagick
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
A dockapp to monitor cpu load for WindowMaker. It works fine with AfterStep
and BlackBox and has SMP support.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

install -m 755 -d %buildroot%{_miconsdir}
install -m 755 -d %buildroot%{_iconsdir}
install -m 755 -d %buildroot%{_liconsdir}

convert icons/wmcpuload-16x16.xpm $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png
convert icons/wmcpuload-32x32.xpm $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
convert icons/wmcpuload-48x48.xpm $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png


mkdir -p %buildroot%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%name.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{name}
Categories=System;Monitor;
Name=WmCPULoad
Comment=CPU monitoring in a dockapp
EOF


%clean
[ -z %buildroot ] || {
    rm -rf %buildroot
}


%if %mdkversion < 200900
%post
%{update_menus}
%endif


%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%files
%defattr (-,root,root)
%doc AUTHORS INSTALL NEWS COPYING README ChangeLog TODO THANKS
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man1/*

