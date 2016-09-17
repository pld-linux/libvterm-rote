#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
# TODO: static amd soname

Summary:	libvterm library
Summary(pl.UTF-8):	Bilblioteka libvterm
Name:		libvterm-rote
Version:	0.99.7
Release:	0.1
License:	GPLv2+
Group:		Libraries
Source0:	http://download.sourceforge.net/libvterm/libvterm-%{version}.tar.gz
# Source0-md5:	ac68b77eb33086f7532ab303245efb77
URL:		http://libvterm.sourceforge.net/
BuildRequires:	glib2-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

BuildRequires:	rpmbuild(macros) >= 1.583

%description
libvterm library.

%description -l pl.UTF-8
Biblioteka libvterm.

%package devel
Summary:	Header files for libvterm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvterm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libvterm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvterm.

%package static
Summary:	Static libvterm library
Summary(pl.UTF-8):	Statyczna biblioteka libvterm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libvterm library.

%description static -l pl.UTF-8
Statyczna biblioteka libvterm.

%prep
%setup -q -n libvterm

%build
%{__cc} %{rpmcflags} -D_REENTRANT -I/usr/include/ncurses -c -fPIC *.c `pkg-config --cflags glib-2.0`
LDFLAGS="%{rpmldflags}" %{__cc} -shared -o libvterm.so -lutil *.o

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_libdir},%{_includedir}}
install libvterm.so $RPM_BUILD_ROOT/%{_libdir}
install vterm.h $RPM_BUILD_ROOT/%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%attr(755,root,root) %{_libdir}/libvterm.so
#%attr(755,root,root) %ghost %{_libdir}/libvterm.so.N

%files devel
%defattr(644,root,root,755)
%doc API demo/*
%{_includedir}/vterm.h

%if 0
%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libvterm.a
%endif
%endif
