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

class DataTypeCollectionConfiguration(object):
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
        'collection_frequency': 'int',
        'data_type': 'str'
    }

    attribute_map = {
        'collection_frequency': 'collection_frequency',
        'data_type': 'data_type'
    }

    def __init__(self, collection_frequency=None, data_type=None):  # noqa: E501
        """DataTypeCollectionConfiguration - a model defined in Swagger"""  # noqa: E501
        self._collection_frequency = None
        self._data_type = None
        self.discriminator = None
        self.collection_frequency = collection_frequency
        self.data_type = data_type

    @property
    def collection_frequency(self):
        """Gets the collection_frequency of this DataTypeCollectionConfiguration.  # noqa: E501

        The frequency in seconds at which data is collected  # noqa: E501

        :return: The collection_frequency of this DataTypeCollectionConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._collection_frequency

    @collection_frequency.setter
    def collection_frequency(self, collection_frequency):
        """Sets the collection_frequency of this DataTypeCollectionConfiguration.

        The frequency in seconds at which data is collected  # noqa: E501

        :param collection_frequency: The collection_frequency of this DataTypeCollectionConfiguration.  # noqa: E501
        :type: int
        """
        if collection_frequency is None:
            raise ValueError("Invalid value for `collection_frequency`, must not be `None`")  # noqa: E501

        self._collection_frequency = collection_frequency

    @property
    def data_type(self):
        """Gets the data_type of this DataTypeCollectionConfiguration.  # noqa: E501

        Defines the type of data being collected  # noqa: E501

        :return: The data_type of this DataTypeCollectionConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this DataTypeCollectionConfiguration.

        Defines the type of data being collected  # noqa: E501

        :param data_type: The data_type of this DataTypeCollectionConfiguration.  # noqa: E501
        :type: str
        """
        if data_type is None:
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["STATUS", "STATISTICS"]  # noqa: E501
        if data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_type, allowed_values)
            )

        self._data_type = data_type

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
        if issubclass(DataTypeCollectionConfiguration, dict):
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
        if not isinstance(other, DataTypeCollectionConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other