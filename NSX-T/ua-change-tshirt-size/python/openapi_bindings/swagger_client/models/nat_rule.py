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

class NatRule(ManagedResource):
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
        'match_destination_network': 'str',
        'translated_network': 'str',
        'rule_priority': 'int',
        'match_service': 'NSServiceElement',
        'applied_tos': 'list[ResourceReference]',
        'enabled': 'bool',
        'internal_rule_id': 'str',
        'logging': 'bool',
        'translated_ports': 'str',
        'action': 'str',
        'firewall_match': 'str',
        'nat_pass': 'bool',
        'logical_router_id': 'str',
        'match_source_network': 'str'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'match_destination_network': 'match_destination_network',
        'translated_network': 'translated_network',
        'rule_priority': 'rule_priority',
        'match_service': 'match_service',
        'applied_tos': 'applied_tos',
        'enabled': 'enabled',
        'internal_rule_id': 'internal_rule_id',
        'logging': 'logging',
        'translated_ports': 'translated_ports',
        'action': 'action',
        'firewall_match': 'firewall_match',
        'nat_pass': 'nat_pass',
        'logical_router_id': 'logical_router_id',
        'match_source_network': 'match_source_network'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, match_destination_network=None, translated_network=None, rule_priority=1024, match_service=None, applied_tos=None, enabled=True, internal_rule_id=None, logging=False, translated_ports=None, action=None, firewall_match=None, nat_pass=True, logical_router_id=None, match_source_network=None, *args, **kwargs):  # noqa: E501
        """NatRule - a model defined in Swagger"""  # noqa: E501
        self._match_destination_network = None
        self._translated_network = None
        self._rule_priority = None
        self._match_service = None
        self._applied_tos = None
        self._enabled = None
        self._internal_rule_id = None
        self._logging = None
        self._translated_ports = None
        self._action = None
        self._firewall_match = None
        self._nat_pass = None
        self._logical_router_id = None
        self._match_source_network = None
        self.discriminator = None
        if match_destination_network is not None:
            self.match_destination_network = match_destination_network
        if translated_network is not None:
            self.translated_network = translated_network
        if rule_priority is not None:
            self.rule_priority = rule_priority
        if match_service is not None:
            self.match_service = match_service
        if applied_tos is not None:
            self.applied_tos = applied_tos
        if enabled is not None:
            self.enabled = enabled
        if internal_rule_id is not None:
            self.internal_rule_id = internal_rule_id
        if logging is not None:
            self.logging = logging
        if translated_ports is not None:
            self.translated_ports = translated_ports
        self.action = action
        if firewall_match is not None:
            self.firewall_match = firewall_match
        if nat_pass is not None:
            self.nat_pass = nat_pass
        if logical_router_id is not None:
            self.logical_router_id = logical_router_id
        if match_source_network is not None:
            self.match_source_network = match_source_network
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def match_destination_network(self):
        """Gets the match_destination_network of this NatRule.  # noqa: E501

        IP Address | CIDR | (null implies Any)   # noqa: E501

        :return: The match_destination_network of this NatRule.  # noqa: E501
        :rtype: str
        """
        return self._match_destination_network

    @match_destination_network.setter
    def match_destination_network(self, match_destination_network):
        """Sets the match_destination_network of this NatRule.

        IP Address | CIDR | (null implies Any)   # noqa: E501

        :param match_destination_network: The match_destination_network of this NatRule.  # noqa: E501
        :type: str
        """

        self._match_destination_network = match_destination_network

    @property
    def translated_network(self):
        """Gets the translated_network of this NatRule.  # noqa: E501

        The translated address for the matched IP packet. For a SNAT, it can be a single ip address, an ip range, or a CIDR block. For a DNAT and a REFLEXIVE, it can be a single ip address or a CIDR block. Translated network is not supported for NO_SNAT or NO_DNAT.   # noqa: E501

        :return: The translated_network of this NatRule.  # noqa: E501
        :rtype: str
        """
        return self._translated_network

    @translated_network.setter
    def translated_network(self, translated_network):
        """Sets the translated_network of this NatRule.

        The translated address for the matched IP packet. For a SNAT, it can be a single ip address, an ip range, or a CIDR block. For a DNAT and a REFLEXIVE, it can be a single ip address or a CIDR block. Translated network is not supported for NO_SNAT or NO_DNAT.   # noqa: E501

        :param translated_network: The translated_network of this NatRule.  # noqa: E501
        :type: str
        """

        self._translated_network = translated_network

    @property
    def rule_priority(self):
        """Gets the rule_priority of this NatRule.  # noqa: E501

        Ascending, valid range [0-2147483647]. If multiple rules have the same priority, evaluation sequence is undefined.   # noqa: E501

        :return: The rule_priority of this NatRule.  # noqa: E501
        :rtype: int
        """
        return self._rule_priority

    @rule_priority.setter
    def rule_priority(self, rule_priority):
        """Sets the rule_priority of this NatRule.

        Ascending, valid range [0-2147483647]. If multiple rules have the same priority, evaluation sequence is undefined.   # noqa: E501

        :param rule_priority: The rule_priority of this NatRule.  # noqa: E501
        :type: int
        """

        self._rule_priority = rule_priority

    @property
    def match_service(self):
        """Gets the match_service of this NatRule.  # noqa: E501


        :return: The match_service of this NatRule.  # noqa: E501
        :rtype: NSServiceElement
        """
        return self._match_service

    @match_service.setter
    def match_service(self, match_service):
        """Sets the match_service of this NatRule.


        :param match_service: The match_service of this NatRule.  # noqa: E501
        :type: NSServiceElement
        """

        self._match_service = match_service

    @property
    def applied_tos(self):
        """Gets the applied_tos of this NatRule.  # noqa: E501

        Holds the list of LogicalRouterPort Ids that a NAT rule can be applied to. The LogicalRouterPort used must belong to the same LogicalRouter for which the NAT Rule is created. As of now a NAT rule can only have a single LogicalRouterPort as applied_tos. When applied_tos is not set, the NAT rule is applied to all LogicalRouterPorts beloging to the LogicalRouter.  # noqa: E501

        :return: The applied_tos of this NatRule.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._applied_tos

    @applied_tos.setter
    def applied_tos(self, applied_tos):
        """Sets the applied_tos of this NatRule.

        Holds the list of LogicalRouterPort Ids that a NAT rule can be applied to. The LogicalRouterPort used must belong to the same LogicalRouter for which the NAT Rule is created. As of now a NAT rule can only have a single LogicalRouterPort as applied_tos. When applied_tos is not set, the NAT rule is applied to all LogicalRouterPorts beloging to the LogicalRouter.  # noqa: E501

        :param applied_tos: The applied_tos of this NatRule.  # noqa: E501
        :type: list[ResourceReference]
        """

        self._applied_tos = applied_tos

    @property
    def enabled(self):
        """Gets the enabled of this NatRule.  # noqa: E501

        Indicator to enable/disable the rule.   # noqa: E501

        :return: The enabled of this NatRule.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NatRule.

        Indicator to enable/disable the rule.   # noqa: E501

        :param enabled: The enabled of this NatRule.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def internal_rule_id(self):
        """Gets the internal_rule_id of this NatRule.  # noqa: E501

        Internal NAT rule uuid for debug used in Controller and backend.  # noqa: E501

        :return: The internal_rule_id of this NatRule.  # noqa: E501
        :rtype: str
        """
        return self._internal_rule_id

    @internal_rule_id.setter
    def internal_rule_id(self, internal_rule_id):
        """Sets the internal_rule_id of this NatRule.

        Internal NAT rule uuid for debug used in Controller and backend.  # noqa: E501

        :param internal_rule_id: The internal_rule_id of this NatRule.  # noqa: E501
        :type: str
        """

        self._internal_rule_id = internal_rule_id

    @property
    def logging(self):
        """Gets the logging of this NatRule.  # noqa: E501

        Enable/disable the logging of rule.   # noqa: E501

        :return: The logging of this NatRule.  # noqa: E501
        :rtype: bool
        """
        return self._logging

    @logging.setter
    def logging(self, logging):
        """Sets the logging of this NatRule.

        Enable/disable the logging of rule.   # noqa: E501

        :param logging: The logging of this NatRule.  # noqa: E501
        :type: bool
        """

        self._logging = logging

    @property
    def translated_ports(self):
        """Gets the translated_ports of this NatRule.  # noqa: E501

        The translated port(s) for the mtached IP packet. It can be a single port or a port range. Please note, port translating is supported only for DNAT.   # noqa: E501

        :return: The translated_ports of this NatRule.  # noqa: E501
        :rtype: str
        """
        return self._translated_ports

    @translated_ports.setter
    def translated_ports(self, translated_ports):
        """Sets the translated_ports of this NatRule.

        The translated port(s) for the mtached IP packet. It can be a single port or a port range. Please note, port translating is supported only for DNAT.   # noqa: E501

        :param translated_ports: The translated_ports of this NatRule.  # noqa: E501
        :type: str
        """

        self._translated_ports = translated_ports

    @property
    def action(self):
        """Gets the action of this NatRule.  # noqa: E501

        Valid actions: SNAT, DNAT, NO_SNAT, NO_DNAT, REFLEXIVE, NAT64. All rules in a logical router are either stateless or stateful. Mix is not supported. SNAT and DNAT are stateful, can NOT be supported when the logical router is running at active-active HA mode; REFLEXIVE is stateless. NO_SNAT and NO_DNAT have no translated_fields, only match fields are supported.   # noqa: E501

        :return: The action of this NatRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NatRule.

        Valid actions: SNAT, DNAT, NO_SNAT, NO_DNAT, REFLEXIVE, NAT64. All rules in a logical router are either stateless or stateful. Mix is not supported. SNAT and DNAT are stateful, can NOT be supported when the logical router is running at active-active HA mode; REFLEXIVE is stateless. NO_SNAT and NO_DNAT have no translated_fields, only match fields are supported.   # noqa: E501

        :param action: The action of this NatRule.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["SNAT", "DNAT", "REFLEXIVE", "NO_SNAT", "NO_DNAT", "NAT64"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def firewall_match(self):
        """Gets the firewall_match of this NatRule.  # noqa: E501

        Indicate how firewall is applied to a traffic packet. Firewall can be bypassed, or be applied to external/internal address of NAT rule.  The firewall_match will take priority over nat_pass. If the firewall_match is not provided, the nat_pass will be picked up.   # noqa: E501

        :return: The firewall_match of this NatRule.  # noqa: E501
        :rtype: str
        """
        return self._firewall_match

    @firewall_match.setter
    def firewall_match(self, firewall_match):
        """Sets the firewall_match of this NatRule.

        Indicate how firewall is applied to a traffic packet. Firewall can be bypassed, or be applied to external/internal address of NAT rule.  The firewall_match will take priority over nat_pass. If the firewall_match is not provided, the nat_pass will be picked up.   # noqa: E501

        :param firewall_match: The firewall_match of this NatRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["MATCH_EXTERNAL_ADDRESS", "MATCH_INTERNAL_ADDRESS", "BYPASS"]  # noqa: E501
        if firewall_match not in allowed_values:
            raise ValueError(
                "Invalid value for `firewall_match` ({0}), must be one of {1}"  # noqa: E501
                .format(firewall_match, allowed_values)
            )

        self._firewall_match = firewall_match

    @property
    def nat_pass(self):
        """Gets the nat_pass of this NatRule.  # noqa: E501

        Default is true. If the nat_pass is set to true, the following firewall stage will be skipped. Please note, if action is NO_SNAT or NO_DNAT, then nat_pass must be set to true or omitted.  Nat_pass was deprecated with an alternative firewall_match. Please stop using nat_pass to specify whether firewall stage is skipped. if you want to skip, please set firewall_match to BYPASS. If you do not want to skip, please set the firewall_match to MATCH_EXTERNAL_ADDRESS or MATCH_INTERNAL_ADDRESS.  Please note, the firewall_match will take priority over the nat_pass. If both are provided, the nat_pass is ignored. If firewall_match is not provided while the nat_pass is specified, the nat_pass will still be picked up. In this case, if nat_pass is set to false, firewall rule will be applied on internall address of a packet, i.e. MATCH_INTERNAL_ADDRESS.   # noqa: E501

        :return: The nat_pass of this NatRule.  # noqa: E501
        :rtype: bool
        """
        return self._nat_pass

    @nat_pass.setter
    def nat_pass(self, nat_pass):
        """Sets the nat_pass of this NatRule.

        Default is true. If the nat_pass is set to true, the following firewall stage will be skipped. Please note, if action is NO_SNAT or NO_DNAT, then nat_pass must be set to true or omitted.  Nat_pass was deprecated with an alternative firewall_match. Please stop using nat_pass to specify whether firewall stage is skipped. if you want to skip, please set firewall_match to BYPASS. If you do not want to skip, please set the firewall_match to MATCH_EXTERNAL_ADDRESS or MATCH_INTERNAL_ADDRESS.  Please note, the firewall_match will take priority over the nat_pass. If both are provided, the nat_pass is ignored. If firewall_match is not provided while the nat_pass is specified, the nat_pass will still be picked up. In this case, if nat_pass is set to false, firewall rule will be applied on internall address of a packet, i.e. MATCH_INTERNAL_ADDRESS.   # noqa: E501

        :param nat_pass: The nat_pass of this NatRule.  # noqa: E501
        :type: bool
        """

        self._nat_pass = nat_pass

    @property
    def logical_router_id(self):
        """Gets the logical_router_id of this NatRule.  # noqa: E501

        The logical router id which the nat rule runs on.  # noqa: E501

        :return: The logical_router_id of this NatRule.  # noqa: E501
        :rtype: str
        """
        return self._logical_router_id

    @logical_router_id.setter
    def logical_router_id(self, logical_router_id):
        """Sets the logical_router_id of this NatRule.

        The logical router id which the nat rule runs on.  # noqa: E501

        :param logical_router_id: The logical_router_id of this NatRule.  # noqa: E501
        :type: str
        """

        self._logical_router_id = logical_router_id

    @property
    def match_source_network(self):
        """Gets the match_source_network of this NatRule.  # noqa: E501

        IP Address | CIDR | (null implies Any)   # noqa: E501

        :return: The match_source_network of this NatRule.  # noqa: E501
        :rtype: str
        """
        return self._match_source_network

    @match_source_network.setter
    def match_source_network(self, match_source_network):
        """Sets the match_source_network of this NatRule.

        IP Address | CIDR | (null implies Any)   # noqa: E501

        :param match_source_network: The match_source_network of this NatRule.  # noqa: E501
        :type: str
        """

        self._match_source_network = match_source_network

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
        if issubclass(NatRule, dict):
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
        if not isinstance(other, NatRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
