Summary:	DUMB - Dedicated Universal Music Bastardisation
Summary(pl.UTF-8):   DUMB - Dedicated Universal Music Bastardisation
Name:		dumb
Version:	0.9.3
Release:	1
License:	GPL-like
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/dumb/%{name}-%{version}.tar.gz
# Source0-md5:	f48da5b990aa8aa822d3b6a951baf5c2
URL:		http://dumb.sourceforge.net/
BuildRequires:	allegro-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	 -fomit-frame-pointer 

%description
DUMB - Dedicated Universal Music Bastardisation library.

%description -l pl.UTF-8
Biblioteka DUMB - Dedicated Universal Music Bastardisation.

%package devel
Summary:	Header files for dumb
Summary(pl.UTF-8):   Pliki nagłówkowe dla dumb
Group:		Development/Libraries
Requires:	%{name}-static = %{version}-%{release}

%description devel
dumb header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla dumb.

%package static
Summary:	Static libraries for dumb
Summary(pl.UTF-8):   Statyczne biblioteki dla dumb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
dumb static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne dla dumb.

%prep
%setup -q

%build
cat <<EOF > make/config.txt
include make/unix.inc
ALL_TARGETS := core core-examples core-headers
ALL_TARGETS += allegro allegro-examples allegro-headers
PREFIX := /usr
EOF

%{__make} all \
	CC="%{__cc}" \
	OFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_bindir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} DEBUGMODE=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt docs/*
%attr(755,root,root) %{_bindir}/dumb*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
