%define MS_REL %{nil}

Name:           mapcache%{MS_REL}
Version:        1.6.0
Release:        1%{?dist}
Summary:        Caching server for WMS layers

Group:          Development/Tools
License:        MIT
URL:            http://mapserver.org/mapcache/

Source0:        http://download.osgeo.org/mapserver/mapcache-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       webserver

BuildRequires:  httpd-devel fcgi-devel cmake libcurl-devel make gcc
BuildRequires:  geos-devel proj-devel gdal-devel libjpeg-turbo-devel
BuildRequires:  libpng-devel libtiff-devel pixman-devel sqlite-devel


%description
MapCache is a server that implements tile caching to speed up access to WMS layers. 
The primary objectives are to be fast and easily deployable, while offering the 
essential features (and more!) expected from a tile caching solution.

%prep
%setup -q -n mapcache-%{version}

%build
mkdir build
pushd build
%cmake ..
make
popd

%install
pushd build
rm -rf %{buildroot}
make DESTDIR=%{buildroot} \
    install
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL README* LICENSE 
%{_bindir}/*
%{_libdir}/libmapcache.so
%{_libdir}/libmapcache.so.1
%{_libdir}/libmapcache.so.%{version}

%changelog
