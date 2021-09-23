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

class VmknicNetwork(object):
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
        'destination_network': 'str',
        'device_name': 'str'
    }

    attribute_map = {
        'destination_network': 'destination_network',
        'device_name': 'device_name'
    }

    def __init__(self, destination_network=None, device_name=None):  # noqa: E501
        """VmknicNetwork - a model defined in Swagger"""  # noqa: E501
        self._destination_network = None
        self._device_name = None
        self.discriminator = None
        self.destination_network = destination_network
        self.device_name = device_name

    @property
    def destination_network(self):
        """Gets the destination_network of this VmknicNetwork.  # noqa: E501

        When migrating vmks to N-VDS/logical switches, the id is the logical switch id. When migrating out of N-VDS/logical switches, the id is the vSphere Switch portgroup name in a single vSphere Standard Switch (VSS), or distributed virtual portgroup name in a single distributed virtual switch (DVS).  # noqa: E501

        :return: The destination_network of this VmknicNetwork.  # noqa: E501
        :rtype: str
        """
        return self._destination_network

    @destination_network.setter
    def destination_network(self, destination_network):
        """Sets the destination_network of this VmknicNetwork.

        When migrating vmks to N-VDS/logical switches, the id is the logical switch id. When migrating out of N-VDS/logical switches, the id is the vSphere Switch portgroup name in a single vSphere Standard Switch (VSS), or distributed virtual portgroup name in a single distributed virtual switch (DVS).  # noqa: E501

        :param destination_network: The destination_network of this VmknicNetwork.  # noqa: E501
        :type: str
        """
        if destination_network is None:
            raise ValueError("Invalid value for `destination_network`, must not be `None`")  # noqa: E501

        self._destination_network = destination_network

    @property
    def device_name(self):
        """Gets the device_name of this VmknicNetwork.  # noqa: E501

        The vmk interface name, e.g., vmk0, vmk1; the id assigned by vCenter.  # noqa: E501

        :return: The device_name of this VmknicNetwork.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this VmknicNetwork.

        The vmk interface name, e.g., vmk0, vmk1; the id assigned by vCenter.  # noqa: E501

        :param device_name: The device_name of this VmknicNetwork.  # noqa: E501
        :type: str
        """
        if device_name is None:
            raise ValueError("Invalid value for `device_name`, must not be `None`")  # noqa: E501

        self._device_name = device_name

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
        if issubclass(VmknicNetwork, dict):
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
        if not isinstance(other, VmknicNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
