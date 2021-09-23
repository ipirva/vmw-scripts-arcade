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

class CrlObjectData(ManagedResource):
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
        'pem_encoded': 'str'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'pem_encoded': 'pem_encoded'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, pem_encoded=None, *args, **kwargs):  # noqa: E501
        """CrlObjectData - a model defined in Swagger"""  # noqa: E501
        self._pem_encoded = None
        self.discriminator = None
        self.pem_encoded = pem_encoded
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def pem_encoded(self):
        """Gets the pem_encoded of this CrlObjectData.  # noqa: E501

        PEM encoded CRL data.  # noqa: E501

        :return: The pem_encoded of this CrlObjectData.  # noqa: E501
        :rtype: str
        """
        return self._pem_encoded

    @pem_encoded.setter
    def pem_encoded(self, pem_encoded):
        """Sets the pem_encoded of this CrlObjectData.

        PEM encoded CRL data.  # noqa: E501

        :param pem_encoded: The pem_encoded of this CrlObjectData.  # noqa: E501
        :type: str
        """
        if pem_encoded is None:
            raise ValueError("Invalid value for `pem_encoded`, must not be `None`")  # noqa: E501

        self._pem_encoded = pem_encoded

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
        if issubclass(CrlObjectData, dict):
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
        if not isinstance(other, CrlObjectData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
