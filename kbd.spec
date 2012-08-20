Summary:	Linux console utilities
Name:		kbd
Version:	1.15.3
Release:	3
License:	GPL
Group:		Applications/Console
Source0:	ftp://ftp.altlinux.org/pub/people/legion/kbd/%{name}-%{version}.tar.gz
# Source0-md5:	8143e179a0f3c25646ce5085e8777200
Source1:	lat2u-16.psf
Source2:	lat2u.sfm
Source10:	%{name}-pl1.kmap
Source11:	%{name}-mac-pl.kmap
Source12:	%{name}-pl3.map
Source13:	%{name}-pl4.map
#
Patch0:		%{name}-unicode_start.patch
Patch1:		%{name}-defkeymap.patch
Patch2:		%{name}-po.patch
URL:		http://www.win.tue.nl/~aeb/linux/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
Requires:	sed
Requires:	util-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ldatadir	%{_datadir}/%{name}

%description
This package contains utilities to load console fonts and keyboard
maps. It also includes a number of different fonts and keyboard maps.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--datadir=%{_ldatadir}	\
	--enable-nls		\
	--localedir=%{_datadir}/locale
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale

install %{SOURCE1} $RPM_BUILD_ROOT%{_ldatadir}/consolefonts/lat2u-16.psfu
install %{SOURCE2} $RPM_BUILD_ROOT%{_ldatadir}/unimaps/lat2u.uni

install %{SOURCE10} $RPM_BUILD_ROOT%{_ldatadir}/keymaps/i386/qwerty/pl1.map
install %{SOURCE11} $RPM_BUILD_ROOT%{_ldatadir}/keymaps/mac/all/mac-pl.map
install %{SOURCE12} $RPM_BUILD_ROOT%{_ldatadir}/keymaps/i386/qwerty/pl3.map
install %{SOURCE13} $RPM_BUILD_ROOT%{_ldatadir}/keymaps/i386/qwerty/pl4.map

rm -f doc/{*,*/*}.sgml
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/gr

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README doc/*.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_ldatadir}
%{_ldatadir}/console*
%{_ldatadir}/keymaps
%{_ldatadir}/unimaps
%{_mandir}/man?/*

