# coding: utf-8

"""
    NSX-T Manager API

    VMware NSX-T Manager REST API  # noqa: E501

    OpenAPI spec version: 3.1.0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.managed_resource import ManagedResource  # noqa: F401,E501

class UpdatePrincipalIdentityCertificateRequest(ManagedResource):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'principal_identity_id': 'str',
        'certificate_id': 'str'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'principal_identity_id': 'principal_identity_id',
        'certificate_id': 'certificate_id'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, principal_identity_id=None, certificate_id=None, *args, **kwargs):  # noqa: E501
        """UpdatePrincipalIdentityCertificateRequest - a model defined in Swagger"""  # noqa: E501
        self._principal_identity_id = None
        self._certificate_id = None
        self.discriminator = None
        self.principal_identity_id = principal_identity_id
        self.certificate_id = certificate_id
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def principal_identity_id(self):
        """Gets the principal_identity_id of this UpdatePrincipalIdentityCertificateRequest.  # noqa: E501

        Unique ID of the principal.  # noqa: E501

        :return: The principal_identity_id of this UpdatePrincipalIdentityCertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._principal_identity_id

    @principal_identity_id.setter
    def principal_identity_id(self, principal_identity_id):
        """Sets the principal_identity_id of this UpdatePrincipalIdentityCertificateRequest.

        Unique ID of the principal.  # noqa: E501

        :param principal_identity_id: The principal_identity_id of this UpdatePrincipalIdentityCertificateRequest.  # noqa: E501
        :type: str
        """
        if principal_identity_id is None:
            raise ValueError("Invalid value for `principal_identity_id`, must not be `None`")  # noqa: E501

        self._principal_identity_id = principal_identity_id

    @property
    def certificate_id(self):
        """Gets the certificate_id of this UpdatePrincipalIdentityCertificateRequest.  # noqa: E501

        Id of the stored certificate.  # noqa: E501

        :return: The certificate_id of this UpdatePrincipalIdentityCertificateRequest.  # noqa: E501
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this UpdatePrincipalIdentityCertificateRequest.

        Id of the stored certificate.  # noqa: E501

        :param certificate_id: The certificate_id of this UpdatePrincipalIdentityCertificateRequest.  # noqa: E501
        :type: str
        """
        if certificate_id is None:
            raise ValueError("Invalid value for `certificate_id`, must not be `None`")  # noqa: E501

        self._certificate_id = certificate_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdatePrincipalIdentityCertificateRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdatePrincipalIdentityCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
