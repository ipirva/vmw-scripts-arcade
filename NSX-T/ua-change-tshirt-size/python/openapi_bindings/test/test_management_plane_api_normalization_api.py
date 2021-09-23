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
from swagger_client.api.management_plane_api_normalization_api import ManagementPlaneAPINormalizationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestManagementPlaneAPINormalizationApi(unittest.TestCase):
    """ManagementPlaneAPINormalizationApi unit test stubs"""

    def setUp(self):
        self.api = ManagementPlaneAPINormalizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_normalizations(self):
        """Test case for get_normalizations

        Get normalizations based on the query parameters  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()