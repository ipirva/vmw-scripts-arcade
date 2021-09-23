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

class BfdConfig(ManagedResource):
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
        'receive_interval': 'int',
        'declare_dead_multiple': 'int',
        'enabled': 'bool',
        'logical_router_id': 'str',
        'transmit_interval': 'int'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'receive_interval': 'receive_interval',
        'declare_dead_multiple': 'declare_dead_multiple',
        'enabled': 'enabled',
        'logical_router_id': 'logical_router_id',
        'transmit_interval': 'transmit_interval'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, receive_interval=500, declare_dead_multiple=3, enabled=False, logical_router_id=None, transmit_interval=500, *args, **kwargs):  # noqa: E501
        """BfdConfig - a model defined in Swagger"""  # noqa: E501
        self._receive_interval = None
        self._declare_dead_multiple = None
        self._enabled = None
        self._logical_router_id = None
        self._transmit_interval = None
        self.discriminator = None
        if receive_interval is not None:
            self.receive_interval = receive_interval
        if declare_dead_multiple is not None:
            self.declare_dead_multiple = declare_dead_multiple
        if enabled is not None:
            self.enabled = enabled
        if logical_router_id is not None:
            self.logical_router_id = logical_router_id
        if transmit_interval is not None:
            self.transmit_interval = transmit_interval
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def receive_interval(self):
        """Gets the receive_interval of this BfdConfig.  # noqa: E501

        the time interval (in milliseconds) between heartbeat packets for BFD when receiving heartbeats.  # noqa: E501

        :return: The receive_interval of this BfdConfig.  # noqa: E501
        :rtype: int
        """
        return self._receive_interval

    @receive_interval.setter
    def receive_interval(self, receive_interval):
        """Sets the receive_interval of this BfdConfig.

        the time interval (in milliseconds) between heartbeat packets for BFD when receiving heartbeats.  # noqa: E501

        :param receive_interval: The receive_interval of this BfdConfig.  # noqa: E501
        :type: int
        """

        self._receive_interval = receive_interval

    @property
    def declare_dead_multiple(self):
        """Gets the declare_dead_multiple of this BfdConfig.  # noqa: E501

        Number of times a packet is missed before BFD declares the neighbor down.  # noqa: E501

        :return: The declare_dead_multiple of this BfdConfig.  # noqa: E501
        :rtype: int
        """
        return self._declare_dead_multiple

    @declare_dead_multiple.setter
    def declare_dead_multiple(self, declare_dead_multiple):
        """Sets the declare_dead_multiple of this BfdConfig.

        Number of times a packet is missed before BFD declares the neighbor down.  # noqa: E501

        :param declare_dead_multiple: The declare_dead_multiple of this BfdConfig.  # noqa: E501
        :type: int
        """

        self._declare_dead_multiple = declare_dead_multiple

    @property
    def enabled(self):
        """Gets the enabled of this BfdConfig.  # noqa: E501

        Flag to enable BFD for this LogicalRouter  # noqa: E501

        :return: The enabled of this BfdConfig.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this BfdConfig.

        Flag to enable BFD for this LogicalRouter  # noqa: E501

        :param enabled: The enabled of this BfdConfig.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def logical_router_id(self):
        """Gets the logical_router_id of this BfdConfig.  # noqa: E501

        Logical router id  # noqa: E501

        :return: The logical_router_id of this BfdConfig.  # noqa: E501
        :rtype: str
        """
        return self._logical_router_id

    @logical_router_id.setter
    def logical_router_id(self, logical_router_id):
        """Sets the logical_router_id of this BfdConfig.

        Logical router id  # noqa: E501

        :param logical_router_id: The logical_router_id of this BfdConfig.  # noqa: E501
        :type: str
        """

        self._logical_router_id = logical_router_id

    @property
    def transmit_interval(self):
        """Gets the transmit_interval of this BfdConfig.  # noqa: E501

        the time interval (in milliseconds) between heartbeat packets for BFD when sending heartbeats.  # noqa: E501

        :return: The transmit_interval of this BfdConfig.  # noqa: E501
        :rtype: int
        """
        return self._transmit_interval

    @transmit_interval.setter
    def transmit_interval(self, transmit_interval):
        """Sets the transmit_interval of this BfdConfig.

        the time interval (in milliseconds) between heartbeat packets for BFD when sending heartbeats.  # noqa: E501

        :param transmit_interval: The transmit_interval of this BfdConfig.  # noqa: E501
        :type: int
        """

        self._transmit_interval = transmit_interval

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
        if issubclass(BfdConfig, dict):
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
        if not isinstance(other, BfdConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
