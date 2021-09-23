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
from swagger_client.api.management_plane_api_networking_logical_switching_logical_switch_ports_api import ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi(unittest.TestCase):
    """ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi unit test stubs"""

    def setUp(self):
        self.api = ManagementPlaneAPINetworkingLogicalSwitchingLogicalSwitchPortsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_logical_port(self):
        """Test case for create_logical_port

        Create a Logical Port  # noqa: E501
        """
        pass

    def test_create_switching_profile(self):
        """Test case for create_switching_profile

        Create a Switching Profile  # noqa: E501
        """
        pass

    def test_delete_logical_port(self):
        """Test case for delete_logical_port

        Delete a Logical Port  # noqa: E501
        """
        pass

    def test_delete_switching_profile(self):
        """Test case for delete_switching_profile

        Delete a Switching Profile  # noqa: E501
        """
        pass

    def test_get_logical_port(self):
        """Test case for get_logical_port

        Get Information About a Logical Port  # noqa: E501
        """
        pass

    def test_get_logical_port_mac_table(self):
        """Test case for get_logical_port_mac_table

        Get MAC table of a logical port with a given port id (lport-id)  # noqa: E501
        """
        pass

    def test_get_logical_port_mac_table_in_csv_format_csv(self):
        """Test case for get_logical_port_mac_table_in_csv_format_csv

        Get MAC table of a logical port with a given port id (lport-id)  # noqa: E501
        """
        pass

    def test_get_logical_port_operational_status(self):
        """Test case for get_logical_port_operational_status

        Get Operational Status for Logical Port of a Given Port ID (lport-id)  # noqa: E501
        """
        pass

    def test_get_logical_port_state(self):
        """Test case for get_logical_port_state

        Get realized state & location of a logical port  # noqa: E501
        """
        pass

    def test_get_logical_port_statistics(self):
        """Test case for get_logical_port_statistics

        Get Statistics for Logical Port of a Given Port ID (lport-id)  # noqa: E501
        """
        pass

    def test_get_logical_port_status_summary(self):
        """Test case for get_logical_port_status_summary

        Get Operational Status Summary of All Logical Ports in the System  # noqa: E501
        """
        pass

    def test_get_switching_profile(self):
        """Test case for get_switching_profile

        Get Switching Profile by ID  # noqa: E501
        """
        pass

    def test_get_switching_profile_status(self):
        """Test case for get_switching_profile_status

        Get Counts of Ports and Switches Using This Switching Profile  # noqa: E501
        """
        pass

    def test_list_logical_ports(self):
        """Test case for list_logical_ports

        List All Logical Ports  # noqa: E501
        """
        pass

    def test_list_switching_profiles(self):
        """Test case for list_switching_profiles

        List Switching Profiles  # noqa: E501
        """
        pass

    def test_update_logical_port(self):
        """Test case for update_logical_port

        Update a Logical Port  # noqa: E501
        """
        pass

    def test_update_switching_profile(self):
        """Test case for update_switching_profile

        Update a Switching Profile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
