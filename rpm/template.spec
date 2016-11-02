Name:           ros-indigo-rqt-shell
Version:        0.4.3
Release:        0%{?dist}
Summary:        ROS rqt_shell package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_shell
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-rospkg
Requires:       ros-indigo-python-qt-binding >= 0.2.19
Requires:       ros-indigo-qt-gui
Requires:       ros-indigo-qt-gui-py-common
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-py
BuildRequires:  ros-indigo-catkin

%description
rqt_shell is a Python GUI plugin providing an interactive shell.

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
* Wed Nov 02 2016 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.4.3-0
- Autogenerated by Bloom

* Tue Mar 08 2016 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.13-0
- Autogenerated by Bloom

* Fri Jul 24 2015 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.12-0
- Autogenerated by Bloom

* Sat May 02 2015 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.11-0
- Autogenerated by Bloom

* Wed Oct 01 2014 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.10-0
- Autogenerated by Bloom

* Mon Aug 18 2014 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.9-0
- Autogenerated by Bloom

