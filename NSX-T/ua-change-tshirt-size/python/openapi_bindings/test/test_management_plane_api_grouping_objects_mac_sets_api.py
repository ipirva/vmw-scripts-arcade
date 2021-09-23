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
from swagger_client.api.management_plane_api_grouping_objects_mac_sets_api import ManagementPlaneAPIGroupingObjectsMACSetsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneAPIGroupingObjectsMACSetsApi(unittest.TestCase):
    """ManagementPlaneAPIGroupingObjectsMACSetsApi unit test stubs"""

    def setUp(self):
        self.api = ManagementPlaneAPIGroupingObjectsMACSetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_mac_address(self):
        """Test case for add_mac_address

        Add a MAC address to a MACSet  # noqa: E501
        """
        pass

    def test_delete_mac_set(self):
        """Test case for delete_mac_set

        Delete MACSet  # noqa: E501
        """
        pass

    def test_get_mac_addresses(self):
        """Test case for get_mac_addresses

        Get all MACAddresses in a MACSet  # noqa: E501
        """
        pass

    def test_list_mac_sets(self):
        """Test case for list_mac_sets

        List MACSets  # noqa: E501
        """
        pass

    def test_read_mac_set(self):
        """Test case for read_mac_set

        Read MACSet  # noqa: E501
        """
        pass

    def test_remove_mac_address(self):
        """Test case for remove_mac_address

        Remove a MAC address from given MACSet  # noqa: E501
        """
        pass

    def test_update_mac_set(self):
        """Test case for update_mac_set

        Update MACSet  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
