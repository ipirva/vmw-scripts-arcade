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
from swagger_client.models.resource import Resource  # noqa: F401,E501

class FileThumbprint(Resource):
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
        'sha256': 'str',
        'name': 'str',
        'sha1': 'str'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        'sha256': 'sha256',
        'name': 'name',
        'sha1': 'sha1'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, sha256=None, name=None, sha1=None, *args, **kwargs):  # noqa: E501
        """FileThumbprint - a model defined in Swagger"""  # noqa: E501
        self._sha256 = None
        self._name = None
        self._sha1 = None
        self.discriminator = None
        self.sha256 = sha256
        self.name = name
        self.sha1 = sha1
        Resource.__init__(self, *args, **kwargs)

    @property
    def sha256(self):
        """Gets the sha256 of this FileThumbprint.  # noqa: E501

        File's SHA256 thumbprint  # noqa: E501

        :return: The sha256 of this FileThumbprint.  # noqa: E501
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this FileThumbprint.

        File's SHA256 thumbprint  # noqa: E501

        :param sha256: The sha256 of this FileThumbprint.  # noqa: E501
        :type: str
        """
        if sha256 is None:
            raise ValueError("Invalid value for `sha256`, must not be `None`")  # noqa: E501

        self._sha256 = sha256

    @property
    def name(self):
        """Gets the name of this FileThumbprint.  # noqa: E501

        File name  # noqa: E501

        :return: The name of this FileThumbprint.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileThumbprint.

        File name  # noqa: E501

        :param name: The name of this FileThumbprint.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def sha1(self):
        """Gets the sha1 of this FileThumbprint.  # noqa: E501

        File's SHA1 thumbprint  # noqa: E501

        :return: The sha1 of this FileThumbprint.  # noqa: E501
        :rtype: str
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this FileThumbprint.

        File's SHA1 thumbprint  # noqa: E501

        :param sha1: The sha1 of this FileThumbprint.  # noqa: E501
        :type: str
        """
        if sha1 is None:
            raise ValueError("Invalid value for `sha1`, must not be `None`")  # noqa: E501

        self._sha1 = sha1

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
        if issubclass(FileThumbprint, dict):
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
        if not isinstance(other, FileThumbprint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
