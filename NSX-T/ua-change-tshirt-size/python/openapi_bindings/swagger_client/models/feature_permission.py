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

class FeaturePermission(object):
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
        'is_execute_recommended': 'bool',
        'feature_name': 'str',
        'permission': 'str',
        'is_internal': 'bool',
        'feature': 'str',
        'feature_description': 'str'
    }

    attribute_map = {
        'is_execute_recommended': 'is_execute_recommended',
        'feature_name': 'feature_name',
        'permission': 'permission',
        'is_internal': 'is_internal',
        'feature': 'feature',
        'feature_description': 'feature_description'
    }

    def __init__(self, is_execute_recommended=None, feature_name=None, permission=None, is_internal=None, feature=None, feature_description=None):  # noqa: E501
        """FeaturePermission - a model defined in Swagger"""  # noqa: E501
        self._is_execute_recommended = None
        self._feature_name = None
        self._permission = None
        self._is_internal = None
        self._feature = None
        self._feature_description = None
        self.discriminator = None
        if is_execute_recommended is not None:
            self.is_execute_recommended = is_execute_recommended
        if feature_name is not None:
            self.feature_name = feature_name
        self.permission = permission
        if is_internal is not None:
            self.is_internal = is_internal
        self.feature = feature
        if feature_description is not None:
            self.feature_description = feature_description

    @property
    def is_execute_recommended(self):
        """Gets the is_execute_recommended of this FeaturePermission.  # noqa: E501

        Is execute recommended  # noqa: E501

        :return: The is_execute_recommended of this FeaturePermission.  # noqa: E501
        :rtype: bool
        """
        return self._is_execute_recommended

    @is_execute_recommended.setter
    def is_execute_recommended(self, is_execute_recommended):
        """Sets the is_execute_recommended of this FeaturePermission.

        Is execute recommended  # noqa: E501

        :param is_execute_recommended: The is_execute_recommended of this FeaturePermission.  # noqa: E501
        :type: bool
        """

        self._is_execute_recommended = is_execute_recommended

    @property
    def feature_name(self):
        """Gets the feature_name of this FeaturePermission.  # noqa: E501

        Feature Name  # noqa: E501

        :return: The feature_name of this FeaturePermission.  # noqa: E501
        :rtype: str
        """
        return self._feature_name

    @feature_name.setter
    def feature_name(self, feature_name):
        """Sets the feature_name of this FeaturePermission.

        Feature Name  # noqa: E501

        :param feature_name: The feature_name of this FeaturePermission.  # noqa: E501
        :type: str
        """

        self._feature_name = feature_name

    @property
    def permission(self):
        """Gets the permission of this FeaturePermission.  # noqa: E501

        Permission  # noqa: E501

        :return: The permission of this FeaturePermission.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this FeaturePermission.

        Permission  # noqa: E501

        :param permission: The permission of this FeaturePermission.  # noqa: E501
        :type: str
        """
        if permission is None:
            raise ValueError("Invalid value for `permission`, must not be `None`")  # noqa: E501
        allowed_values = ["crud", "read", "execute", "none"]  # noqa: E501
        if permission not in allowed_values:
            raise ValueError(
                "Invalid value for `permission` ({0}), must be one of {1}"  # noqa: E501
                .format(permission, allowed_values)
            )

        self._permission = permission

    @property
    def is_internal(self):
        """Gets the is_internal of this FeaturePermission.  # noqa: E501

        Is internal  # noqa: E501

        :return: The is_internal of this FeaturePermission.  # noqa: E501
        :rtype: bool
        """
        return self._is_internal

    @is_internal.setter
    def is_internal(self, is_internal):
        """Sets the is_internal of this FeaturePermission.

        Is internal  # noqa: E501

        :param is_internal: The is_internal of this FeaturePermission.  # noqa: E501
        :type: bool
        """

        self._is_internal = is_internal

    @property
    def feature(self):
        """Gets the feature of this FeaturePermission.  # noqa: E501

        Feature Id  # noqa: E501

        :return: The feature of this FeaturePermission.  # noqa: E501
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this FeaturePermission.

        Feature Id  # noqa: E501

        :param feature: The feature of this FeaturePermission.  # noqa: E501
        :type: str
        """
        if feature is None:
            raise ValueError("Invalid value for `feature`, must not be `None`")  # noqa: E501

        self._feature = feature

    @property
    def feature_description(self):
        """Gets the feature_description of this FeaturePermission.  # noqa: E501

        Feature Description  # noqa: E501

        :return: The feature_description of this FeaturePermission.  # noqa: E501
        :rtype: str
        """
        return self._feature_description

    @feature_description.setter
    def feature_description(self, feature_description):
        """Sets the feature_description of this FeaturePermission.

        Feature Description  # noqa: E501

        :param feature_description: The feature_description of this FeaturePermission.  # noqa: E501
        :type: str
        """

        self._feature_description = feature_description

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
        if issubclass(FeaturePermission, dict):
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
        if not isinstance(other, FeaturePermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other