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
from swagger_client.models.ipfix_config import IpfixConfig  # noqa: F401,E501

class IpfixSwitchConfig(IpfixConfig):
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
        'active_timeout': 'int',
        'idle_timeout': 'int',
        'packet_sample_probability': 'float',
        'max_flows': 'int'
    }
    if hasattr(IpfixConfig, "swagger_types"):
        swagger_types.update(IpfixConfig.swagger_types)

    attribute_map = {
        'active_timeout': 'active_timeout',
        'idle_timeout': 'idle_timeout',
        'packet_sample_probability': 'packet_sample_probability',
        'max_flows': 'max_flows'
    }
    if hasattr(IpfixConfig, "attribute_map"):
        attribute_map.update(IpfixConfig.attribute_map)

    def __init__(self, active_timeout=300, idle_timeout=300, packet_sample_probability=None, max_flows=16384, *args, **kwargs):  # noqa: E501
        """IpfixSwitchConfig - a model defined in Swagger"""  # noqa: E501
        self._active_timeout = None
        self._idle_timeout = None
        self._packet_sample_probability = None
        self._max_flows = None
        self.discriminator = None
        if active_timeout is not None:
            self.active_timeout = active_timeout
        if idle_timeout is not None:
            self.idle_timeout = idle_timeout
        if packet_sample_probability is not None:
            self.packet_sample_probability = packet_sample_probability
        if max_flows is not None:
            self.max_flows = max_flows
        IpfixConfig.__init__(self, *args, **kwargs)

    @property
    def active_timeout(self):
        """Gets the active_timeout of this IpfixSwitchConfig.  # noqa: E501

        The time in seconds after a Flow is expired even if more packets matching this Flow are received by the cache.   # noqa: E501

        :return: The active_timeout of this IpfixSwitchConfig.  # noqa: E501
        :rtype: int
        """
        return self._active_timeout

    @active_timeout.setter
    def active_timeout(self, active_timeout):
        """Sets the active_timeout of this IpfixSwitchConfig.

        The time in seconds after a Flow is expired even if more packets matching this Flow are received by the cache.   # noqa: E501

        :param active_timeout: The active_timeout of this IpfixSwitchConfig.  # noqa: E501
        :type: int
        """

        self._active_timeout = active_timeout

    @property
    def idle_timeout(self):
        """Gets the idle_timeout of this IpfixSwitchConfig.  # noqa: E501

        The time in seconds after a Flow is expired if no more packets matching this Flow are received by the cache.   # noqa: E501

        :return: The idle_timeout of this IpfixSwitchConfig.  # noqa: E501
        :rtype: int
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        """Sets the idle_timeout of this IpfixSwitchConfig.

        The time in seconds after a Flow is expired if no more packets matching this Flow are received by the cache.   # noqa: E501

        :param idle_timeout: The idle_timeout of this IpfixSwitchConfig.  # noqa: E501
        :type: int
        """

        self._idle_timeout = idle_timeout

    @property
    def packet_sample_probability(self):
        """Gets the packet_sample_probability of this IpfixSwitchConfig.  # noqa: E501

        The probability in percentage that a packet is sampled. The value should be  in range (0,100] and can only have three decimal places at most. The probability  is equal for every packet.   # noqa: E501

        :return: The packet_sample_probability of this IpfixSwitchConfig.  # noqa: E501
        :rtype: float
        """
        return self._packet_sample_probability

    @packet_sample_probability.setter
    def packet_sample_probability(self, packet_sample_probability):
        """Sets the packet_sample_probability of this IpfixSwitchConfig.

        The probability in percentage that a packet is sampled. The value should be  in range (0,100] and can only have three decimal places at most. The probability  is equal for every packet.   # noqa: E501

        :param packet_sample_probability: The packet_sample_probability of this IpfixSwitchConfig.  # noqa: E501
        :type: float
        """

        self._packet_sample_probability = packet_sample_probability

    @property
    def max_flows(self):
        """Gets the max_flows of this IpfixSwitchConfig.  # noqa: E501

        The maximum number of flow entries in each exporter flow cache.   # noqa: E501

        :return: The max_flows of this IpfixSwitchConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_flows

    @max_flows.setter
    def max_flows(self, max_flows):
        """Sets the max_flows of this IpfixSwitchConfig.

        The maximum number of flow entries in each exporter flow cache.   # noqa: E501

        :param max_flows: The max_flows of this IpfixSwitchConfig.  # noqa: E501
        :type: int
        """

        self._max_flows = max_flows

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
        if issubclass(IpfixSwitchConfig, dict):
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
        if not isinstance(other, IpfixSwitchConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
