%bcond_with x

Name:           xf86-video-fbdev
Version:        0.4.4
Release:        0
License:        MIT
Summary:        Framebuffer video driver for the Xorg X server
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Servers/XF86_4
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Source1001: 	xf86-video-fbdev.manifest
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.0.99.901
BuildRequires:  pkgconfig(xproto)

%if !%{with x}
ExclusiveArch:
%endif

%description
fbdev is an Xorg driver for framebuffer devices.

This is a non-accelerated driver, the following framebuffer depths are
supported: 8, 15, 16, 24. All visual types are supported for depth 8,
and TrueColor visual is supported for the other depths. Multi-head
configurations are supported.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen
make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%doc COPYING
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/fbdev_drv.so
%{_mandir}/man4/fbdev.4%{?ext_man}

%changelog
