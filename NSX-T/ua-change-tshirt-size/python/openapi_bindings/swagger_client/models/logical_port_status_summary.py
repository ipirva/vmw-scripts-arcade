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

class LogicalPortStatusSummary(object):
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
        'total_ports': 'int',
        'last_update_timestamp': 'int',
        'up_ports': 'int',
        'filters': 'list[Filter]'
    }

    attribute_map = {
        'total_ports': 'total_ports',
        'last_update_timestamp': 'last_update_timestamp',
        'up_ports': 'up_ports',
        'filters': 'filters'
    }

    def __init__(self, total_ports=None, last_update_timestamp=None, up_ports=None, filters=None):  # noqa: E501
        """LogicalPortStatusSummary - a model defined in Swagger"""  # noqa: E501
        self._total_ports = None
        self._last_update_timestamp = None
        self._up_ports = None
        self._filters = None
        self.discriminator = None
        self.total_ports = total_ports
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        self.up_ports = up_ports
        if filters is not None:
            self.filters = filters

    @property
    def total_ports(self):
        """Gets the total_ports of this LogicalPortStatusSummary.  # noqa: E501

        The total number of logical ports.  # noqa: E501

        :return: The total_ports of this LogicalPortStatusSummary.  # noqa: E501
        :rtype: int
        """
        return self._total_ports

    @total_ports.setter
    def total_ports(self, total_ports):
        """Sets the total_ports of this LogicalPortStatusSummary.

        The total number of logical ports.  # noqa: E501

        :param total_ports: The total_ports of this LogicalPortStatusSummary.  # noqa: E501
        :type: int
        """
        if total_ports is None:
            raise ValueError("Invalid value for `total_ports`, must not be `None`")  # noqa: E501

        self._total_ports = total_ports

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this LogicalPortStatusSummary.  # noqa: E501

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :return: The last_update_timestamp of this LogicalPortStatusSummary.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this LogicalPortStatusSummary.

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this LogicalPortStatusSummary.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def up_ports(self):
        """Gets the up_ports of this LogicalPortStatusSummary.  # noqa: E501

        The number of logical ports whose Operational status is UP  # noqa: E501

        :return: The up_ports of this LogicalPortStatusSummary.  # noqa: E501
        :rtype: int
        """
        return self._up_ports

    @up_ports.setter
    def up_ports(self, up_ports):
        """Sets the up_ports of this LogicalPortStatusSummary.

        The number of logical ports whose Operational status is UP  # noqa: E501

        :param up_ports: The up_ports of this LogicalPortStatusSummary.  # noqa: E501
        :type: int
        """
        if up_ports is None:
            raise ValueError("Invalid value for `up_ports`, must not be `None`")  # noqa: E501

        self._up_ports = up_ports

    @property
    def filters(self):
        """Gets the filters of this LogicalPortStatusSummary.  # noqa: E501

        The filters used to find the logical ports- TransportZone id, LogicalSwitch id or LogicalSwitchProfile id  # noqa: E501

        :return: The filters of this LogicalPortStatusSummary.  # noqa: E501
        :rtype: list[Filter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this LogicalPortStatusSummary.

        The filters used to find the logical ports- TransportZone id, LogicalSwitch id or LogicalSwitchProfile id  # noqa: E501

        :param filters: The filters of this LogicalPortStatusSummary.  # noqa: E501
        :type: list[Filter]
        """

        self._filters = filters

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
        if issubclass(LogicalPortStatusSummary, dict):
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
        if not isinstance(other, LogicalPortStatusSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
