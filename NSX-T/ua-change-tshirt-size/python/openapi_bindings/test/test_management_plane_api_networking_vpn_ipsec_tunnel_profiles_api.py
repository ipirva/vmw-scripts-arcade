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
from swagger_client.api.management_plane_api_networking_vpn_ipsec_tunnel_profiles_api import ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi(unittest.TestCase):
    """ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi unit test stubs"""

    def setUp(self):
        self.api = ManagementPlaneAPINetworkingVPNIPSECTunnelProfilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_ip_sec_vpn_tunnel_profile(self):
        """Test case for create_ip_sec_vpn_tunnel_profile

        Create custom IPSec tunnel profile  # noqa: E501
        """
        pass

    def test_delete_ip_sec_vpn_tunnel_profile(self):
        """Test case for delete_ip_sec_vpn_tunnel_profile

        Delete custom IPSecTunnelProfile  # noqa: E501
        """
        pass

    def test_get_ip_sec_vpn_tunnel_profile(self):
        """Test case for get_ip_sec_vpn_tunnel_profile

        Get IPSec tunnel profile  # noqa: E501
        """
        pass

    def test_list_ip_sec_vpn_tunnel_profiles(self):
        """Test case for list_ip_sec_vpn_tunnel_profiles

        Get IPSecTunnelProfile List Result  # noqa: E501
        """
        pass

    def test_update_ip_sec_vpn_tunnel_profile(self):
        """Test case for update_ip_sec_vpn_tunnel_profile

        Edit custom IPSecTunnelProfile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()