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
from swagger_client.models.service_insertion_section import ServiceInsertionSection  # noqa: F401,E501

class ServiceInsertionSectionRuleList(ServiceInsertionSection):
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
        'rules': 'list[ServiceInsertionRule]'
    }
    if hasattr(ServiceInsertionSection, "swagger_types"):
        swagger_types.update(ServiceInsertionSection.swagger_types)

    attribute_map = {
        'rules': 'rules'
    }
    if hasattr(ServiceInsertionSection, "attribute_map"):
        attribute_map.update(ServiceInsertionSection.attribute_map)

    def __init__(self, rules=None, *args, **kwargs):  # noqa: E501
        """ServiceInsertionSectionRuleList - a model defined in Swagger"""  # noqa: E501
        self._rules = None
        self.discriminator = None
        self.rules = rules
        ServiceInsertionSection.__init__(self, *args, **kwargs)

    @property
    def rules(self):
        """Gets the rules of this ServiceInsertionSectionRuleList.  # noqa: E501

        List of Service Insertion rules in the section. Only homogeneous rules are supported.  # noqa: E501

        :return: The rules of this ServiceInsertionSectionRuleList.  # noqa: E501
        :rtype: list[ServiceInsertionRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this ServiceInsertionSectionRuleList.

        List of Service Insertion rules in the section. Only homogeneous rules are supported.  # noqa: E501

        :param rules: The rules of this ServiceInsertionSectionRuleList.  # noqa: E501
        :type: list[ServiceInsertionRule]
        """
        if rules is None:
            raise ValueError("Invalid value for `rules`, must not be `None`")  # noqa: E501

        self._rules = rules

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
        if issubclass(ServiceInsertionSectionRuleList, dict):
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
        if not isinstance(other, ServiceInsertionSectionRuleList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
