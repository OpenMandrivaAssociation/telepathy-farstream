%define major		0
%define libname		%mklibname %{name} %major
%define develname	%mklibname -d %{name}

Summary:	Stream Engine to handle media streaming channels
Name:		telepathy-farstream
Version:	0.1.2
Release:	%mkrel 1
Source0:	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
License:	LGPLv2+
Group:		Networking/Instant messaging
Url:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	dbus-glib-devel
BuildRequires:	libtelepathy-glib-devel >= 0.13.4
BuildRequires:	farsight2-devel
BuildRequires:	gstreamer0.10-python-devel
BuildRequires:	python-devel

%description
Stream Engine is a Telepathy client that uses Farsight and GStreamer
to handle media streaming channels. It's used as a background process
by other Telepathy clients, rather than presenting any user interface
of its own.

Telepathy is a D-Bus framework for unifying real time communication,
including instant messaging, voice calls and video calls. It abstracts
differences between protocols to provide a unified interface for
applications.

%package -n %{libname}
Group:		System/Libraries
Summary:	Stream Engine to handle media streaming channels

%description -n %{libname}
Stream Engine is a Telepathy client that uses Farsight and GStreamer
to handle media streaming channels. It's used as a background process
by other Telepathy clients, rather than presenting any user interface
of its own.

Telepathy is a D-Bus framework for unifying real time communication,
including instant messaging, voice calls and video calls. It abstracts
differences between protocols to provide a unified interface for
applications.

%package -n %{develname}
Group:		Development/C
Summary:	Stream Engine to handle media streaming channels
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Stream Engine is a Telepathy client that uses Farsight and GStreamer
to handle media streaming channels. It's used as a background process
by other Telepathy clients, rather than presenting any user interface
of its own.

Telepathy is a D-Bus framework for unifying real time communication,
including instant messaging, voice calls and video calls. It abstracts
differences between protocols to provide a unified interface for
applications.

%package -n python-%{name}
Group:		Development/Python
Summary:	Stream Engine to handle media streaming channels
Requires:	%{libname} = %{version}-%{release}
Requires:	gstreamer0.10-python

%description -n python-%{name}
Stream Engine is a Telepathy client that uses Farsight and GStreamer
to handle media streaming channels. It's used as a background process
by other Telepathy clients, rather than presenting any user interface
of its own.

Telepathy is a D-Bus framework for unifying real time communication,
including instant messaging, voice calls and video calls. It abstracts
differences between protocols to provide a unified interface for
applications.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# don't ship .la
find %{buildroot} -name "*.la" -delete

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libtelepathy-farstream.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog
%{_libdir}/libtelepathy-farstream.so
%{_includedir}/telepathy-1.0/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gtk-doc/html/%{name}

%files -n python-%{name}
%defattr(-,root,root)
%{python_sitearch}/tpfarstream.*


