Name:           ros-hydro-rqt-msg
Version:        0.3.12
Release:        0%{?dist}
Summary:        ROS rqt_msg package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_msg
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-rospkg
Requires:       ros-hydro-roslib
Requires:       ros-hydro-rosmsg
Requires:       ros-hydro-rospy
Requires:       ros-hydro-rqt-console
Requires:       ros-hydro-rqt-gui
Requires:       ros-hydro-rqt-gui-py
Requires:       ros-hydro-rqt-py-common
BuildRequires:  ros-hydro-catkin

%description
A Python GUI plugin for introspecting available ROS message types. Note that the
msgs available through this plugin is the ones that are stored on your machine,
not on the ROS core your rqt instance connects to.

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

