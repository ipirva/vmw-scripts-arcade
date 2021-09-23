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
from swagger_client.models.lb_active_monitor import LbActiveMonitor  # noqa: F401,E501

class LbUdpMonitor(LbActiveMonitor):
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
        'receive': 'str',
        'send': 'str'
    }
    if hasattr(LbActiveMonitor, "swagger_types"):
        swagger_types.update(LbActiveMonitor.swagger_types)

    attribute_map = {
        'receive': 'receive',
        'send': 'send'
    }
    if hasattr(LbActiveMonitor, "attribute_map"):
        attribute_map.update(LbActiveMonitor.attribute_map)

    def __init__(self, receive=None, send=None, *args, **kwargs):  # noqa: E501
        """LbUdpMonitor - a model defined in Swagger"""  # noqa: E501
        self._receive = None
        self._send = None
        self.discriminator = None
        self.receive = receive
        self.send = send
        LbActiveMonitor.__init__(self, *args, **kwargs)

    @property
    def receive(self):
        """Gets the receive of this LbUdpMonitor.  # noqa: E501

        Expected data, can be anywhere in the response and it has to be a string, regular expressions are not supported. UDP healthcheck is considered failed if there is no server response within the timeout period.   # noqa: E501

        :return: The receive of this LbUdpMonitor.  # noqa: E501
        :rtype: str
        """
        return self._receive

    @receive.setter
    def receive(self, receive):
        """Sets the receive of this LbUdpMonitor.

        Expected data, can be anywhere in the response and it has to be a string, regular expressions are not supported. UDP healthcheck is considered failed if there is no server response within the timeout period.   # noqa: E501

        :param receive: The receive of this LbUdpMonitor.  # noqa: E501
        :type: str
        """
        if receive is None:
            raise ValueError("Invalid value for `receive`, must not be `None`")  # noqa: E501

        self._receive = receive

    @property
    def send(self):
        """Gets the send of this LbUdpMonitor.  # noqa: E501

        The data to be sent to the monitored server.   # noqa: E501

        :return: The send of this LbUdpMonitor.  # noqa: E501
        :rtype: str
        """
        return self._send

    @send.setter
    def send(self, send):
        """Sets the send of this LbUdpMonitor.

        The data to be sent to the monitored server.   # noqa: E501

        :param send: The send of this LbUdpMonitor.  # noqa: E501
        :type: str
        """
        if send is None:
            raise ValueError("Invalid value for `send`, must not be `None`")  # noqa: E501

        self._send = send

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
        if issubclass(LbUdpMonitor, dict):
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
        if not isinstance(other, LbUdpMonitor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other