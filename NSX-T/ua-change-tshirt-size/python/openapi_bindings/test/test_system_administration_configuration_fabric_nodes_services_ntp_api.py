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
from swagger_client.api.system_administration_configuration_fabric_nodes_services_ntp_api import SystemAdministrationConfigurationFabricNodesServicesNTPApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemAdministrationConfigurationFabricNodesServicesNTPApi(unittest.TestCase):
    """SystemAdministrationConfigurationFabricNodesServicesNTPApi unit test stubs"""

    def setUp(self):
        self.api = SystemAdministrationConfigurationFabricNodesServicesNTPApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_ntp_service_action_restart(self):
        """Test case for create_ntp_service_action_restart

        Restart, start or stop the NTP service  # noqa: E501
        """
        pass

    def test_create_ntp_service_action_start(self):
        """Test case for create_ntp_service_action_start

        Restart, start or stop the NTP service  # noqa: E501
        """
        pass

    def test_create_ntp_service_action_stop(self):
        """Test case for create_ntp_service_action_stop

        Restart, start or stop the NTP service  # noqa: E501
        """
        pass

    def test_read_ntp_service(self):
        """Test case for read_ntp_service

        Read NTP service properties  # noqa: E501
        """
        pass

    def test_read_ntp_service_status(self):
        """Test case for read_ntp_service_status

        Read NTP service status  # noqa: E501
        """
        pass

    def test_update_ntp_service(self):
        """Test case for update_ntp_service

        Update NTP service properties  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
