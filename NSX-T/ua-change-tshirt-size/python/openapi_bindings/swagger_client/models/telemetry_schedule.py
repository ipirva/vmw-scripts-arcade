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

class TelemetrySchedule(object):
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
        'frequency_type': 'str'
    }

    attribute_map = {
        'frequency_type': 'frequency_type'
    }

    discriminator_value_class_map = {
          'WeeklyTelemetrySchedule': 'WeeklyTelemetrySchedule',
'MonthlyTelemetrySchedule': 'MonthlyTelemetrySchedule',
'DailyTelemetrySchedule': 'DailyTelemetrySchedule'    }

    def __init__(self, frequency_type=None):  # noqa: E501
        """TelemetrySchedule - a model defined in Swagger"""  # noqa: E501
        self._frequency_type = None
        self.discriminator = 'frequency_type'
        self.frequency_type = frequency_type

    @property
    def frequency_type(self):
        """Gets the frequency_type of this TelemetrySchedule.  # noqa: E501

        Specify one of DailyTelemetrySchedule, WeeklyTelemetrySchedule, or MonthlyTelemetrySchedule.  # noqa: E501

        :return: The frequency_type of this TelemetrySchedule.  # noqa: E501
        :rtype: str
        """
        return self._frequency_type

    @frequency_type.setter
    def frequency_type(self, frequency_type):
        """Sets the frequency_type of this TelemetrySchedule.

        Specify one of DailyTelemetrySchedule, WeeklyTelemetrySchedule, or MonthlyTelemetrySchedule.  # noqa: E501

        :param frequency_type: The frequency_type of this TelemetrySchedule.  # noqa: E501
        :type: str
        """
        if frequency_type is None:
            raise ValueError("Invalid value for `frequency_type`, must not be `None`")  # noqa: E501

        self._frequency_type = frequency_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(TelemetrySchedule, dict):
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
        if not isinstance(other, TelemetrySchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
