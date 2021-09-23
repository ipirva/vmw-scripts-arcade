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

class TransportNodeRemoteTunnelEndpointConfig(object):
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
        'named_teaming_policy': 'str',
        'host_switch_name': 'str',
        'rtep_vlan': 'int',
        'ip_assignment_spec': 'IpAssignmentSpec'
    }

    attribute_map = {
        'named_teaming_policy': 'named_teaming_policy',
        'host_switch_name': 'host_switch_name',
        'rtep_vlan': 'rtep_vlan',
        'ip_assignment_spec': 'ip_assignment_spec'
    }

    def __init__(self, named_teaming_policy=None, host_switch_name=None, rtep_vlan=None, ip_assignment_spec=None):  # noqa: E501
        """TransportNodeRemoteTunnelEndpointConfig - a model defined in Swagger"""  # noqa: E501
        self._named_teaming_policy = None
        self._host_switch_name = None
        self._rtep_vlan = None
        self._ip_assignment_spec = None
        self.discriminator = None
        if named_teaming_policy is not None:
            self.named_teaming_policy = named_teaming_policy
        self.host_switch_name = host_switch_name
        self.rtep_vlan = rtep_vlan
        self.ip_assignment_spec = ip_assignment_spec

    @property
    def named_teaming_policy(self):
        """Gets the named_teaming_policy of this TransportNodeRemoteTunnelEndpointConfig.  # noqa: E501

        Specifying this field will override the default teaming policy of the host switch and will be used by remote tunnel endpoint traffic.  # noqa: E501

        :return: The named_teaming_policy of this TransportNodeRemoteTunnelEndpointConfig.  # noqa: E501
        :rtype: str
        """
        return self._named_teaming_policy

    @named_teaming_policy.setter
    def named_teaming_policy(self, named_teaming_policy):
        """Sets the named_teaming_policy of this TransportNodeRemoteTunnelEndpointConfig.

        Specifying this field will override the default teaming policy of the host switch and will be used by remote tunnel endpoint traffic.  # noqa: E501

        :param named_teaming_policy: The named_teaming_policy of this TransportNodeRemoteTunnelEndpointConfig.  # noqa: E501
        :type: str
        """

        self._named_teaming_policy = named_teaming_policy

    @property
    def host_switch_name(self):
        """Gets the host_switch_name of this TransportNodeRemoteTunnelEndpointConfig.  # noqa: E501

        The host switch name should reference an existing host switch specified in the transport node configuration. The name will be used to identify the host switch responsible for processing remote tunnel endpoint traffic.  # noqa: E501

        :return: The host_switch_name of this TransportNodeRemoteTunnelEndpointConfig.  # noqa: E501
        :rtype: str
        """
        return self._host_switch_name

    @host_switch_name.setter
    def host_switch_name(self, host_switch_name):
        """Sets the host_switch_name of this TransportNodeRemoteTunnelEndpointConfig.

        The host switch name should reference an existing host switch specified in the transport node configuration. The name will be used to identify the host switch responsible for processing remote tunnel endpoint traffic.  # noqa: E501

        :param host_switch_name: The host_switch_name of this TransportNodeRemoteTunnelEndpointConfig.  # noqa: E501
        :type: str
        """
        if host_switch_name is None:
            raise ValueError("Invalid value for `host_switch_name`, must not be `None`")  # noqa: E501

        self._host_switch_name = host_switch_name

    @property
    def rtep_vlan(self):
        """Gets the rtep_vlan of this TransportNodeRemoteTunnelEndpointConfig.  # noqa: E501

        The transport VLAN id used for tagging intersite overlay traffic between remote tunnel endpoints.  # noqa: E501

        :return: The rtep_vlan of this TransportNodeRemoteTunnelEndpointConfig.  # noqa: E501
        :rtype: int
        """
        return self._rtep_vlan

    @rtep_vlan.setter
    def rtep_vlan(self, rtep_vlan):
        """Sets the rtep_vlan of this TransportNodeRemoteTunnelEndpointConfig.

        The transport VLAN id used for tagging intersite overlay traffic between remote tunnel endpoints.  # noqa: E501

        :param rtep_vlan: The rtep_vlan of this TransportNodeRemoteTunnelEndpointConfig.  # noqa: E501
        :type: int
        """
        if rtep_vlan is None:
            raise ValueError("Invalid value for `rtep_vlan`, must not be `None`")  # noqa: E501

        self._rtep_vlan = rtep_vlan

    @property
    def ip_assignment_spec(self):
        """Gets the ip_assignment_spec of this TransportNodeRemoteTunnelEndpointConfig.  # noqa: E501


        :return: The ip_assignment_spec of this TransportNodeRemoteTunnelEndpointConfig.  # noqa: E501
        :rtype: IpAssignmentSpec
        """
        return self._ip_assignment_spec

    @ip_assignment_spec.setter
    def ip_assignment_spec(self, ip_assignment_spec):
        """Sets the ip_assignment_spec of this TransportNodeRemoteTunnelEndpointConfig.


        :param ip_assignment_spec: The ip_assignment_spec of this TransportNodeRemoteTunnelEndpointConfig.  # noqa: E501
        :type: IpAssignmentSpec
        """
        if ip_assignment_spec is None:
            raise ValueError("Invalid value for `ip_assignment_spec`, must not be `None`")  # noqa: E501

        self._ip_assignment_spec = ip_assignment_spec

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
        if issubclass(TransportNodeRemoteTunnelEndpointConfig, dict):
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
        if not isinstance(other, TransportNodeRemoteTunnelEndpointConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other