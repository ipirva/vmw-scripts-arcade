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

class LbSslProtocolInfo(object):
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
        'is_default': 'bool',
        'is_secure': 'bool',
        'protocol': 'str'
    }

    attribute_map = {
        'is_default': 'is_default',
        'is_secure': 'is_secure',
        'protocol': 'protocol'
    }

    def __init__(self, is_default=None, is_secure=None, protocol=None):  # noqa: E501
        """LbSslProtocolInfo - a model defined in Swagger"""  # noqa: E501
        self._is_default = None
        self._is_secure = None
        self._protocol = None
        self.discriminator = None
        self.is_default = is_default
        self.is_secure = is_secure
        self.protocol = protocol

    @property
    def is_default(self):
        """Gets the is_default of this LbSslProtocolInfo.  # noqa: E501

        Default SSL protocol flag  # noqa: E501

        :return: The is_default of this LbSslProtocolInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this LbSslProtocolInfo.

        Default SSL protocol flag  # noqa: E501

        :param is_default: The is_default of this LbSslProtocolInfo.  # noqa: E501
        :type: bool
        """
        if is_default is None:
            raise ValueError("Invalid value for `is_default`, must not be `None`")  # noqa: E501

        self._is_default = is_default

    @property
    def is_secure(self):
        """Gets the is_secure of this LbSslProtocolInfo.  # noqa: E501

        Secure/insecure SSL protocol flag  # noqa: E501

        :return: The is_secure of this LbSslProtocolInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_secure

    @is_secure.setter
    def is_secure(self, is_secure):
        """Sets the is_secure of this LbSslProtocolInfo.

        Secure/insecure SSL protocol flag  # noqa: E501

        :param is_secure: The is_secure of this LbSslProtocolInfo.  # noqa: E501
        :type: bool
        """
        if is_secure is None:
            raise ValueError("Invalid value for `is_secure`, must not be `None`")  # noqa: E501

        self._is_secure = is_secure

    @property
    def protocol(self):
        """Gets the protocol of this LbSslProtocolInfo.  # noqa: E501

        SSL protocol  # noqa: E501

        :return: The protocol of this LbSslProtocolInfo.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this LbSslProtocolInfo.

        SSL protocol  # noqa: E501

        :param protocol: The protocol of this LbSslProtocolInfo.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501
        allowed_values = ["SSL_V2", "SSL_V3", "TLS_V1", "TLS_V1_1", "TLS_V1_2"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

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
        if issubclass(LbSslProtocolInfo, dict):
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
        if not isinstance(other, LbSslProtocolInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
