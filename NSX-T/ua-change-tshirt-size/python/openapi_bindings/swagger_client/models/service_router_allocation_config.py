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

class ServiceRouterAllocationConfig(object):
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
        'edge_cluster_member_indices': 'list[int]',
        'allocation_pool': 'EdgeClusterMemberAllocationPool',
        'edge_cluster_id': 'str'
    }

    attribute_map = {
        'edge_cluster_member_indices': 'edge_cluster_member_indices',
        'allocation_pool': 'allocation_pool',
        'edge_cluster_id': 'edge_cluster_id'
    }

    def __init__(self, edge_cluster_member_indices=None, allocation_pool=None, edge_cluster_id=None):  # noqa: E501
        """ServiceRouterAllocationConfig - a model defined in Swagger"""  # noqa: E501
        self._edge_cluster_member_indices = None
        self._allocation_pool = None
        self._edge_cluster_id = None
        self.discriminator = None
        if edge_cluster_member_indices is not None:
            self.edge_cluster_member_indices = edge_cluster_member_indices
        if allocation_pool is not None:
            self.allocation_pool = allocation_pool
        self.edge_cluster_id = edge_cluster_id

    @property
    def edge_cluster_member_indices(self):
        """Gets the edge_cluster_member_indices of this ServiceRouterAllocationConfig.  # noqa: E501

        For TIER 1 logical router, for manual placement of service router within the cluster, edge cluster member indices needs to be provided else same will be auto-allocated. You can provide maximum two indices for HA ACTIVE_STANDBY.   # noqa: E501

        :return: The edge_cluster_member_indices of this ServiceRouterAllocationConfig.  # noqa: E501
        :rtype: list[int]
        """
        return self._edge_cluster_member_indices

    @edge_cluster_member_indices.setter
    def edge_cluster_member_indices(self, edge_cluster_member_indices):
        """Sets the edge_cluster_member_indices of this ServiceRouterAllocationConfig.

        For TIER 1 logical router, for manual placement of service router within the cluster, edge cluster member indices needs to be provided else same will be auto-allocated. You can provide maximum two indices for HA ACTIVE_STANDBY.   # noqa: E501

        :param edge_cluster_member_indices: The edge_cluster_member_indices of this ServiceRouterAllocationConfig.  # noqa: E501
        :type: list[int]
        """

        self._edge_cluster_member_indices = edge_cluster_member_indices

    @property
    def allocation_pool(self):
        """Gets the allocation_pool of this ServiceRouterAllocationConfig.  # noqa: E501


        :return: The allocation_pool of this ServiceRouterAllocationConfig.  # noqa: E501
        :rtype: EdgeClusterMemberAllocationPool
        """
        return self._allocation_pool

    @allocation_pool.setter
    def allocation_pool(self, allocation_pool):
        """Sets the allocation_pool of this ServiceRouterAllocationConfig.


        :param allocation_pool: The allocation_pool of this ServiceRouterAllocationConfig.  # noqa: E501
        :type: EdgeClusterMemberAllocationPool
        """

        self._allocation_pool = allocation_pool

    @property
    def edge_cluster_id(self):
        """Gets the edge_cluster_id of this ServiceRouterAllocationConfig.  # noqa: E501

        To reallocate TIER1 logical router on new or existing edge cluster   # noqa: E501

        :return: The edge_cluster_id of this ServiceRouterAllocationConfig.  # noqa: E501
        :rtype: str
        """
        return self._edge_cluster_id

    @edge_cluster_id.setter
    def edge_cluster_id(self, edge_cluster_id):
        """Sets the edge_cluster_id of this ServiceRouterAllocationConfig.

        To reallocate TIER1 logical router on new or existing edge cluster   # noqa: E501

        :param edge_cluster_id: The edge_cluster_id of this ServiceRouterAllocationConfig.  # noqa: E501
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
        if issubclass(ServiceRouterAllocationConfig, dict):
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
        if not isinstance(other, ServiceRouterAllocationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
