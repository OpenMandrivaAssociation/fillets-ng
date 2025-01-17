Summary:	Fish Fillets NG
Name:		fillets-ng
Version:	1.0.1
Release:	3
License:	GPLv2+
Group:		Games/Puzzles
Url:		https://fillets.sourceforge.net/
Source0:	http://downloads.sourceforge.net/fillets/%{name}-%{version}.tar.gz
Source3:	%{name}-48.png
Source4:	%{name}-32.png
Source5:	%{name}-16.png
Requires:	%{name}-data
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_ttf)

%description
Fish Fillets NG is strictly a puzzle game. The goal in every of the seventy
levels is always the same: find a safe way out. The fish utter witty remarks
about their surroundings, the various inhabitants of their underwater realm
quarrel among themselves or comment on the efforts of your fish. The whole
game is accompanied by quiet, comforting music.

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_gamesbindir}/fillets
%{_mandir}/man6/*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir}/%{name}
%make

%install
%makeinstall_std

# Menu entry
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
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

