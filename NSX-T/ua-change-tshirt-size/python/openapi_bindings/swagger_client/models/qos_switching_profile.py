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
from swagger_client.models.base_switching_profile import BaseSwitchingProfile  # noqa: F401,E501

class QosSwitchingProfile(BaseSwitchingProfile):
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
        'shaper_configuration': 'list[QosBaseRateShaper]',
        'class_of_service': 'int',
        'dscp': 'Dscp'
    }
    if hasattr(BaseSwitchingProfile, "swagger_types"):
        swagger_types.update(BaseSwitchingProfile.swagger_types)

    attribute_map = {
        'shaper_configuration': 'shaper_configuration',
        'class_of_service': 'class_of_service',
        'dscp': 'dscp'
    }
    if hasattr(BaseSwitchingProfile, "attribute_map"):
        attribute_map.update(BaseSwitchingProfile.attribute_map)

    def __init__(self, shaper_configuration=None, class_of_service=0, dscp=None, *args, **kwargs):  # noqa: E501
        """QosSwitchingProfile - a model defined in Swagger"""  # noqa: E501
        self._shaper_configuration = None
        self._class_of_service = None
        self._dscp = None
        self.discriminator = None
        if shaper_configuration is not None:
            self.shaper_configuration = shaper_configuration
        if class_of_service is not None:
            self.class_of_service = class_of_service
        if dscp is not None:
            self.dscp = dscp
        BaseSwitchingProfile.__init__(self, *args, **kwargs)

    @property
    def shaper_configuration(self):
        """Gets the shaper_configuration of this QosSwitchingProfile.  # noqa: E501


        :return: The shaper_configuration of this QosSwitchingProfile.  # noqa: E501
        :rtype: list[QosBaseRateShaper]
        """
        return self._shaper_configuration

    @shaper_configuration.setter
    def shaper_configuration(self, shaper_configuration):
        """Sets the shaper_configuration of this QosSwitchingProfile.


        :param shaper_configuration: The shaper_configuration of this QosSwitchingProfile.  # noqa: E501
        :type: list[QosBaseRateShaper]
        """

        self._shaper_configuration = shaper_configuration

    @property
    def class_of_service(self):
        """Gets the class_of_service of this QosSwitchingProfile.  # noqa: E501

        Class of service  # noqa: E501

        :return: The class_of_service of this QosSwitchingProfile.  # noqa: E501
        :rtype: int
        """
        return self._class_of_service

    @class_of_service.setter
    def class_of_service(self, class_of_service):
        """Sets the class_of_service of this QosSwitchingProfile.

        Class of service  # noqa: E501

        :param class_of_service: The class_of_service of this QosSwitchingProfile.  # noqa: E501
        :type: int
        """

        self._class_of_service = class_of_service

    @property
    def dscp(self):
        """Gets the dscp of this QosSwitchingProfile.  # noqa: E501


        :return: The dscp of this QosSwitchingProfile.  # noqa: E501
        :rtype: Dscp
        """
        return self._dscp

    @dscp.setter
    def dscp(self, dscp):
        """Sets the dscp of this QosSwitchingProfile.


        :param dscp: The dscp of this QosSwitchingProfile.  # noqa: E501
        :type: Dscp
        """

        self._dscp = dscp

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
        if issubclass(QosSwitchingProfile, dict):
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
        if not isinstance(other, QosSwitchingProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
