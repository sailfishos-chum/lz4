Summary: Extremely Fast Compression algorithm
Name: lz4
Version: 1.9.3.1
Release: 1%{?dist}
License: BSD-type license
Group: Libraries/Databases
URL: https://github.com/lz4/lz4

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
#Requires: pango

# just for good measure: retire for SFOS versions >= 5.1
%if 0%{?sailfishos_version} >= 50100
ExclusiveArch: none
%endif

%description
LZ4 is lossless compression algorithm

PackageName: LZ4
Categories:
  - Library

%package        libs
Summary:        Libaries for lz4

%description    libs
This package contains the libaries for lz4.

%package        static
Summary:        Static library for lz4

%description    static
LZ4 is an extremely fast loss-less compression algorithm. This package
contains static libraries for static linking of applications.

%package devel
Summary: lz4 development headers and static library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
LZ4 is lossless compression algorithm. This
package provides libraries and headers for development

PackageName: LZ4 Development
Categories:
  - Library

%prep
%setup -q -n %{name}-%{version}/lz4

%build
%{__make} clean || true

CFLAGS="$CFLAGS -fPIC"
CXXFLAGS="$CXXFLAGS -fPIC"

%{__make} prefix=/usr %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install prefix=%{_prefix} LIBDIR=%{_libdir} DESTDIR=%{buildroot}
%{__rm} -rf %{buildroot}/%{_mandir}

%clean
%{__rm} -rf %{buildroot}

%pre

%post -n lz4 -p /sbin/ldconfig

%postun -n lz4 -p /sbin/ldconfig

%files
%license programs/COPYING
%{_bindir}/lz4
%{_bindir}/lz4c
%{_bindir}/lz4cat
%{_bindir}/unlz4

%files libs
%doc lib/LICENSE
%{_libdir}/liblz4.so.*

%files devel
%{_includedir}/lz4*.h
%{_libdir}/liblz4.so
%{_libdir}/pkgconfig/liblz4.pc

%files static
%doc lib/LICENSE
%{_libdir}/liblz4.a

%changelog
* Sat May  9 2026 nephros <sailfish@nephros.org>  - 1.8.1.3
- retire package from Chum (as Sailfish OS 5.1 ships it)
* Thu Mar 29 2018 rinigus <rinigus.git@gmail.com> - 1.8.1.2
- initial packaging release for SFOS
