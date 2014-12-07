%define major	3
%define gmajor	0.6
%define libname	%mklibname %{name} %{major}
%define girname	%mklibname %{name}-gir %{gmajor}
%define devname	%mklibname -d %{name}

Summary:	Stream Engine to handle media streaming channels
Name:		telepathy-farstream
Version:	0.6.2
Release:	2
License:	LGPLv2+
Group:		Networking/Instant messaging
Url:		http://telepathy.freedesktop.org/wiki/
Source0:	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz.asc

BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(farstream-0.2)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
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

%description -n	%{libname}
Shared libraries for %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	Stream Engine to handle media streaming channels
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development library and header files for 
%{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libtelepathy-farstream.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/TelepathyFarstream-%{gmajor}.typelib

%files -n %{devname}
%doc ChangeLog
%{_includedir}/telepathy-1.0/%{name}
%{_libdir}/libtelepathy-farstream.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/TelepathyFarstream-%{gmajor}.gir
%doc %{_datadir}/gtk-doc/html/%{name}

