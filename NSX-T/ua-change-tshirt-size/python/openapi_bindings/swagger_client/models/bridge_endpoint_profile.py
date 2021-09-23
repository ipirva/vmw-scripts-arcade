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

class BridgeEndpointProfile(ManagedResource):
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
        'failover_mode': 'str',
        'edge_cluster_member_indexes': 'list[int]',
        'high_availability_mode': 'str',
        'edge_cluster_id': 'str'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'failover_mode': 'failover_mode',
        'edge_cluster_member_indexes': 'edge_cluster_member_indexes',
        'high_availability_mode': 'high_availability_mode',
        'edge_cluster_id': 'edge_cluster_id'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, failover_mode='PREEMPTIVE', edge_cluster_member_indexes=None, high_availability_mode='ACTIVE_STANDBY', edge_cluster_id=None, *args, **kwargs):  # noqa: E501
        """BridgeEndpointProfile - a model defined in Swagger"""  # noqa: E501
        self._failover_mode = None
        self._edge_cluster_member_indexes = None
        self._high_availability_mode = None
        self._edge_cluster_id = None
        self.discriminator = None
        if failover_mode is not None:
            self.failover_mode = failover_mode
        if edge_cluster_member_indexes is not None:
            self.edge_cluster_member_indexes = edge_cluster_member_indexes
        if high_availability_mode is not None:
            self.high_availability_mode = high_availability_mode
        self.edge_cluster_id = edge_cluster_id
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def failover_mode(self):
        """Gets the failover_mode of this BridgeEndpointProfile.  # noqa: E501

        Faileover mode can be preemmptive or non-preemptive  # noqa: E501

        :return: The failover_mode of this BridgeEndpointProfile.  # noqa: E501
        :rtype: str
        """
        return self._failover_mode

    @failover_mode.setter
    def failover_mode(self, failover_mode):
        """Sets the failover_mode of this BridgeEndpointProfile.

        Faileover mode can be preemmptive or non-preemptive  # noqa: E501

        :param failover_mode: The failover_mode of this BridgeEndpointProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["PREEMPTIVE", "NON_PREEMPTIVE"]  # noqa: E501
        if failover_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `failover_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(failover_mode, allowed_values)
            )

        self._failover_mode = failover_mode

    @property
    def edge_cluster_member_indexes(self):
        """Gets the edge_cluster_member_indexes of this BridgeEndpointProfile.  # noqa: E501

        First index will be used as the preferred member  # noqa: E501

        :return: The edge_cluster_member_indexes of this BridgeEndpointProfile.  # noqa: E501
        :rtype: list[int]
        """
        return self._edge_cluster_member_indexes

    @edge_cluster_member_indexes.setter
    def edge_cluster_member_indexes(self, edge_cluster_member_indexes):
        """Sets the edge_cluster_member_indexes of this BridgeEndpointProfile.

        First index will be used as the preferred member  # noqa: E501

        :param edge_cluster_member_indexes: The edge_cluster_member_indexes of this BridgeEndpointProfile.  # noqa: E501
        :type: list[int]
        """

        self._edge_cluster_member_indexes = edge_cluster_member_indexes

    @property
    def high_availability_mode(self):
        """Gets the high_availability_mode of this BridgeEndpointProfile.  # noqa: E501

        High avaialability mode can be active-active or active-standby  # noqa: E501

        :return: The high_availability_mode of this BridgeEndpointProfile.  # noqa: E501
        :rtype: str
        """
        return self._high_availability_mode

    @high_availability_mode.setter
    def high_availability_mode(self, high_availability_mode):
        """Sets the high_availability_mode of this BridgeEndpointProfile.

        High avaialability mode can be active-active or active-standby  # noqa: E501

        :param high_availability_mode: The high_availability_mode of this BridgeEndpointProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE_STANDBY"]  # noqa: E501
        if high_availability_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `high_availability_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(high_availability_mode, allowed_values)
            )

        self._high_availability_mode = high_availability_mode

    @property
    def edge_cluster_id(self):
        """Gets the edge_cluster_id of this BridgeEndpointProfile.  # noqa: E501

        UUID of the edge cluster for this bridge endpoint  # noqa: E501

        :return: The edge_cluster_id of this BridgeEndpointProfile.  # noqa: E501
        :rtype: str
        """
        return self._edge_cluster_id

    @edge_cluster_id.setter
    def edge_cluster_id(self, edge_cluster_id):
        """Sets the edge_cluster_id of this BridgeEndpointProfile.

        UUID of the edge cluster for this bridge endpoint  # noqa: E501

        :param edge_cluster_id: The edge_cluster_id of this BridgeEndpointProfile.  # noqa: E501
        :type: str
        """
        if edge_cluster_id is None:
            raise ValueError("Invalid value for `edge_cluster_id`, must not be `None`")  # noqa: E501

        self._edge_cluster_id = edge_cluster_id

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
        if issubclass(BridgeEndpointProfile, dict):
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
        if not isinstance(other, BridgeEndpointProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other