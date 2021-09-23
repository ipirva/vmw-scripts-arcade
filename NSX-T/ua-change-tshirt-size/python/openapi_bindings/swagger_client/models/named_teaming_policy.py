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
from swagger_client.models.teaming_policy import TeamingPolicy  # noqa: F401,E501

class NamedTeamingPolicy(TeamingPolicy):
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
        'name': 'str'
    }
    if hasattr(TeamingPolicy, "swagger_types"):
        swagger_types.update(TeamingPolicy.swagger_types)

    attribute_map = {
        'name': 'name'
    }
    if hasattr(TeamingPolicy, "attribute_map"):
        attribute_map.update(TeamingPolicy.attribute_map)

    def __init__(self, name=None, *args, **kwargs):  # noqa: E501
        """NamedTeamingPolicy - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self.discriminator = None
        self.name = name
        TeamingPolicy.__init__(self, *args, **kwargs)

    @property
    def name(self):
        """Gets the name of this NamedTeamingPolicy.  # noqa: E501

        An uplink teaming policy of a given name defined in UplinkHostSwitchProfile. The names of all NamedTeamingPolicies in an UplinkHostSwitchProfile must be different, but a name can be shared by different UplinkHostSwitchProfiles. Different TransportNodes can use different NamedTeamingPolicies having the same name in different UplinkHostSwitchProfiles to realize an uplink teaming policy on a logical switch. An uplink teaming policy on a logical switch can be any policy defined by a user; it does not have to be a single type of FAILOVER or LOADBALANCE. It can be a combination of types, for instance, a user can define a policy with name \"MyHybridTeamingPolicy\" as \"FAILOVER on all ESX TransportNodes and LOADBALANCE on all KVM TransportNodes\". The name is the key of the teaming policy and can not be changed once assigned.  # noqa: E501

        :return: The name of this NamedTeamingPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NamedTeamingPolicy.

        An uplink teaming policy of a given name defined in UplinkHostSwitchProfile. The names of all NamedTeamingPolicies in an UplinkHostSwitchProfile must be different, but a name can be shared by different UplinkHostSwitchProfiles. Different TransportNodes can use different NamedTeamingPolicies having the same name in different UplinkHostSwitchProfiles to realize an uplink teaming policy on a logical switch. An uplink teaming policy on a logical switch can be any policy defined by a user; it does not have to be a single type of FAILOVER or LOADBALANCE. It can be a combination of types, for instance, a user can define a policy with name \"MyHybridTeamingPolicy\" as \"FAILOVER on all ESX TransportNodes and LOADBALANCE on all KVM TransportNodes\". The name is the key of the teaming policy and can not be changed once assigned.  # noqa: E501

        :param name: The name of this NamedTeamingPolicy.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(NamedTeamingPolicy, dict):
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
        if not isinstance(other, NamedTeamingPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
