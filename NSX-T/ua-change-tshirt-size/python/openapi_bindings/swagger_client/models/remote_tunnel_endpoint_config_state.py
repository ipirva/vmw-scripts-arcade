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

class RemoteTunnelEndpointConfigState(object):
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
        'endpoints': 'list[RemoteTunnelEndpoint]'
    }

    attribute_map = {
        'endpoints': 'endpoints'
    }

    def __init__(self, endpoints=None):  # noqa: E501
        """RemoteTunnelEndpointConfigState - a model defined in Swagger"""  # noqa: E501
        self._endpoints = None
        self.discriminator = None
        if endpoints is not None:
            self.endpoints = endpoints

    @property
    def endpoints(self):
        """Gets the endpoints of this RemoteTunnelEndpointConfigState.  # noqa: E501

        List of remote tunnel endpoints which are configured on this node  # noqa: E501

        :return: The endpoints of this RemoteTunnelEndpointConfigState.  # noqa: E501
        :rtype: list[RemoteTunnelEndpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this RemoteTunnelEndpointConfigState.

        List of remote tunnel endpoints which are configured on this node  # noqa: E501

        :param endpoints: The endpoints of this RemoteTunnelEndpointConfigState.  # noqa: E501
        :type: list[RemoteTunnelEndpoint]
        """

        self._endpoints = endpoints

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
        if issubclass(RemoteTunnelEndpointConfigState, dict):
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
        if not isinstance(other, RemoteTunnelEndpointConfigState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
