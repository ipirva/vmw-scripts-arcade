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

class RelatedApiError(object):
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
        'module_name': 'str',
        'error_message': 'str',
        'error_code': 'int',
        'details': 'str',
        'error_data': 'object'
    }

    attribute_map = {
        'module_name': 'module_name',
        'error_message': 'error_message',
        'error_code': 'error_code',
        'details': 'details',
        'error_data': 'error_data'
    }

    def __init__(self, module_name=None, error_message=None, error_code=None, details=None, error_data=None):  # noqa: E501
        """RelatedApiError - a model defined in Swagger"""  # noqa: E501
        self._module_name = None
        self._error_message = None
        self._error_code = None
        self._details = None
        self._error_data = None
        self.discriminator = None
        if module_name is not None:
            self.module_name = module_name
        if error_message is not None:
            self.error_message = error_message
        if error_code is not None:
            self.error_code = error_code
        if details is not None:
            self.details = details
        if error_data is not None:
            self.error_data = error_data

    @property
    def module_name(self):
        """Gets the module_name of this RelatedApiError.  # noqa: E501

        The module name where the error occurred  # noqa: E501

        :return: The module_name of this RelatedApiError.  # noqa: E501
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """Sets the module_name of this RelatedApiError.

        The module name where the error occurred  # noqa: E501

        :param module_name: The module_name of this RelatedApiError.  # noqa: E501
        :type: str
        """

        self._module_name = module_name

    @property
    def error_message(self):
        """Gets the error_message of this RelatedApiError.  # noqa: E501

        A description of the error  # noqa: E501

        :return: The error_message of this RelatedApiError.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this RelatedApiError.

        A description of the error  # noqa: E501

        :param error_message: The error_message of this RelatedApiError.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def error_code(self):
        """Gets the error_code of this RelatedApiError.  # noqa: E501

        A numeric error code  # noqa: E501

        :return: The error_code of this RelatedApiError.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this RelatedApiError.

        A numeric error code  # noqa: E501

        :param error_code: The error_code of this RelatedApiError.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def details(self):
        """Gets the details of this RelatedApiError.  # noqa: E501

        Further details about the error  # noqa: E501

        :return: The details of this RelatedApiError.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this RelatedApiError.

        Further details about the error  # noqa: E501

        :param details: The details of this RelatedApiError.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def error_data(self):
        """Gets the error_data of this RelatedApiError.  # noqa: E501

        Additional data about the error  # noqa: E501

        :return: The error_data of this RelatedApiError.  # noqa: E501
        :rtype: object
        """
        return self._error_data

    @error_data.setter
    def error_data(self, error_data):
        """Sets the error_data of this RelatedApiError.

        Additional data about the error  # noqa: E501

        :param error_data: The error_data of this RelatedApiError.  # noqa: E501
        :type: object
        """

        self._error_data = error_data

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
        if issubclass(RelatedApiError, dict):
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
        if not isinstance(other, RelatedApiError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
