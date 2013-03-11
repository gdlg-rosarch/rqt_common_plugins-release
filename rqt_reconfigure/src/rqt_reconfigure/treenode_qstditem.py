# Software License Agreement (BSD License)
#
# Copyright (c) 2012, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: Isaac Saito

from __future__ import division

import dynamic_reconfigure.client
from python_qt_binding.QtCore import Qt
from python_qt_binding.QtGui import QBrush, QStandardItem, QWidget
import rospy
from rqt_py_common.data_items import ReadonlyItem

from .dynreconf_client_widget import DynreconfClientWidget


class TreenodeQstdItem(ReadonlyItem):
    """
    Extending ReadonlyItem - the display content of this item shouldn't be
    modified.
    """

    NODE_FULLPATH = 1

    def __init__(self, *args):
        """
        :param args[0]: str (will become 1st arg of QStandardItem)
        :param args[1]: integer value that indicates whether this class
                               is node that has GRN (Graph Resource Names, see
                               http://www.ros.org/wiki/Names). This can be None
        """
        grn_current_treenode = args[0]
        self._param_name_raw = grn_current_treenode
        self._set_param_name(grn_current_treenode)
        super(TreenodeQstdItem, self).__init__(grn_current_treenode)

        self._dynreconf_client = None
        self._is_rosnode = False

        try:
            if args[1] != None:
                self._is_rosnode = True
        except IndexError:  # tuple index out of range etc.
                rospy.logerr('TreenodeQstdItem IndexError')

    def get_widget(self):
        """
        :rtype: DynreconfClientWidget (QWidget)
        """
        return self._dynreconf_client

    def connect_param_server(self):
        """
        Connect to parameter server using dynamic_reconfigure client.
        Behavior is delegated to a private method _connect_param_server, and
        its return value, client, is set to member variable.

        @return void
        @raise ROSException:
        """
        try:
            self._dynreconf_client = self._connect_param_server(
                                                          self._param_name_raw)
        except rospy.exceptions.ROSException as e:
            raise e

    def _connect_param_server(self, nodename_grn_full):
        """
        Callback when user chooses a node.

        :param nodename_grn_full: GRN (Graph Resource Names,
                         see http://www.ros.org/wiki/Names) of node name.
        :type node: str
        :return None if the treenode doesn't represent ROS Node.
        :rtype: DynreconfClientWidget
        """
        # If the treenode doesn't represent ROS Node, return None.
        if not self._is_rosnode:
            return None

        try:
            _dynreconf_client = dynamic_reconfigure.client.Client(
                                           str(nodename_grn_full), timeout=5.0)
        except rospy.exceptions.ROSException as e:
            raise type(e)(e.message +
                          "TreenodeQstdItem. Couldn't connect to {}".format(
                                                            nodename_grn_full))

        _dynreconf_widget = DynreconfClientWidget(_dynreconf_client,
                                                 nodename_grn_full)
        return _dynreconf_widget

    def enable_param_items(self):
        """
        Create QStdItem per parameter and addColumn them to myself.
        :rtype: None if _dynreconf_client is not initiated.
        """
        if self._dynreconf_client == None:
            return None
        paramnames = self._dynreconf_client.get_treenode_names()
        paramnames_items = []
        brush = QBrush(Qt.lightGray)
        for paramname in paramnames:
            item = ReadonlyItem(paramname)
            item.setBackground(brush)
            paramnames_items.append(item)
        rospy.logdebug('enable_param_items len of paramnames={}'.format(
                                                        len(paramnames_items)))
        self.appendColumn(paramnames_items)

    def _set_param_name(self, param_name):
        """
        :param param_name: A string formatted as GRN (Graph Resource Names, see
                           http://www.ros.org/wiki/Names).
                           Example: /paramname/subpara/subsubpara/...
        """
        rospy.logdebug('_set_param_name param_name={} '.format(param_name))

        #  separate param_name by forward slash
        self._list_treenode_names = param_name.split('/')

        #  Deleting the 1st elem which is zero-length str.
        del self._list_treenode_names[0]

        self._toplevel_treenode_name = self._list_treenode_names[0]

        rospy.logdebug('paramname={} nodename={} _list_params[-1]={}'.format(
                       param_name, self._toplevel_treenode_name,
                       self._list_treenode_names[-1]))

    def get_param_name_toplv(self):
        """
        :rtype: String of the top level param name.
        """

        return self._name_top

    def get_raw_param_name(self):
        return self._param_name_raw

    def get_treenode_names(self):
        """
        :rtype: List of string. Null if param
        """

        #TODO: what if self._list_treenode_names is empty or null?
        return self._list_treenode_names

    def get_node_name(self):
        """
        :return: A value of single tree node (ie. NOT the fullpath node name).
                 Ex. suppose fullpath name is /top/sub/subsub/subsubsub and you
                     are at 2nd from top, the return value is subsub.
        """
        return self._toplevel_treenode_name

    def type(self):
        return QStandardItem.UserType
