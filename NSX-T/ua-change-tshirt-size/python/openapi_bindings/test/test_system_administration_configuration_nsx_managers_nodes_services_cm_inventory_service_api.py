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
from swagger_client.api.system_administration_configuration_nsx_managers_nodes_services_cm_inventory_service_api import SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi(unittest.TestCase):
    """SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi unit test stubs"""

    def setUp(self):
        self.api = SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cminventory_service_action_restart(self):
        """Test case for create_cminventory_service_action_restart

        Restart, start or stop the manager service  # noqa: E501
        """
        pass

    def test_create_cminventory_service_action_start(self):
        """Test case for create_cminventory_service_action_start

        Restart, start or stop the manager service  # noqa: E501
        """
        pass

    def test_create_cminventory_service_action_stop(self):
        """Test case for create_cminventory_service_action_stop

        Restart, start or stop the manager service  # noqa: E501
        """
        pass

    def test_read_cminventory_service(self):
        """Test case for read_cminventory_service

        Read cm inventory service properties  # noqa: E501
        """
        pass

    def test_read_cminventory_service_status(self):
        """Test case for read_cminventory_service_status

        Read manager service status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()