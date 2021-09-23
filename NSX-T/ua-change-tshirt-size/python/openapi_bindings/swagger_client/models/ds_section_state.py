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
from swagger_client.models.configuration_state import ConfigurationState  # noqa: F401,E501

class DSSectionState(ConfigurationState):
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
        'revision_desired': 'int'
    }
    if hasattr(ConfigurationState, "swagger_types"):
        swagger_types.update(ConfigurationState.swagger_types)

    attribute_map = {
        'revision_desired': 'revision_desired'
    }
    if hasattr(ConfigurationState, "attribute_map"):
        attribute_map.update(ConfigurationState.attribute_map)

    def __init__(self, revision_desired=None, *args, **kwargs):  # noqa: E501
        """DSSectionState - a model defined in Swagger"""  # noqa: E501
        self._revision_desired = None
        self.discriminator = None
        if revision_desired is not None:
            self.revision_desired = revision_desired
        ConfigurationState.__init__(self, *args, **kwargs)

    @property
    def revision_desired(self):
        """Gets the revision_desired of this DSSectionState.  # noqa: E501

        This attribute represents revision number of section's desired state.  # noqa: E501

        :return: The revision_desired of this DSSectionState.  # noqa: E501
        :rtype: int
        """
        return self._revision_desired

    @revision_desired.setter
    def revision_desired(self, revision_desired):
        """Sets the revision_desired of this DSSectionState.

        This attribute represents revision number of section's desired state.  # noqa: E501

        :param revision_desired: The revision_desired of this DSSectionState.  # noqa: E501
        :type: int
        """

        self._revision_desired = revision_desired

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
        if issubclass(DSSectionState, dict):
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
        if not isinstance(other, DSSectionState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
