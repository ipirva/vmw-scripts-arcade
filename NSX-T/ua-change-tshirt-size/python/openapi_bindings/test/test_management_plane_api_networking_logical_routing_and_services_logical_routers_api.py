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
from swagger_client.api.management_plane_api_networking_logical_routing_and_services_logical_routers_api import ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(unittest.TestCase):
    """ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi unit test stubs"""

    def setUp(self):
        self.api = ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_logical_router(self):
        """Test case for create_logical_router

        Create a Logical Router  # noqa: E501
        """
        pass

    def test_delete_logical_router(self):
        """Test case for delete_logical_router

        Delete a Logical Router  # noqa: E501
        """
        pass

    def test_get_bgp_neighbor_advertised_routes(self):
        """Test case for get_bgp_neighbor_advertised_routes

        Get BGP neighbor advertised routes  # noqa: E501
        """
        pass

    def test_get_bgp_neighbor_advertised_routes_in_csv_format_csv(self):
        """Test case for get_bgp_neighbor_advertised_routes_in_csv_format_csv

        Get BGP neighbor advertised routes in CSV format   # noqa: E501
        """
        pass

    def test_get_bgp_neighbor_routes(self):
        """Test case for get_bgp_neighbor_routes

        Get BGP neighbor learned routes  # noqa: E501
        """
        pass

    def test_get_bgp_neighbor_routes_in_csv_format_csv(self):
        """Test case for get_bgp_neighbor_routes_in_csv_format_csv

        Get BGP neighbor learned routes in CSV format   # noqa: E501
        """
        pass

    def test_get_bgp_neighbors_status(self):
        """Test case for get_bgp_neighbors_status

        Get the status of all the BGP neighbors for the Logical Router of the given id  # noqa: E501
        """
        pass

    def test_get_logical_router_forwarding_table(self):
        """Test case for get_logical_router_forwarding_table

        Get FIB table on a specified node for a logical router  # noqa: E501
        """
        pass

    def test_get_logical_router_forwarding_table_in_csv_format_csv(self):
        """Test case for get_logical_router_forwarding_table_in_csv_format_csv

        Get FIB table on a specified node for a logical router  # noqa: E501
        """
        pass

    def test_get_logical_router_route_table(self):
        """Test case for get_logical_router_route_table

        Get route table on a given node for a logical router  # noqa: E501
        """
        pass

    def test_get_logical_router_route_table_in_csv_format_csv(self):
        """Test case for get_logical_router_route_table_in_csv_format_csv

        Get route table on a node for a logical router  # noqa: E501
        """
        pass

    def test_get_logical_router_routing_table(self):
        """Test case for get_logical_router_routing_table

        Get RIB table on a specified node for a logical router  # noqa: E501
        """
        pass

    def test_get_logical_router_routing_table_in_csv_format_csv(self):
        """Test case for get_logical_router_routing_table_in_csv_format_csv

        Get RIB table on a specified node for a logical router  # noqa: E501
        """
        pass

    def test_get_logical_router_state(self):
        """Test case for get_logical_router_state

        Get the Realized State of a Logical Router  # noqa: E501
        """
        pass

    def test_get_logical_router_status(self):
        """Test case for get_logical_router_status

        Get the status for the Logical Router of the given id  # noqa: E501
        """
        pass

    def test_get_logical_service_router_cluster_state(self):
        """Test case for get_logical_service_router_cluster_state

        Get the Realized State of a Logical Service Router Cluster  # noqa: E501
        """
        pass

    def test_list_logical_routers(self):
        """Test case for list_logical_routers

        List Logical Routers  # noqa: E501
        """
        pass

    def test_re_allocate_service_routers_reallocate(self):
        """Test case for re_allocate_service_routers_reallocate

        Re allocate edge node placement of TIER1 service routers  # noqa: E501
        """
        pass

    def test_re_process_logical_router_reprocess(self):
        """Test case for re_process_logical_router_reprocess

        Reprocesses a logical router configuration and publish updates to controller  # noqa: E501
        """
        pass

    def test_read_logical_router(self):
        """Test case for read_logical_router

        Read Logical Router  # noqa: E501
        """
        pass

    def test_update_logical_router(self):
        """Test case for update_logical_router

        Update a Logical Router  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
