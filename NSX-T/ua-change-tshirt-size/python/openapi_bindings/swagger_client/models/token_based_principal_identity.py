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
from swagger_client.models.managed_resource import ManagedResource  # noqa: F401,E501

class TokenBasedPrincipalIdentity(ManagedResource):
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
        'node_id': 'str',
        'name': 'str',
        'is_protected': 'bool'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'node_id': 'node_id',
        'name': 'name',
        'is_protected': 'is_protected'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, node_id=None, name=None, is_protected=None, *args, **kwargs):  # noqa: E501
        """TokenBasedPrincipalIdentity - a model defined in Swagger"""  # noqa: E501
        self._node_id = None
        self._name = None
        self._is_protected = None
        self.discriminator = None
        self.node_id = node_id
        self.name = name
        if is_protected is not None:
            self.is_protected = is_protected
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def node_id(self):
        """Gets the node_id of this TokenBasedPrincipalIdentity.  # noqa: E501

        Unique node-id of a principal. This is used primarily in the case where a cluster of nodes is used to make calls to the NSX Manager and the same 'name' is used so that the nodes can access and modify the same data while still accessing NSX through their individual secret (certificate or JWT). In all other cases this can be any string.   # noqa: E501

        :return: The node_id of this TokenBasedPrincipalIdentity.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this TokenBasedPrincipalIdentity.

        Unique node-id of a principal. This is used primarily in the case where a cluster of nodes is used to make calls to the NSX Manager and the same 'name' is used so that the nodes can access and modify the same data while still accessing NSX through their individual secret (certificate or JWT). In all other cases this can be any string.   # noqa: E501

        :param node_id: The node_id of this TokenBasedPrincipalIdentity.  # noqa: E501
        :type: str
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

    @property
    def name(self):
        """Gets the name of this TokenBasedPrincipalIdentity.  # noqa: E501

        Name of the principal. This will be matched to the name provided in the token.  # noqa: E501

        :return: The name of this TokenBasedPrincipalIdentity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TokenBasedPrincipalIdentity.

        Name of the principal. This will be matched to the name provided in the token.  # noqa: E501

        :param name: The name of this TokenBasedPrincipalIdentity.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_protected(self):
        """Gets the is_protected of this TokenBasedPrincipalIdentity.  # noqa: E501

        Indicator whether the entities created by this principal should be protected.  # noqa: E501

        :return: The is_protected of this TokenBasedPrincipalIdentity.  # noqa: E501
        :rtype: bool
        """
        return self._is_protected

    @is_protected.setter
    def is_protected(self, is_protected):
        """Sets the is_protected of this TokenBasedPrincipalIdentity.

        Indicator whether the entities created by this principal should be protected.  # noqa: E501

        :param is_protected: The is_protected of this TokenBasedPrincipalIdentity.  # noqa: E501
        :type: bool
        """

        self._is_protected = is_protected

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
        if issubclass(TokenBasedPrincipalIdentity, dict):
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
        if not isinstance(other, TokenBasedPrincipalIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
