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
from swagger_client.models.edge_cluster_member_allocation_pool import EdgeClusterMemberAllocationPool  # noqa: F401,E501

class LoadBalancerAllocationPool(EdgeClusterMemberAllocationPool):
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
        'allocation_size': 'str'
    }
    if hasattr(EdgeClusterMemberAllocationPool, "swagger_types"):
        swagger_types.update(EdgeClusterMemberAllocationPool.swagger_types)

    attribute_map = {
        'allocation_size': 'allocation_size'
    }
    if hasattr(EdgeClusterMemberAllocationPool, "attribute_map"):
        attribute_map.update(EdgeClusterMemberAllocationPool.attribute_map)

    def __init__(self, allocation_size='SMALL', *args, **kwargs):  # noqa: E501
        """LoadBalancerAllocationPool - a model defined in Swagger"""  # noqa: E501
        self._allocation_size = None
        self.discriminator = None
        self.allocation_size = allocation_size
        EdgeClusterMemberAllocationPool.__init__(self, *args, **kwargs)

    @property
    def allocation_size(self):
        """Gets the allocation_size of this LoadBalancerAllocationPool.  # noqa: E501

        To address varied customer performance and scalability requirements, different sizes for load balancer service are supported: SMALL, MEDIUM, LARGE and XLARGE, each with its own set of resource and performance. Specify size of load balancer service which you will bind to TIER1 router.   # noqa: E501

        :return: The allocation_size of this LoadBalancerAllocationPool.  # noqa: E501
        :rtype: str
        """
        return self._allocation_size

    @allocation_size.setter
    def allocation_size(self, allocation_size):
        """Sets the allocation_size of this LoadBalancerAllocationPool.

        To address varied customer performance and scalability requirements, different sizes for load balancer service are supported: SMALL, MEDIUM, LARGE and XLARGE, each with its own set of resource and performance. Specify size of load balancer service which you will bind to TIER1 router.   # noqa: E501

        :param allocation_size: The allocation_size of this LoadBalancerAllocationPool.  # noqa: E501
        :type: str
        """
        if allocation_size is None:
            raise ValueError("Invalid value for `allocation_size`, must not be `None`")  # noqa: E501
        allowed_values = ["SMALL", "MEDIUM", "LARGE", "XLARGE"]  # noqa: E501
        if allocation_size not in allowed_values:
            raise ValueError(
                "Invalid value for `allocation_size` ({0}), must be one of {1}"  # noqa: E501
                .format(allocation_size, allowed_values)
            )

        self._allocation_size = allocation_size

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
        if issubclass(LoadBalancerAllocationPool, dict):
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
        if not isinstance(other, LoadBalancerAllocationPool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other