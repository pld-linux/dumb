# TODO: don't build debug version of libraries when not packaging them
#
# Conditional build:
%bcond_without	allegro		# Allegro libraries
%bcond_without	debug_libs	# debug libraries packaging (they are built anyway)
#
Summary:	DUMB - Dynamic Universal Music Bibliotheque
Summary(pl.UTF-8):	DUMB - uniwersalna biblioteka do odtwarzania muzyki
Name:		dumb
Version:	0.9.3
Release:	6
License:	GPL-like
Group:		Development/Libraries
Source0:	http://downloads.sourceforge.net/dumb/%{name}-%{version}.tar.gz
# Source0-md5:	f48da5b990aa8aa822d3b6a951baf5c2
Patch0:		%{name}-shared.patch
URL:		http://dumb.sourceforge.net/
%{?with_allegro:BuildRequires:	allegro-devel}
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32		-fomit-frame-pointer

%description
DUMB (Dynamic Universal Music Bibliotheque, formerly Dedicated
Universal Music Bastardisation) - IT, XM, S3M and MOD player library.

%description -l pl.UTF-8
DUMB (Dynamic Universal Music Bibliotheque, dawniej Dedicated
Universal Music Bastardisation) - biblioteka do odtwarzania muzyki w
formatach IT, XM, S3M i MOD.

%package devel
Summary:	Header files for DUMB library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki DUMB
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for DUMB library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki DUMB.

%package static
Summary:	Static DUMB libraries
Summary(pl.UTF-8):	Statyczne biblioteki DUMB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static DUMB libraries.

%description static -l pl.UTF-8
Statyczne biblioteki DUMB.

%package allegro
Summary:	DUMB Allegro library
Summary(pl.UTF-8):	Biblioteka DUMB dla Allegro
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description allegro
DUMB Allegro library.

%description allegro -l pl.UTF-8
Biblioteka DUMB dla Allegro.

%package allegro-devel
Summary:	Header files for DUMB Allegro library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki DUMB dla Allegro
Group:		Development/Libraries
Requires:	%{name}-allegro = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	allegro-devel

%description allegro-devel
Header files for DUMB Allegro library.

%description allegro-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki DUMB dla Allegro.

%package allegro-static
Summary:	Static DUMB Allegro libraries
Summary(pl.UTF-8):	Statyczne biblioteki DUMB dla Allegro
Group:		Development/Libraries
Requires:	%{name}-allegro-devel = %{version}-%{release}

%description allegro-static
Static DUMB Allegro libraries.

%description allegro-static -l pl.UTF-8
Statyczne biblioteki DUMB dla Allegro.

%prep
%setup -q
%patch -P0 -p1

%build
cat <<EOF > make/config.txt
include make/unix.inc
ALL_TARGETS := core core-examples core-headers
%if %{with allegro}
ALL_TARGETS += allegro allegro-examples allegro-headers
%endif
PREFIX := /usr
EOF

%{__make} -j1 all \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	OFLAGS="%{rpmcflags}" \
	DBGFLAGS="-DDEBUGMODE=1 %{rpmcflags}" \
	LIB_INSTALL_PATH=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_bindir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	LIB_INSTALL_PATH=$RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	allegro -p /sbin/ldconfig
%postun	allegro -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.txt docs/*.txt
%attr(755,root,root) %{_bindir}/dumb2wav
%attr(755,root,root) %{_bindir}/dumbout
%attr(755,root,root) %{_libdir}/libdumb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdumb.so.0
%if %{with debug_libs}
%attr(755,root,root) %{_libdir}/libdumbd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdumbd.so.0
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdumb.so
%{_libdir}/libdumb.la
%if %{with debug_libs}
%attr(755,root,root) %{_libdir}/libdumbd.so
%{_libdir}/libdumbd.la
%endif
%{_includedir}/dumb.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libdumb.a
%if %{with debug_libs}
%{_libdir}/libdumbd.a
%endif

%files allegro
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dumbplay
%attr(755,root,root) %{_libdir}/libaldmb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaldmb.so.0
%if %{with debug_libs}
%attr(755,root,root) %{_libdir}/libaldmd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaldmd.so.0
%endif

%files allegro-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaldmb.so
%{_libdir}/libaldmb.la
%if %{with debug_libs}
%attr(755,root,root) %{_libdir}/libaldmd.so
%{_libdir}/libaldmd.la
%endif
%{_includedir}/aldumb.h

%files allegro-static
%defattr(644,root,root,755)
%{_libdir}/libaldmb.a
%if %{with debug_libs}
%{_libdir}/libaldmd.a
%endif
