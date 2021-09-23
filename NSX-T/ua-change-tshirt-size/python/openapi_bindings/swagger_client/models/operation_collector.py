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

class OperationCollector(object):
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
        'collector_port': 'int',
        'collector_type': 'str',
        'collector_ip': 'str'
    }

    attribute_map = {
        'collector_port': 'collector_port',
        'collector_type': 'collector_type',
        'collector_ip': 'collector_ip'
    }

    def __init__(self, collector_port=None, collector_type='VRNI', collector_ip=None):  # noqa: E501
        """OperationCollector - a model defined in Swagger"""  # noqa: E501
        self._collector_port = None
        self._collector_type = None
        self._collector_ip = None
        self.discriminator = None
        self.collector_port = collector_port
        if collector_type is not None:
            self.collector_type = collector_type
        self.collector_ip = collector_ip

    @property
    def collector_port(self):
        """Gets the collector_port of this OperationCollector.  # noqa: E501

        Port for the operation collector.  # noqa: E501

        :return: The collector_port of this OperationCollector.  # noqa: E501
        :rtype: int
        """
        return self._collector_port

    @collector_port.setter
    def collector_port(self, collector_port):
        """Sets the collector_port of this OperationCollector.

        Port for the operation collector.  # noqa: E501

        :param collector_port: The collector_port of this OperationCollector.  # noqa: E501
        :type: int
        """
        if collector_port is None:
            raise ValueError("Invalid value for `collector_port`, must not be `None`")  # noqa: E501

        self._collector_port = collector_port

    @property
    def collector_type(self):
        """Gets the collector_type of this OperationCollector.  # noqa: E501

        Define the operation collector type.  # noqa: E501

        :return: The collector_type of this OperationCollector.  # noqa: E501
        :rtype: str
        """
        return self._collector_type

    @collector_type.setter
    def collector_type(self, collector_type):
        """Sets the collector_type of this OperationCollector.

        Define the operation collector type.  # noqa: E501

        :param collector_type: The collector_type of this OperationCollector.  # noqa: E501
        :type: str
        """
        allowed_values = ["VRNI", "WAVE_FRONT"]  # noqa: E501
        if collector_type not in allowed_values:
            raise ValueError(
                "Invalid value for `collector_type` ({0}), must be one of {1}"  # noqa: E501
                .format(collector_type, allowed_values)
            )

        self._collector_type = collector_type

    @property
    def collector_ip(self):
        """Gets the collector_ip of this OperationCollector.  # noqa: E501

        IP address for the operation collector.  # noqa: E501

        :return: The collector_ip of this OperationCollector.  # noqa: E501
        :rtype: str
        """
        return self._collector_ip

    @collector_ip.setter
    def collector_ip(self, collector_ip):
        """Sets the collector_ip of this OperationCollector.

        IP address for the operation collector.  # noqa: E501

        :param collector_ip: The collector_ip of this OperationCollector.  # noqa: E501
        :type: str
        """
        if collector_ip is None:
            raise ValueError("Invalid value for `collector_ip`, must not be `None`")  # noqa: E501

        self._collector_ip = collector_ip

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
        if issubclass(OperationCollector, dict):
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
        if not isinstance(other, OperationCollector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
