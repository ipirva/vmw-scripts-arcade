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

class UsernamePasswordLoginCredential(LoginCredential):
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
        'username': 'str',
        'password': 'str',
        'thumbprint': 'str'
    }
    if hasattr(LoginCredential, "swagger_types"):
        swagger_types.update(LoginCredential.swagger_types)

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'thumbprint': 'thumbprint'
    }
    if hasattr(LoginCredential, "attribute_map"):
        attribute_map.update(LoginCredential.attribute_map)

    def __init__(self, username=None, password=None, thumbprint=None, *args, **kwargs):  # noqa: E501
        """UsernamePasswordLoginCredential - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._password = None
        self._thumbprint = None
        self.discriminator = None
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if thumbprint is not None:
            self.thumbprint = thumbprint
        LoginCredential.__init__(self, *args, **kwargs)

    @property
    def username(self):
        """Gets the username of this UsernamePasswordLoginCredential.  # noqa: E501

        The username for login  # noqa: E501

        :return: The username of this UsernamePasswordLoginCredential.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UsernamePasswordLoginCredential.

        The username for login  # noqa: E501

        :param username: The username of this UsernamePasswordLoginCredential.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this UsernamePasswordLoginCredential.  # noqa: E501

        The authentication password for login  # noqa: E501

        :return: The password of this UsernamePasswordLoginCredential.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UsernamePasswordLoginCredential.

        The authentication password for login  # noqa: E501

        :param password: The password of this UsernamePasswordLoginCredential.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def thumbprint(self):
        """Gets the thumbprint of this UsernamePasswordLoginCredential.  # noqa: E501

        Thumbprint of the login server  # noqa: E501

        :return: The thumbprint of this UsernamePasswordLoginCredential.  # noqa: E501
        :rtype: str
        """
        return self._thumbprint

    @thumbprint.setter
    def thumbprint(self, thumbprint):
        """Sets the thumbprint of this UsernamePasswordLoginCredential.

        Thumbprint of the login server  # noqa: E501

        :param thumbprint: The thumbprint of this UsernamePasswordLoginCredential.  # noqa: E501
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
        if issubclass(UsernamePasswordLoginCredential, dict):
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
        if not isinstance(other, UsernamePasswordLoginCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
