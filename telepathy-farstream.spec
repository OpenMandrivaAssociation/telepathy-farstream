%define major		2
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname -d %{name}

Summary:	Stream Engine to handle media streaming channels
Name:		telepathy-farstream
Version:	0.4.0
Release:	1
License:	LGPLv2+
Group:		Networking/Instant messaging
Url:		http://telepathy.freedesktop.org/wiki/
Source0:	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	farsight2-devel
BuildRequires:	pkgconfig(gst-python-0.10)
BuildRequires:	pkgconfig(farstream-0.1)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(telepathy-glib) >= 0.13.4

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
This package contains the development library and header files for %{name}.

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

%files -n %{libname}
%{_libdir}/libtelepathy-farstream.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_libdir}/libtelepathy-farstream.so
%{_includedir}/telepathy-1.0/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gtk-doc/html/%{name}

%files -n python-%{name}
%doc README NEWS
%{python_sitearch}/tpfarstream.*

