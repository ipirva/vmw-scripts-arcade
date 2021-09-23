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

class LayoutProperties(object):
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
        'num_rows': 'int',
        'num_columns': 'int'
    }

    attribute_map = {
        'num_rows': 'num_rows',
        'num_columns': 'num_columns'
    }

    def __init__(self, num_rows=None, num_columns=None):  # noqa: E501
        """LayoutProperties - a model defined in Swagger"""  # noqa: E501
        self._num_rows = None
        self._num_columns = None
        self.discriminator = None
        if num_rows is not None:
            self.num_rows = num_rows
        if num_columns is not None:
            self.num_columns = num_columns

    @property
    def num_rows(self):
        """Gets the num_rows of this LayoutProperties.  # noqa: E501

        Describes the number of rows of grid layout of a container or widget. This property is applicable for grid layout only.  # noqa: E501

        :return: The num_rows of this LayoutProperties.  # noqa: E501
        :rtype: int
        """
        return self._num_rows

    @num_rows.setter
    def num_rows(self, num_rows):
        """Sets the num_rows of this LayoutProperties.

        Describes the number of rows of grid layout of a container or widget. This property is applicable for grid layout only.  # noqa: E501

        :param num_rows: The num_rows of this LayoutProperties.  # noqa: E501
        :type: int
        """

        self._num_rows = num_rows

    @property
    def num_columns(self):
        """Gets the num_columns of this LayoutProperties.  # noqa: E501

        Describes the number of columns of grid layout of a container or widget. This property is applicable for grid layout only.  # noqa: E501

        :return: The num_columns of this LayoutProperties.  # noqa: E501
        :rtype: int
        """
        return self._num_columns

    @num_columns.setter
    def num_columns(self, num_columns):
        """Sets the num_columns of this LayoutProperties.

        Describes the number of columns of grid layout of a container or widget. This property is applicable for grid layout only.  # noqa: E501

        :param num_columns: The num_columns of this LayoutProperties.  # noqa: E501
        :type: int
        """

        self._num_columns = num_columns

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
        if issubclass(LayoutProperties, dict):
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
        if not isinstance(other, LayoutProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
