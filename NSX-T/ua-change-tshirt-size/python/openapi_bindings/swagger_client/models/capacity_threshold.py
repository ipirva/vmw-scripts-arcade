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

class CapacityThreshold(object):
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
        'max_threshold_percentage': 'float',
        'threshold_type': 'str',
        'min_threshold_percentage': 'float'
    }

    attribute_map = {
        'max_threshold_percentage': 'max_threshold_percentage',
        'threshold_type': 'threshold_type',
        'min_threshold_percentage': 'min_threshold_percentage'
    }

    def __init__(self, max_threshold_percentage=None, threshold_type=None, min_threshold_percentage=None):  # noqa: E501
        """CapacityThreshold - a model defined in Swagger"""  # noqa: E501
        self._max_threshold_percentage = None
        self._threshold_type = None
        self._min_threshold_percentage = None
        self.discriminator = None
        self.max_threshold_percentage = max_threshold_percentage
        self.threshold_type = threshold_type
        self.min_threshold_percentage = min_threshold_percentage

    @property
    def max_threshold_percentage(self):
        """Gets the max_threshold_percentage of this CapacityThreshold.  # noqa: E501

        Set the maximum threshold percentage. Specify a value between 0 and 100. Usage percentage above this value is tagged as critical.   # noqa: E501

        :return: The max_threshold_percentage of this CapacityThreshold.  # noqa: E501
        :rtype: float
        """
        return self._max_threshold_percentage

    @max_threshold_percentage.setter
    def max_threshold_percentage(self, max_threshold_percentage):
        """Sets the max_threshold_percentage of this CapacityThreshold.

        Set the maximum threshold percentage. Specify a value between 0 and 100. Usage percentage above this value is tagged as critical.   # noqa: E501

        :param max_threshold_percentage: The max_threshold_percentage of this CapacityThreshold.  # noqa: E501
        :type: float
        """
        if max_threshold_percentage is None:
            raise ValueError("Invalid value for `max_threshold_percentage`, must not be `None`")  # noqa: E501

        self._max_threshold_percentage = max_threshold_percentage

    @property
    def threshold_type(self):
        """Gets the threshold_type of this CapacityThreshold.  # noqa: E501

        Indicate the object type for which threshold is to be set.   # noqa: E501

        :return: The threshold_type of this CapacityThreshold.  # noqa: E501
        :rtype: str
        """
        return self._threshold_type

    @threshold_type.setter
    def threshold_type(self, threshold_type):
        """Sets the threshold_type of this CapacityThreshold.

        Indicate the object type for which threshold is to be set.   # noqa: E501

        :param threshold_type: The threshold_type of this CapacityThreshold.  # noqa: E501
        :type: str
        """
        if threshold_type is None:
            raise ValueError("Invalid value for `threshold_type`, must not be `None`")  # noqa: E501

        self._threshold_type = threshold_type

    @property
    def min_threshold_percentage(self):
        """Gets the min_threshold_percentage of this CapacityThreshold.  # noqa: E501

        Set the minimum threshold percentage. Specify a value between 0 and 100. Usage percentage above this value is tagged as warning.   # noqa: E501

        :return: The min_threshold_percentage of this CapacityThreshold.  # noqa: E501
        :rtype: float
        """
        return self._min_threshold_percentage

    @min_threshold_percentage.setter
    def min_threshold_percentage(self, min_threshold_percentage):
        """Sets the min_threshold_percentage of this CapacityThreshold.

        Set the minimum threshold percentage. Specify a value between 0 and 100. Usage percentage above this value is tagged as warning.   # noqa: E501

        :param min_threshold_percentage: The min_threshold_percentage of this CapacityThreshold.  # noqa: E501
        :type: float
        """
        if min_threshold_percentage is None:
            raise ValueError("Invalid value for `min_threshold_percentage`, must not be `None`")  # noqa: E501

        self._min_threshold_percentage = min_threshold_percentage

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
        if issubclass(CapacityThreshold, dict):
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
        if not isinstance(other, CapacityThreshold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
