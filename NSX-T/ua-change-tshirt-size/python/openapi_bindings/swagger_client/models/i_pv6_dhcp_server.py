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

class IPv6DhcpServer(object):
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
        'dhcp_server_ip': 'str',
        'server_id': 'str',
        'dns_nameservers': 'list[str]',
        'sntp_servers': 'list[str]',
        'domain_names': 'list[str]'
    }

    attribute_map = {
        'dhcp_server_ip': 'dhcp_server_ip',
        'server_id': 'server_id',
        'dns_nameservers': 'dns_nameservers',
        'sntp_servers': 'sntp_servers',
        'domain_names': 'domain_names'
    }

    def __init__(self, dhcp_server_ip=None, server_id=None, dns_nameservers=None, sntp_servers=None, domain_names=None):  # noqa: E501
        """IPv6DhcpServer - a model defined in Swagger"""  # noqa: E501
        self._dhcp_server_ip = None
        self._server_id = None
        self._dns_nameservers = None
        self._sntp_servers = None
        self._domain_names = None
        self.discriminator = None
        if dhcp_server_ip is not None:
            self.dhcp_server_ip = dhcp_server_ip
        if server_id is not None:
            self.server_id = server_id
        if dns_nameservers is not None:
            self.dns_nameservers = dns_nameservers
        if sntp_servers is not None:
            self.sntp_servers = sntp_servers
        if domain_names is not None:
            self.domain_names = domain_names

    @property
    def dhcp_server_ip(self):
        """Gets the dhcp_server_ip of this IPv6DhcpServer.  # noqa: E501

        DHCP server ip in CIDR format.  # noqa: E501

        :return: The dhcp_server_ip of this IPv6DhcpServer.  # noqa: E501
        :rtype: str
        """
        return self._dhcp_server_ip

    @dhcp_server_ip.setter
    def dhcp_server_ip(self, dhcp_server_ip):
        """Sets the dhcp_server_ip of this IPv6DhcpServer.

        DHCP server ip in CIDR format.  # noqa: E501

        :param dhcp_server_ip: The dhcp_server_ip of this IPv6DhcpServer.  # noqa: E501
        :type: str
        """

        self._dhcp_server_ip = dhcp_server_ip

    @property
    def server_id(self):
        """Gets the server_id of this IPv6DhcpServer.  # noqa: E501

        DHCP server id.  # noqa: E501

        :return: The server_id of this IPv6DhcpServer.  # noqa: E501
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this IPv6DhcpServer.

        DHCP server id.  # noqa: E501

        :param server_id: The server_id of this IPv6DhcpServer.  # noqa: E501
        :type: str
        """

        self._server_id = server_id

    @property
    def dns_nameservers(self):
        """Gets the dns_nameservers of this IPv6DhcpServer.  # noqa: E501

        Primary and secondary DNS server address to assign host. They can be overridden by ip-pool or static-binding level property.   # noqa: E501

        :return: The dns_nameservers of this IPv6DhcpServer.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_nameservers

    @dns_nameservers.setter
    def dns_nameservers(self, dns_nameservers):
        """Sets the dns_nameservers of this IPv6DhcpServer.

        Primary and secondary DNS server address to assign host. They can be overridden by ip-pool or static-binding level property.   # noqa: E501

        :param dns_nameservers: The dns_nameservers of this IPv6DhcpServer.  # noqa: E501
        :type: list[str]
        """

        self._dns_nameservers = dns_nameservers

    @property
    def sntp_servers(self):
        """Gets the sntp_servers of this IPv6DhcpServer.  # noqa: E501

        SNTP server ips.  # noqa: E501

        :return: The sntp_servers of this IPv6DhcpServer.  # noqa: E501
        :rtype: list[str]
        """
        return self._sntp_servers

    @sntp_servers.setter
    def sntp_servers(self, sntp_servers):
        """Sets the sntp_servers of this IPv6DhcpServer.

        SNTP server ips.  # noqa: E501

        :param sntp_servers: The sntp_servers of this IPv6DhcpServer.  # noqa: E501
        :type: list[str]
        """

        self._sntp_servers = sntp_servers

    @property
    def domain_names(self):
        """Gets the domain_names of this IPv6DhcpServer.  # noqa: E501

        Host name or prefix to be assigned to host. It can be overridden by ip-pool or static-binding level property.   # noqa: E501

        :return: The domain_names of this IPv6DhcpServer.  # noqa: E501
        :rtype: list[str]
        """
        return self._domain_names

    @domain_names.setter
    def domain_names(self, domain_names):
        """Sets the domain_names of this IPv6DhcpServer.

        Host name or prefix to be assigned to host. It can be overridden by ip-pool or static-binding level property.   # noqa: E501

        :param domain_names: The domain_names of this IPv6DhcpServer.  # noqa: E501
        :type: list[str]
        """

        self._domain_names = domain_names

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
        if issubclass(IPv6DhcpServer, dict):
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
        if not isinstance(other, IPv6DhcpServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
