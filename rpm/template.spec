Name:           ros-indigo-rqt-common-plugins
Version:        0.3.13
Release:        0%{?dist}
Summary:        ROS rqt_common_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_common_plugins
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-rqt-action
Requires:       ros-indigo-rqt-bag
Requires:       ros-indigo-rqt-bag-plugins
Requires:       ros-indigo-rqt-console
Requires:       ros-indigo-rqt-dep
Requires:       ros-indigo-rqt-graph
Requires:       ros-indigo-rqt-image-view
Requires:       ros-indigo-rqt-launch
Requires:       ros-indigo-rqt-logger-level
Requires:       ros-indigo-rqt-msg
Requires:       ros-indigo-rqt-plot
Requires:       ros-indigo-rqt-publisher
Requires:       ros-indigo-rqt-py-common
Requires:       ros-indigo-rqt-py-console
Requires:       ros-indigo-rqt-reconfigure
Requires:       ros-indigo-rqt-service-caller
Requires:       ros-indigo-rqt-shell
Requires:       ros-indigo-rqt-srv
Requires:       ros-indigo-rqt-top
Requires:       ros-indigo-rqt-topic
Requires:       ros-indigo-rqt-web
BuildRequires:  ros-indigo-catkin

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
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Mar 08 2016 Aaron Blasdel <ablasdel@gmail.com> - 0.3.13-0
- Autogenerated by Bloom

* Fri Jul 24 2015 Aaron Blasdel <ablasdel@gmail.com> - 0.3.12-0
- Autogenerated by Bloom

* Sat May 02 2015 Aaron Blasdel <ablasdel@gmail.com> - 0.3.11-0
- Autogenerated by Bloom

