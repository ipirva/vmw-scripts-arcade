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

class TelemetryAgreement(ManagedResource):
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
        'telemetry_agreement_displayed': 'bool'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'telemetry_agreement_displayed': 'telemetry_agreement_displayed'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, telemetry_agreement_displayed=None, *args, **kwargs):  # noqa: E501
        """TelemetryAgreement - a model defined in Swagger"""  # noqa: E501
        self._telemetry_agreement_displayed = None
        self.discriminator = None
        self.telemetry_agreement_displayed = telemetry_agreement_displayed
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def telemetry_agreement_displayed(self):
        """Gets the telemetry_agreement_displayed of this TelemetryAgreement.  # noqa: E501

        Determine if telemetry agreement has been displayed. If false, the agreement text will be displayed at login time.   # noqa: E501

        :return: The telemetry_agreement_displayed of this TelemetryAgreement.  # noqa: E501
        :rtype: bool
        """
        return self._telemetry_agreement_displayed

    @telemetry_agreement_displayed.setter
    def telemetry_agreement_displayed(self, telemetry_agreement_displayed):
        """Sets the telemetry_agreement_displayed of this TelemetryAgreement.

        Determine if telemetry agreement has been displayed. If false, the agreement text will be displayed at login time.   # noqa: E501

        :param telemetry_agreement_displayed: The telemetry_agreement_displayed of this TelemetryAgreement.  # noqa: E501
        :type: bool
        """
        if telemetry_agreement_displayed is None:
            raise ValueError("Invalid value for `telemetry_agreement_displayed`, must not be `None`")  # noqa: E501

        self._telemetry_agreement_displayed = telemetry_agreement_displayed

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
        if issubclass(TelemetryAgreement, dict):
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
        if not isinstance(other, TelemetryAgreement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
