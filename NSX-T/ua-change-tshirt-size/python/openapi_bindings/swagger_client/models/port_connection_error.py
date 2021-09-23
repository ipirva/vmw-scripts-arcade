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

class PortConnectionError(object):
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
        'error_summary': 'str',
        'error_details': 'object',
        'entity_type': 'str'
    }

    attribute_map = {
        'error_summary': 'error_summary',
        'error_details': 'error_details',
        'entity_type': 'entity_type'
    }

    def __init__(self, error_summary=None, error_details=None, entity_type=None):  # noqa: E501
        """PortConnectionError - a model defined in Swagger"""  # noqa: E501
        self._error_summary = None
        self._error_details = None
        self._entity_type = None
        self.discriminator = None
        if error_summary is not None:
            self.error_summary = error_summary
        if error_details is not None:
            self.error_details = error_details
        if entity_type is not None:
            self.entity_type = entity_type

    @property
    def error_summary(self):
        """Gets the error_summary of this PortConnectionError.  # noqa: E501


        :return: The error_summary of this PortConnectionError.  # noqa: E501
        :rtype: str
        """
        return self._error_summary

    @error_summary.setter
    def error_summary(self, error_summary):
        """Sets the error_summary of this PortConnectionError.


        :param error_summary: The error_summary of this PortConnectionError.  # noqa: E501
        :type: str
        """

        self._error_summary = error_summary

    @property
    def error_details(self):
        """Gets the error_details of this PortConnectionError.  # noqa: E501


        :return: The error_details of this PortConnectionError.  # noqa: E501
        :rtype: object
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this PortConnectionError.


        :param error_details: The error_details of this PortConnectionError.  # noqa: E501
        :type: object
        """

        self._error_details = error_details

    @property
    def entity_type(self):
        """Gets the entity_type of this PortConnectionError.  # noqa: E501


        :return: The entity_type of this PortConnectionError.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this PortConnectionError.


        :param entity_type: The entity_type of this PortConnectionError.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

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
        if issubclass(PortConnectionError, dict):
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
        if not isinstance(other, PortConnectionError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
