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
from swagger_client.models.managed_resource import ManagedResource  # noqa: F401,E501

class LatencyStatProfile(ManagedResource):
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
        'sampling_interval': 'int',
        'sampling_rate': 'int',
        'pnic_latency_enabled': 'bool'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'sampling_interval': 'sampling_interval',
        'sampling_rate': 'sampling_rate',
        'pnic_latency_enabled': 'pnic_latency_enabled'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, sampling_interval=None, sampling_rate=None, pnic_latency_enabled=False, *args, **kwargs):  # noqa: E501
        """LatencyStatProfile - a model defined in Swagger"""  # noqa: E501
        self._sampling_interval = None
        self._sampling_rate = None
        self._pnic_latency_enabled = None
        self.discriminator = None
        if sampling_interval is not None:
            self.sampling_interval = sampling_interval
        if sampling_rate is not None:
            self.sampling_rate = sampling_rate
        if pnic_latency_enabled is not None:
            self.pnic_latency_enabled = pnic_latency_enabled
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def sampling_interval(self):
        """Gets the sampling_interval of this LatencyStatProfile.  # noqa: E501

        Event nth milliseconds packet is sampled. When a value less than 1000 is given, the realized sampling interval will be 1000 milliseconds.   # noqa: E501

        :return: The sampling_interval of this LatencyStatProfile.  # noqa: E501
        :rtype: int
        """
        return self._sampling_interval

    @sampling_interval.setter
    def sampling_interval(self, sampling_interval):
        """Sets the sampling_interval of this LatencyStatProfile.

        Event nth milliseconds packet is sampled. When a value less than 1000 is given, the realized sampling interval will be 1000 milliseconds.   # noqa: E501

        :param sampling_interval: The sampling_interval of this LatencyStatProfile.  # noqa: E501
        :type: int
        """

        self._sampling_interval = sampling_interval

    @property
    def sampling_rate(self):
        """Gets the sampling_rate of this LatencyStatProfile.  # noqa: E501

        Event nth packet is sampled.   # noqa: E501

        :return: The sampling_rate of this LatencyStatProfile.  # noqa: E501
        :rtype: int
        """
        return self._sampling_rate

    @sampling_rate.setter
    def sampling_rate(self, sampling_rate):
        """Sets the sampling_rate of this LatencyStatProfile.

        Event nth packet is sampled.   # noqa: E501

        :param sampling_rate: The sampling_rate of this LatencyStatProfile.  # noqa: E501
        :type: int
        """

        self._sampling_rate = sampling_rate

    @property
    def pnic_latency_enabled(self):
        """Gets the pnic_latency_enabled of this LatencyStatProfile.  # noqa: E501

        Enable or Disable pnic latency.   # noqa: E501

        :return: The pnic_latency_enabled of this LatencyStatProfile.  # noqa: E501
        :rtype: bool
        """
        return self._pnic_latency_enabled

    @pnic_latency_enabled.setter
    def pnic_latency_enabled(self, pnic_latency_enabled):
        """Sets the pnic_latency_enabled of this LatencyStatProfile.

        Enable or Disable pnic latency.   # noqa: E501

        :param pnic_latency_enabled: The pnic_latency_enabled of this LatencyStatProfile.  # noqa: E501
        :type: bool
        """

        self._pnic_latency_enabled = pnic_latency_enabled

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
        if issubclass(LatencyStatProfile, dict):
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
        if not isinstance(other, LatencyStatProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other