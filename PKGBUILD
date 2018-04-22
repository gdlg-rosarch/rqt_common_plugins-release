# Script generated with Bloom
pkgdesc="ROS - rqt_logger_level provides a GUI plugin for configuring the logger level of ROS nodes.<br/> <br/> rqt_logger_level takes over `wx`-based tool [[rxloggerlevel]]."
url='http://ros.org/wiki/rqt_logger_level'

pkgname='ros-kinetic-rqt-logger-level'
pkgver='0.4.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('python2-rospkg'
'ros-kinetic-python-qt-binding>=0.2.19'
'ros-kinetic-rosnode'
'ros-kinetic-rospy'
'ros-kinetic-rosservice'
'ros-kinetic-rqt-gui'
'ros-kinetic-rqt-gui-py'
)

conflicts=()
replaces=()

_dir=rqt_logger_level
source=()
md5sums=()

prepare() {
    cp -R $startdir/rqt_logger_level $srcdir/rqt_logger_level
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

