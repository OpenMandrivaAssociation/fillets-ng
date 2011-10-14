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

