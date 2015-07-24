Name:           ros-hydro-rqt-image-view
Version:        0.3.12
Release:        0%{?dist}
Summary:        ROS rqt_image_view package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_image_view
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-cv-bridge
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-rqt-gui
Requires:       ros-hydro-rqt-gui-cpp
Requires:       ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-rqt-gui
BuildRequires:  ros-hydro-rqt-gui-cpp
BuildRequires:  ros-hydro-sensor-msgs

%description
rqt_image_view provides a GUI plugin for displaying images using
image_transport.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Jul 24 2015 Aaron Blasdel <ablasdel@gmail.com> - 0.3.12-0
- Autogenerated by Bloom

