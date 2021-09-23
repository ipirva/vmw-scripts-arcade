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

class LogicalRouterCentralizedServicePort(LogicalRouterPort):
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
        'linked_logical_switch_port_id': 'ResourceReference',
        'subnets': 'list[IPSubnet]',
        'enable_netx': 'bool',
        'urpf_mode': 'str',
        'ndra_profile_id': 'str',
        'mtu': 'int'
    }
    if hasattr(LogicalRouterPort, "swagger_types"):
        swagger_types.update(LogicalRouterPort.swagger_types)

    attribute_map = {
        'linked_logical_switch_port_id': 'linked_logical_switch_port_id',
        'subnets': 'subnets',
        'enable_netx': 'enable_netx',
        'urpf_mode': 'urpf_mode',
        'ndra_profile_id': 'ndra_profile_id',
        'mtu': 'mtu'
    }
    if hasattr(LogicalRouterPort, "attribute_map"):
        attribute_map.update(LogicalRouterPort.attribute_map)

    def __init__(self, linked_logical_switch_port_id=None, subnets=None, enable_netx=False, urpf_mode='STRICT', ndra_profile_id=None, mtu=None, *args, **kwargs):  # noqa: E501
        """LogicalRouterCentralizedServicePort - a model defined in Swagger"""  # noqa: E501
        self._linked_logical_switch_port_id = None
        self._subnets = None
        self._enable_netx = None
        self._urpf_mode = None
        self._ndra_profile_id = None
        self._mtu = None
        self.discriminator = None
        if linked_logical_switch_port_id is not None:
            self.linked_logical_switch_port_id = linked_logical_switch_port_id
        if subnets is not None:
            self.subnets = subnets
        if enable_netx is not None:
            self.enable_netx = enable_netx
        if urpf_mode is not None:
            self.urpf_mode = urpf_mode
        if ndra_profile_id is not None:
            self.ndra_profile_id = ndra_profile_id
        if mtu is not None:
            self.mtu = mtu
        LogicalRouterPort.__init__(self, *args, **kwargs)

    @property
    def linked_logical_switch_port_id(self):
        """Gets the linked_logical_switch_port_id of this LogicalRouterCentralizedServicePort.  # noqa: E501


        :return: The linked_logical_switch_port_id of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._linked_logical_switch_port_id

    @linked_logical_switch_port_id.setter
    def linked_logical_switch_port_id(self, linked_logical_switch_port_id):
        """Sets the linked_logical_switch_port_id of this LogicalRouterCentralizedServicePort.


        :param linked_logical_switch_port_id: The linked_logical_switch_port_id of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: ResourceReference
        """

        self._linked_logical_switch_port_id = linked_logical_switch_port_id

    @property
    def subnets(self):
        """Gets the subnets of this LogicalRouterCentralizedServicePort.  # noqa: E501

        Logical router port subnets  # noqa: E501

        :return: The subnets of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: list[IPSubnet]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this LogicalRouterCentralizedServicePort.

        Logical router port subnets  # noqa: E501

        :param subnets: The subnets of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: list[IPSubnet]
        """

        self._subnets = subnets

    @property
    def enable_netx(self):
        """Gets the enable_netx of this LogicalRouterCentralizedServicePort.  # noqa: E501

        Port is exclusively used for N-S service insertion  # noqa: E501

        :return: The enable_netx of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: bool
        """
        return self._enable_netx

    @enable_netx.setter
    def enable_netx(self, enable_netx):
        """Sets the enable_netx of this LogicalRouterCentralizedServicePort.

        Port is exclusively used for N-S service insertion  # noqa: E501

        :param enable_netx: The enable_netx of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: bool
        """

        self._enable_netx = enable_netx

    @property
    def urpf_mode(self):
        """Gets the urpf_mode of this LogicalRouterCentralizedServicePort.  # noqa: E501

        Unicast Reverse Path Forwarding mode  # noqa: E501

        :return: The urpf_mode of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: str
        """
        return self._urpf_mode

    @urpf_mode.setter
    def urpf_mode(self, urpf_mode):
        """Sets the urpf_mode of this LogicalRouterCentralizedServicePort.

        Unicast Reverse Path Forwarding mode  # noqa: E501

        :param urpf_mode: The urpf_mode of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "STRICT"]  # noqa: E501
        if urpf_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `urpf_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(urpf_mode, allowed_values)
            )

        self._urpf_mode = urpf_mode

    @property
    def ndra_profile_id(self):
        """Gets the ndra_profile_id of this LogicalRouterCentralizedServicePort.  # noqa: E501

        Identifier of Neighbor Discovery Router Advertisement profile associated with port. When NDRA profile id is associated at both the port level and logical router level, the profile id specified at port level takes the precedence.   # noqa: E501

        :return: The ndra_profile_id of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: str
        """
        return self._ndra_profile_id

    @ndra_profile_id.setter
    def ndra_profile_id(self, ndra_profile_id):
        """Sets the ndra_profile_id of this LogicalRouterCentralizedServicePort.

        Identifier of Neighbor Discovery Router Advertisement profile associated with port. When NDRA profile id is associated at both the port level and logical router level, the profile id specified at port level takes the precedence.   # noqa: E501

        :param ndra_profile_id: The ndra_profile_id of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: str
        """

        self._ndra_profile_id = ndra_profile_id

    @property
    def mtu(self):
        """Gets the mtu of this LogicalRouterCentralizedServicePort.  # noqa: E501

        Maximum transmission unit specifies the size of the largest packet that a network protocol can transmit. If not specified, the global logical MTU set in the /api/v1/global-configs/RoutingGlobalConfig API will be used.   # noqa: E501

        :return: The mtu of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this LogicalRouterCentralizedServicePort.

        Maximum transmission unit specifies the size of the largest packet that a network protocol can transmit. If not specified, the global logical MTU set in the /api/v1/global-configs/RoutingGlobalConfig API will be used.   # noqa: E501

        :param mtu: The mtu of this LogicalRouterCentralizedServicePort.  # noqa: E501
        :type: int
        """

        self._mtu = mtu

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
        if issubclass(LogicalRouterCentralizedServicePort, dict):
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
        if not isinstance(other, LogicalRouterCentralizedServicePort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other