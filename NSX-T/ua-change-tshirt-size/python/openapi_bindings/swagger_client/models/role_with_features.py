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

class RoleWithFeatures(ManagedResource):
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
        'role': 'str',
        'features': 'list[FeaturePermission]'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'role': 'role',
        'features': 'features'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, role=None, features=None, *args, **kwargs):  # noqa: E501
        """RoleWithFeatures - a model defined in Swagger"""  # noqa: E501
        self._role = None
        self._features = None
        self.discriminator = None
        if role is not None:
            self.role = role
        self.features = features
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def role(self):
        """Gets the role of this RoleWithFeatures.  # noqa: E501

        Short identifier for the role. Must be all lower case with no spaces.  # noqa: E501

        :return: The role of this RoleWithFeatures.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this RoleWithFeatures.

        Short identifier for the role. Must be all lower case with no spaces.  # noqa: E501

        :param role: The role of this RoleWithFeatures.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def features(self):
        """Gets the features of this RoleWithFeatures.  # noqa: E501

        Features  # noqa: E501

        :return: The features of this RoleWithFeatures.  # noqa: E501
        :rtype: list[FeaturePermission]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this RoleWithFeatures.

        Features  # noqa: E501

        :param features: The features of this RoleWithFeatures.  # noqa: E501
        :type: list[FeaturePermission]
        """
        if features is None:
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

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
        if issubclass(RoleWithFeatures, dict):
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
        if not isinstance(other, RoleWithFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other