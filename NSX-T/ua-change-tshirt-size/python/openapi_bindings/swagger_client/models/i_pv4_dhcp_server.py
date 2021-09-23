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

class IPv4DhcpServer(object):
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
        'options': 'DhcpOptions',
        'monitor_ippool_usage': 'bool',
        'dhcp_server_ip': 'str',
        'dns_nameservers': 'list[str]',
        'domain_name': 'str',
        'gateway_ip': 'str'
    }

    attribute_map = {
        'options': 'options',
        'monitor_ippool_usage': 'monitor_ippool_usage',
        'dhcp_server_ip': 'dhcp_server_ip',
        'dns_nameservers': 'dns_nameservers',
        'domain_name': 'domain_name',
        'gateway_ip': 'gateway_ip'
    }

    def __init__(self, options=None, monitor_ippool_usage=False, dhcp_server_ip=None, dns_nameservers=None, domain_name=None, gateway_ip=None):  # noqa: E501
        """IPv4DhcpServer - a model defined in Swagger"""  # noqa: E501
        self._options = None
        self._monitor_ippool_usage = None
        self._dhcp_server_ip = None
        self._dns_nameservers = None
        self._domain_name = None
        self._gateway_ip = None
        self.discriminator = None
        if options is not None:
            self.options = options
        if monitor_ippool_usage is not None:
            self.monitor_ippool_usage = monitor_ippool_usage
        self.dhcp_server_ip = dhcp_server_ip
        if dns_nameservers is not None:
            self.dns_nameservers = dns_nameservers
        if domain_name is not None:
            self.domain_name = domain_name
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip

    @property
    def options(self):
        """Gets the options of this IPv4DhcpServer.  # noqa: E501


        :return: The options of this IPv4DhcpServer.  # noqa: E501
        :rtype: DhcpOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this IPv4DhcpServer.


        :param options: The options of this IPv4DhcpServer.  # noqa: E501
        :type: DhcpOptions
        """

        self._options = options

    @property
    def monitor_ippool_usage(self):
        """Gets the monitor_ippool_usage of this IPv4DhcpServer.  # noqa: E501

        Enable or disable monitoring of DHCP ip-pools usage. When enabled, system events are generated when pool usage exceeds the configured thresholds. System events can be viewed in REST API /api/v2/hpm/alarms   # noqa: E501

        :return: The monitor_ippool_usage of this IPv4DhcpServer.  # noqa: E501
        :rtype: bool
        """
        return self._monitor_ippool_usage

    @monitor_ippool_usage.setter
    def monitor_ippool_usage(self, monitor_ippool_usage):
        """Sets the monitor_ippool_usage of this IPv4DhcpServer.

        Enable or disable monitoring of DHCP ip-pools usage. When enabled, system events are generated when pool usage exceeds the configured thresholds. System events can be viewed in REST API /api/v2/hpm/alarms   # noqa: E501

        :param monitor_ippool_usage: The monitor_ippool_usage of this IPv4DhcpServer.  # noqa: E501
        :type: bool
        """

        self._monitor_ippool_usage = monitor_ippool_usage

    @property
    def dhcp_server_ip(self):
        """Gets the dhcp_server_ip of this IPv4DhcpServer.  # noqa: E501

        DHCP server ip in CIDR format.  # noqa: E501

        :return: The dhcp_server_ip of this IPv4DhcpServer.  # noqa: E501
        :rtype: str
        """
        return self._dhcp_server_ip

    @dhcp_server_ip.setter
    def dhcp_server_ip(self, dhcp_server_ip):
        """Sets the dhcp_server_ip of this IPv4DhcpServer.

        DHCP server ip in CIDR format.  # noqa: E501

        :param dhcp_server_ip: The dhcp_server_ip of this IPv4DhcpServer.  # noqa: E501
        :type: str
        """
        if dhcp_server_ip is None:
            raise ValueError("Invalid value for `dhcp_server_ip`, must not be `None`")  # noqa: E501

        self._dhcp_server_ip = dhcp_server_ip

    @property
    def dns_nameservers(self):
        """Gets the dns_nameservers of this IPv4DhcpServer.  # noqa: E501

        Primary and secondary DNS server address to assign host. They can be overridden by ip-pool or static-binding level property.   # noqa: E501

        :return: The dns_nameservers of this IPv4DhcpServer.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_nameservers

    @dns_nameservers.setter
    def dns_nameservers(self, dns_nameservers):
        """Sets the dns_nameservers of this IPv4DhcpServer.

        Primary and secondary DNS server address to assign host. They can be overridden by ip-pool or static-binding level property.   # noqa: E501

        :param dns_nameservers: The dns_nameservers of this IPv4DhcpServer.  # noqa: E501
        :type: list[str]
        """

        self._dns_nameservers = dns_nameservers

    @property
    def domain_name(self):
        """Gets the domain_name of this IPv4DhcpServer.  # noqa: E501

        Host name or prefix to be assigned to host. It can be overridden by ip-pool or static-binding level property.   # noqa: E501

        :return: The domain_name of this IPv4DhcpServer.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this IPv4DhcpServer.

        Host name or prefix to be assigned to host. It can be overridden by ip-pool or static-binding level property.   # noqa: E501

        :param domain_name: The domain_name of this IPv4DhcpServer.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this IPv4DhcpServer.  # noqa: E501

        Gateway ip to be assigned to host. It can be overridden by ip-pool or static-binding level property.   # noqa: E501

        :return: The gateway_ip of this IPv4DhcpServer.  # noqa: E501
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this IPv4DhcpServer.

        Gateway ip to be assigned to host. It can be overridden by ip-pool or static-binding level property.   # noqa: E501

        :param gateway_ip: The gateway_ip of this IPv4DhcpServer.  # noqa: E501
        :type: str
        """

        self._gateway_ip = gateway_ip

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
        if issubclass(IPv4DhcpServer, dict):
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
        if not isinstance(other, IPv4DhcpServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
