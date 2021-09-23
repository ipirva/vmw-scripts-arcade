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
from swagger_client.models.resource_reference import ResourceReference  # noqa: F401,E501

class NSXProfileReference(ResourceReference):
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
        'profile_type': 'str'
    }
    if hasattr(ResourceReference, "swagger_types"):
        swagger_types.update(ResourceReference.swagger_types)

    attribute_map = {
        'profile_type': 'profile_type'
    }
    if hasattr(ResourceReference, "attribute_map"):
        attribute_map.update(ResourceReference.attribute_map)

    def __init__(self, profile_type=None, *args, **kwargs):  # noqa: E501
        """NSXProfileReference - a model defined in Swagger"""  # noqa: E501
        self._profile_type = None
        self.discriminator = None
        self.profile_type = profile_type
        ResourceReference.__init__(self, *args, **kwargs)

    @property
    def profile_type(self):
        """Gets the profile_type of this NSXProfileReference.  # noqa: E501

        Profile type of the ServiceConfig  # noqa: E501

        :return: The profile_type of this NSXProfileReference.  # noqa: E501
        :rtype: str
        """
        return self._profile_type

    @profile_type.setter
    def profile_type(self, profile_type):
        """Sets the profile_type of this NSXProfileReference.

        Profile type of the ServiceConfig  # noqa: E501

        :param profile_type: The profile_type of this NSXProfileReference.  # noqa: E501
        :type: str
        """
        if profile_type is None:
            raise ValueError("Invalid value for `profile_type`, must not be `None`")  # noqa: E501
        allowed_values = ["FirewallSessionTimerProfile", "FirewallCpuMemThresholdsProfile", "GiServiceProfile", "FirewallFloodProtectionProfile", "FirewallDnsProfile", "LatencyStatProfile", "SHAProfile", "IpDiscoverySwitchingUpmProfile", "SystemHealthPluginProfile", "GeneralSecuritySettingsProfile"]  # noqa: E501
        if profile_type not in allowed_values:
            raise ValueError(
                "Invalid value for `profile_type` ({0}), must be one of {1}"  # noqa: E501
                .format(profile_type, allowed_values)
            )

        self._profile_type = profile_type

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
        if issubclass(NSXProfileReference, dict):
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
        if not isinstance(other, NSXProfileReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other