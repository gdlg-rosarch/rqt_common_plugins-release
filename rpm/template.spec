Name:           ros-hydro-rqt-plot
Version:        0.3.12
Release:        0%{?dist}
Summary:        ROS rqt_plot package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_plot
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       PyQwt-devel
Requires:       python-matplotlib
Requires:       python-rospkg
Requires:       ros-hydro-qt-gui-py-common >= 0.2.25
Requires:       ros-hydro-rosgraph
Requires:       ros-hydro-rostopic
Requires:       ros-hydro-rqt-gui
Requires:       ros-hydro-rqt-gui-py
Requires:       ros-hydro-rqt-py-common
BuildRequires:  ros-hydro-catkin

%description
rqt_plot provides a GUI plugin visualizing numeric values in a 2D plot using
different plotting backends.

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
* Fri Jul 24 2015 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.12-0
- Autogenerated by Bloom

