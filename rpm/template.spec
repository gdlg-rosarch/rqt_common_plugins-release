Name:           ros-kinetic-rqt-common-plugins
Version:        0.4.0
Release:        1%{?dist}
Summary:        ROS rqt_common_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_common_plugins
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-rqt-action
Requires:       ros-kinetic-rqt-bag
Requires:       ros-kinetic-rqt-bag-plugins
Requires:       ros-kinetic-rqt-console
Requires:       ros-kinetic-rqt-dep
Requires:       ros-kinetic-rqt-graph
Requires:       ros-kinetic-rqt-image-view
Requires:       ros-kinetic-rqt-launch
Requires:       ros-kinetic-rqt-logger-level
Requires:       ros-kinetic-rqt-msg
Requires:       ros-kinetic-rqt-plot
Requires:       ros-kinetic-rqt-publisher
Requires:       ros-kinetic-rqt-py-common
Requires:       ros-kinetic-rqt-py-console
Requires:       ros-kinetic-rqt-reconfigure
Requires:       ros-kinetic-rqt-service-caller
Requires:       ros-kinetic-rqt-shell
Requires:       ros-kinetic-rqt-srv
Requires:       ros-kinetic-rqt-top
Requires:       ros-kinetic-rqt-topic
Requires:       ros-kinetic-rqt-web
BuildRequires:  ros-kinetic-catkin

%description
rqt_common_plugins metapackage provides ROS backend graphical tools suite that
can be used on/off of robot runtime. To run any rqt plugins, just type in a
single command &quot;rqt&quot;, then select any plugins you want from the GUI
that launches afterwards. rqt consists of three following metapackages: rqt -
core modules of rqt (ROS GUI) framework. rqt plugin developers barely needs to
pay attention to this metapackage. rqt_common_plugins (you're here!)
rqt_robot_plugins - rqt plugins that are particularly used with robots during
their runtime.

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
* Fri Apr 29 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.4.0-1
- Autogenerated by Bloom

* Wed Apr 27 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.4.0-0
- Autogenerated by Bloom

