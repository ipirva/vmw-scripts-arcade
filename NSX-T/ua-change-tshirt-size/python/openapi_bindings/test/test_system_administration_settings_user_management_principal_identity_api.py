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
from swagger_client.api.system_administration_settings_user_management_principal_identity_api import SystemAdministrationSettingsUserManagementPrincipalIdentityApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemAdministrationSettingsUserManagementPrincipalIdentityApi(unittest.TestCase):
    """SystemAdministrationSettingsUserManagementPrincipalIdentityApi unit test stubs"""

    def setUp(self):
        self.api = SystemAdministrationSettingsUserManagementPrincipalIdentityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_oidc_end_point(self):
        """Test case for add_oidc_end_point

        Add an OpenID Connect end-point.  # noqa: E501
        """
        pass

    def test_delete_principal_identity(self):
        """Test case for delete_principal_identity

        Delete a principal identity  # noqa: E501
        """
        pass

    def test_delete_token_based_principal_identity(self):
        """Test case for delete_token_based_principal_identity

        Delete a token-based principal identity  # noqa: E501
        """
        pass

    def test_get_oidc_end_point(self):
        """Test case for get_oidc_end_point

        Get an OpenID Connect end-point.  # noqa: E501
        """
        pass

    def test_get_principal_identities(self):
        """Test case for get_principal_identities

        Return the list of principal identities  # noqa: E501
        """
        pass

    def test_get_principal_identity(self):
        """Test case for get_principal_identity

        Get a principal identity  # noqa: E501
        """
        pass

    def test_get_token_based_principal_identity(self):
        """Test case for get_token_based_principal_identity

        Get a token-based principal identity  # noqa: E501
        """
        pass

    def test_list_oidc_end_points(self):
        """Test case for list_oidc_end_points

        Return the list of OpenID Connect end-points.  # noqa: E501
        """
        pass

    def test_list_token_based_principal_identities(self):
        """Test case for list_token_based_principal_identities

        Return the list of token-based principal identities. | These don't have certificate or role information.  # noqa: E501
        """
        pass

    def test_register_principal_identity(self):
        """Test case for register_principal_identity

        Register a name-certificate combination.  # noqa: E501
        """
        pass

    def test_register_principal_identity_with_certificate(self):
        """Test case for register_principal_identity_with_certificate

        Register a name-certificate combination.  # noqa: E501
        """
        pass

    def test_register_token_based_principal_identity(self):
        """Test case for register_token_based_principal_identity

        Register a token-based principal identity.  # noqa: E501
        """
        pass

    def test_update_oidc_end_point_thumbprint_update_thumbprint(self):
        """Test case for update_oidc_end_point_thumbprint_update_thumbprint

        Update a OpenID Connect end-point's thumbprint  # noqa: E501
        """
        pass

    def test_update_principal_identity_certificate_update_certificate(self):
        """Test case for update_principal_identity_certificate_update_certificate

        Update a principal identity's certificate  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
