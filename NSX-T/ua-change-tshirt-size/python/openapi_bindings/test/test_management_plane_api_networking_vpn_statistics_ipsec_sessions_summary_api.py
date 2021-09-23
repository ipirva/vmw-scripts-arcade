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
from swagger_client.api.management_plane_api_networking_vpn_statistics_ipsec_sessions_summary_api import ManagementPlaneAPINetworkingVPNStatisticsIPSECSessionsSummaryApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneAPINetworkingVPNStatisticsIPSECSessionsSummaryApi(unittest.TestCase):
    """ManagementPlaneAPINetworkingVPNStatisticsIPSECSessionsSummaryApi unit test stubs"""

    def setUp(self):
        self.api = ManagementPlaneAPINetworkingVPNStatisticsIPSECSessionsSummaryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_ip_sec_vpn_session_summary(self):
        """Test case for get_ip_sec_vpn_session_summary

        VPN session summary  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
