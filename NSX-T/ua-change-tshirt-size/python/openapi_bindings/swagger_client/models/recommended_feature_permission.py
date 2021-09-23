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

class RecommendedFeaturePermission(object):
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
        'src_features': 'list[str]',
        'target_feature': 'str',
        'recommended_permissions': 'list[str]'
    }

    attribute_map = {
        'src_features': 'src_features',
        'target_feature': 'target_feature',
        'recommended_permissions': 'recommended_permissions'
    }

    def __init__(self, src_features=None, target_feature=None, recommended_permissions=None):  # noqa: E501
        """RecommendedFeaturePermission - a model defined in Swagger"""  # noqa: E501
        self._src_features = None
        self._target_feature = None
        self._recommended_permissions = None
        self.discriminator = None
        self.src_features = src_features
        self.target_feature = target_feature
        self.recommended_permissions = recommended_permissions

    @property
    def src_features(self):
        """Gets the src_features of this RecommendedFeaturePermission.  # noqa: E501

        List of source features  # noqa: E501

        :return: The src_features of this RecommendedFeaturePermission.  # noqa: E501
        :rtype: list[str]
        """
        return self._src_features

    @src_features.setter
    def src_features(self, src_features):
        """Sets the src_features of this RecommendedFeaturePermission.

        List of source features  # noqa: E501

        :param src_features: The src_features of this RecommendedFeaturePermission.  # noqa: E501
        :type: list[str]
        """
        if src_features is None:
            raise ValueError("Invalid value for `src_features`, must not be `None`")  # noqa: E501

        self._src_features = src_features

    @property
    def target_feature(self):
        """Gets the target_feature of this RecommendedFeaturePermission.  # noqa: E501

        Feature  # noqa: E501

        :return: The target_feature of this RecommendedFeaturePermission.  # noqa: E501
        :rtype: str
        """
        return self._target_feature

    @target_feature.setter
    def target_feature(self, target_feature):
        """Sets the target_feature of this RecommendedFeaturePermission.

        Feature  # noqa: E501

        :param target_feature: The target_feature of this RecommendedFeaturePermission.  # noqa: E501
        :type: str
        """
        if target_feature is None:
            raise ValueError("Invalid value for `target_feature`, must not be `None`")  # noqa: E501

        self._target_feature = target_feature

    @property
    def recommended_permissions(self):
        """Gets the recommended_permissions of this RecommendedFeaturePermission.  # noqa: E501

        Permission  # noqa: E501

        :return: The recommended_permissions of this RecommendedFeaturePermission.  # noqa: E501
        :rtype: list[str]
        """
        return self._recommended_permissions

    @recommended_permissions.setter
    def recommended_permissions(self, recommended_permissions):
        """Sets the recommended_permissions of this RecommendedFeaturePermission.

        Permission  # noqa: E501

        :param recommended_permissions: The recommended_permissions of this RecommendedFeaturePermission.  # noqa: E501
        :type: list[str]
        """
        if recommended_permissions is None:
            raise ValueError("Invalid value for `recommended_permissions`, must not be `None`")  # noqa: E501

        self._recommended_permissions = recommended_permissions

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
        if issubclass(RecommendedFeaturePermission, dict):
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
        if not isinstance(other, RecommendedFeaturePermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
