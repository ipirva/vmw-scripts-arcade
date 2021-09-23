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
from swagger_client.api.system_administration_monitoring_system_health_profiles_api import SystemAdministrationMonitoringSystemHealthProfilesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemAdministrationMonitoringSystemHealthProfilesApi(unittest.TestCase):
    """SystemAdministrationMonitoringSystemHealthProfilesApi unit test stubs"""

    def setUp(self):
        self.api = SystemAdministrationMonitoringSystemHealthProfilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_system_health_agent_profile(self):
        """Test case for create_system_health_agent_profile

        Create a system health profile  # noqa: E501
        """
        pass

    def test_delete_system_health_agent_profile(self):
        """Test case for delete_system_health_agent_profile

        Delete an existing system health profile  # noqa: E501
        """
        pass

    def test_list_system_health_agent_profiles(self):
        """Test case for list_system_health_agent_profiles

        List all system health profiles  # noqa: E501
        """
        pass

    def test_show_system_health_agent_profile(self):
        """Test case for show_system_health_agent_profile

        Show the details of a system health profile  # noqa: E501
        """
        pass

    def test_update_system_health_agent_profile(self):
        """Test case for update_system_health_agent_profile

        Update a system health profile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()