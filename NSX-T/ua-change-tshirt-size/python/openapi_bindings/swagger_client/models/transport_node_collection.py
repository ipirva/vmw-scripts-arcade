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

class TransportNodeCollection(ManagedResource):
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
        'has_nvds': 'bool',
        'transport_node_profile_id': 'str',
        'compute_collection_id': 'str'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'has_nvds': 'has_nvds',
        'transport_node_profile_id': 'transport_node_profile_id',
        'compute_collection_id': 'compute_collection_id'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, has_nvds=None, transport_node_profile_id=None, compute_collection_id=None, *args, **kwargs):  # noqa: E501
        """TransportNodeCollection - a model defined in Swagger"""  # noqa: E501
        self._has_nvds = None
        self._transport_node_profile_id = None
        self._compute_collection_id = None
        self.discriminator = None
        if has_nvds is not None:
            self.has_nvds = has_nvds
        self.transport_node_profile_id = transport_node_profile_id
        self.compute_collection_id = compute_collection_id
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def has_nvds(self):
        """Gets the has_nvds of this TransportNodeCollection.  # noqa: E501

        Flag indicating if applied profile has NVDS  # noqa: E501

        :return: The has_nvds of this TransportNodeCollection.  # noqa: E501
        :rtype: bool
        """
        return self._has_nvds

    @has_nvds.setter
    def has_nvds(self, has_nvds):
        """Sets the has_nvds of this TransportNodeCollection.

        Flag indicating if applied profile has NVDS  # noqa: E501

        :param has_nvds: The has_nvds of this TransportNodeCollection.  # noqa: E501
        :type: bool
        """

        self._has_nvds = has_nvds

    @property
    def transport_node_profile_id(self):
        """Gets the transport_node_profile_id of this TransportNodeCollection.  # noqa: E501

        Transport Node Profile ID  # noqa: E501

        :return: The transport_node_profile_id of this TransportNodeCollection.  # noqa: E501
        :rtype: str
        """
        return self._transport_node_profile_id

    @transport_node_profile_id.setter
    def transport_node_profile_id(self, transport_node_profile_id):
        """Sets the transport_node_profile_id of this TransportNodeCollection.

        Transport Node Profile ID  # noqa: E501

        :param transport_node_profile_id: The transport_node_profile_id of this TransportNodeCollection.  # noqa: E501
        :type: str
        """
        if transport_node_profile_id is None:
            raise ValueError("Invalid value for `transport_node_profile_id`, must not be `None`")  # noqa: E501

        self._transport_node_profile_id = transport_node_profile_id

    @property
    def compute_collection_id(self):
        """Gets the compute_collection_id of this TransportNodeCollection.  # noqa: E501

        Compute collection id  # noqa: E501

        :return: The compute_collection_id of this TransportNodeCollection.  # noqa: E501
        :rtype: str
        """
        return self._compute_collection_id

    @compute_collection_id.setter
    def compute_collection_id(self, compute_collection_id):
        """Sets the compute_collection_id of this TransportNodeCollection.

        Compute collection id  # noqa: E501

        :param compute_collection_id: The compute_collection_id of this TransportNodeCollection.  # noqa: E501
        :type: str
        """
        if compute_collection_id is None:
            raise ValueError("Invalid value for `compute_collection_id`, must not be `None`")  # noqa: E501

        self._compute_collection_id = compute_collection_id

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
        if issubclass(TransportNodeCollection, dict):
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
        if not isinstance(other, TransportNodeCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other