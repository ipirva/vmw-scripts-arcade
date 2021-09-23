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
from swagger_client.models.list_result import ListResult  # noqa: F401,E501

class AutomaticHealthCheckListResult(ListResult):
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
        'results': 'list[AutomaticHealthCheck]'
    }
    if hasattr(ListResult, "swagger_types"):
        swagger_types.update(ListResult.swagger_types)

    attribute_map = {
        'results': 'results'
    }
    if hasattr(ListResult, "attribute_map"):
        attribute_map.update(ListResult.attribute_map)

    def __init__(self, results=None, *args, **kwargs):  # noqa: E501
        """AutomaticHealthCheckListResult - a model defined in Swagger"""  # noqa: E501
        self._results = None
        self.discriminator = None
        if results is not None:
            self.results = results
        ListResult.__init__(self, *args, **kwargs)

    @property
    def results(self):
        """Gets the results of this AutomaticHealthCheckListResult.  # noqa: E501

        Automatic Health Check List  # noqa: E501

        :return: The results of this AutomaticHealthCheckListResult.  # noqa: E501
        :rtype: list[AutomaticHealthCheck]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this AutomaticHealthCheckListResult.

        Automatic Health Check List  # noqa: E501

        :param results: The results of this AutomaticHealthCheckListResult.  # noqa: E501
        :type: list[AutomaticHealthCheck]
        """

        self._results = results

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
        if issubclass(AutomaticHealthCheckListResult, dict):
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
        if not isinstance(other, AutomaticHealthCheckListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
