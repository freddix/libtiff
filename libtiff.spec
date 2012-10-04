Summary:	Library for handling TIFF files
Name:		libtiff
Version:	4.0.3
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/pub/libtiff/tiff-%{version}.tar.gz
# Source0-md5:	051c1068e6a0627f461948c365290410
Patch0:		%{name}-glut.patch
URL:		http://www.remotesensing.org/libtiff/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freeglut-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is a library of functions that manipulate TIFF images.

%package devel
Summary:	Header files for developing programs using libtiff
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package is all you need to develop programs that manipulate tiff
images.

%package cxx
Summary:	libtiff C++ streams library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description cxx
libtiff C++ streams library.

%package cxx-devel
Summary:	libtiff C++ streams API
Group:		Development/Libraries
Requires:	%{name}-cxx = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description cxx-devel
libtiff C++ streams API.

%package progs
Summary:	Simple clients for manipulating tiff images
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
Simple clients for manipulating tiff images.


%prep
%setup -qn tiff-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf html{,/*}/Makefile* $RPM_BUILD_ROOT%{_docdir}/tiff-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog README TODO
%attr(755,root,root) %ghost %{_libdir}/libtiff.so.?
%attr(755,root,root) %{_libdir}/libtiff.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc html/*
%attr(755,root,root) %{_libdir}/libtiff.so
%{_libdir}/libtiff.la
%{_includedir}/tiff*.h
%{_pkgconfigdir}/libtiff-4.pc
%{_mandir}/man3/*

%files cxx
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libtiffxx.so.?
%attr(755,root,root) %{_libdir}/libtiffxx.so.*.*.*

%files cxx-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtiffxx.so
%{_libdir}/libtiffxx.la
%{_includedir}/tiffio.hxx

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

