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

class LogicalDhcpServer(ManagedResource):
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
        'attached_logical_port_id': 'str',
        'ipv6_dhcp_server': 'IPv6DhcpServer',
        'ipv4_dhcp_server': 'IPv4DhcpServer',
        'dhcp_profile_id': 'str'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'attached_logical_port_id': 'attached_logical_port_id',
        'ipv6_dhcp_server': 'ipv6_dhcp_server',
        'ipv4_dhcp_server': 'ipv4_dhcp_server',
        'dhcp_profile_id': 'dhcp_profile_id'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, attached_logical_port_id=None, ipv6_dhcp_server=None, ipv4_dhcp_server=None, dhcp_profile_id=None, *args, **kwargs):  # noqa: E501
        """LogicalDhcpServer - a model defined in Swagger"""  # noqa: E501
        self._attached_logical_port_id = None
        self._ipv6_dhcp_server = None
        self._ipv4_dhcp_server = None
        self._dhcp_profile_id = None
        self.discriminator = None
        if attached_logical_port_id is not None:
            self.attached_logical_port_id = attached_logical_port_id
        if ipv6_dhcp_server is not None:
            self.ipv6_dhcp_server = ipv6_dhcp_server
        if ipv4_dhcp_server is not None:
            self.ipv4_dhcp_server = ipv4_dhcp_server
        self.dhcp_profile_id = dhcp_profile_id
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def attached_logical_port_id(self):
        """Gets the attached_logical_port_id of this LogicalDhcpServer.  # noqa: E501

        The uuid of the attached logical port. Read only.  # noqa: E501

        :return: The attached_logical_port_id of this LogicalDhcpServer.  # noqa: E501
        :rtype: str
        """
        return self._attached_logical_port_id

    @attached_logical_port_id.setter
    def attached_logical_port_id(self, attached_logical_port_id):
        """Sets the attached_logical_port_id of this LogicalDhcpServer.

        The uuid of the attached logical port. Read only.  # noqa: E501

        :param attached_logical_port_id: The attached_logical_port_id of this LogicalDhcpServer.  # noqa: E501
        :type: str
        """

        self._attached_logical_port_id = attached_logical_port_id

    @property
    def ipv6_dhcp_server(self):
        """Gets the ipv6_dhcp_server of this LogicalDhcpServer.  # noqa: E501


        :return: The ipv6_dhcp_server of this LogicalDhcpServer.  # noqa: E501
        :rtype: IPv6DhcpServer
        """
        return self._ipv6_dhcp_server

    @ipv6_dhcp_server.setter
    def ipv6_dhcp_server(self, ipv6_dhcp_server):
        """Sets the ipv6_dhcp_server of this LogicalDhcpServer.


        :param ipv6_dhcp_server: The ipv6_dhcp_server of this LogicalDhcpServer.  # noqa: E501
        :type: IPv6DhcpServer
        """

        self._ipv6_dhcp_server = ipv6_dhcp_server

    @property
    def ipv4_dhcp_server(self):
        """Gets the ipv4_dhcp_server of this LogicalDhcpServer.  # noqa: E501


        :return: The ipv4_dhcp_server of this LogicalDhcpServer.  # noqa: E501
        :rtype: IPv4DhcpServer
        """
        return self._ipv4_dhcp_server

    @ipv4_dhcp_server.setter
    def ipv4_dhcp_server(self, ipv4_dhcp_server):
        """Sets the ipv4_dhcp_server of this LogicalDhcpServer.


        :param ipv4_dhcp_server: The ipv4_dhcp_server of this LogicalDhcpServer.  # noqa: E501
        :type: IPv4DhcpServer
        """

        self._ipv4_dhcp_server = ipv4_dhcp_server

    @property
    def dhcp_profile_id(self):
        """Gets the dhcp_profile_id of this LogicalDhcpServer.  # noqa: E501

        The DHCP profile uuid the logical DHCP server references.  # noqa: E501

        :return: The dhcp_profile_id of this LogicalDhcpServer.  # noqa: E501
        :rtype: str
        """
        return self._dhcp_profile_id

    @dhcp_profile_id.setter
    def dhcp_profile_id(self, dhcp_profile_id):
        """Sets the dhcp_profile_id of this LogicalDhcpServer.

        The DHCP profile uuid the logical DHCP server references.  # noqa: E501

        :param dhcp_profile_id: The dhcp_profile_id of this LogicalDhcpServer.  # noqa: E501
        :type: str
        """
        if dhcp_profile_id is None:
            raise ValueError("Invalid value for `dhcp_profile_id`, must not be `None`")  # noqa: E501

        self._dhcp_profile_id = dhcp_profile_id

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
        if issubclass(LogicalDhcpServer, dict):
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
        if not isinstance(other, LogicalDhcpServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other