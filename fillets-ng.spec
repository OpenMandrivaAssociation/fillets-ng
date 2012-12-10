%define name fillets-ng
%define version 1.0.1
%define release %mkrel 1

%define dataversion 1.0.0

Summary: Fish Fillets NG
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group: Games/Puzzles
URL: http://fillets.sourceforge.net/
Source0: http://downloads.sourceforge.net/fillets/%{name}-%{version}.tar.gz
Source3: %{name}-48.png
Source4: %{name}-32.png
Source5: %{name}-16.png
Requires: %{name}-data = %{dataversion}
BuildRequires: lua-devel
BuildRequires: libSDL-devel
BuildRequires: libSDL_mixer-devel
BuildRequires: libSDL_image-devel
BuildRequires: libSDL_ttf-devel
BuildRequires: fribidi-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

%description
Fish Fillets NG is strictly a puzzle game. The goal in every of the seventy
levels is always the same: find a safe way out. The fish utter witty remarks
about their surroundings, the various inhabitants of their underwater realm
quarrel among themselves or comment on the efforts of your fish. The whole
game is accompanied by quiet, comforting music.

%prep
%setup -q

%build
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}/%{name}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# Menu entry
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Fish Fillets NG
Comment=Fish Fillets NG puzzle game
Exec= %{_gamesbindir}/fillets
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;LogicGame;
EOF

# Icon installation
install -D -m 644 %{SOURCE3} %{buildroot}%{_liconsdir}/%{name}.png
install -D -m 644 %{SOURCE4} %{buildroot}%{_iconsdir}/%{name}.png
install -D -m 644 %{SOURCE5} %{buildroot}%{_miconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_gamesbindir}/fillets
%{_mandir}/man6/*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Fri Oct 14 2011 Andrey Bondrov <abondrov@mandriva.org> 1.0.1-1mdv2011.0
+ Revision: 704658
- New version: 1.0.1

* Wed Jan 05 2011 Tomas Kindl <supp@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 628807
- update to 1.0.0

* Sat Dec 04 2010 Tomas Kindl <supp@mandriva.org> 0.9.3-2mdv2011.0
+ Revision: 609456
- rebuild

* Sat Feb 27 2010 Tomas Kindl <supp@mandriva.org> 0.9.3-1mdv2010.1
+ Revision: 512223
- bump to version 0.9.3
- drop unneeded fribidi patch

* Sun Oct 18 2009 Samuel Verschelde <stormi@mandriva.org> 0.9.2-2mdv2010.1
+ Revision: 458117
- fix data version
- update to new version 0.9.2

* Sat Jul 18 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.1-1mdv2010.0
+ Revision: 397215
- Update to new version 0.9.1

* Wed May 13 2009 Samuel Verschelde <stormi@mandriva.org> 0.8.1-2mdv2010.0
+ Revision: 375232
- fix Group and menu category (fixes #36371)
- fix licence

* Sun Mar 15 2009 Funda Wang <fwang@mandriva.org> 0.8.1-1mdv2009.1
+ Revision: 355308
- new data version
- New version 0.8.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 05 2008 Guillaume Bedot <littletux@mandriva.org> 0.8.0-1mdv2008.1
+ Revision: 179681
- 0.8.0

* Fri Jan 04 2008 Thierry Vignaud <tv@mandriva.org> 0.7.3-2mdv2008.1
+ Revision: 145271
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Sat Dec 02 2006 Olivier Blin <oblin@mandriva.com> 0.7.3-2mdv2007.0
+ Revision: 89938
- buildrequire lua-devel 5.0
- add xdg menu
- Import fillets-ng

* Fri Dec 23 2005 Anssi Hannula <anssi@mandriva.org> 0.7.3-1mdk
- 0.7.3
- fix BuildRequires
- split fillets-ng-data to another src.rpm
- bzip2 source
- use original binary name

* Thu Dec 22 2005 Götz Waschk <waschk@mandriva.org> 0.6.0-5mdk
- fix buildrequires for x86_64

* Wed Oct 12 2005 Götz Waschk <waschk@mandriva.org> 0.6.0-4mdk
- build fix for new tar
- rebuild for new liblua5

* Sat Oct 08 2005 Götz Waschk <waschk@mandriva.org> 0.6.0-3mdk
- build fix for new tar
- rebuild for new liblua5

* Mon Nov 01 2004 Michael Scherer <misc@mandrake.org> 0.6.0-2mdk
- Buildrequires

* Thu Oct 21 2004 Robert Vojta <robert.vojta@mandrake.cz> 0.6.0-1mdk
- Fish Fillets NG 0.6.0 release

