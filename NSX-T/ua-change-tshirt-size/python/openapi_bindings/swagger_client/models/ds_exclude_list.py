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

class DSExcludeList(ManagedResource):
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
        'member_count': 'int',
        'members': 'list[ResourceReference]'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'member_count': 'member_count',
        'members': 'members'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, member_count=None, members=None, *args, **kwargs):  # noqa: E501
        """DSExcludeList - a model defined in Swagger"""  # noqa: E501
        self._member_count = None
        self._members = None
        self.discriminator = None
        if member_count is not None:
            self.member_count = member_count
        self.members = members
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def member_count(self):
        """Gets the member_count of this DSExcludeList.  # noqa: E501

        Total number of members present in Exclude List.  # noqa: E501

        :return: The member_count of this DSExcludeList.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this DSExcludeList.

        Total number of members present in Exclude List.  # noqa: E501

        :param member_count: The member_count of this DSExcludeList.  # noqa: E501
        :type: int
        """

        self._member_count = member_count

    @property
    def members(self):
        """Gets the members of this DSExcludeList.  # noqa: E501

        List of members in Exclusion List  # noqa: E501

        :return: The members of this DSExcludeList.  # noqa: E501
        :rtype: list[ResourceReference]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this DSExcludeList.

        List of members in Exclusion List  # noqa: E501

        :param members: The members of this DSExcludeList.  # noqa: E501
        :type: list[ResourceReference]
        """
        if members is None:
            raise ValueError("Invalid value for `members`, must not be `None`")  # noqa: E501

        self._members = members

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
        if issubclass(DSExcludeList, dict):
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
        if not isinstance(other, DSExcludeList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
