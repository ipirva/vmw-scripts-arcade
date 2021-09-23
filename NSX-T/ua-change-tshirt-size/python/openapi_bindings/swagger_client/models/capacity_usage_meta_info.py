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

class CapacityUsageMetaInfo(object):
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
        'max_global_threshold_percentage': 'float',
        'min_global_threshold_percentage': 'float',
        'last_updated_timestamp': 'int'
    }

    attribute_map = {
        'max_global_threshold_percentage': 'max_global_threshold_percentage',
        'min_global_threshold_percentage': 'min_global_threshold_percentage',
        'last_updated_timestamp': 'last_updated_timestamp'
    }

    def __init__(self, max_global_threshold_percentage=None, min_global_threshold_percentage=None, last_updated_timestamp=None):  # noqa: E501
        """CapacityUsageMetaInfo - a model defined in Swagger"""  # noqa: E501
        self._max_global_threshold_percentage = None
        self._min_global_threshold_percentage = None
        self._last_updated_timestamp = None
        self.discriminator = None
        self.max_global_threshold_percentage = max_global_threshold_percentage
        self.min_global_threshold_percentage = min_global_threshold_percentage
        self.last_updated_timestamp = last_updated_timestamp

    @property
    def max_global_threshold_percentage(self):
        """Gets the max_global_threshold_percentage of this CapacityUsageMetaInfo.  # noqa: E501

        Indicates the maximum global threshold percentage   # noqa: E501

        :return: The max_global_threshold_percentage of this CapacityUsageMetaInfo.  # noqa: E501
        :rtype: float
        """
        return self._max_global_threshold_percentage

    @max_global_threshold_percentage.setter
    def max_global_threshold_percentage(self, max_global_threshold_percentage):
        """Sets the max_global_threshold_percentage of this CapacityUsageMetaInfo.

        Indicates the maximum global threshold percentage   # noqa: E501

        :param max_global_threshold_percentage: The max_global_threshold_percentage of this CapacityUsageMetaInfo.  # noqa: E501
        :type: float
        """
        if max_global_threshold_percentage is None:
            raise ValueError("Invalid value for `max_global_threshold_percentage`, must not be `None`")  # noqa: E501

        self._max_global_threshold_percentage = max_global_threshold_percentage

    @property
    def min_global_threshold_percentage(self):
        """Gets the min_global_threshold_percentage of this CapacityUsageMetaInfo.  # noqa: E501

        Indicates the minimum global threshold percentage   # noqa: E501

        :return: The min_global_threshold_percentage of this CapacityUsageMetaInfo.  # noqa: E501
        :rtype: float
        """
        return self._min_global_threshold_percentage

    @min_global_threshold_percentage.setter
    def min_global_threshold_percentage(self, min_global_threshold_percentage):
        """Sets the min_global_threshold_percentage of this CapacityUsageMetaInfo.

        Indicates the minimum global threshold percentage   # noqa: E501

        :param min_global_threshold_percentage: The min_global_threshold_percentage of this CapacityUsageMetaInfo.  # noqa: E501
        :type: float
        """
        if min_global_threshold_percentage is None:
            raise ValueError("Invalid value for `min_global_threshold_percentage`, must not be `None`")  # noqa: E501

        self._min_global_threshold_percentage = min_global_threshold_percentage

    @property
    def last_updated_timestamp(self):
        """Gets the last_updated_timestamp of this CapacityUsageMetaInfo.  # noqa: E501

        Timestamp at which capacity usage was last calculated  # noqa: E501

        :return: The last_updated_timestamp of this CapacityUsageMetaInfo.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_timestamp

    @last_updated_timestamp.setter
    def last_updated_timestamp(self, last_updated_timestamp):
        """Sets the last_updated_timestamp of this CapacityUsageMetaInfo.

        Timestamp at which capacity usage was last calculated  # noqa: E501

        :param last_updated_timestamp: The last_updated_timestamp of this CapacityUsageMetaInfo.  # noqa: E501
        :type: int
        """
        if last_updated_timestamp is None:
            raise ValueError("Invalid value for `last_updated_timestamp`, must not be `None`")  # noqa: E501

        self._last_updated_timestamp = last_updated_timestamp

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
        if issubclass(CapacityUsageMetaInfo, dict):
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
        if not isinstance(other, CapacityUsageMetaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
