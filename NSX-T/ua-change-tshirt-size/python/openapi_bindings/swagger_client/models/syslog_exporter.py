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

class SyslogExporter(object):
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
        'max_log_level': 'str',
        'protocol': 'str',
        'port': 'int',
        'server': 'str'
    }

    attribute_map = {
        'max_log_level': 'max_log_level',
        'protocol': 'protocol',
        'port': 'port',
        'server': 'server'
    }

    def __init__(self, max_log_level=None, protocol=None, port=514, server=None):  # noqa: E501
        """SyslogExporter - a model defined in Swagger"""  # noqa: E501
        self._max_log_level = None
        self._protocol = None
        self._port = None
        self._server = None
        self.discriminator = None
        self.max_log_level = max_log_level
        self.protocol = protocol
        if port is not None:
            self.port = port
        self.server = server

    @property
    def max_log_level(self):
        """Gets the max_log_level of this SyslogExporter.  # noqa: E501

        Maximum logging level for messages to be exported.  # noqa: E501

        :return: The max_log_level of this SyslogExporter.  # noqa: E501
        :rtype: str
        """
        return self._max_log_level

    @max_log_level.setter
    def max_log_level(self, max_log_level):
        """Sets the max_log_level of this SyslogExporter.

        Maximum logging level for messages to be exported.  # noqa: E501

        :param max_log_level: The max_log_level of this SyslogExporter.  # noqa: E501
        :type: str
        """
        if max_log_level is None:
            raise ValueError("Invalid value for `max_log_level`, must not be `None`")  # noqa: E501
        allowed_values = ["EMERG", "ALERT", "CRIT", "ERR", "WARNING", "NOTICE", "INFO", "DEBUG"]  # noqa: E501
        if max_log_level not in allowed_values:
            raise ValueError(
                "Invalid value for `max_log_level` ({0}), must be one of {1}"  # noqa: E501
                .format(max_log_level, allowed_values)
            )

        self._max_log_level = max_log_level

    @property
    def protocol(self):
        """Gets the protocol of this SyslogExporter.  # noqa: E501

        Protocol to be used to export logs to syslog server.  # noqa: E501

        :return: The protocol of this SyslogExporter.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SyslogExporter.

        Protocol to be used to export logs to syslog server.  # noqa: E501

        :param protocol: The protocol of this SyslogExporter.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501
        allowed_values = ["TCP", "UDP", "LI"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def port(self):
        """Gets the port of this SyslogExporter.  # noqa: E501

        Server port on which syslog listener is listening.  # noqa: E501

        :return: The port of this SyslogExporter.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SyslogExporter.

        Server port on which syslog listener is listening.  # noqa: E501

        :param port: The port of this SyslogExporter.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def server(self):
        """Gets the server of this SyslogExporter.  # noqa: E501

        Syslog server IP address or hostname.  # noqa: E501

        :return: The server of this SyslogExporter.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this SyslogExporter.

        Syslog server IP address or hostname.  # noqa: E501

        :param server: The server of this SyslogExporter.  # noqa: E501
        :type: str
        """
        if server is None:
            raise ValueError("Invalid value for `server`, must not be `None`")  # noqa: E501

        self._server = server

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
        if issubclass(SyslogExporter, dict):
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
        if not isinstance(other, SyslogExporter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other