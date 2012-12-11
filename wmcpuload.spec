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



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 1.1.0pre4-9mdv2011.0
+ Revision: 634783
- simplify BR

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0pre4-8mdv2010.0
+ Revision: 434777
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0pre4-7mdv2009.0
+ Revision: 262017
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0pre4-6mdv2009.0
+ Revision: 256101
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0pre4-4mdv2008.1
+ Revision: 149787
- remove bogus dep on X11-libs, let's automatic deps handle that

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 21 2007 Thierry Vignaud <tv@mandriva.org> 1.1.0pre4-3mdv2008.1
+ Revision: 136446
- fix requires (#26584)
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Tue Aug 28 2007 Thierry Vignaud <tv@mandriva.org> 1.1.0pre4-2mdv2008.0
+ Revision: 72274
- convert menu to XDG
- use %%mkrel


* Mon Mar 21 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 1.1.0.pre4-1mdk
- pre4 release

* Sat Jul 17 2004 Franck Villaume <fvill@freesurf.fr> 1.1.0.pre2-1mdk
- new version 1.1.0.pre2
- fix spec file

* Thu Apr 10 2003 HA Quôc-Viêt <viet@mandrakesoft.com> 1.0.1-1mdk
- 1.0.1
- icons are converted from the archive instead of statically embedded

* Mon Jul 15 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-1mdk
- icons are now separate from sources
- 1.0.0

* Wed Mar 27 2002 HA Quôc-Viêt <viet@mandrakesoft.com> 0.9.0-1mdk
- New revision.
- xpm icons converted to png.
- workaround for installed names (binary and manpage).

* Mon Feb 11 2002 HA Quôc-Viêt <viet@mandrakesoft.com> 0.8.1-1mdk
- New revision.
- xpm icons converted to png (new MdK policy).

* Thu Jan 03 2002 HA Quôc-Viêt <viet@mandrakesoft.com> 0.8.0-2mdk
- The forgotten manpage has been added.

* Thu Jan 03 2002 HA Quôc-Viêt <viet@mandrakesoft.com> 0.8.0-1mdk
- New revision. Adds SMP support and tons of new options.
  See the README file.

* Wed Sep 19 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.7.1-1mdk
- New revision. Fixes a bug with event handling with enlightenment.
  Fixes a bug with blended-color in 2/8/16 depth.
  Adds a few options. See the Changelog file.

* Mon Aug 13 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.6.0-1mdk
- New revision : libdockapp is integrated now

* Wed Jul 25 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.5.6-1mdk
- New revision, icons are now integrated :o)

* Tue Jun 19 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.5.0-2mdk
- Added icons from the author Seiichi SATO <sato@cvs-net.co.jp>

* Tue Jun 05 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.5.0-1mdk
- New revision
- wrong commentaries fixed and my apologies to the author
  Seiichi SATO <sato@cvs-net.co.jp>

* Fri Jun 01 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.1.1-1mdk
- Initial packaging.

