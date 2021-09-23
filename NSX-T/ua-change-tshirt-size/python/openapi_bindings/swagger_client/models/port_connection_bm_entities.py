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

class PortConnectionBMEntities(object):
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
        'src_port': 'LogicalPort',
        'dst_port': 'LogicalPort'
    }

    attribute_map = {
        'src_port': 'src_port',
        'dst_port': 'dst_port'
    }

    def __init__(self, src_port=None, dst_port=None):  # noqa: E501
        """PortConnectionBMEntities - a model defined in Swagger"""  # noqa: E501
        self._src_port = None
        self._dst_port = None
        self.discriminator = None
        if src_port is not None:
            self.src_port = src_port
        if dst_port is not None:
            self.dst_port = dst_port

    @property
    def src_port(self):
        """Gets the src_port of this PortConnectionBMEntities.  # noqa: E501


        :return: The src_port of this PortConnectionBMEntities.  # noqa: E501
        :rtype: LogicalPort
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        """Sets the src_port of this PortConnectionBMEntities.


        :param src_port: The src_port of this PortConnectionBMEntities.  # noqa: E501
        :type: LogicalPort
        """

        self._src_port = src_port

    @property
    def dst_port(self):
        """Gets the dst_port of this PortConnectionBMEntities.  # noqa: E501


        :return: The dst_port of this PortConnectionBMEntities.  # noqa: E501
        :rtype: LogicalPort
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        """Sets the dst_port of this PortConnectionBMEntities.


        :param dst_port: The dst_port of this PortConnectionBMEntities.  # noqa: E501
        :type: LogicalPort
        """

        self._dst_port = dst_port

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
        if issubclass(PortConnectionBMEntities, dict):
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
        if not isinstance(other, PortConnectionBMEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
