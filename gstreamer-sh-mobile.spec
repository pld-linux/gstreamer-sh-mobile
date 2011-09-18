Summary:	GStreamer plugins that provide accelerated video encode and decode, scale and blend for SH-Mobile
Summary(pl.UTF-8):	Wtyczki GStreamera zapewniające akcelerowane kodowanie i dekodowanie oraz skalowanie i konwersji kolorów obrazu dla SH-Mobile
Name:		gstreamer-sh-mobile
Version:	0.10.2
Release:	0.1
License:	LGPL v2+
Group:		Libraries
# trailing #/gst-sh-mobile-%{version}.tar.gz is a hack for df
#Source0Download: https://oss.renesas.com/modules/document/?GStreamer
Source0:	https://oss.renesas.com/modules/document/gate.php/?way=attach&refer=GStreamer&openfile=gst-sh-mobile-%{version}.tar.gz#/gst-sh-mobile-%{version}.tar.gz
# Source0-md5:	d5f16c448f9afc7b4f99746e8cb8804b
URL:		https://oss.renesas.com/modules/document/?GStreamer
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.10
BuildRequires:	doxygen
BuildRequires:	gstreamer-devel >= 0.10.16
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.16
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libshbeu-devel >= 1.0.0
BuildRequires:	libshcodecs-devel >= 1.4.0
BuildRequires:	libshveu-devel >= 1.5.0
BuildRequires:	libuiomux-devel >= 1.5.0
BuildRequires:	pkgconfig
Requires:	libshbeu >= 1.0.0
Requires:	libshcodecs >= 1.4.0
Requires:	libshveu >= 1.5.0
Requires:	libuiomux >= 1.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains hardware accelerated GStreamer elements for
SH-Mobile devices that perform video encode, decode, scale and
colorspace conversion.

%description -l pl.UTF-8
Ten pakiet zawiera elementy GStreamera zapewniające sprzętową
akcelerację dla urządzeń SH-Mobile, wykonujące kodowanie, dekodowanie,
skalowanie obrazu oraz konwersję przestrzeni kolorów.

%prep
%setup -q -n gst-sh-mobile-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# gstreamer module
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/libgst*.la
# don't package source code documentation
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gst-shmobile

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstshvideo.so
