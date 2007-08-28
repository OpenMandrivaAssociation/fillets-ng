%define name fillets-ng
%define version 0.7.3
%define release %mkrel 2

%define dataversion 0.7.1

Summary: Fish Fillets NG
Name:    %{name}
Version: %{version}
Release: %{release}
License: GPL 
Group:   Games/Arcade
URL:     http://fillets.sourceforge.net/
Source0: %{name}-%{version}.tar.bz2
Source3: %{name}-48.png
Source4: %{name}-32.png
Source5: %{name}-16.png
Requires: %{name}-data = %{dataversion}
BuildRequires: lua5.0-devel
BuildRequires: libSDL-devel, libSDL_mixer-devel, libSDL_image-devel
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
# Doesn't work without --with-lua, don't know why
%configure2_5x --with-lua=/usr --bindir=%{_gamesbindir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# Menu entry
mkdir -p $RPM_BUILD_ROOT/%{_menudir}
cat > $RPM_BUILD_ROOT/%{_menudir}/%{name} << EOF
?package(%{name}): \
command="%{_gamesbindir}/fillets" \
icon="%{name}.png" \
section="More Applications/Games/Arcade" \
title="Fish Fillets NG" \
longtitle="Fish Fillets NG" \
needs="x11"
EOF

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

%post
%update_menus

%postun
%update_menus

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_gamesbindir}/fillets
%{_mandir}/man6/*
%{_menudir}/%{name}
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop

