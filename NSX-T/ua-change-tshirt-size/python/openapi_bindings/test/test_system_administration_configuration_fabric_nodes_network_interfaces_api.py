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
from swagger_client.api.system_administration_configuration_fabric_nodes_network_interfaces_api import SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemAdministrationConfigurationFabricNodesNetworkInterfacesApi(unittest.TestCase):
    """SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi unit test stubs"""

    def setUp(self):
        self.api = SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_node_interfaces(self):
        """Test case for list_node_interfaces

        List the Node's Network Interfaces  # noqa: E501
        """
        pass

    def test_read_network_interface_statistics(self):
        """Test case for read_network_interface_statistics

        Read the Node's Network Interface Statistics  # noqa: E501
        """
        pass

    def test_read_network_properties(self):
        """Test case for read_network_properties

        Read network configuration properties  # noqa: E501
        """
        pass

    def test_read_node_interface(self):
        """Test case for read_node_interface

        Read the Node's Network Interface  # noqa: E501
        """
        pass

    def test_update_node_interface(self):
        """Test case for update_node_interface

        Update the Node's Network Interface  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
