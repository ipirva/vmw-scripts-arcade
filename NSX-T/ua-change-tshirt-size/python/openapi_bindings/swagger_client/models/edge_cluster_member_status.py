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

class EdgeClusterMemberStatus(object):
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
        'transport_node': 'ResourceReference',
        'status': 'str'
    }

    attribute_map = {
        'transport_node': 'transport_node',
        'status': 'status'
    }

    def __init__(self, transport_node=None, status=None):  # noqa: E501
        """EdgeClusterMemberStatus - a model defined in Swagger"""  # noqa: E501
        self._transport_node = None
        self._status = None
        self.discriminator = None
        self.transport_node = transport_node
        self.status = status

    @property
    def transport_node(self):
        """Gets the transport_node of this EdgeClusterMemberStatus.  # noqa: E501


        :return: The transport_node of this EdgeClusterMemberStatus.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._transport_node

    @transport_node.setter
    def transport_node(self, transport_node):
        """Sets the transport_node of this EdgeClusterMemberStatus.


        :param transport_node: The transport_node of this EdgeClusterMemberStatus.  # noqa: E501
        :type: ResourceReference
        """
        if transport_node is None:
            raise ValueError("Invalid value for `transport_node`, must not be `None`")  # noqa: E501

        self._transport_node = transport_node

    @property
    def status(self):
        """Gets the status of this EdgeClusterMemberStatus.  # noqa: E501

        Status of an edge node  # noqa: E501

        :return: The status of this EdgeClusterMemberStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EdgeClusterMemberStatus.

        Status of an edge node  # noqa: E501

        :param status: The status of this EdgeClusterMemberStatus.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["UP", "DOWN", "ADMIN_DOWN", "PARTIALLY_DISCONNECTED", "UNKNOWN"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(EdgeClusterMemberStatus, dict):
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
        if not isinstance(other, EdgeClusterMemberStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
