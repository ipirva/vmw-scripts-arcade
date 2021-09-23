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

class NodeEntityInfo(object):
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
        'ip_address': 'str',
        'port': 'int',
        'entity_type': 'str'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'port': 'port',
        'entity_type': 'entity_type'
    }

    def __init__(self, ip_address=None, port=None, entity_type=None):  # noqa: E501
        """NodeEntityInfo - a model defined in Swagger"""  # noqa: E501
        self._ip_address = None
        self._port = None
        self._entity_type = None
        self.discriminator = None
        if ip_address is not None:
            self.ip_address = ip_address
        if port is not None:
            self.port = port
        if entity_type is not None:
            self.entity_type = entity_type

    @property
    def ip_address(self):
        """Gets the ip_address of this NodeEntityInfo.  # noqa: E501

        IP address of service provider  # noqa: E501

        :return: The ip_address of this NodeEntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this NodeEntityInfo.

        IP address of service provider  # noqa: E501

        :param ip_address: The ip_address of this NodeEntityInfo.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def port(self):
        """Gets the port of this NodeEntityInfo.  # noqa: E501

        Port number of service provider  # noqa: E501

        :return: The port of this NodeEntityInfo.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this NodeEntityInfo.

        Port number of service provider  # noqa: E501

        :param port: The port of this NodeEntityInfo.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def entity_type(self):
        """Gets the entity_type of this NodeEntityInfo.  # noqa: E501

        Entity type of this service endpoint  # noqa: E501

        :return: The entity_type of this NodeEntityInfo.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this NodeEntityInfo.

        Entity type of this service endpoint  # noqa: E501

        :param entity_type: The entity_type of this NodeEntityInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["HTTP", "DATASTORE", "MANAGER", "POLICY", "CONTROLLER"]  # noqa: E501
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

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
        if issubclass(NodeEntityInfo, dict):
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
        if not isinstance(other, NodeEntityInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
