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
from swagger_client.api.system_administration_configuration_nsx_managers_clusters_cluster_status_api import SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemAdministrationConfigurationNSXManagersClustersClusterStatusApi(unittest.TestCase):
    """SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi unit test stubs"""

    def setUp(self):
        self.api = SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_read_cluster_node_status(self):
        """Test case for read_cluster_node_status

        Read cluster node runtime status  # noqa: E501
        """
        pass

    def test_read_cluster_nodes_aggregate_status(self):
        """Test case for read_cluster_nodes_aggregate_status

        Read cluster runtime status  # noqa: E501
        """
        pass

    def test_read_cluster_status(self):
        """Test case for read_cluster_status

        Read Cluster Status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
