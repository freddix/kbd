Summary:	Linux console utilities
Name:		kbd
Version:	2.0.2
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	ftp://ftp.altlinux.org/pub/people/legion/kbd/%{name}-%{version}.tar.gz
# Source0-md5:	f1f75f0dd5f7dde89ce47585274366f8
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
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/gr

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/*
%dir %{_ldatadir}
%{_ldatadir}/console*
%{_ldatadir}/keymaps
%{_ldatadir}/unimaps
%{_mandir}/man?/*

