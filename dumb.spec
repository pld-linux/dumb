Summary:	DUMB - Dedicated Universal Music Bastardisation
Summary(pl):	DUMB - Dedicated Universal Music Bastardisation
Name:		dumb
Version:	0.9.1
Release:	1
License:	GPL-like
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/dumb/%{name}-%{version}.tar.gz
# Source0-md5:	bf8a8cc3af4c5f6700b812b69a7cbb35
URL:		http://dumb.sourceforge.net/
BuildRequires:	allegro-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DUMB - Dedicated Universal Music Bastardisation library.

%description -l pl
Biblioteka DUMB - Dedicated Universal Music Bastardisation.

%prep
%setup -q -n %{name}

%build
./fix.sh unix
%{__make} all CC="%{__cc}" OFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

%{__make} install PREFIX=$RPM_BUILD_ROOT%{_prefix}
%{__make} install PREFIX=$RPM_BUILD_ROOT%{_prefix} DEBUGMODE=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt docs/*
%{_includedir}/*
%{_libdir}/*
