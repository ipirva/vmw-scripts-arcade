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
from swagger_client.models.traceflow_observation import TraceflowObservation  # noqa: F401,E501

class TraceflowObservationDropped(TraceflowObservation):
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
        'nat_rule_id': 'int',
        'reason': 'str',
        'lport_id': 'str',
        'lport_name': 'str',
        'acl_rule_id': 'int',
        'arp_fail_reason': 'str'
    }
    if hasattr(TraceflowObservation, "swagger_types"):
        swagger_types.update(TraceflowObservation.swagger_types)

    attribute_map = {
        'nat_rule_id': 'nat_rule_id',
        'reason': 'reason',
        'lport_id': 'lport_id',
        'lport_name': 'lport_name',
        'acl_rule_id': 'acl_rule_id',
        'arp_fail_reason': 'arp_fail_reason'
    }
    if hasattr(TraceflowObservation, "attribute_map"):
        attribute_map.update(TraceflowObservation.attribute_map)

    def __init__(self, nat_rule_id=None, reason=None, lport_id=None, lport_name=None, acl_rule_id=None, arp_fail_reason=None, *args, **kwargs):  # noqa: E501
        """TraceflowObservationDropped - a model defined in Swagger"""  # noqa: E501
        self._nat_rule_id = None
        self._reason = None
        self._lport_id = None
        self._lport_name = None
        self._acl_rule_id = None
        self._arp_fail_reason = None
        self.discriminator = None
        if nat_rule_id is not None:
            self.nat_rule_id = nat_rule_id
        if reason is not None:
            self.reason = reason
        if lport_id is not None:
            self.lport_id = lport_id
        if lport_name is not None:
            self.lport_name = lport_name
        if acl_rule_id is not None:
            self.acl_rule_id = acl_rule_id
        if arp_fail_reason is not None:
            self.arp_fail_reason = arp_fail_reason
        TraceflowObservation.__init__(self, *args, **kwargs)

    @property
    def nat_rule_id(self):
        """Gets the nat_rule_id of this TraceflowObservationDropped.  # noqa: E501

        The ID of the NAT rule that was applied to forward the traceflow packet  # noqa: E501

        :return: The nat_rule_id of this TraceflowObservationDropped.  # noqa: E501
        :rtype: int
        """
        return self._nat_rule_id

    @nat_rule_id.setter
    def nat_rule_id(self, nat_rule_id):
        """Sets the nat_rule_id of this TraceflowObservationDropped.

        The ID of the NAT rule that was applied to forward the traceflow packet  # noqa: E501

        :param nat_rule_id: The nat_rule_id of this TraceflowObservationDropped.  # noqa: E501
        :type: int
        """

        self._nat_rule_id = nat_rule_id

    @property
    def reason(self):
        """Gets the reason of this TraceflowObservationDropped.  # noqa: E501

        The reason traceflow packet was dropped  # noqa: E501

        :return: The reason of this TraceflowObservationDropped.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this TraceflowObservationDropped.

        The reason traceflow packet was dropped  # noqa: E501

        :param reason: The reason of this TraceflowObservationDropped.  # noqa: E501
        :type: str
        """
        allowed_values = ["ARP_FAIL", "BFD", "DHCP", "DLB", "FW_RULE", "GENEVE", "GRE", "IFACE", "IP", "IP_REASS", "IPSEC", "IPSEC_VTI", "L2VPN", "L4PORT", "LB", "LROUTER", "LSERVICE", "LSWITCH", "MD_PROXY", "NAT", "ND_NS_FAIL", "NEIGH", "NO_EIP_FOUND", "NO_EIP_ASSOCIATION", "NO_ENI_FOR_IP", "NO_ENI_FOR_LIF", "NO_ROUTE", "NO_ROUTE_TABLE_FOUND", "NO_UNDERLAY_ROUTE_FOUND", "NOT_VDR_DOWNLINK,", "NO_VDR_FOUND", "NO_VDR_ON_HOST", "NOT_VDR_UPLINK,", "SERVICE_INSERT", "SPOOFGUARD", "TTL_ZERO", "TUNNEL", "VXLAN", "VXSTT", "VMC_NO_RESPONSE", "WRONG_UPLINK", "UNKNOWN"]  # noqa: E501
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def lport_id(self):
        """Gets the lport_id of this TraceflowObservationDropped.  # noqa: E501

        The id of the logical port at which the traceflow packet was dropped  # noqa: E501

        :return: The lport_id of this TraceflowObservationDropped.  # noqa: E501
        :rtype: str
        """
        return self._lport_id

    @lport_id.setter
    def lport_id(self, lport_id):
        """Sets the lport_id of this TraceflowObservationDropped.

        The id of the logical port at which the traceflow packet was dropped  # noqa: E501

        :param lport_id: The lport_id of this TraceflowObservationDropped.  # noqa: E501
        :type: str
        """

        self._lport_id = lport_id

    @property
    def lport_name(self):
        """Gets the lport_name of this TraceflowObservationDropped.  # noqa: E501

        The name of the logical port at which the traceflow packet was dropped  # noqa: E501

        :return: The lport_name of this TraceflowObservationDropped.  # noqa: E501
        :rtype: str
        """
        return self._lport_name

    @lport_name.setter
    def lport_name(self, lport_name):
        """Sets the lport_name of this TraceflowObservationDropped.

        The name of the logical port at which the traceflow packet was dropped  # noqa: E501

        :param lport_name: The lport_name of this TraceflowObservationDropped.  # noqa: E501
        :type: str
        """

        self._lport_name = lport_name

    @property
    def acl_rule_id(self):
        """Gets the acl_rule_id of this TraceflowObservationDropped.  # noqa: E501

        The id of the acl rule that was applied to drop the traceflow packet  # noqa: E501

        :return: The acl_rule_id of this TraceflowObservationDropped.  # noqa: E501
        :rtype: int
        """
        return self._acl_rule_id

    @acl_rule_id.setter
    def acl_rule_id(self, acl_rule_id):
        """Sets the acl_rule_id of this TraceflowObservationDropped.

        The id of the acl rule that was applied to drop the traceflow packet  # noqa: E501

        :param acl_rule_id: The acl_rule_id of this TraceflowObservationDropped.  # noqa: E501
        :type: int
        """

        self._acl_rule_id = acl_rule_id

    @property
    def arp_fail_reason(self):
        """Gets the arp_fail_reason of this TraceflowObservationDropped.  # noqa: E501

        This field specifies the ARP fails reason ARP_TIMEOUT - ARP failure due to query control plane timeout ARP_CPFAIL - ARP failure due post ARP query message to control plane failure ARP_FROMCP - ARP failure due to deleting ARP entry from control plane ARP_PORTDESTROY - ARP failure due to port destruction ARP_TABLEDESTROY - ARP failure due to ARP table destruction ARP_NETDESTROY - ARP failure due to overlay network destruction  # noqa: E501

        :return: The arp_fail_reason of this TraceflowObservationDropped.  # noqa: E501
        :rtype: str
        """
        return self._arp_fail_reason

    @arp_fail_reason.setter
    def arp_fail_reason(self, arp_fail_reason):
        """Sets the arp_fail_reason of this TraceflowObservationDropped.

        This field specifies the ARP fails reason ARP_TIMEOUT - ARP failure due to query control plane timeout ARP_CPFAIL - ARP failure due post ARP query message to control plane failure ARP_FROMCP - ARP failure due to deleting ARP entry from control plane ARP_PORTDESTROY - ARP failure due to port destruction ARP_TABLEDESTROY - ARP failure due to ARP table destruction ARP_NETDESTROY - ARP failure due to overlay network destruction  # noqa: E501

        :param arp_fail_reason: The arp_fail_reason of this TraceflowObservationDropped.  # noqa: E501
        :type: str
        """
        allowed_values = ["ARP_UNKNOWN", "ARP_TIMEOUT", "ARP_CPFAIL", "ARP_FROMCP", "ARP_PORTDESTROY", "ARP_TABLEDESTROY", "ARP_NETDESTROY"]  # noqa: E501
        if arp_fail_reason not in allowed_values:
            raise ValueError(
                "Invalid value for `arp_fail_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(arp_fail_reason, allowed_values)
            )

        self._arp_fail_reason = arp_fail_reason

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
        if issubclass(TraceflowObservationDropped, dict):
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
        if not isinstance(other, TraceflowObservationDropped):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other