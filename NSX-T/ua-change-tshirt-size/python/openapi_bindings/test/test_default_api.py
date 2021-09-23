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
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_apply_certificate_apply_certificate(self):
        """Test case for apply_certificate_apply_certificate

        Apply a certificate for a CertificateProfile  # noqa: E501
        """
        pass

    def test_set_principal_identity_certificate_for_federation_set_pi_certificate_for_federation(self):
        """Test case for set_principal_identity_certificate_for_federation_set_pi_certificate_for_federation

        Set a certificate as a GM or LM Principal Identity certificate  # noqa: E501
        """
        pass

    def test_validate_certificate_validate(self):
        """Test case for validate_certificate_validate

        Validate a certificate  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
