#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2009, Willow Garage, Inc.
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

import unittest

# get mock from pypi as 'mock'
from mock import Mock, patch

from rqt_dep.dotcode_pack import RosPackageGraphDotcodeGenerator


PKG = 'rqt_deps'


class DotcodeGeneratorTest(unittest.TestCase):

    def test_packages_only(self):
        with patch('rospkg.RosPack') as rospack:
            with patch('rospkg.RosStack') as rosstack:
                factoryMock = Mock()
                graphMock = Mock()
                rospack.list.return_value = []
                rosstack.list.return_value = []
                factoryMock.get_graph.return_value = graphMock
                gen = RosPackageGraphDotcodeGenerator(rospack, rosstack)
                graph = gen.generate_dotcode(factoryMock)

                rospack.list.assert_any_call()
                rosstack.list.assert_any_call()
                factoryMock.get_graph.assert_called_with(simplify=True, rank='same', ranksep=0.2, rankdir='TB')
                factoryMock.create_dot.assert_called_with(graphMock)


if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(PKG, 'test_packages_only', DotcodeGeneratorTest)
