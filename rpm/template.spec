Name:           ros-lunar-rqt-common-plugins
Version:        0.4.8
Release:        0%{?dist}
Summary:        ROS rqt_common_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_common_plugins
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-rqt-action
Requires:       ros-lunar-rqt-bag
Requires:       ros-lunar-rqt-bag-plugins
Requires:       ros-lunar-rqt-console
Requires:       ros-lunar-rqt-dep
Requires:       ros-lunar-rqt-graph
Requires:       ros-lunar-rqt-image-view
Requires:       ros-lunar-rqt-launch
Requires:       ros-lunar-rqt-logger-level
Requires:       ros-lunar-rqt-msg
Requires:       ros-lunar-rqt-plot
Requires:       ros-lunar-rqt-publisher
Requires:       ros-lunar-rqt-py-common
Requires:       ros-lunar-rqt-py-console
Requires:       ros-lunar-rqt-reconfigure
Requires:       ros-lunar-rqt-service-caller
Requires:       ros-lunar-rqt-shell
Requires:       ros-lunar-rqt-srv
Requires:       ros-lunar-rqt-top
Requires:       ros-lunar-rqt-topic
Requires:       ros-lunar-rqt-web
BuildRequires:  ros-lunar-catkin

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
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri Apr 28 2017 Aaron Blasdel <ablasdel@gmail.com> - 0.4.8-0
- Autogenerated by Bloom

