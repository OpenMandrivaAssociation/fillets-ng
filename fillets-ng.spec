%define name fillets-ng
%define version 0.8.0
%define release %mkrel 1

%define dataversion 0.8.0

Summary: Fish Fillets NG
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL 
Group: Games/Arcade
URL: http://fillets.sourceforge.net/
Source0: http://downloads.sourceforge.net/fillets/%{name}-%{version}.tar.gz
Source3: %{name}-48.png
Source4: %{name}-32.png
Source5: %{name}-16.png
Requires: %{name}-data = %{dataversion}
Requires: soundwrapper
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
perl -pi -e "s|-lualib ||" configure

%build
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}/%{name}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# Menu entry
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Fish Fillets NG
Comment=Fish Fillets NG puzzle game
Exec=soundwrapper %_gamesbindir/fillets
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

# Icon installation
install -D -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -D -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%update_menus
%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_gamesbindir}/fillets
%{_mandir}/man6/*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop

