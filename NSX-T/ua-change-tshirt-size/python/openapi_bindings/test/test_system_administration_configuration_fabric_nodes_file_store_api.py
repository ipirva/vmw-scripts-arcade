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
from swagger_client.api.system_administration_configuration_fabric_nodes_file_store_api import SystemAdministrationConfigurationFabricNodesFileStoreApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemAdministrationConfigurationFabricNodesFileStoreApi(unittest.TestCase):
    """SystemAdministrationConfigurationFabricNodesFileStoreApi unit test stubs"""

    def setUp(self):
        self.api = SystemAdministrationConfigurationFabricNodesFileStoreApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_copy_from_remote_file_copy_from_remote_file(self):
        """Test case for copy_from_remote_file_copy_from_remote_file

        Copy a remote file to the file store  # noqa: E501
        """
        pass

    def test_copy_to_remote_file_copy_to_remote_file(self):
        """Test case for copy_to_remote_file_copy_to_remote_file

        Copy file in the file store to a remote file store  # noqa: E501
        """
        pass

    def test_create_file(self):
        """Test case for create_file

        Upload a file to the file store  # noqa: E501
        """
        pass

    def test_create_remote_directory_create_remote_directory(self):
        """Test case for create_remote_directory_create_remote_directory

        Create directory in remote file server  # noqa: E501
        """
        pass

    def test_delete_file(self):
        """Test case for delete_file

        Delete file  # noqa: E501
        """
        pass

    def test_list_files(self):
        """Test case for list_files

        List node files  # noqa: E501
        """
        pass

    def test_read_file(self):
        """Test case for read_file

        Read file contents  # noqa: E501
        """
        pass

    def test_read_file_properties(self):
        """Test case for read_file_properties

        Read file properties  # noqa: E501
        """
        pass

    def test_read_file_thumbprint(self):
        """Test case for read_file_thumbprint

        Read file thumbprint  # noqa: E501
        """
        pass

    def test_update_file(self):
        """Test case for update_file

        Replace file contents  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()