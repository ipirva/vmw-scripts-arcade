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

class IdfwMasterSwitchSetting(object):
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
        'idfw_master_switch_enabled': 'bool'
    }

    attribute_map = {
        'idfw_master_switch_enabled': 'idfw_master_switch_enabled'
    }

    def __init__(self, idfw_master_switch_enabled=None):  # noqa: E501
        """IdfwMasterSwitchSetting - a model defined in Swagger"""  # noqa: E501
        self._idfw_master_switch_enabled = None
        self.discriminator = None
        self.idfw_master_switch_enabled = idfw_master_switch_enabled

    @property
    def idfw_master_switch_enabled(self):
        """Gets the idfw_master_switch_enabled of this IdfwMasterSwitchSetting.  # noqa: E501

        IDFW master switch (true=Enabled / false=Disabled).  # noqa: E501

        :return: The idfw_master_switch_enabled of this IdfwMasterSwitchSetting.  # noqa: E501
        :rtype: bool
        """
        return self._idfw_master_switch_enabled

    @idfw_master_switch_enabled.setter
    def idfw_master_switch_enabled(self, idfw_master_switch_enabled):
        """Sets the idfw_master_switch_enabled of this IdfwMasterSwitchSetting.

        IDFW master switch (true=Enabled / false=Disabled).  # noqa: E501

        :param idfw_master_switch_enabled: The idfw_master_switch_enabled of this IdfwMasterSwitchSetting.  # noqa: E501
        :type: bool
        """
        if idfw_master_switch_enabled is None:
            raise ValueError("Invalid value for `idfw_master_switch_enabled`, must not be `None`")  # noqa: E501

        self._idfw_master_switch_enabled = idfw_master_switch_enabled

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
        if issubclass(IdfwMasterSwitchSetting, dict):
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
        if not isinstance(other, IdfwMasterSwitchSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
