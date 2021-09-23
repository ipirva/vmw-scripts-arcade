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
from swagger_client.models.login_credential import LoginCredential  # noqa: F401,E501

class AccessTokenLoginCredential(LoginCredential):
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
        'token': 'str',
        'token_expiry': 'int',
        'thumbprint': 'str'
    }
    if hasattr(LoginCredential, "swagger_types"):
        swagger_types.update(LoginCredential.swagger_types)

    attribute_map = {
        'token': 'token',
        'token_expiry': 'token_expiry',
        'thumbprint': 'thumbprint'
    }
    if hasattr(LoginCredential, "attribute_map"):
        attribute_map.update(LoginCredential.attribute_map)

    def __init__(self, token=None, token_expiry=None, thumbprint=None, *args, **kwargs):  # noqa: E501
        """AccessTokenLoginCredential - a model defined in Swagger"""  # noqa: E501
        self._token = None
        self._token_expiry = None
        self._thumbprint = None
        self.discriminator = None
        if token is not None:
            self.token = token
        if token_expiry is not None:
            self.token_expiry = token_expiry
        if thumbprint is not None:
            self.thumbprint = thumbprint
        LoginCredential.__init__(self, *args, **kwargs)

    @property
    def token(self):
        """Gets the token of this AccessTokenLoginCredential.  # noqa: E501

        Token obtained while validating connection config  # noqa: E501

        :return: The token of this AccessTokenLoginCredential.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AccessTokenLoginCredential.

        Token obtained while validating connection config  # noqa: E501

        :param token: The token of this AccessTokenLoginCredential.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def token_expiry(self):
        """Gets the token_expiry of this AccessTokenLoginCredential.  # noqa: E501

        Token expiry in epoch  # noqa: E501

        :return: The token_expiry of this AccessTokenLoginCredential.  # noqa: E501
        :rtype: int
        """
        return self._token_expiry

    @token_expiry.setter
    def token_expiry(self, token_expiry):
        """Sets the token_expiry of this AccessTokenLoginCredential.

        Token expiry in epoch  # noqa: E501

        :param token_expiry: The token_expiry of this AccessTokenLoginCredential.  # noqa: E501
        :type: int
        """

        self._token_expiry = token_expiry

    @property
    def thumbprint(self):
        """Gets the thumbprint of this AccessTokenLoginCredential.  # noqa: E501

        Thumbprint of the data source server  # noqa: E501

        :return: The thumbprint of this AccessTokenLoginCredential.  # noqa: E501
        :rtype: str
        """
        return self._thumbprint

    @thumbprint.setter
    def thumbprint(self, thumbprint):
        """Sets the thumbprint of this AccessTokenLoginCredential.

        Thumbprint of the data source server  # noqa: E501

        :param thumbprint: The thumbprint of this AccessTokenLoginCredential.  # noqa: E501
        :type: str
        """

        self._thumbprint = thumbprint

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
        if issubclass(AccessTokenLoginCredential, dict):
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
        if not isinstance(other, AccessTokenLoginCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other