#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import syslog

import testtools

import daiquiri


class TestDaiquiri(testtools.TestCase):
    def test_find_facility(self):
        self.assertEqual(syslog.LOG_USER,
                         daiquiri._find_facility("user"))
        self.assertEqual(syslog.LOG_LOCAL1,
                         daiquiri._find_facility("log_local1"))
        self.assertEqual(syslog.LOG_LOCAL2,
                         daiquiri._find_facility("LOG_local2"))
        self.assertEqual(syslog.LOG_LOCAL3,
                         daiquiri._find_facility("LOG_LOCAL3"))
        self.assertEqual(syslog.LOG_LOCAL4,
                         daiquiri._find_facility("LOCaL4"))

    def test_get_log_file_path(self):
        self.assertEqual("foobar.log",
                         daiquiri._get_log_file_path("foobar.log"))
        self.assertEqual("/var/log/foo/foobar.log",
                         daiquiri._get_log_file_path("foobar.log",
                                                     logdir="/var/log/foo"))
        self.assertEqual("/var/log/foobar.log",
                         daiquiri._get_log_file_path(logdir="/var/log",
                                                     binary="foobar"))
        self.assertEqual("/var/log/foobar.log",
                         daiquiri._get_log_file_path(logdir="/var/log",
                                                     binary="foobar"))
        self.assertEqual("/var/log/foobar.journal",
                         daiquiri._get_log_file_path(logdir="/var/log",
                                                     logfile_suffix=".journal",
                                                     binary="foobar"))

    def test_setup(self):
        daiquiri.setup()
        daiquiri.setup(debug=True)
        daiquiri.setup(use_syslog=True)
        daiquiri.setup(binary="foobar")
