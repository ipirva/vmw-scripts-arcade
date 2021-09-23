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

class LogicalRouterStatusPerNode(object):
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
        'high_availability_status': 'str',
        'service_router_id': 'str',
        'transport_node_id': 'str'
    }

    attribute_map = {
        'high_availability_status': 'high_availability_status',
        'service_router_id': 'service_router_id',
        'transport_node_id': 'transport_node_id'
    }

    def __init__(self, high_availability_status=None, service_router_id=None, transport_node_id=None):  # noqa: E501
        """LogicalRouterStatusPerNode - a model defined in Swagger"""  # noqa: E501
        self._high_availability_status = None
        self._service_router_id = None
        self._transport_node_id = None
        self.discriminator = None
        self.high_availability_status = high_availability_status
        if service_router_id is not None:
            self.service_router_id = service_router_id
        self.transport_node_id = transport_node_id

    @property
    def high_availability_status(self):
        """Gets the high_availability_status of this LogicalRouterStatusPerNode.  # noqa: E501

        A service router's HA status on an edge node  # noqa: E501

        :return: The high_availability_status of this LogicalRouterStatusPerNode.  # noqa: E501
        :rtype: str
        """
        return self._high_availability_status

    @high_availability_status.setter
    def high_availability_status(self, high_availability_status):
        """Sets the high_availability_status of this LogicalRouterStatusPerNode.

        A service router's HA status on an edge node  # noqa: E501

        :param high_availability_status: The high_availability_status of this LogicalRouterStatusPerNode.  # noqa: E501
        :type: str
        """
        if high_availability_status is None:
            raise ValueError("Invalid value for `high_availability_status`, must not be `None`")  # noqa: E501
        allowed_values = ["ACTIVE", "STANDBY", "DOWN", "SYNC", "UNKNOWN", "ADMIN_DOWN"]  # noqa: E501
        if high_availability_status not in allowed_values:
            raise ValueError(
                "Invalid value for `high_availability_status` ({0}), must be one of {1}"  # noqa: E501
                .format(high_availability_status, allowed_values)
            )

        self._high_availability_status = high_availability_status

    @property
    def service_router_id(self):
        """Gets the service_router_id of this LogicalRouterStatusPerNode.  # noqa: E501

        id of the service router where the router status is retrieved.  # noqa: E501

        :return: The service_router_id of this LogicalRouterStatusPerNode.  # noqa: E501
        :rtype: str
        """
        return self._service_router_id

    @service_router_id.setter
    def service_router_id(self, service_router_id):
        """Sets the service_router_id of this LogicalRouterStatusPerNode.

        id of the service router where the router status is retrieved.  # noqa: E501

        :param service_router_id: The service_router_id of this LogicalRouterStatusPerNode.  # noqa: E501
        :type: str
        """

        self._service_router_id = service_router_id

    @property
    def transport_node_id(self):
        """Gets the transport_node_id of this LogicalRouterStatusPerNode.  # noqa: E501

        id of the transport node where the router status is retrieved.  # noqa: E501

        :return: The transport_node_id of this LogicalRouterStatusPerNode.  # noqa: E501
        :rtype: str
        """
        return self._transport_node_id

    @transport_node_id.setter
    def transport_node_id(self, transport_node_id):
        """Sets the transport_node_id of this LogicalRouterStatusPerNode.

        id of the transport node where the router status is retrieved.  # noqa: E501

        :param transport_node_id: The transport_node_id of this LogicalRouterStatusPerNode.  # noqa: E501
        :type: str
        """
        if transport_node_id is None:
            raise ValueError("Invalid value for `transport_node_id`, must not be `None`")  # noqa: E501

        self._transport_node_id = transport_node_id

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
        if issubclass(LogicalRouterStatusPerNode, dict):
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
        if not isinstance(other, LogicalRouterStatusPerNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
