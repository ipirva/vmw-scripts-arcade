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

class LogicalSwitchStatus(object):
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
        'num_logical_ports': 'int',
        'logical_switch_id': 'str'
    }

    attribute_map = {
        'num_logical_ports': 'num_logical_ports',
        'logical_switch_id': 'logical_switch_id'
    }

    def __init__(self, num_logical_ports=None, logical_switch_id=None):  # noqa: E501
        """LogicalSwitchStatus - a model defined in Swagger"""  # noqa: E501
        self._num_logical_ports = None
        self._logical_switch_id = None
        self.discriminator = None
        if num_logical_ports is not None:
            self.num_logical_ports = num_logical_ports
        if logical_switch_id is not None:
            self.logical_switch_id = logical_switch_id

    @property
    def num_logical_ports(self):
        """Gets the num_logical_ports of this LogicalSwitchStatus.  # noqa: E501

        Count of Logical Ports belonging to this switch  # noqa: E501

        :return: The num_logical_ports of this LogicalSwitchStatus.  # noqa: E501
        :rtype: int
        """
        return self._num_logical_ports

    @num_logical_ports.setter
    def num_logical_ports(self, num_logical_ports):
        """Sets the num_logical_ports of this LogicalSwitchStatus.

        Count of Logical Ports belonging to this switch  # noqa: E501

        :param num_logical_ports: The num_logical_ports of this LogicalSwitchStatus.  # noqa: E501
        :type: int
        """

        self._num_logical_ports = num_logical_ports

    @property
    def logical_switch_id(self):
        """Gets the logical_switch_id of this LogicalSwitchStatus.  # noqa: E501

        Unique ID identifying the the Logical Switch  # noqa: E501

        :return: The logical_switch_id of this LogicalSwitchStatus.  # noqa: E501
        :rtype: str
        """
        return self._logical_switch_id

    @logical_switch_id.setter
    def logical_switch_id(self, logical_switch_id):
        """Sets the logical_switch_id of this LogicalSwitchStatus.

        Unique ID identifying the the Logical Switch  # noqa: E501

        :param logical_switch_id: The logical_switch_id of this LogicalSwitchStatus.  # noqa: E501
        :type: str
        """

        self._logical_switch_id = logical_switch_id

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
        if issubclass(LogicalSwitchStatus, dict):
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
        if not isinstance(other, LogicalSwitchStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other