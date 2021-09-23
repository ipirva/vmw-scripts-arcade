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

class AdvertisementRuleFilter(object):
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
        'prefix_operator': 'str',
        'match_route_types': 'list[str]'
    }

    attribute_map = {
        'prefix_operator': 'prefix_operator',
        'match_route_types': 'match_route_types'
    }

    def __init__(self, prefix_operator='GE', match_route_types=None):  # noqa: E501
        """AdvertisementRuleFilter - a model defined in Swagger"""  # noqa: E501
        self._prefix_operator = None
        self._match_route_types = None
        self.discriminator = None
        self.prefix_operator = prefix_operator
        self.match_route_types = match_route_types

    @property
    def prefix_operator(self):
        """Gets the prefix_operator of this AdvertisementRuleFilter.  # noqa: E501

        GE prefix operator filters all the routes having network subset of any of the networks configured in Advertise rule. EQ prefix operator filter all the routes having network equal to any of the network configured in Advertise rule.  # noqa: E501

        :return: The prefix_operator of this AdvertisementRuleFilter.  # noqa: E501
        :rtype: str
        """
        return self._prefix_operator

    @prefix_operator.setter
    def prefix_operator(self, prefix_operator):
        """Sets the prefix_operator of this AdvertisementRuleFilter.

        GE prefix operator filters all the routes having network subset of any of the networks configured in Advertise rule. EQ prefix operator filter all the routes having network equal to any of the network configured in Advertise rule.  # noqa: E501

        :param prefix_operator: The prefix_operator of this AdvertisementRuleFilter.  # noqa: E501
        :type: str
        """
        if prefix_operator is None:
            raise ValueError("Invalid value for `prefix_operator`, must not be `None`")  # noqa: E501
        allowed_values = ["GE", "EQ"]  # noqa: E501
        if prefix_operator not in allowed_values:
            raise ValueError(
                "Invalid value for `prefix_operator` ({0}), must be one of {1}"  # noqa: E501
                .format(prefix_operator, allowed_values)
            )

        self._prefix_operator = prefix_operator

    @property
    def match_route_types(self):
        """Gets the match_route_types of this AdvertisementRuleFilter.  # noqa: E501

        Array of route types to filter routes  # noqa: E501

        :return: The match_route_types of this AdvertisementRuleFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._match_route_types

    @match_route_types.setter
    def match_route_types(self, match_route_types):
        """Sets the match_route_types of this AdvertisementRuleFilter.

        Array of route types to filter routes  # noqa: E501

        :param match_route_types: The match_route_types of this AdvertisementRuleFilter.  # noqa: E501
        :type: list[str]
        """
        if match_route_types is None:
            raise ValueError("Invalid value for `match_route_types`, must not be `None`")  # noqa: E501
        allowed_values = ["ANY", "STATIC", "T1_STATIC", "NSX_CONNECTED", "T1_CONNECTED", "T1_NAT", "T1_LB_VIP", "T1_LB_SNAT", "T1_DNSFORWARDER", "T1_IPSEC_LOCAL_IP"]  # noqa: E501
        if not set(match_route_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `match_route_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(match_route_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._match_route_types = match_route_types

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
        if issubclass(AdvertisementRuleFilter, dict):
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
        if not isinstance(other, AdvertisementRuleFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
