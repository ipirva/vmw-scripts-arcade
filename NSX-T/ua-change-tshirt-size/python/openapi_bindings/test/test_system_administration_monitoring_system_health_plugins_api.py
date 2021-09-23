# coding: utf-8

"""
    NSX-T Manager API

    VMware NSX-T Manager REST API  # noqa: E501

    OpenAPI spec version: 3.1.0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.system_administration_monitoring_system_health_plugins_api import SystemAdministrationMonitoringSystemHealthPluginsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemAdministrationMonitoringSystemHealthPluginsApi(unittest.TestCase):
    """SystemAdministrationMonitoringSystemHealthPluginsApi unit test stubs"""

    def setUp(self):
        self.api = SystemAdministrationMonitoringSystemHealthPluginsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_plugin_file(self):
        """Test case for create_plugin_file

        Upload a plugin File to MP  # noqa: E501
        """
        pass

    def test_create_system_health_plugin(self):
        """Test case for create_system_health_plugin

        Create a system health plugin  # noqa: E501
        """
        pass

    def test_delete_system_health_plugin(self):
        """Test case for delete_system_health_plugin

        Delete an existing system health plugin  # noqa: E501
        """
        pass

    def test_list_all_system_health_plugins(self):
        """Test case for list_all_system_health_plugins

        Show all the system health plugin  # noqa: E501
        """
        pass

    def test_show_system_health_plugin(self):
        """Test case for show_system_health_plugin

        Show the details of a system health plugin  # noqa: E501
        """
        pass

    def test_show_system_health_plugin_on_node(self):
        """Test case for show_system_health_plugin_on_node

        Show the installed system health plugin list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()