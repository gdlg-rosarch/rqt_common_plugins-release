Name:           ros-indigo-rqt-graph
Version:        0.3.10
Release:        0%{?dist}
Summary:        ROS rqt_graph package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_graph
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-rospkg
Requires:       ros-indigo-qt-dotgraph
Requires:       ros-indigo-rosgraph
Requires:       ros-indigo-rosgraph-msgs
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rosnode
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rosservice
Requires:       ros-indigo-rostopic
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-py
BuildRequires:  ros-indigo-catkin

%description
rqt_graph provides a GUI plugin for visualizing the ROS computation graph. Its
components are made generic so that other packages where you want to achieve
graph representation can depend upon this pkg (use rqt_dep to find out the pkgs
that depend. rqt_dep itself depends on rqt_graph too).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Oct 01 2014 Aaron Blasdel <ablasdel@gmail.com> - 0.3.10-0
- Autogenerated by Bloom

* Mon Aug 18 2014 Aaron Blasdel <ablasdel@gmail.com> - 0.3.9-0
- Autogenerated by Bloom

