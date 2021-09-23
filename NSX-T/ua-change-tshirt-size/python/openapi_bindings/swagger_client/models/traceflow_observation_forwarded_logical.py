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

class TraceflowObservationForwardedLogical(TraceflowObservation):
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
        'service_path_index': 'int',
        'component_id': 'str',
        'spoofguard_vlan_id': 'int',
        'resend_type': 'str',
        'lport_name': 'str',
        'acl_rule_id': 'int',
        'service_index': 'int',
        'vni': 'int',
        'dst_component_name': 'str',
        'nat_rule_id': 'int',
        'translated_src_ip': 'str',
        'translated_dst_ip': 'str',
        'spoofguard_mac': 'str',
        'dst_component_type': 'str',
        'lport_id': 'str',
        'dst_component_id': 'str',
        'spoofguard_ip': 'str',
        'service_ttl': 'int',
        'svc_nh_mac': 'str'
    }
    if hasattr(TraceflowObservation, "swagger_types"):
        swagger_types.update(TraceflowObservation.swagger_types)

    attribute_map = {
        'service_path_index': 'service_path_index',
        'component_id': 'component_id',
        'spoofguard_vlan_id': 'spoofguard_vlan_id',
        'resend_type': 'resend_type',
        'lport_name': 'lport_name',
        'acl_rule_id': 'acl_rule_id',
        'service_index': 'service_index',
        'vni': 'vni',
        'dst_component_name': 'dst_component_name',
        'nat_rule_id': 'nat_rule_id',
        'translated_src_ip': 'translated_src_ip',
        'translated_dst_ip': 'translated_dst_ip',
        'spoofguard_mac': 'spoofguard_mac',
        'dst_component_type': 'dst_component_type',
        'lport_id': 'lport_id',
        'dst_component_id': 'dst_component_id',
        'spoofguard_ip': 'spoofguard_ip',
        'service_ttl': 'service_ttl',
        'svc_nh_mac': 'svc_nh_mac'
    }
    if hasattr(TraceflowObservation, "attribute_map"):
        attribute_map.update(TraceflowObservation.attribute_map)

    def __init__(self, service_path_index=None, component_id=None, spoofguard_vlan_id=None, resend_type=None, lport_name=None, acl_rule_id=None, service_index=None, vni=None, dst_component_name=None, nat_rule_id=None, translated_src_ip=None, translated_dst_ip=None, spoofguard_mac=None, dst_component_type=None, lport_id=None, dst_component_id=None, spoofguard_ip=None, service_ttl=None, svc_nh_mac=None, *args, **kwargs):  # noqa: E501
        """TraceflowObservationForwardedLogical - a model defined in Swagger"""  # noqa: E501
        self._service_path_index = None
        self._component_id = None
        self._spoofguard_vlan_id = None
        self._resend_type = None
        self._lport_name = None
        self._acl_rule_id = None
        self._service_index = None
        self._vni = None
        self._dst_component_name = None
        self._nat_rule_id = None
        self._translated_src_ip = None
        self._translated_dst_ip = None
        self._spoofguard_mac = None
        self._dst_component_type = None
        self._lport_id = None
        self._dst_component_id = None
        self._spoofguard_ip = None
        self._service_ttl = None
        self._svc_nh_mac = None
        self.discriminator = None
        if service_path_index is not None:
            self.service_path_index = service_path_index
        if component_id is not None:
            self.component_id = component_id
        if spoofguard_vlan_id is not None:
            self.spoofguard_vlan_id = spoofguard_vlan_id
        if resend_type is not None:
            self.resend_type = resend_type
        if lport_name is not None:
            self.lport_name = lport_name
        if acl_rule_id is not None:
            self.acl_rule_id = acl_rule_id
        if service_index is not None:
            self.service_index = service_index
        if vni is not None:
            self.vni = vni
        if dst_component_name is not None:
            self.dst_component_name = dst_component_name
        if nat_rule_id is not None:
            self.nat_rule_id = nat_rule_id
        if translated_src_ip is not None:
            self.translated_src_ip = translated_src_ip
        if translated_dst_ip is not None:
            self.translated_dst_ip = translated_dst_ip
        if spoofguard_mac is not None:
            self.spoofguard_mac = spoofguard_mac
        if dst_component_type is not None:
            self.dst_component_type = dst_component_type
        if lport_id is not None:
            self.lport_id = lport_id
        if dst_component_id is not None:
            self.dst_component_id = dst_component_id
        if spoofguard_ip is not None:
            self.spoofguard_ip = spoofguard_ip
        if service_ttl is not None:
            self.service_ttl = service_ttl
        if svc_nh_mac is not None:
            self.svc_nh_mac = svc_nh_mac
        TraceflowObservation.__init__(self, *args, **kwargs)

    @property
    def service_path_index(self):
        """Gets the service_path_index of this TraceflowObservationForwardedLogical.  # noqa: E501

        The path index of the service insertion component  # noqa: E501

        :return: The service_path_index of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: int
        """
        return self._service_path_index

    @service_path_index.setter
    def service_path_index(self, service_path_index):
        """Sets the service_path_index of this TraceflowObservationForwardedLogical.

        The path index of the service insertion component  # noqa: E501

        :param service_path_index: The service_path_index of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: int
        """

        self._service_path_index = service_path_index

    @property
    def component_id(self):
        """Gets the component_id of this TraceflowObservationForwardedLogical.  # noqa: E501

        The id of the component that forwarded the traceflow packet.  # noqa: E501

        :return: The component_id of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this TraceflowObservationForwardedLogical.

        The id of the component that forwarded the traceflow packet.  # noqa: E501

        :param component_id: The component_id of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: str
        """

        self._component_id = component_id

    @property
    def spoofguard_vlan_id(self):
        """Gets the spoofguard_vlan_id of this TraceflowObservationForwardedLogical.  # noqa: E501

        This field specified the VLAN id a traceflow packet matched in the whitelist in spoofguard.  # noqa: E501

        :return: The spoofguard_vlan_id of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: int
        """
        return self._spoofguard_vlan_id

    @spoofguard_vlan_id.setter
    def spoofguard_vlan_id(self, spoofguard_vlan_id):
        """Sets the spoofguard_vlan_id of this TraceflowObservationForwardedLogical.

        This field specified the VLAN id a traceflow packet matched in the whitelist in spoofguard.  # noqa: E501

        :param spoofguard_vlan_id: The spoofguard_vlan_id of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: int
        """

        self._spoofguard_vlan_id = spoofguard_vlan_id

    @property
    def resend_type(self):
        """Gets the resend_type of this TraceflowObservationForwardedLogical.  # noqa: E501

        ARP_UNKNOWN_FROM_CP - Unknown ARP query result emitted by control plane ND_NS_UNKNOWN_FROM_CP - Unknown neighbor solicitation query result emitted by control plane UNKNOWN - Unknown resend type  # noqa: E501

        :return: The resend_type of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: str
        """
        return self._resend_type

    @resend_type.setter
    def resend_type(self, resend_type):
        """Sets the resend_type of this TraceflowObservationForwardedLogical.

        ARP_UNKNOWN_FROM_CP - Unknown ARP query result emitted by control plane ND_NS_UNKNOWN_FROM_CP - Unknown neighbor solicitation query result emitted by control plane UNKNOWN - Unknown resend type  # noqa: E501

        :param resend_type: The resend_type of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "ARP_UNKNOWN_FROM_CP", "ND_NS_UNKNWON_FROM_CP"]  # noqa: E501
        if resend_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resend_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resend_type, allowed_values)
            )

        self._resend_type = resend_type

    @property
    def lport_name(self):
        """Gets the lport_name of this TraceflowObservationForwardedLogical.  # noqa: E501

        The name of the logical port through which the traceflow packet was forwarded.  # noqa: E501

        :return: The lport_name of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: str
        """
        return self._lport_name

    @lport_name.setter
    def lport_name(self, lport_name):
        """Sets the lport_name of this TraceflowObservationForwardedLogical.

        The name of the logical port through which the traceflow packet was forwarded.  # noqa: E501

        :param lport_name: The lport_name of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: str
        """

        self._lport_name = lport_name

    @property
    def acl_rule_id(self):
        """Gets the acl_rule_id of this TraceflowObservationForwardedLogical.  # noqa: E501

        The id of the acl rule that was applied to forward the traceflow packet  # noqa: E501

        :return: The acl_rule_id of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: int
        """
        return self._acl_rule_id

    @acl_rule_id.setter
    def acl_rule_id(self, acl_rule_id):
        """Sets the acl_rule_id of this TraceflowObservationForwardedLogical.

        The id of the acl rule that was applied to forward the traceflow packet  # noqa: E501

        :param acl_rule_id: The acl_rule_id of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: int
        """

        self._acl_rule_id = acl_rule_id

    @property
    def service_index(self):
        """Gets the service_index of this TraceflowObservationForwardedLogical.  # noqa: E501

        The index of the service insertion component  # noqa: E501

        :return: The service_index of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: int
        """
        return self._service_index

    @service_index.setter
    def service_index(self, service_index):
        """Sets the service_index of this TraceflowObservationForwardedLogical.

        The index of the service insertion component  # noqa: E501

        :param service_index: The service_index of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: int
        """

        self._service_index = service_index

    @property
    def vni(self):
        """Gets the vni of this TraceflowObservationForwardedLogical.  # noqa: E501

        VNI for the logical network on which the traceflow packet was forwarded.  # noqa: E501

        :return: The vni of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: int
        """
        return self._vni

    @vni.setter
    def vni(self, vni):
        """Sets the vni of this TraceflowObservationForwardedLogical.

        VNI for the logical network on which the traceflow packet was forwarded.  # noqa: E501

        :param vni: The vni of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: int
        """

        self._vni = vni

    @property
    def dst_component_name(self):
        """Gets the dst_component_name of this TraceflowObservationForwardedLogical.  # noqa: E501

        The name of the destination component to which the traceflow packet was forwarded.  # noqa: E501

        :return: The dst_component_name of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: str
        """
        return self._dst_component_name

    @dst_component_name.setter
    def dst_component_name(self, dst_component_name):
        """Sets the dst_component_name of this TraceflowObservationForwardedLogical.

        The name of the destination component to which the traceflow packet was forwarded.  # noqa: E501

        :param dst_component_name: The dst_component_name of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: str
        """

        self._dst_component_name = dst_component_name

    @property
    def nat_rule_id(self):
        """Gets the nat_rule_id of this TraceflowObservationForwardedLogical.  # noqa: E501

        The ID of the NAT rule that was applied to forward the traceflow packet  # noqa: E501

        :return: The nat_rule_id of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: int
        """
        return self._nat_rule_id

    @nat_rule_id.setter
    def nat_rule_id(self, nat_rule_id):
        """Sets the nat_rule_id of this TraceflowObservationForwardedLogical.

        The ID of the NAT rule that was applied to forward the traceflow packet  # noqa: E501

        :param nat_rule_id: The nat_rule_id of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: int
        """

        self._nat_rule_id = nat_rule_id

    @property
    def translated_src_ip(self):
        """Gets the translated_src_ip of this TraceflowObservationForwardedLogical.  # noqa: E501

        The translated source IP address of VPN/NAT  # noqa: E501

        :return: The translated_src_ip of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: str
        """
        return self._translated_src_ip

    @translated_src_ip.setter
    def translated_src_ip(self, translated_src_ip):
        """Sets the translated_src_ip of this TraceflowObservationForwardedLogical.

        The translated source IP address of VPN/NAT  # noqa: E501

        :param translated_src_ip: The translated_src_ip of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: str
        """

        self._translated_src_ip = translated_src_ip

    @property
    def translated_dst_ip(self):
        """Gets the translated_dst_ip of this TraceflowObservationForwardedLogical.  # noqa: E501

        The translated destination IP address of VNP/NAT  # noqa: E501

        :return: The translated_dst_ip of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: str
        """
        return self._translated_dst_ip

    @translated_dst_ip.setter
    def translated_dst_ip(self, translated_dst_ip):
        """Sets the translated_dst_ip of this TraceflowObservationForwardedLogical.

        The translated destination IP address of VNP/NAT  # noqa: E501

        :param translated_dst_ip: The translated_dst_ip of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: str
        """

        self._translated_dst_ip = translated_dst_ip

    @property
    def spoofguard_mac(self):
        """Gets the spoofguard_mac of this TraceflowObservationForwardedLogical.  # noqa: E501

        The source MAC address of form: \"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$\". For example: 00:00:00:00:00:00.   # noqa: E501

        :return: The spoofguard_mac of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: str
        """
        return self._spoofguard_mac

    @spoofguard_mac.setter
    def spoofguard_mac(self, spoofguard_mac):
        """Sets the spoofguard_mac of this TraceflowObservationForwardedLogical.

        The source MAC address of form: \"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$\". For example: 00:00:00:00:00:00.   # noqa: E501

        :param spoofguard_mac: The spoofguard_mac of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: str
        """

        self._spoofguard_mac = spoofguard_mac

    @property
    def dst_component_type(self):
        """Gets the dst_component_type of this TraceflowObservationForwardedLogical.  # noqa: E501

        The type of the destination component to which the traceflow packet was forwarded.  # noqa: E501

        :return: The dst_component_type of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: str
        """
        return self._dst_component_type

    @dst_component_type.setter
    def dst_component_type(self, dst_component_type):
        """Sets the dst_component_type of this TraceflowObservationForwardedLogical.

        The type of the destination component to which the traceflow packet was forwarded.  # noqa: E501

        :param dst_component_type: The dst_component_type of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: str
        """
        allowed_values = ["PHYSICAL", "LR", "LS", "DFW", "BRIDGE", "EDGE_TUNNEL", "EDGE_HOSTSWITCH", "FW_BRIDGE", "LOAD_BALANCER", "NAT", "IPSEC", "SERVICE_INSERTION", "VMC", "SPOOFGUARD", "EDGE_FW", "DLB", "UNKNOWN"]  # noqa: E501
        if dst_component_type not in allowed_values:
            raise ValueError(
                "Invalid value for `dst_component_type` ({0}), must be one of {1}"  # noqa: E501
                .format(dst_component_type, allowed_values)
            )

        self._dst_component_type = dst_component_type

    @property
    def lport_id(self):
        """Gets the lport_id of this TraceflowObservationForwardedLogical.  # noqa: E501

        The id of the logical port through which the traceflow packet was forwarded.  # noqa: E501

        :return: The lport_id of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: str
        """
        return self._lport_id

    @lport_id.setter
    def lport_id(self, lport_id):
        """Sets the lport_id of this TraceflowObservationForwardedLogical.

        The id of the logical port through which the traceflow packet was forwarded.  # noqa: E501

        :param lport_id: The lport_id of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: str
        """

        self._lport_id = lport_id

    @property
    def dst_component_id(self):
        """Gets the dst_component_id of this TraceflowObservationForwardedLogical.  # noqa: E501

        The id of the destination component to which the traceflow packet was forwarded.  # noqa: E501

        :return: The dst_component_id of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: str
        """
        return self._dst_component_id

    @dst_component_id.setter
    def dst_component_id(self, dst_component_id):
        """Sets the dst_component_id of this TraceflowObservationForwardedLogical.

        The id of the destination component to which the traceflow packet was forwarded.  # noqa: E501

        :param dst_component_id: The dst_component_id of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: str
        """

        self._dst_component_id = dst_component_id

    @property
    def spoofguard_ip(self):
        """Gets the spoofguard_ip of this TraceflowObservationForwardedLogical.  # noqa: E501

        This field specified the prefix IP address a traceflow packet matched in the whitelist in spoofguard.  # noqa: E501

        :return: The spoofguard_ip of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: str
        """
        return self._spoofguard_ip

    @spoofguard_ip.setter
    def spoofguard_ip(self, spoofguard_ip):
        """Sets the spoofguard_ip of this TraceflowObservationForwardedLogical.

        This field specified the prefix IP address a traceflow packet matched in the whitelist in spoofguard.  # noqa: E501

        :param spoofguard_ip: The spoofguard_ip of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: str
        """

        self._spoofguard_ip = spoofguard_ip

    @property
    def service_ttl(self):
        """Gets the service_ttl of this TraceflowObservationForwardedLogical.  # noqa: E501

        The ttl of the service insertion component  # noqa: E501

        :return: The service_ttl of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: int
        """
        return self._service_ttl

    @service_ttl.setter
    def service_ttl(self, service_ttl):
        """Sets the service_ttl of this TraceflowObservationForwardedLogical.

        The ttl of the service insertion component  # noqa: E501

        :param service_ttl: The service_ttl of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: int
        """

        self._service_ttl = service_ttl

    @property
    def svc_nh_mac(self):
        """Gets the svc_nh_mac of this TraceflowObservationForwardedLogical.  # noqa: E501

        MAC address of nexthop for service insertion(SI) in service VM(SVM) where the traceflow packet was received.   # noqa: E501

        :return: The svc_nh_mac of this TraceflowObservationForwardedLogical.  # noqa: E501
        :rtype: str
        """
        return self._svc_nh_mac

    @svc_nh_mac.setter
    def svc_nh_mac(self, svc_nh_mac):
        """Sets the svc_nh_mac of this TraceflowObservationForwardedLogical.

        MAC address of nexthop for service insertion(SI) in service VM(SVM) where the traceflow packet was received.   # noqa: E501

        :param svc_nh_mac: The svc_nh_mac of this TraceflowObservationForwardedLogical.  # noqa: E501
        :type: str
        """

        self._svc_nh_mac = svc_nh_mac

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
        if issubclass(TraceflowObservationForwardedLogical, dict):
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
        if not isinstance(other, TraceflowObservationForwardedLogical):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
