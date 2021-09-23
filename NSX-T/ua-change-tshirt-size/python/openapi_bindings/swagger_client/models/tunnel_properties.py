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
from swagger_client.models.resource import Resource  # noqa: F401,E501

class TunnelProperties(Resource):
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
        'status': 'str',
        'egress_interface': 'str',
        'remote_node_id': 'str',
        'bfd': 'BFDProperties',
        'local_ip': 'str',
        'last_updated_time': 'int',
        'name': 'str',
        'remote_node_display_name': 'str',
        'encap': 'str',
        'latency_type': 'str',
        'latency_value': 'int',
        'remote_ip': 'str'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        'status': 'status',
        'egress_interface': 'egress_interface',
        'remote_node_id': 'remote_node_id',
        'bfd': 'bfd',
        'local_ip': 'local_ip',
        'last_updated_time': 'last_updated_time',
        'name': 'name',
        'remote_node_display_name': 'remote_node_display_name',
        'encap': 'encap',
        'latency_type': 'latency_type',
        'latency_value': 'latency_value',
        'remote_ip': 'remote_ip'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, status=None, egress_interface=None, remote_node_id=None, bfd=None, local_ip=None, last_updated_time=None, name=None, remote_node_display_name=None, encap=None, latency_type=None, latency_value=None, remote_ip=None, *args, **kwargs):  # noqa: E501
        """TunnelProperties - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._egress_interface = None
        self._remote_node_id = None
        self._bfd = None
        self._local_ip = None
        self._last_updated_time = None
        self._name = None
        self._remote_node_display_name = None
        self._encap = None
        self._latency_type = None
        self._latency_value = None
        self._remote_ip = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if egress_interface is not None:
            self.egress_interface = egress_interface
        if remote_node_id is not None:
            self.remote_node_id = remote_node_id
        if bfd is not None:
            self.bfd = bfd
        if local_ip is not None:
            self.local_ip = local_ip
        if last_updated_time is not None:
            self.last_updated_time = last_updated_time
        if name is not None:
            self.name = name
        if remote_node_display_name is not None:
            self.remote_node_display_name = remote_node_display_name
        if encap is not None:
            self.encap = encap
        if latency_type is not None:
            self.latency_type = latency_type
        if latency_value is not None:
            self.latency_value = latency_value
        if remote_ip is not None:
            self.remote_ip = remote_ip
        Resource.__init__(self, *args, **kwargs)

    @property
    def status(self):
        """Gets the status of this TunnelProperties.  # noqa: E501

        Status of tunnel  # noqa: E501

        :return: The status of this TunnelProperties.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TunnelProperties.

        Status of tunnel  # noqa: E501

        :param status: The status of this TunnelProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "DOWN", "UNKNOWN"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def egress_interface(self):
        """Gets the egress_interface of this TunnelProperties.  # noqa: E501

        Corresponds to the interface where local_ip_address is routed.  # noqa: E501

        :return: The egress_interface of this TunnelProperties.  # noqa: E501
        :rtype: str
        """
        return self._egress_interface

    @egress_interface.setter
    def egress_interface(self, egress_interface):
        """Sets the egress_interface of this TunnelProperties.

        Corresponds to the interface where local_ip_address is routed.  # noqa: E501

        :param egress_interface: The egress_interface of this TunnelProperties.  # noqa: E501
        :type: str
        """

        self._egress_interface = egress_interface

    @property
    def remote_node_id(self):
        """Gets the remote_node_id of this TunnelProperties.  # noqa: E501

        UUID of the remote transport node  # noqa: E501

        :return: The remote_node_id of this TunnelProperties.  # noqa: E501
        :rtype: str
        """
        return self._remote_node_id

    @remote_node_id.setter
    def remote_node_id(self, remote_node_id):
        """Sets the remote_node_id of this TunnelProperties.

        UUID of the remote transport node  # noqa: E501

        :param remote_node_id: The remote_node_id of this TunnelProperties.  # noqa: E501
        :type: str
        """

        self._remote_node_id = remote_node_id

    @property
    def bfd(self):
        """Gets the bfd of this TunnelProperties.  # noqa: E501


        :return: The bfd of this TunnelProperties.  # noqa: E501
        :rtype: BFDProperties
        """
        return self._bfd

    @bfd.setter
    def bfd(self, bfd):
        """Sets the bfd of this TunnelProperties.


        :param bfd: The bfd of this TunnelProperties.  # noqa: E501
        :type: BFDProperties
        """

        self._bfd = bfd

    @property
    def local_ip(self):
        """Gets the local_ip of this TunnelProperties.  # noqa: E501

        Local IP address of tunnel  # noqa: E501

        :return: The local_ip of this TunnelProperties.  # noqa: E501
        :rtype: str
        """
        return self._local_ip

    @local_ip.setter
    def local_ip(self, local_ip):
        """Sets the local_ip of this TunnelProperties.

        Local IP address of tunnel  # noqa: E501

        :param local_ip: The local_ip of this TunnelProperties.  # noqa: E501
        :type: str
        """

        self._local_ip = local_ip

    @property
    def last_updated_time(self):
        """Gets the last_updated_time of this TunnelProperties.  # noqa: E501

        Time at which the Tunnel status has been fetched last time.  # noqa: E501

        :return: The last_updated_time of this TunnelProperties.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, last_updated_time):
        """Sets the last_updated_time of this TunnelProperties.

        Time at which the Tunnel status has been fetched last time.  # noqa: E501

        :param last_updated_time: The last_updated_time of this TunnelProperties.  # noqa: E501
        :type: int
        """

        self._last_updated_time = last_updated_time

    @property
    def name(self):
        """Gets the name of this TunnelProperties.  # noqa: E501

        Name of tunnel  # noqa: E501

        :return: The name of this TunnelProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TunnelProperties.

        Name of tunnel  # noqa: E501

        :param name: The name of this TunnelProperties.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def remote_node_display_name(self):
        """Gets the remote_node_display_name of this TunnelProperties.  # noqa: E501

        Represents the display name of the remote transport node at the other end of the tunnel.  # noqa: E501

        :return: The remote_node_display_name of this TunnelProperties.  # noqa: E501
        :rtype: str
        """
        return self._remote_node_display_name

    @remote_node_display_name.setter
    def remote_node_display_name(self, remote_node_display_name):
        """Sets the remote_node_display_name of this TunnelProperties.

        Represents the display name of the remote transport node at the other end of the tunnel.  # noqa: E501

        :param remote_node_display_name: The remote_node_display_name of this TunnelProperties.  # noqa: E501
        :type: str
        """

        self._remote_node_display_name = remote_node_display_name

    @property
    def encap(self):
        """Gets the encap of this TunnelProperties.  # noqa: E501

        Tunnel encap  # noqa: E501

        :return: The encap of this TunnelProperties.  # noqa: E501
        :rtype: str
        """
        return self._encap

    @encap.setter
    def encap(self, encap):
        """Sets the encap of this TunnelProperties.

        Tunnel encap  # noqa: E501

        :param encap: The encap of this TunnelProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["STT", "VXLAN", "GENEVE", "UNKNOWN_ENCAP"]  # noqa: E501
        if encap not in allowed_values:
            raise ValueError(
                "Invalid value for `encap` ({0}), must be one of {1}"  # noqa: E501
                .format(encap, allowed_values)
            )

        self._encap = encap

    @property
    def latency_type(self):
        """Gets the latency_type of this TunnelProperties.  # noqa: E501

        Latency type.  # noqa: E501

        :return: The latency_type of this TunnelProperties.  # noqa: E501
        :rtype: str
        """
        return self._latency_type

    @latency_type.setter
    def latency_type(self, latency_type):
        """Sets the latency_type of this TunnelProperties.

        Latency type.  # noqa: E501

        :param latency_type: The latency_type of this TunnelProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN_LATENCY", "VALID", "NOT_READY", "TIMEOUT"]  # noqa: E501
        if latency_type not in allowed_values:
            raise ValueError(
                "Invalid value for `latency_type` ({0}), must be one of {1}"  # noqa: E501
                .format(latency_type, allowed_values)
            )

        self._latency_type = latency_type

    @property
    def latency_value(self):
        """Gets the latency_value of this TunnelProperties.  # noqa: E501

        The latency value is set only when latency_type is VALID.  # noqa: E501

        :return: The latency_value of this TunnelProperties.  # noqa: E501
        :rtype: int
        """
        return self._latency_value

    @latency_value.setter
    def latency_value(self, latency_value):
        """Sets the latency_value of this TunnelProperties.

        The latency value is set only when latency_type is VALID.  # noqa: E501

        :param latency_value: The latency_value of this TunnelProperties.  # noqa: E501
        :type: int
        """

        self._latency_value = latency_value

    @property
    def remote_ip(self):
        """Gets the remote_ip of this TunnelProperties.  # noqa: E501

        Remote IP address of tunnel  # noqa: E501

        :return: The remote_ip of this TunnelProperties.  # noqa: E501
        :rtype: str
        """
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, remote_ip):
        """Sets the remote_ip of this TunnelProperties.

        Remote IP address of tunnel  # noqa: E501

        :param remote_ip: The remote_ip of this TunnelProperties.  # noqa: E501
        :type: str
        """

        self._remote_ip = remote_ip

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
        if issubclass(TunnelProperties, dict):
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
        if not isinstance(other, TunnelProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
