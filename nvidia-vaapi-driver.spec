Name:           nvidia-vaapi-driver
Summary:        VA-API driver for nvidia
License:        MIT
URL:            https://github.com/elFarto/nvidia-vaapi-driver
Obsoletes:      libva-vdpau-driver < 0.8

%global gitver 441c03d6315c37c6c1b3e0ea35c302cf370100f5

Version:        0.0.3
Release:        1.%{gitver}%{?dist}
Source0:        https://github.com/elFarto/nvidia-vaapi-driver/archive/%{gitver}.zip

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0)
BuildRequires:  pkgconfig(ffnvcodec)
Requires:       mesa-dri-filesystem

%description
This is an VA-API implementation that uses NVDEC as a backend.

%prep
%setup -n %{name}-%{gitver}

%build
%meson
%meson_build

%install
%meson_install

%files
%{_libdir}/dri/nvidia_drv_video.so
