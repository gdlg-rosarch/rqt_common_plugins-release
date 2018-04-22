# Script generated with Bloom
pkgdesc="ROS - rqt_common_plugins metapackage provides ROS backend graphical tools suite that can be used on/off of robot runtime.<br/> <br/> To run any rqt plugins, just type in a single command &quot;rqt&quot;, then select any plugins you want from the GUI that launches afterwards.<br/> <br/> rqt consists of three following metapackages:<br/> <ul> <li><a href="http://ros.org/wiki/rqt">rqt</a> - core modules of rqt (ROS GUI) framework. rqt plugin developers barely needs to pay attention to this metapackage.</li> <li>rqt_common_plugins (you're here!)</li> <li><a href="http://ros.org/wiki/rqt_robot_plugins">rqt_robot_plugins</a> - rqt plugins that are particularly used with robots during their runtime.</li><br/> </ul> <br/>"
url='http://ros.org/wiki/rqt_common_plugins'

pkgname='ros-kinetic-rqt-common-plugins'
pkgver='0.4.8_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-rqt-action'
'ros-kinetic-rqt-bag'
'ros-kinetic-rqt-bag-plugins'
'ros-kinetic-rqt-console'
'ros-kinetic-rqt-dep'
'ros-kinetic-rqt-graph'
'ros-kinetic-rqt-image-view'
'ros-kinetic-rqt-launch'
'ros-kinetic-rqt-logger-level'
'ros-kinetic-rqt-msg'
'ros-kinetic-rqt-plot'
'ros-kinetic-rqt-publisher'
'ros-kinetic-rqt-py-common'
'ros-kinetic-rqt-py-console'
'ros-kinetic-rqt-reconfigure'
'ros-kinetic-rqt-service-caller'
'ros-kinetic-rqt-shell'
'ros-kinetic-rqt-srv'
'ros-kinetic-rqt-top'
'ros-kinetic-rqt-topic'
'ros-kinetic-rqt-web'
)

conflicts=()
replaces=()

_dir=rqt_common_plugins
source=()
md5sums=()

prepare() {
    cp -R $startdir/rqt_common_plugins $srcdir/rqt_common_plugins
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

