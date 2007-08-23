%define	name	wmcpuload
%define version 1.1.0pre4
%define release %mkrel 2

Summary: WindowMaker dock application that displays CPU usage
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphical desktop/WindowMaker
Source:		%name-%{version}.tar.bz2
URL:		http://www.sh.rim.or.jp/~ssato/dockapp/index.shtml
Requires:	X11-libs, xpm
BuildRequires:	X11-devel, xpm-devel, ImageMagick
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
A dockapp to monitor cpu load for WindowMaker. It works fine with AfterStep
and BlackBox and has SMP support.

%prep

%setup -q
%configure --prefix %{_prefix}

%build
%make

%install
%makeinstall
#[ -d %buildroot ] && rm -rf %buildroot

#install -m 755 -d %buildroot%prefix/bin
#install -m 755 src/%name %buildroot%prefix/bin/

#install -m 755 -d %buildroot%_mandir/man1
#install -m 755 doc/%name.1 %buildroot%_mandir/man1/

install -m 755 -d %buildroot%{_miconsdir}
install -m 755 -d %buildroot%{_iconsdir}
install -m 755 -d %buildroot%{_liconsdir}

convert icons/wmcpuload-16x16.xpm $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png
convert icons/wmcpuload-32x32.xpm $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
convert icons/wmcpuload-48x48.xpm $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png


install -m 755 -d %buildroot%{_menudir}
cat << EOF > %buildroot%{_menudir}/%{name}
?package(%{name}):command="%{_prefix}/bin/%{name}" icon="%{name}.png"\\
                  needs="X11" section="Applications/Monitoring" \\
                  title="WmCPULoad" longtitle="CPU monitoring in a dockapp"
EOF


%clean
[ -z %buildroot ] || {
    rm -rf %buildroot
}


%post
%{update_menus}


%postun
%{clean_menus}


%files
%defattr (-,root,root)
%doc AUTHORS INSTALL NEWS COPYING README ChangeLog TODO THANKS
%{_prefix}/bin/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_menudir}/%{name}
%{_mandir}/man1/*

