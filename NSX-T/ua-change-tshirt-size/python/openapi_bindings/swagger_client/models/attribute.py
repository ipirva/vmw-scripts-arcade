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

class Attribute(object):
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
        'read_only': 'bool',
        'attribute_type': 'str',
        'display_name': 'str',
        'value': 'str',
        'key': 'str'
    }

    attribute_map = {
        'read_only': 'read_only',
        'attribute_type': 'attribute_type',
        'display_name': 'display_name',
        'value': 'value',
        'key': 'key'
    }

    def __init__(self, read_only=False, attribute_type=None, display_name=None, value=None, key=None):  # noqa: E501
        """Attribute - a model defined in Swagger"""  # noqa: E501
        self._read_only = None
        self._attribute_type = None
        self._display_name = None
        self._value = None
        self._key = None
        self.discriminator = None
        if read_only is not None:
            self.read_only = read_only
        if attribute_type is not None:
            self.attribute_type = attribute_type
        if display_name is not None:
            self.display_name = display_name
        if value is not None:
            self.value = value
        self.key = key

    @property
    def read_only(self):
        """Gets the read_only of this Attribute.  # noqa: E501

        Read only Attribute cannot be overdidden by service instance/deployment.  # noqa: E501

        :return: The read_only of this Attribute.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this Attribute.

        Read only Attribute cannot be overdidden by service instance/deployment.  # noqa: E501

        :param read_only: The read_only of this Attribute.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def attribute_type(self):
        """Gets the attribute_type of this Attribute.  # noqa: E501

        Attribute Type can be of any of the allowed enum type.  # noqa: E501

        :return: The attribute_type of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """Sets the attribute_type of this Attribute.

        Attribute Type can be of any of the allowed enum type.  # noqa: E501

        :param attribute_type: The attribute_type of this Attribute.  # noqa: E501
        :type: str
        """
        allowed_values = ["IP_ADDRESS", "PORT", "PASSWORD", "STRING", "LONG", "BOOLEAN"]  # noqa: E501
        if attribute_type not in allowed_values:
            raise ValueError(
                "Invalid value for `attribute_type` ({0}), must be one of {1}"  # noqa: E501
                .format(attribute_type, allowed_values)
            )

        self._attribute_type = attribute_type

    @property
    def display_name(self):
        """Gets the display_name of this Attribute.  # noqa: E501

        Attribute display name string value.  # noqa: E501

        :return: The display_name of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Attribute.

        Attribute display name string value.  # noqa: E501

        :param display_name: The display_name of this Attribute.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def value(self):
        """Gets the value of this Attribute.  # noqa: E501

        Attribute value string value.  # noqa: E501

        :return: The value of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Attribute.

        Attribute value string value.  # noqa: E501

        :param value: The value of this Attribute.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def key(self):
        """Gets the key of this Attribute.  # noqa: E501

        Attribute key string value.  # noqa: E501

        :return: The key of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Attribute.

        Attribute key string value.  # noqa: E501

        :param key: The key of this Attribute.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

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
        if issubclass(Attribute, dict):
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
        if not isinstance(other, Attribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
