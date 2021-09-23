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

class NvdsUpgradePrecheckId(object):
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
        'precheck_id': 'str'
    }

    attribute_map = {
        'precheck_id': 'precheck_id'
    }

    def __init__(self, precheck_id=None):  # noqa: E501
        """NvdsUpgradePrecheckId - a model defined in Swagger"""  # noqa: E501
        self._precheck_id = None
        self.discriminator = None
        if precheck_id is not None:
            self.precheck_id = precheck_id

    @property
    def precheck_id(self):
        """Gets the precheck_id of this NvdsUpgradePrecheckId.  # noqa: E501

        Tracking ID of nvds upgrade precheck  # noqa: E501

        :return: The precheck_id of this NvdsUpgradePrecheckId.  # noqa: E501
        :rtype: str
        """
        return self._precheck_id

    @precheck_id.setter
    def precheck_id(self, precheck_id):
        """Sets the precheck_id of this NvdsUpgradePrecheckId.

        Tracking ID of nvds upgrade precheck  # noqa: E501

        :param precheck_id: The precheck_id of this NvdsUpgradePrecheckId.  # noqa: E501
        :type: str
        """

        self._precheck_id = precheck_id

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
        if issubclass(NvdsUpgradePrecheckId, dict):
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
        if not isinstance(other, NvdsUpgradePrecheckId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
