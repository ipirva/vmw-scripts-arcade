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
from swagger_client.models.cluster_node_vm_deployment_config import ClusterNodeVMDeploymentConfig  # noqa: F401,E501

class VsphereClusterNodeVMDeploymentConfig(ClusterNodeVMDeploymentConfig):
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
        'dns_servers': 'list[str]',
        'search_domains': 'list[str]',
        'hostname': 'str',
        'enable_ssh': 'bool',
        'allow_ssh_root_login': 'bool',
        'compute_id': 'str',
        'ntp_servers': 'list[str]',
        'disk_provisioning': 'str',
        'vc_id': 'str',
        'storage_id': 'str',
        'default_gateway_addresses': 'list[str]',
        'management_port_subnets': 'list[IPSubnet]',
        'host_id': 'str',
        'management_network_id': 'str'
    }
    if hasattr(ClusterNodeVMDeploymentConfig, "swagger_types"):
        swagger_types.update(ClusterNodeVMDeploymentConfig.swagger_types)

    attribute_map = {
        'dns_servers': 'dns_servers',
        'search_domains': 'search_domains',
        'hostname': 'hostname',
        'enable_ssh': 'enable_ssh',
        'allow_ssh_root_login': 'allow_ssh_root_login',
        'compute_id': 'compute_id',
        'ntp_servers': 'ntp_servers',
        'disk_provisioning': 'disk_provisioning',
        'vc_id': 'vc_id',
        'storage_id': 'storage_id',
        'default_gateway_addresses': 'default_gateway_addresses',
        'management_port_subnets': 'management_port_subnets',
        'host_id': 'host_id',
        'management_network_id': 'management_network_id'
    }
    if hasattr(ClusterNodeVMDeploymentConfig, "attribute_map"):
        attribute_map.update(ClusterNodeVMDeploymentConfig.attribute_map)

    def __init__(self, dns_servers=None, search_domains=None, hostname=None, enable_ssh=False, allow_ssh_root_login=False, compute_id=None, ntp_servers=None, disk_provisioning='THIN', vc_id=None, storage_id=None, default_gateway_addresses=None, management_port_subnets=None, host_id=None, management_network_id=None, *args, **kwargs):  # noqa: E501
        """VsphereClusterNodeVMDeploymentConfig - a model defined in Swagger"""  # noqa: E501
        self._dns_servers = None
        self._search_domains = None
        self._hostname = None
        self._enable_ssh = None
        self._allow_ssh_root_login = None
        self._compute_id = None
        self._ntp_servers = None
        self._disk_provisioning = None
        self._vc_id = None
        self._storage_id = None
        self._default_gateway_addresses = None
        self._management_port_subnets = None
        self._host_id = None
        self._management_network_id = None
        self.discriminator = None
        if dns_servers is not None:
            self.dns_servers = dns_servers
        if search_domains is not None:
            self.search_domains = search_domains
        self.hostname = hostname
        if enable_ssh is not None:
            self.enable_ssh = enable_ssh
        if allow_ssh_root_login is not None:
            self.allow_ssh_root_login = allow_ssh_root_login
        self.compute_id = compute_id
        if ntp_servers is not None:
            self.ntp_servers = ntp_servers
        if disk_provisioning is not None:
            self.disk_provisioning = disk_provisioning
        self.vc_id = vc_id
        self.storage_id = storage_id
        if default_gateway_addresses is not None:
            self.default_gateway_addresses = default_gateway_addresses
        if management_port_subnets is not None:
            self.management_port_subnets = management_port_subnets
        if host_id is not None:
            self.host_id = host_id
        self.management_network_id = management_network_id
        ClusterNodeVMDeploymentConfig.__init__(self, *args, **kwargs)

    @property
    def dns_servers(self):
        """Gets the dns_servers of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        List of DNS servers. If DHCP is used, the default DNS servers associated with the DHCP server will be used instead. Required if using static IP.   # noqa: E501

        :return: The dns_servers of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        """Sets the dns_servers of this VsphereClusterNodeVMDeploymentConfig.

        List of DNS servers. If DHCP is used, the default DNS servers associated with the DHCP server will be used instead. Required if using static IP.   # noqa: E501

        :param dns_servers: The dns_servers of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: list[str]
        """

        self._dns_servers = dns_servers

    @property
    def search_domains(self):
        """Gets the search_domains of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        List of domain names that are used to complete unqualified host names.   # noqa: E501

        :return: The search_domains of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._search_domains

    @search_domains.setter
    def search_domains(self, search_domains):
        """Sets the search_domains of this VsphereClusterNodeVMDeploymentConfig.

        List of domain names that are used to complete unqualified host names.   # noqa: E501

        :param search_domains: The search_domains of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: list[str]
        """

        self._search_domains = search_domains

    @property
    def hostname(self):
        """Gets the hostname of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        Desired host name/FQDN for the VM to be deployed  # noqa: E501

        :return: The hostname of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this VsphereClusterNodeVMDeploymentConfig.

        Desired host name/FQDN for the VM to be deployed  # noqa: E501

        :param hostname: The hostname of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: str
        """
        if hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def enable_ssh(self):
        """Gets the enable_ssh of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        If true, the SSH service will automatically be started on the VM. Enabling SSH service is not recommended for security reasons.   # noqa: E501

        :return: The enable_ssh of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ssh

    @enable_ssh.setter
    def enable_ssh(self, enable_ssh):
        """Sets the enable_ssh of this VsphereClusterNodeVMDeploymentConfig.

        If true, the SSH service will automatically be started on the VM. Enabling SSH service is not recommended for security reasons.   # noqa: E501

        :param enable_ssh: The enable_ssh of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: bool
        """

        self._enable_ssh = enable_ssh

    @property
    def allow_ssh_root_login(self):
        """Gets the allow_ssh_root_login of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        If true, the root user will be allowed to log into the VM. Allowing root SSH logins is not recommended for security reasons.   # noqa: E501

        :return: The allow_ssh_root_login of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: bool
        """
        return self._allow_ssh_root_login

    @allow_ssh_root_login.setter
    def allow_ssh_root_login(self, allow_ssh_root_login):
        """Sets the allow_ssh_root_login of this VsphereClusterNodeVMDeploymentConfig.

        If true, the root user will be allowed to log into the VM. Allowing root SSH logins is not recommended for security reasons.   # noqa: E501

        :param allow_ssh_root_login: The allow_ssh_root_login of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: bool
        """

        self._allow_ssh_root_login = allow_ssh_root_login

    @property
    def compute_id(self):
        """Gets the compute_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        The cluster node VM will be deployed on the specified cluster or resourcepool for specified VC server.   # noqa: E501

        :return: The compute_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        """Sets the compute_id of this VsphereClusterNodeVMDeploymentConfig.

        The cluster node VM will be deployed on the specified cluster or resourcepool for specified VC server.   # noqa: E501

        :param compute_id: The compute_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: str
        """
        if compute_id is None:
            raise ValueError("Invalid value for `compute_id`, must not be `None`")  # noqa: E501

        self._compute_id = compute_id

    @property
    def ntp_servers(self):
        """Gets the ntp_servers of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        List of NTP servers. To use hostnames, a DNS server must be defined. If not using DHCP, a DNS server should be specified under dns_servers.   # noqa: E501

        :return: The ntp_servers of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._ntp_servers

    @ntp_servers.setter
    def ntp_servers(self, ntp_servers):
        """Sets the ntp_servers of this VsphereClusterNodeVMDeploymentConfig.

        List of NTP servers. To use hostnames, a DNS server must be defined. If not using DHCP, a DNS server should be specified under dns_servers.   # noqa: E501

        :param ntp_servers: The ntp_servers of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: list[str]
        """

        self._ntp_servers = ntp_servers

    @property
    def disk_provisioning(self):
        """Gets the disk_provisioning of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        Specifies the disk provisioning type of the VM.   # noqa: E501

        :return: The disk_provisioning of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: str
        """
        return self._disk_provisioning

    @disk_provisioning.setter
    def disk_provisioning(self, disk_provisioning):
        """Sets the disk_provisioning of this VsphereClusterNodeVMDeploymentConfig.

        Specifies the disk provisioning type of the VM.   # noqa: E501

        :param disk_provisioning: The disk_provisioning of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["THIN", "LAZY_ZEROED_THICK", "EAGER_ZEROED_THICK"]  # noqa: E501
        if disk_provisioning not in allowed_values:
            raise ValueError(
                "Invalid value for `disk_provisioning` ({0}), must be one of {1}"  # noqa: E501
                .format(disk_provisioning, allowed_values)
            )

        self._disk_provisioning = disk_provisioning

    @property
    def vc_id(self):
        """Gets the vc_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        The VC-specific identifiers will be resolved on this VC, so all other identifiers specified in the config must belong to this vCenter server.   # noqa: E501

        :return: The vc_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: str
        """
        return self._vc_id

    @vc_id.setter
    def vc_id(self, vc_id):
        """Sets the vc_id of this VsphereClusterNodeVMDeploymentConfig.

        The VC-specific identifiers will be resolved on this VC, so all other identifiers specified in the config must belong to this vCenter server.   # noqa: E501

        :param vc_id: The vc_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: str
        """
        if vc_id is None:
            raise ValueError("Invalid value for `vc_id`, must not be `None`")  # noqa: E501

        self._vc_id = vc_id

    @property
    def storage_id(self):
        """Gets the storage_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        The cluster node VM will be deployed on the specified datastore in the specified VC server. User must ensure that storage is accessible by the specified cluster/host.   # noqa: E501

        :return: The storage_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this VsphereClusterNodeVMDeploymentConfig.

        The cluster node VM will be deployed on the specified datastore in the specified VC server. User must ensure that storage is accessible by the specified cluster/host.   # noqa: E501

        :param storage_id: The storage_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: str
        """
        if storage_id is None:
            raise ValueError("Invalid value for `storage_id`, must not be `None`")  # noqa: E501

        self._storage_id = storage_id

    @property
    def default_gateway_addresses(self):
        """Gets the default_gateway_addresses of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        The default gateway for the VM to be deployed must be specified if all the other VMs it communicates with are not in the same subnet. Do not specify this field and management_port_subnets to use DHCP. Note: only single IPv4 default gateway address is supported and it must belong to management network. IMPORTANT: VMs deployed using DHCP are currently not supported, so this parameter should be specified.   # noqa: E501

        :return: The default_gateway_addresses of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._default_gateway_addresses

    @default_gateway_addresses.setter
    def default_gateway_addresses(self, default_gateway_addresses):
        """Sets the default_gateway_addresses of this VsphereClusterNodeVMDeploymentConfig.

        The default gateway for the VM to be deployed must be specified if all the other VMs it communicates with are not in the same subnet. Do not specify this field and management_port_subnets to use DHCP. Note: only single IPv4 default gateway address is supported and it must belong to management network. IMPORTANT: VMs deployed using DHCP are currently not supported, so this parameter should be specified.   # noqa: E501

        :param default_gateway_addresses: The default_gateway_addresses of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: list[str]
        """

        self._default_gateway_addresses = default_gateway_addresses

    @property
    def management_port_subnets(self):
        """Gets the management_port_subnets of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        IP Address and subnet configuration for the management port. Do not specify this field and default_gateway_addresses to use DHCP. Note: only one IPv4 address is supported for the management port. IMPORTANT: VMs deployed using DHCP are currently not supported, so this parameter should be specified.   # noqa: E501

        :return: The management_port_subnets of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: list[IPSubnet]
        """
        return self._management_port_subnets

    @management_port_subnets.setter
    def management_port_subnets(self, management_port_subnets):
        """Sets the management_port_subnets of this VsphereClusterNodeVMDeploymentConfig.

        IP Address and subnet configuration for the management port. Do not specify this field and default_gateway_addresses to use DHCP. Note: only one IPv4 address is supported for the management port. IMPORTANT: VMs deployed using DHCP are currently not supported, so this parameter should be specified.   # noqa: E501

        :param management_port_subnets: The management_port_subnets of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: list[IPSubnet]
        """

        self._management_port_subnets = management_port_subnets

    @property
    def host_id(self):
        """Gets the host_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        The cluster node VM will be deployed on the specified host in the specified VC server within the cluster if host_id is specified. Note: User must ensure that storage and specified networks are accessible by this host.   # noqa: E501

        :return: The host_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this VsphereClusterNodeVMDeploymentConfig.

        The cluster node VM will be deployed on the specified host in the specified VC server within the cluster if host_id is specified. Note: User must ensure that storage and specified networks are accessible by this host.   # noqa: E501

        :param host_id: The host_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: str
        """

        self._host_id = host_id

    @property
    def management_network_id(self):
        """Gets the management_network_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501

        Distributed portgroup identifier to which the management vnic of cluster node VM will be connected.   # noqa: E501

        :return: The management_network_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :rtype: str
        """
        return self._management_network_id

    @management_network_id.setter
    def management_network_id(self, management_network_id):
        """Sets the management_network_id of this VsphereClusterNodeVMDeploymentConfig.

        Distributed portgroup identifier to which the management vnic of cluster node VM will be connected.   # noqa: E501

        :param management_network_id: The management_network_id of this VsphereClusterNodeVMDeploymentConfig.  # noqa: E501
        :type: str
        """
        if management_network_id is None:
            raise ValueError("Invalid value for `management_network_id`, must not be `None`")  # noqa: E501

        self._management_network_id = management_network_id

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
        if issubclass(VsphereClusterNodeVMDeploymentConfig, dict):
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
        if not isinstance(other, VsphereClusterNodeVMDeploymentConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other