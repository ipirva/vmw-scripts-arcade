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
from swagger_client.models.qos_base_rate_shaper import QosBaseRateShaper  # noqa: F401,E501

class IngressBroadcastRateShaper(QosBaseRateShaper):
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
        'average_bandwidth_kbps': 'int',
        'peak_bandwidth_kbps': 'int',
        'burst_size_bytes': 'int'
    }
    if hasattr(QosBaseRateShaper, "swagger_types"):
        swagger_types.update(QosBaseRateShaper.swagger_types)

    attribute_map = {
        'average_bandwidth_kbps': 'average_bandwidth_kbps',
        'peak_bandwidth_kbps': 'peak_bandwidth_kbps',
        'burst_size_bytes': 'burst_size_bytes'
    }
    if hasattr(QosBaseRateShaper, "attribute_map"):
        attribute_map.update(QosBaseRateShaper.attribute_map)

    def __init__(self, average_bandwidth_kbps=0, peak_bandwidth_kbps=0, burst_size_bytes=0, *args, **kwargs):  # noqa: E501
        """IngressBroadcastRateShaper - a model defined in Swagger"""  # noqa: E501
        self._average_bandwidth_kbps = None
        self._peak_bandwidth_kbps = None
        self._burst_size_bytes = None
        self.discriminator = None
        if average_bandwidth_kbps is not None:
            self.average_bandwidth_kbps = average_bandwidth_kbps
        if peak_bandwidth_kbps is not None:
            self.peak_bandwidth_kbps = peak_bandwidth_kbps
        if burst_size_bytes is not None:
            self.burst_size_bytes = burst_size_bytes
        QosBaseRateShaper.__init__(self, *args, **kwargs)

    @property
    def average_bandwidth_kbps(self):
        """Gets the average_bandwidth_kbps of this IngressBroadcastRateShaper.  # noqa: E501

        Average bandwidth in kb/s  # noqa: E501

        :return: The average_bandwidth_kbps of this IngressBroadcastRateShaper.  # noqa: E501
        :rtype: int
        """
        return self._average_bandwidth_kbps

    @average_bandwidth_kbps.setter
    def average_bandwidth_kbps(self, average_bandwidth_kbps):
        """Sets the average_bandwidth_kbps of this IngressBroadcastRateShaper.

        Average bandwidth in kb/s  # noqa: E501

        :param average_bandwidth_kbps: The average_bandwidth_kbps of this IngressBroadcastRateShaper.  # noqa: E501
        :type: int
        """

        self._average_bandwidth_kbps = average_bandwidth_kbps

    @property
    def peak_bandwidth_kbps(self):
        """Gets the peak_bandwidth_kbps of this IngressBroadcastRateShaper.  # noqa: E501

        Peak bandwidth in kb/s  # noqa: E501

        :return: The peak_bandwidth_kbps of this IngressBroadcastRateShaper.  # noqa: E501
        :rtype: int
        """
        return self._peak_bandwidth_kbps

    @peak_bandwidth_kbps.setter
    def peak_bandwidth_kbps(self, peak_bandwidth_kbps):
        """Sets the peak_bandwidth_kbps of this IngressBroadcastRateShaper.

        Peak bandwidth in kb/s  # noqa: E501

        :param peak_bandwidth_kbps: The peak_bandwidth_kbps of this IngressBroadcastRateShaper.  # noqa: E501
        :type: int
        """

        self._peak_bandwidth_kbps = peak_bandwidth_kbps

    @property
    def burst_size_bytes(self):
        """Gets the burst_size_bytes of this IngressBroadcastRateShaper.  # noqa: E501

        Burst size in bytes  # noqa: E501

        :return: The burst_size_bytes of this IngressBroadcastRateShaper.  # noqa: E501
        :rtype: int
        """
        return self._burst_size_bytes

    @burst_size_bytes.setter
    def burst_size_bytes(self, burst_size_bytes):
        """Sets the burst_size_bytes of this IngressBroadcastRateShaper.

        Burst size in bytes  # noqa: E501

        :param burst_size_bytes: The burst_size_bytes of this IngressBroadcastRateShaper.  # noqa: E501
        :type: int
        """

        self._burst_size_bytes = burst_size_bytes

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
        if issubclass(IngressBroadcastRateShaper, dict):
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
        if not isinstance(other, IngressBroadcastRateShaper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
