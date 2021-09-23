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
from swagger_client.models.logical_router_port import LogicalRouterPort  # noqa: F401,E501

class LogicalRouterIPTunnelPort(LogicalRouterPort):
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
        'subnets': 'list[IPSubnet]',
        'admin_state': 'str',
        'vpn_session_id': 'str'
    }
    if hasattr(LogicalRouterPort, "swagger_types"):
        swagger_types.update(LogicalRouterPort.swagger_types)

    attribute_map = {
        'subnets': 'subnets',
        'admin_state': 'admin_state',
        'vpn_session_id': 'vpn_session_id'
    }
    if hasattr(LogicalRouterPort, "attribute_map"):
        attribute_map.update(LogicalRouterPort.attribute_map)

    def __init__(self, subnets=None, admin_state=None, vpn_session_id=None, *args, **kwargs):  # noqa: E501
        """LogicalRouterIPTunnelPort - a model defined in Swagger"""  # noqa: E501
        self._subnets = None
        self._admin_state = None
        self._vpn_session_id = None
        self.discriminator = None
        if subnets is not None:
            self.subnets = subnets
        if admin_state is not None:
            self.admin_state = admin_state
        if vpn_session_id is not None:
            self.vpn_session_id = vpn_session_id
        LogicalRouterPort.__init__(self, *args, **kwargs)

    @property
    def subnets(self):
        """Gets the subnets of this LogicalRouterIPTunnelPort.  # noqa: E501

        Tunnel port subnets.  # noqa: E501

        :return: The subnets of this LogicalRouterIPTunnelPort.  # noqa: E501
        :rtype: list[IPSubnet]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this LogicalRouterIPTunnelPort.

        Tunnel port subnets.  # noqa: E501

        :param subnets: The subnets of this LogicalRouterIPTunnelPort.  # noqa: E501
        :type: list[IPSubnet]
        """

        self._subnets = subnets

    @property
    def admin_state(self):
        """Gets the admin_state of this LogicalRouterIPTunnelPort.  # noqa: E501

        Admin state of port.  # noqa: E501

        :return: The admin_state of this LogicalRouterIPTunnelPort.  # noqa: E501
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this LogicalRouterIPTunnelPort.

        Admin state of port.  # noqa: E501

        :param admin_state: The admin_state of this LogicalRouterIPTunnelPort.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "DOWN"]  # noqa: E501
        if admin_state not in allowed_values:
            raise ValueError(
                "Invalid value for `admin_state` ({0}), must be one of {1}"  # noqa: E501
                .format(admin_state, allowed_values)
            )

        self._admin_state = admin_state

    @property
    def vpn_session_id(self):
        """Gets the vpn_session_id of this LogicalRouterIPTunnelPort.  # noqa: E501

        Associated VPN session identifier.  # noqa: E501

        :return: The vpn_session_id of this LogicalRouterIPTunnelPort.  # noqa: E501
        :rtype: str
        """
        return self._vpn_session_id

    @vpn_session_id.setter
    def vpn_session_id(self, vpn_session_id):
        """Sets the vpn_session_id of this LogicalRouterIPTunnelPort.

        Associated VPN session identifier.  # noqa: E501

        :param vpn_session_id: The vpn_session_id of this LogicalRouterIPTunnelPort.  # noqa: E501
        :type: str
        """

        self._vpn_session_id = vpn_session_id

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
        if issubclass(LogicalRouterIPTunnelPort, dict):
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
        if not isinstance(other, LogicalRouterIPTunnelPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other