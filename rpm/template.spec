Name:           ros-kinetic-rqt-dep
Version:        0.4.0
Release:        1%{?dist}
Summary:        ROS rqt_dep package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_dep
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-rospkg
Requires:       ros-kinetic-python-qt-binding >= 0.2.19
Requires:       ros-kinetic-qt-dotgraph
Requires:       ros-kinetic-qt-gui
Requires:       ros-kinetic-qt-gui-py-common
Requires:       ros-kinetic-rqt-graph
Requires:       ros-kinetic-rqt-gui-py
BuildRequires:  python-mock
BuildRequires:  ros-kinetic-catkin

%description
rqt_dep provides a GUI plugin for visualizing the ROS dependency graph.

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

