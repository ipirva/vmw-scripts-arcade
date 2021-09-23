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
from swagger_client.api.management_plane_api_networking_logical_routing_and_services_logical_router_ports_api import ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi(unittest.TestCase):
    """ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi unit test stubs"""

    def setUp(self):
        self.api = ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_logical_router_port(self):
        """Test case for create_logical_router_port

        Create a Logical Router Port  # noqa: E501
        """
        pass

    def test_delete_logical_router_port(self):
        """Test case for delete_logical_router_port

        Delete a Logical Router Port  # noqa: E501
        """
        pass

    def test_get_logical_router_port_arp_table(self):
        """Test case for get_logical_router_port_arp_table

        Get the ARP table (IPv4) or Neighbor Discovery table (IPv6) for the Logical Router Port of the given id   # noqa: E501
        """
        pass

    def test_get_logical_router_port_arp_table_in_csv_format_csv(self):
        """Test case for get_logical_router_port_arp_table_in_csv_format_csv

        Get the ARP table (IPv4) or Neighbor Discovery table (IPv6) for the Logical Router Port of the given id   # noqa: E501
        """
        pass

    def test_get_logical_router_port_state(self):
        """Test case for get_logical_router_port_state

        Get the Realized State of a Logical Router Port  # noqa: E501
        """
        pass

    def test_get_logical_router_port_statistics(self):
        """Test case for get_logical_router_port_statistics

        Get the statistics of a specified logical router port on all or a specified node  # noqa: E501
        """
        pass

    def test_get_logical_router_port_statistics_summary(self):
        """Test case for get_logical_router_port_statistics_summary

        Get the statistics summary of a specified logical router port  # noqa: E501
        """
        pass

    def test_list_logical_router_ports(self):
        """Test case for list_logical_router_ports

        List Logical Router Ports  # noqa: E501
        """
        pass

    def test_read_logical_router_port(self):
        """Test case for read_logical_router_port

        Read Logical Router Port  # noqa: E501
        """
        pass

    def test_update_logical_router_port(self):
        """Test case for update_logical_router_port

        Update a Logical Router Port  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
