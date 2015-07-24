Name:           ros-jade-rqt-common-plugins
Version:        0.3.12
Release:        0%{?dist}
Summary:        ROS rqt_common_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_common_plugins
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-rqt-action
Requires:       ros-jade-rqt-bag
Requires:       ros-jade-rqt-bag-plugins
Requires:       ros-jade-rqt-console
Requires:       ros-jade-rqt-dep
Requires:       ros-jade-rqt-graph
Requires:       ros-jade-rqt-image-view
Requires:       ros-jade-rqt-launch
Requires:       ros-jade-rqt-logger-level
Requires:       ros-jade-rqt-msg
Requires:       ros-jade-rqt-plot
Requires:       ros-jade-rqt-publisher
Requires:       ros-jade-rqt-py-common
Requires:       ros-jade-rqt-py-console
Requires:       ros-jade-rqt-reconfigure
Requires:       ros-jade-rqt-service-caller
Requires:       ros-jade-rqt-shell
Requires:       ros-jade-rqt-srv
Requires:       ros-jade-rqt-top
Requires:       ros-jade-rqt-topic
Requires:       ros-jade-rqt-web
BuildRequires:  ros-jade-catkin

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

