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
from swagger_client.api.management_plane_api_networking_vpn_ipsec_sessions_api import ManagementPlaneAPINetworkingVPNIPSECSessionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneAPINetworkingVPNIPSECSessionsApi(unittest.TestCase):
    """ManagementPlaneAPINetworkingVPNIPSECSessionsApi unit test stubs"""

    def setUp(self):
        self.api = ManagementPlaneAPINetworkingVPNIPSECSessionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_ip_sec_vpn_session(self):
        """Test case for create_ip_sec_vpn_session

        Create new VPN session  # noqa: E501
        """
        pass

    def test_delete_ip_sec_vpn_session(self):
        """Test case for delete_ip_sec_vpn_session

        Delete IPSec VPN session  # noqa: E501
        """
        pass

    def test_get_ip_sec_vpn_session(self):
        """Test case for get_ip_sec_vpn_session

        Fetch IPSec VPN session  # noqa: E501
        """
        pass

    def test_get_ip_sec_vpn_session_state(self):
        """Test case for get_ip_sec_vpn_session_state

        Get the Realized State of a IPSec VPN Session  # noqa: E501
        """
        pass

    def test_get_peer_config(self):
        """Test case for get_peer_config

        Get VPN configuration for the peer site  # noqa: E501
        """
        pass

    def test_list_ip_sec_vpn_sessions(self):
        """Test case for list_ip_sec_vpn_sessions

        Get IPSec VPN session list result  # noqa: E501
        """
        pass

    def test_update_ip_sec_vpn_session(self):
        """Test case for update_ip_sec_vpn_session

        Edit IPSec VPN session  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()