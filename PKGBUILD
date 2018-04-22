# Script generated with Bloom
pkgdesc="ROS - rqt_common_plugins metapackage provides ROS backend graphical tools suite that can be used on/off of robot runtime.<br/> <br/> To run any rqt plugins, just type in a single command &quot;rqt&quot;, then select any plugins you want from the GUI that launches afterwards.<br/> <br/> rqt consists of three following metapackages:<br/> <ul> <li><a href="http://ros.org/wiki/rqt">rqt</a> - core modules of rqt (ROS GUI) framework. rqt plugin developers barely needs to pay attention to this metapackage.</li> <li>rqt_common_plugins (you're here!)</li> <li><a href="http://ros.org/wiki/rqt_robot_plugins">rqt_robot_plugins</a> - rqt plugins that are particularly used with robots during their runtime.</li><br/> </ul> <br/>"
url='http://ros.org/wiki/rqt_common_plugins'

pkgname='ros-lunar-rqt-common-plugins'
pkgver='0.4.8_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-rqt-action'
'ros-lunar-rqt-bag'
'ros-lunar-rqt-bag-plugins'
'ros-lunar-rqt-console'
'ros-lunar-rqt-dep'
'ros-lunar-rqt-graph'
'ros-lunar-rqt-image-view'
'ros-lunar-rqt-launch'
'ros-lunar-rqt-logger-level'
'ros-lunar-rqt-msg'
'ros-lunar-rqt-plot'
'ros-lunar-rqt-publisher'
'ros-lunar-rqt-py-common'
'ros-lunar-rqt-py-console'
'ros-lunar-rqt-reconfigure'
'ros-lunar-rqt-service-caller'
'ros-lunar-rqt-shell'
'ros-lunar-rqt-srv'
'ros-lunar-rqt-top'
'ros-lunar-rqt-topic'
'ros-lunar-rqt-web'
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
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

