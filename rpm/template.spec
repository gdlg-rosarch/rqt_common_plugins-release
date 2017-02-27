Name:           ros-kinetic-rqt-srv
Version:        0.4.6
Release:        0%{?dist}
Summary:        ROS rqt_srv package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_srv
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-rosmsg
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rqt-gui
Requires:       ros-kinetic-rqt-gui-py
Requires:       ros-kinetic-rqt-msg
BuildRequires:  ros-kinetic-catkin

%description
A Python GUI plugin for introspecting available ROS message types. Note that the
srvs available through this plugin is the ones that are stored on your machine,
not on the ROS core your rqt instance connects to.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Feb 27 2017 Aaron Blasdel <ablasdel@gmail.com> - 0.4.6-0
- Autogenerated by Bloom

* Fri Feb 03 2017 Aaron Blasdel <ablasdel@gmail.com> - 0.4.5-0
- Autogenerated by Bloom

* Tue Jan 24 2017 Aaron Blasdel <ablasdel@gmail.com> - 0.4.4-0
- Autogenerated by Bloom

* Wed Nov 02 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.4.3-0
- Autogenerated by Bloom

* Mon Sep 19 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.4.2-0
- Autogenerated by Bloom

* Mon May 16 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.4.1-0
- Autogenerated by Bloom

* Fri Apr 29 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.4.0-1
- Autogenerated by Bloom

* Wed Apr 27 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.4.0-0
- Autogenerated by Bloom

