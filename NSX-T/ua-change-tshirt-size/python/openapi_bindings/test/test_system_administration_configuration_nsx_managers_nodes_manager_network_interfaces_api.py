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
from swagger_client.api.system_administration_configuration_nsx_managers_nodes_manager_network_interfaces_api import SystemAdministrationConfigurationNSXManagersNodesManagerNetworkInterfacesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemAdministrationConfigurationNSXManagersNodesManagerNetworkInterfacesApi(unittest.TestCase):
    """SystemAdministrationConfigurationNSXManagersNodesManagerNetworkInterfacesApi unit test stubs"""

    def setUp(self):
        self.api = SystemAdministrationConfigurationNSXManagersNodesManagerNetworkInterfacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_read_cluster_node_interface_statistics(self):
        """Test case for read_cluster_node_interface_statistics

        Read the NSX Manager/Controller's Network Interface Statistics  # noqa: E501
        """
        pass

    def test_read_fabric_node_interface_statistics(self):
        """Test case for read_fabric_node_interface_statistics

        Read the NSX Manager's Network Interface Statistics  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()