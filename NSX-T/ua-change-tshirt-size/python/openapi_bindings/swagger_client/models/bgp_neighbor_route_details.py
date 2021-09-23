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

class BgpNeighborRouteDetails(object):
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
        'logical_router_id': 'str',
        'neighbor_id': 'str',
        'per_transport_node_routes': 'list[RoutesPerTransportNode]',
        'neighbor_address': 'str'
    }

    attribute_map = {
        'logical_router_id': 'logical_router_id',
        'neighbor_id': 'neighbor_id',
        'per_transport_node_routes': 'per_transport_node_routes',
        'neighbor_address': 'neighbor_address'
    }

    def __init__(self, logical_router_id=None, neighbor_id=None, per_transport_node_routes=None, neighbor_address=None):  # noqa: E501
        """BgpNeighborRouteDetails - a model defined in Swagger"""  # noqa: E501
        self._logical_router_id = None
        self._neighbor_id = None
        self._per_transport_node_routes = None
        self._neighbor_address = None
        self.discriminator = None
        if logical_router_id is not None:
            self.logical_router_id = logical_router_id
        if neighbor_id is not None:
            self.neighbor_id = neighbor_id
        if per_transport_node_routes is not None:
            self.per_transport_node_routes = per_transport_node_routes
        if neighbor_address is not None:
            self.neighbor_address = neighbor_address

    @property
    def logical_router_id(self):
        """Gets the logical_router_id of this BgpNeighborRouteDetails.  # noqa: E501

        Logical router id  # noqa: E501

        :return: The logical_router_id of this BgpNeighborRouteDetails.  # noqa: E501
        :rtype: str
        """
        return self._logical_router_id

    @logical_router_id.setter
    def logical_router_id(self, logical_router_id):
        """Sets the logical_router_id of this BgpNeighborRouteDetails.

        Logical router id  # noqa: E501

        :param logical_router_id: The logical_router_id of this BgpNeighborRouteDetails.  # noqa: E501
        :type: str
        """

        self._logical_router_id = logical_router_id

    @property
    def neighbor_id(self):
        """Gets the neighbor_id of this BgpNeighborRouteDetails.  # noqa: E501

        BGP neighbor id  # noqa: E501

        :return: The neighbor_id of this BgpNeighborRouteDetails.  # noqa: E501
        :rtype: str
        """
        return self._neighbor_id

    @neighbor_id.setter
    def neighbor_id(self, neighbor_id):
        """Sets the neighbor_id of this BgpNeighborRouteDetails.

        BGP neighbor id  # noqa: E501

        :param neighbor_id: The neighbor_id of this BgpNeighborRouteDetails.  # noqa: E501
        :type: str
        """

        self._neighbor_id = neighbor_id

    @property
    def per_transport_node_routes(self):
        """Gets the per_transport_node_routes of this BgpNeighborRouteDetails.  # noqa: E501

        Array of BGP neighbor route details per transport node.   # noqa: E501

        :return: The per_transport_node_routes of this BgpNeighborRouteDetails.  # noqa: E501
        :rtype: list[RoutesPerTransportNode]
        """
        return self._per_transport_node_routes

    @per_transport_node_routes.setter
    def per_transport_node_routes(self, per_transport_node_routes):
        """Sets the per_transport_node_routes of this BgpNeighborRouteDetails.

        Array of BGP neighbor route details per transport node.   # noqa: E501

        :param per_transport_node_routes: The per_transport_node_routes of this BgpNeighborRouteDetails.  # noqa: E501
        :type: list[RoutesPerTransportNode]
        """

        self._per_transport_node_routes = per_transport_node_routes

    @property
    def neighbor_address(self):
        """Gets the neighbor_address of this BgpNeighborRouteDetails.  # noqa: E501

        BGP neighbor peer IP address.  # noqa: E501

        :return: The neighbor_address of this BgpNeighborRouteDetails.  # noqa: E501
        :rtype: str
        """
        return self._neighbor_address

    @neighbor_address.setter
    def neighbor_address(self, neighbor_address):
        """Sets the neighbor_address of this BgpNeighborRouteDetails.

        BGP neighbor peer IP address.  # noqa: E501

        :param neighbor_address: The neighbor_address of this BgpNeighborRouteDetails.  # noqa: E501
        :type: str
        """

        self._neighbor_address = neighbor_address

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
        if issubclass(BgpNeighborRouteDetails, dict):
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
        if not isinstance(other, BgpNeighborRouteDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other