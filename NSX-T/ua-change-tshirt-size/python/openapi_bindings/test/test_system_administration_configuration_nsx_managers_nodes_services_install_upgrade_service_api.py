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
from swagger_client.api.system_administration_configuration_nsx_managers_nodes_services_install_upgrade_service_api import SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi(unittest.TestCase):
    """SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi unit test stubs"""

    def setUp(self):
        self.api = SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_repository_service_action_restart(self):
        """Test case for create_repository_service_action_restart

        Restart, start or stop the NSX install-upgrade service  # noqa: E501
        """
        pass

    def test_create_repository_service_action_start(self):
        """Test case for create_repository_service_action_start

        Restart, start or stop the NSX install-upgrade service  # noqa: E501
        """
        pass

    def test_create_repository_service_action_stop(self):
        """Test case for create_repository_service_action_stop

        Restart, start or stop the NSX install-upgrade service  # noqa: E501
        """
        pass

    def test_read_repository_service(self):
        """Test case for read_repository_service

        Read NSX install-upgrade service properties  # noqa: E501
        """
        pass

    def test_read_repository_service_status(self):
        """Test case for read_repository_service_status

        Read NSX install-upgrade service status  # noqa: E501
        """
        pass

    def test_update_repository_service(self):
        """Test case for update_repository_service

        Update NSX install-upgrade service properties  # noqa: E501
        """
        pass

    def test_update_uc_state(self):
        """Test case for update_uc_state

        Update UC state properties  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()