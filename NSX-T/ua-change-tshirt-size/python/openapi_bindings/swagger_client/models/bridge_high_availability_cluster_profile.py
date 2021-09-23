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
from swagger_client.models.cluster_profile import ClusterProfile  # noqa: F401,E501

class BridgeHighAvailabilityClusterProfile(ClusterProfile):
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
        'enable': 'bool',
        'bfd_probe_interval': 'int'
    }
    if hasattr(ClusterProfile, "swagger_types"):
        swagger_types.update(ClusterProfile.swagger_types)

    attribute_map = {
        'enable': 'enable',
        'bfd_probe_interval': 'bfd_probe_interval'
    }
    if hasattr(ClusterProfile, "attribute_map"):
        attribute_map.update(ClusterProfile.attribute_map)

    def __init__(self, enable=True, bfd_probe_interval=1000, *args, **kwargs):  # noqa: E501
        """BridgeHighAvailabilityClusterProfile - a model defined in Swagger"""  # noqa: E501
        self._enable = None
        self._bfd_probe_interval = None
        self.discriminator = None
        if enable is not None:
            self.enable = enable
        if bfd_probe_interval is not None:
            self.bfd_probe_interval = bfd_probe_interval
        ClusterProfile.__init__(self, *args, **kwargs)

    @property
    def enable(self):
        """Gets the enable of this BridgeHighAvailabilityClusterProfile.  # noqa: E501

        whether the heartbeat is enabled  # noqa: E501

        :return: The enable of this BridgeHighAvailabilityClusterProfile.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this BridgeHighAvailabilityClusterProfile.

        whether the heartbeat is enabled  # noqa: E501

        :param enable: The enable of this BridgeHighAvailabilityClusterProfile.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def bfd_probe_interval(self):
        """Gets the bfd_probe_interval of this BridgeHighAvailabilityClusterProfile.  # noqa: E501

        the time interval (in millisec) between probe packets for heartbeat purpose  # noqa: E501

        :return: The bfd_probe_interval of this BridgeHighAvailabilityClusterProfile.  # noqa: E501
        :rtype: int
        """
        return self._bfd_probe_interval

    @bfd_probe_interval.setter
    def bfd_probe_interval(self, bfd_probe_interval):
        """Sets the bfd_probe_interval of this BridgeHighAvailabilityClusterProfile.

        the time interval (in millisec) between probe packets for heartbeat purpose  # noqa: E501

        :param bfd_probe_interval: The bfd_probe_interval of this BridgeHighAvailabilityClusterProfile.  # noqa: E501
        :type: int
        """

        self._bfd_probe_interval = bfd_probe_interval

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
        if issubclass(BridgeHighAvailabilityClusterProfile, dict):
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
        if not isinstance(other, BridgeHighAvailabilityClusterProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
