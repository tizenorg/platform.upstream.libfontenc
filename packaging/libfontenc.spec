#sbs-git:slp/pkgs/xorg/lib/libfontenc libfontenc 1.1.0 f90008750770748ef68ee2c0ec1c7c9d3ecb4980

Name:           libfontenc
Version:        1.1.0
Release:        3
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
font encoding library

%package devel
Summary:        X
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
font encoding library development package

%prep
%setup -q

%build

./autogen.sh
%configure --disable-static \
    --with-encodingsdir=%{_datadir}/fonts/X11/encodings

make %{?_smp_mflags}

%install
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
%doc COPYING README ChangeLog
%{_libdir}/libfontenc.so.1
%{_libdir}/libfontenc.so.1.0.0


%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/fontenc.h
%{_libdir}/libfontenc.so
%{_libdir}/pkgconfig/fontenc.pc

