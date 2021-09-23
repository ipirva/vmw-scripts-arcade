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
from swagger_client.api.management_plane_api_networking_vpn_l2_vpn_sessions_api import ManagementPlaneAPINetworkingVPNL2VPNSessionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneAPINetworkingVPNL2VPNSessionsApi(unittest.TestCase):
    """ManagementPlaneAPINetworkingVPNL2VPNSessionsApi unit test stubs"""

    def setUp(self):
        self.api = ManagementPlaneAPINetworkingVPNL2VPNSessionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_l2_vpn_session(self):
        """Test case for create_l2_vpn_session

        Create L2VPN session  # noqa: E501
        """
        pass

    def test_delete_l2_vpn_session(self):
        """Test case for delete_l2_vpn_session

        Delete a L2VPN session  # noqa: E501
        """
        pass

    def test_get_l2_vpn_session(self):
        """Test case for get_l2_vpn_session

        Get a L2VPN session  # noqa: E501
        """
        pass

    def test_get_l2_vpn_session_peer_codes(self):
        """Test case for get_l2_vpn_session_peer_codes

        Get peer codes for the L2VpnSession  # noqa: E501
        """
        pass

    def test_list_l2_vpn_sessions(self):
        """Test case for list_l2_vpn_sessions

        Get all L2VPN sessions  # noqa: E501
        """
        pass

    def test_update_l2_vpn_session(self):
        """Test case for update_l2_vpn_session

        Edit a L2VPN session  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()