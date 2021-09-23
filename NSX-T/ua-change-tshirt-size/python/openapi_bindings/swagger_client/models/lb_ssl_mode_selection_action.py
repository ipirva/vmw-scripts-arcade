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
from swagger_client.models.lb_rule_action import LbRuleAction  # noqa: F401,E501

class LbSslModeSelectionAction(LbRuleAction):
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
        'ssl_mode': 'str'
    }
    if hasattr(LbRuleAction, "swagger_types"):
        swagger_types.update(LbRuleAction.swagger_types)

    attribute_map = {
        'ssl_mode': 'ssl_mode'
    }
    if hasattr(LbRuleAction, "attribute_map"):
        attribute_map.update(LbRuleAction.attribute_map)

    def __init__(self, ssl_mode=None, *args, **kwargs):  # noqa: E501
        """LbSslModeSelectionAction - a model defined in Swagger"""  # noqa: E501
        self._ssl_mode = None
        self.discriminator = None
        self.ssl_mode = ssl_mode
        LbRuleAction.__init__(self, *args, **kwargs)

    @property
    def ssl_mode(self):
        """Gets the ssl_mode of this LbSslModeSelectionAction.  # noqa: E501

        SSL Passthrough: LB establishes a TCP connection with client and another connection with selected backend server. LB won't inspect the stream data between client and backend server, but just pass it through. Backend server exchanges SSL connection with client. SSL Offloading: LB terminiates the connections from client, and establishes SSL connection with it. After receiving the HTTP request, LB connects the selected backend server and talk with it via HTTP without SSL. LB estalishes new connection to selected backend server for each HTTP request, in case server_keep_alive or multiplexing are NOT configured. SSL End-to-End: LB terminiates the connections from client, and establishes SSL connection with it. After receiving the HTTP request, LB connects the selected backend server and talk with it via HTTPS. LB estalishes new SSL connection to selected backend server for each HTTP request, in case server_keep_alive or multiplexing are NOT configured.   # noqa: E501

        :return: The ssl_mode of this LbSslModeSelectionAction.  # noqa: E501
        :rtype: str
        """
        return self._ssl_mode

    @ssl_mode.setter
    def ssl_mode(self, ssl_mode):
        """Sets the ssl_mode of this LbSslModeSelectionAction.

        SSL Passthrough: LB establishes a TCP connection with client and another connection with selected backend server. LB won't inspect the stream data between client and backend server, but just pass it through. Backend server exchanges SSL connection with client. SSL Offloading: LB terminiates the connections from client, and establishes SSL connection with it. After receiving the HTTP request, LB connects the selected backend server and talk with it via HTTP without SSL. LB estalishes new connection to selected backend server for each HTTP request, in case server_keep_alive or multiplexing are NOT configured. SSL End-to-End: LB terminiates the connections from client, and establishes SSL connection with it. After receiving the HTTP request, LB connects the selected backend server and talk with it via HTTPS. LB estalishes new SSL connection to selected backend server for each HTTP request, in case server_keep_alive or multiplexing are NOT configured.   # noqa: E501

        :param ssl_mode: The ssl_mode of this LbSslModeSelectionAction.  # noqa: E501
        :type: str
        """
        if ssl_mode is None:
            raise ValueError("Invalid value for `ssl_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["SSL_PASSTHROUGH", "SSL_END_TO_END", "SSL_OFFLOAD"]  # noqa: E501
        if ssl_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `ssl_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(ssl_mode, allowed_values)
            )

        self._ssl_mode = ssl_mode

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
        if issubclass(LbSslModeSelectionAction, dict):
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
        if not isinstance(other, LbSslModeSelectionAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
