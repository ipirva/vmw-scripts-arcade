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
from swagger_client.api.system_administration_configuration_fabric_nodes_transport_node_interfaces_api import SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi(unittest.TestCase):
    """SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi unit test stubs"""

    def setUp(self):
        self.api = SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_fabric_node_interfaces(self):
        """Test case for list_fabric_node_interfaces

        List the specified node's Network Interfaces  # noqa: E501
        """
        pass

    def test_list_transport_node_interfaces(self):
        """Test case for list_transport_node_interfaces

        List the specified transport node's network interfaces  # noqa: E501
        """
        pass

    def test_read_fabric_node_interface(self):
        """Test case for read_fabric_node_interface

        Read the node's Network Interface  # noqa: E501
        """
        pass

    def test_read_transport_node_interface(self):
        """Test case for read_transport_node_interface

        Read the transport node's network interface  # noqa: E501
        """
        pass

    def test_read_transport_node_interface_statistics(self):
        """Test case for read_transport_node_interface_statistics

        Read the NSX Manager's Network Interface Statistics  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
