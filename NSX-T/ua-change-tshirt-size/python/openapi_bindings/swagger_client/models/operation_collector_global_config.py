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
from swagger_client.models.global_configs import GlobalConfigs  # noqa: F401,E501

class OperationCollectorGlobalConfig(GlobalConfigs):
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
        'report_interval': 'int',
        'collectors': 'list[OperationCollector]'
    }
    if hasattr(GlobalConfigs, "swagger_types"):
        swagger_types.update(GlobalConfigs.swagger_types)

    attribute_map = {
        'report_interval': 'report_interval',
        'collectors': 'collectors'
    }
    if hasattr(GlobalConfigs, "attribute_map"):
        attribute_map.update(GlobalConfigs.attribute_map)

    def __init__(self, report_interval=30, collectors=None, *args, **kwargs):  # noqa: E501
        """OperationCollectorGlobalConfig - a model defined in Swagger"""  # noqa: E501
        self._report_interval = None
        self._collectors = None
        self.discriminator = None
        if report_interval is not None:
            self.report_interval = report_interval
        if collectors is not None:
            self.collectors = collectors
        GlobalConfigs.__init__(self, *args, **kwargs)

    @property
    def report_interval(self):
        """Gets the report_interval of this OperationCollectorGlobalConfig.  # noqa: E501

        Report interval for operation data in seconds.  # noqa: E501

        :return: The report_interval of this OperationCollectorGlobalConfig.  # noqa: E501
        :rtype: int
        """
        return self._report_interval

    @report_interval.setter
    def report_interval(self, report_interval):
        """Sets the report_interval of this OperationCollectorGlobalConfig.

        Report interval for operation data in seconds.  # noqa: E501

        :param report_interval: The report_interval of this OperationCollectorGlobalConfig.  # noqa: E501
        :type: int
        """

        self._report_interval = report_interval

    @property
    def collectors(self):
        """Gets the collectors of this OperationCollectorGlobalConfig.  # noqa: E501

        Operation Collector Config.  # noqa: E501

        :return: The collectors of this OperationCollectorGlobalConfig.  # noqa: E501
        :rtype: list[OperationCollector]
        """
        return self._collectors

    @collectors.setter
    def collectors(self, collectors):
        """Sets the collectors of this OperationCollectorGlobalConfig.

        Operation Collector Config.  # noqa: E501

        :param collectors: The collectors of this OperationCollectorGlobalConfig.  # noqa: E501
        :type: list[OperationCollector]
        """

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
        if issubclass(OperationCollectorGlobalConfig, dict):
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
        if not isinstance(other, OperationCollectorGlobalConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
