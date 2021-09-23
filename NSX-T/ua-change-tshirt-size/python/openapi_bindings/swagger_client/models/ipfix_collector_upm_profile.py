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
from swagger_client.models.managed_resource import ManagedResource  # noqa: F401,E501

class IpfixCollectorUpmProfile(ManagedResource):
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
        'resource_type': 'str',
        'collectors': 'list[IpfixCollector]'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'resource_type': 'resource_type',
        'collectors': 'collectors'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, resource_type=None, collectors=None, *args, **kwargs):  # noqa: E501
        """IpfixCollectorUpmProfile - a model defined in Swagger"""  # noqa: E501
        self._resource_type = None
        self._collectors = None
        self.discriminator = None
        self.resource_type = resource_type
        self.collectors = collectors
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def resource_type(self):
        """Gets the resource_type of this IpfixCollectorUpmProfile.  # noqa: E501

        All IPFIX collector profile types.  # noqa: E501

        :return: The resource_type of this IpfixCollectorUpmProfile.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this IpfixCollectorUpmProfile.

        All IPFIX collector profile types.  # noqa: E501

        :param resource_type: The resource_type of this IpfixCollectorUpmProfile.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["IpfixCollectorUpmProfile"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def collectors(self):
        """Gets the collectors of this IpfixCollectorUpmProfile.  # noqa: E501

        IPFIX Collector Set  # noqa: E501

        :return: The collectors of this IpfixCollectorUpmProfile.  # noqa: E501
        :rtype: list[IpfixCollector]
        """
        return self._collectors

    @collectors.setter
    def collectors(self, collectors):
        """Sets the collectors of this IpfixCollectorUpmProfile.

        IPFIX Collector Set  # noqa: E501

        :param collectors: The collectors of this IpfixCollectorUpmProfile.  # noqa: E501
        :type: list[IpfixCollector]
        """
        if collectors is None:
            raise ValueError("Invalid value for `collectors`, must not be `None`")  # noqa: E501

        self._collectors = collectors

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
        if issubclass(IpfixCollectorUpmProfile, dict):
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
        if not isinstance(other, IpfixCollectorUpmProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
