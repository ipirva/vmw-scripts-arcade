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
from swagger_client.models.discovered_resource import DiscoveredResource  # noqa: F401,E501

class ContainerClusterNode(DiscoveredResource):
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
        'network_status': 'str',
        'container_cluster_id': 'str',
        'ip_addresses': 'list[str]',
        'origin_properties': 'list[KeyValuePair]',
        'external_id': 'str',
        'network_errors': 'list[NetworkError]'
    }
    if hasattr(DiscoveredResource, "swagger_types"):
        swagger_types.update(DiscoveredResource.swagger_types)

    attribute_map = {
        'network_status': 'network_status',
        'container_cluster_id': 'container_cluster_id',
        'ip_addresses': 'ip_addresses',
        'origin_properties': 'origin_properties',
        'external_id': 'external_id',
        'network_errors': 'network_errors'
    }
    if hasattr(DiscoveredResource, "attribute_map"):
        attribute_map.update(DiscoveredResource.attribute_map)

    def __init__(self, network_status=None, container_cluster_id=None, ip_addresses=None, origin_properties=None, external_id=None, network_errors=None, *args, **kwargs):  # noqa: E501
        """ContainerClusterNode - a model defined in Swagger"""  # noqa: E501
        self._network_status = None
        self._container_cluster_id = None
        self._ip_addresses = None
        self._origin_properties = None
        self._external_id = None
        self._network_errors = None
        self.discriminator = None
        if network_status is not None:
            self.network_status = network_status
        if container_cluster_id is not None:
            self.container_cluster_id = container_cluster_id
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if origin_properties is not None:
            self.origin_properties = origin_properties
        self.external_id = external_id
        if network_errors is not None:
            self.network_errors = network_errors
        DiscoveredResource.__init__(self, *args, **kwargs)

    @property
    def network_status(self):
        """Gets the network_status of this ContainerClusterNode.  # noqa: E501

        Network status of container cluster node.  # noqa: E501

        :return: The network_status of this ContainerClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._network_status

    @network_status.setter
    def network_status(self, network_status):
        """Sets the network_status of this ContainerClusterNode.

        Network status of container cluster node.  # noqa: E501

        :param network_status: The network_status of this ContainerClusterNode.  # noqa: E501
        :type: str
        """
        allowed_values = ["HEALTHY", "UNHEALTHY"]  # noqa: E501
        if network_status not in allowed_values:
            raise ValueError(
                "Invalid value for `network_status` ({0}), must be one of {1}"  # noqa: E501
                .format(network_status, allowed_values)
            )

        self._network_status = network_status

    @property
    def container_cluster_id(self):
        """Gets the container_cluster_id of this ContainerClusterNode.  # noqa: E501

        External identifier of the container cluster.  # noqa: E501

        :return: The container_cluster_id of this ContainerClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._container_cluster_id

    @container_cluster_id.setter
    def container_cluster_id(self, container_cluster_id):
        """Sets the container_cluster_id of this ContainerClusterNode.

        External identifier of the container cluster.  # noqa: E501

        :param container_cluster_id: The container_cluster_id of this ContainerClusterNode.  # noqa: E501
        :type: str
        """

        self._container_cluster_id = container_cluster_id

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this ContainerClusterNode.  # noqa: E501

        List of IP addresses of container cluster node.  # noqa: E501

        :return: The ip_addresses of this ContainerClusterNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this ContainerClusterNode.

        List of IP addresses of container cluster node.  # noqa: E501

        :param ip_addresses: The ip_addresses of this ContainerClusterNode.  # noqa: E501
        :type: list[str]
        """

        self._ip_addresses = ip_addresses

    @property
    def origin_properties(self):
        """Gets the origin_properties of this ContainerClusterNode.  # noqa: E501

        Array of additional specific properties of container cluster node in key-value format.   # noqa: E501

        :return: The origin_properties of this ContainerClusterNode.  # noqa: E501
        :rtype: list[KeyValuePair]
        """
        return self._origin_properties

    @origin_properties.setter
    def origin_properties(self, origin_properties):
        """Sets the origin_properties of this ContainerClusterNode.

        Array of additional specific properties of container cluster node in key-value format.   # noqa: E501

        :param origin_properties: The origin_properties of this ContainerClusterNode.  # noqa: E501
        :type: list[KeyValuePair]
        """

        self._origin_properties = origin_properties

    @property
    def external_id(self):
        """Gets the external_id of this ContainerClusterNode.  # noqa: E501

        External identifier of the container cluster node in K8S/PAS.   # noqa: E501

        :return: The external_id of this ContainerClusterNode.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this ContainerClusterNode.

        External identifier of the container cluster node in K8S/PAS.   # noqa: E501

        :param external_id: The external_id of this ContainerClusterNode.  # noqa: E501
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")  # noqa: E501

        self._external_id = external_id

    @property
    def network_errors(self):
        """Gets the network_errors of this ContainerClusterNode.  # noqa: E501

        List of network errors related to container cluster node.  # noqa: E501

        :return: The network_errors of this ContainerClusterNode.  # noqa: E501
        :rtype: list[NetworkError]
        """
        return self._network_errors

    @network_errors.setter
    def network_errors(self, network_errors):
        """Sets the network_errors of this ContainerClusterNode.

        List of network errors related to container cluster node.  # noqa: E501

        :param network_errors: The network_errors of this ContainerClusterNode.  # noqa: E501
        :type: list[NetworkError]
        """

        self._network_errors = network_errors

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
        if issubclass(ContainerClusterNode, dict):
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
        if not isinstance(other, ContainerClusterNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
