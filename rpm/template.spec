Name:           ros-jade-rqt-msg
Version:        0.3.12
Release:        0%{?dist}
Summary:        ROS rqt_msg package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_msg
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-rospkg
Requires:       ros-jade-roslib
Requires:       ros-jade-rosmsg
Requires:       ros-jade-rospy
Requires:       ros-jade-rqt-console
Requires:       ros-jade-rqt-gui
Requires:       ros-jade-rqt-gui-py
Requires:       ros-jade-rqt-py-common
BuildRequires:  ros-jade-catkin

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
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Jul 24 2015 Aaron Blasdel <ablasdel@gmail.com> - 0.3.12-0
- Autogenerated by Bloom

* Thu Apr 30 2015 Aaron Blasdel <ablasdel@gmail.com> - 0.3.11-0
- Autogenerated by Bloom

