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

class NSGroupInfo(object):
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
        'nsgroup_policy_path': 'str',
        'nsgroup': 'ResourceReference'
    }

    attribute_map = {
        'nsgroup_policy_path': 'nsgroup_policy_path',
        'nsgroup': 'nsgroup'
    }

    def __init__(self, nsgroup_policy_path=None, nsgroup=None):  # noqa: E501
        """NSGroupInfo - a model defined in Swagger"""  # noqa: E501
        self._nsgroup_policy_path = None
        self._nsgroup = None
        self.discriminator = None
        if nsgroup_policy_path is not None:
            self.nsgroup_policy_path = nsgroup_policy_path
        if nsgroup is not None:
            self.nsgroup = nsgroup

    @property
    def nsgroup_policy_path(self):
        """Gets the nsgroup_policy_path of this NSGroupInfo.  # noqa: E501

        Relative Policy path of a particular NSGroup.  # noqa: E501

        :return: The nsgroup_policy_path of this NSGroupInfo.  # noqa: E501
        :rtype: str
        """
        return self._nsgroup_policy_path

    @nsgroup_policy_path.setter
    def nsgroup_policy_path(self, nsgroup_policy_path):
        """Sets the nsgroup_policy_path of this NSGroupInfo.

        Relative Policy path of a particular NSGroup.  # noqa: E501

        :param nsgroup_policy_path: The nsgroup_policy_path of this NSGroupInfo.  # noqa: E501
        :type: str
        """

        self._nsgroup_policy_path = nsgroup_policy_path

    @property
    def nsgroup(self):
        """Gets the nsgroup of this NSGroupInfo.  # noqa: E501


        :return: The nsgroup of this NSGroupInfo.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._nsgroup

    @nsgroup.setter
    def nsgroup(self, nsgroup):
        """Sets the nsgroup of this NSGroupInfo.


        :param nsgroup: The nsgroup of this NSGroupInfo.  # noqa: E501
        :type: ResourceReference
        """

        self._nsgroup = nsgroup

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
        if issubclass(NSGroupInfo, dict):
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
        if not isinstance(other, NSGroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
