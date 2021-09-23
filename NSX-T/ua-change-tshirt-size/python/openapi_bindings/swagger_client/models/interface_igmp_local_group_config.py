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

class InterfaceIgmpLocalGroupConfig(object):
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
        'igmp_local_join_groups': 'list[str]'
    }

    attribute_map = {
        'igmp_local_join_groups': 'igmp_local_join_groups'
    }

    def __init__(self, igmp_local_join_groups=None):  # noqa: E501
        """InterfaceIgmpLocalGroupConfig - a model defined in Swagger"""  # noqa: E501
        self._igmp_local_join_groups = None
        self.discriminator = None
        if igmp_local_join_groups is not None:
            self.igmp_local_join_groups = igmp_local_join_groups

    @property
    def igmp_local_join_groups(self):
        """Gets the igmp_local_join_groups of this InterfaceIgmpLocalGroupConfig.  # noqa: E501

        IGMP join group manages the membership of hosts and routing devices in the multicast group. Host will join the group by conveying its information through IGMP.   # noqa: E501

        :return: The igmp_local_join_groups of this InterfaceIgmpLocalGroupConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._igmp_local_join_groups

    @igmp_local_join_groups.setter
    def igmp_local_join_groups(self, igmp_local_join_groups):
        """Sets the igmp_local_join_groups of this InterfaceIgmpLocalGroupConfig.

        IGMP join group manages the membership of hosts and routing devices in the multicast group. Host will join the group by conveying its information through IGMP.   # noqa: E501

        :param igmp_local_join_groups: The igmp_local_join_groups of this InterfaceIgmpLocalGroupConfig.  # noqa: E501
        :type: list[str]
        """

        self._igmp_local_join_groups = igmp_local_join_groups

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
        if issubclass(InterfaceIgmpLocalGroupConfig, dict):
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
        if not isinstance(other, InterfaceIgmpLocalGroupConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
