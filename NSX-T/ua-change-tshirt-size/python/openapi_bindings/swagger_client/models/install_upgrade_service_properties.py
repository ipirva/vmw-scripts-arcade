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

class InstallUpgradeServiceProperties(object):
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
        'enabled_on': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'enabled_on': 'enabled_on',
        'enabled': 'enabled'
    }

    def __init__(self, enabled_on=None, enabled=None):  # noqa: E501
        """InstallUpgradeServiceProperties - a model defined in Swagger"""  # noqa: E501
        self._enabled_on = None
        self._enabled = None
        self.discriminator = None
        if enabled_on is not None:
            self.enabled_on = enabled_on
        self.enabled = enabled

    @property
    def enabled_on(self):
        """Gets the enabled_on of this InstallUpgradeServiceProperties.  # noqa: E501

        IP of manager on which install-upgrade is enabled  # noqa: E501

        :return: The enabled_on of this InstallUpgradeServiceProperties.  # noqa: E501
        :rtype: str
        """
        return self._enabled_on

    @enabled_on.setter
    def enabled_on(self, enabled_on):
        """Sets the enabled_on of this InstallUpgradeServiceProperties.

        IP of manager on which install-upgrade is enabled  # noqa: E501

        :param enabled_on: The enabled_on of this InstallUpgradeServiceProperties.  # noqa: E501
        :type: str
        """

        self._enabled_on = enabled_on

    @property
    def enabled(self):
        """Gets the enabled of this InstallUpgradeServiceProperties.  # noqa: E501

        True if service enabled; otherwise, false  # noqa: E501

        :return: The enabled of this InstallUpgradeServiceProperties.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this InstallUpgradeServiceProperties.

        True if service enabled; otherwise, false  # noqa: E501

        :param enabled: The enabled of this InstallUpgradeServiceProperties.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

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
        if issubclass(InstallUpgradeServiceProperties, dict):
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
        if not isinstance(other, InstallUpgradeServiceProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
