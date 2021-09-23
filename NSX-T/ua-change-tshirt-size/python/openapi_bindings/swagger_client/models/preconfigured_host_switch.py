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

class PreconfiguredHostSwitch(object):
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
        'host_switch_id': 'str',
        'endpoints': 'list[PreconfiguredEndpoint]',
        'transport_zone_endpoints': 'list[TransportZoneEndPoint]'
    }

    attribute_map = {
        'host_switch_id': 'host_switch_id',
        'endpoints': 'endpoints',
        'transport_zone_endpoints': 'transport_zone_endpoints'
    }

    def __init__(self, host_switch_id=None, endpoints=None, transport_zone_endpoints=None):  # noqa: E501
        """PreconfiguredHostSwitch - a model defined in Swagger"""  # noqa: E501
        self._host_switch_id = None
        self._endpoints = None
        self._transport_zone_endpoints = None
        self.discriminator = None
        self.host_switch_id = host_switch_id
        if endpoints is not None:
            self.endpoints = endpoints
        if transport_zone_endpoints is not None:
            self.transport_zone_endpoints = transport_zone_endpoints

    @property
    def host_switch_id(self):
        """Gets the host_switch_id of this PreconfiguredHostSwitch.  # noqa: E501

        External Id of the preconfigured host switch.  # noqa: E501

        :return: The host_switch_id of this PreconfiguredHostSwitch.  # noqa: E501
        :rtype: str
        """
        return self._host_switch_id

    @host_switch_id.setter
    def host_switch_id(self, host_switch_id):
        """Sets the host_switch_id of this PreconfiguredHostSwitch.

        External Id of the preconfigured host switch.  # noqa: E501

        :param host_switch_id: The host_switch_id of this PreconfiguredHostSwitch.  # noqa: E501
        :type: str
        """
        if host_switch_id is None:
            raise ValueError("Invalid value for `host_switch_id`, must not be `None`")  # noqa: E501

        self._host_switch_id = host_switch_id

    @property
    def endpoints(self):
        """Gets the endpoints of this PreconfiguredHostSwitch.  # noqa: E501

        List of virtual tunnel endpoints which are preconfigured on this host switch  # noqa: E501

        :return: The endpoints of this PreconfiguredHostSwitch.  # noqa: E501
        :rtype: list[PreconfiguredEndpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this PreconfiguredHostSwitch.

        List of virtual tunnel endpoints which are preconfigured on this host switch  # noqa: E501

        :param endpoints: The endpoints of this PreconfiguredHostSwitch.  # noqa: E501
        :type: list[PreconfiguredEndpoint]
        """

        self._endpoints = endpoints

    @property
    def transport_zone_endpoints(self):
        """Gets the transport_zone_endpoints of this PreconfiguredHostSwitch.  # noqa: E501

        List of TransportZones that are to be associated with specified host switch.  # noqa: E501

        :return: The transport_zone_endpoints of this PreconfiguredHostSwitch.  # noqa: E501
        :rtype: list[TransportZoneEndPoint]
        """
        return self._transport_zone_endpoints

    @transport_zone_endpoints.setter
    def transport_zone_endpoints(self, transport_zone_endpoints):
        """Sets the transport_zone_endpoints of this PreconfiguredHostSwitch.

        List of TransportZones that are to be associated with specified host switch.  # noqa: E501

        :param transport_zone_endpoints: The transport_zone_endpoints of this PreconfiguredHostSwitch.  # noqa: E501
        :type: list[TransportZoneEndPoint]
        """

        self._transport_zone_endpoints = transport_zone_endpoints

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
        if issubclass(PreconfiguredHostSwitch, dict):
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
        if not isinstance(other, PreconfiguredHostSwitch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
