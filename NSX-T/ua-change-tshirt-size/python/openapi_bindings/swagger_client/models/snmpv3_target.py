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

class Snmpv3Target(object):
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
        'security_level': 'str',
        'user_id': 'str',
        'port': 'int',
        'server': 'str'
    }

    attribute_map = {
        'security_level': 'security_level',
        'user_id': 'user_id',
        'port': 'port',
        'server': 'server'
    }

    def __init__(self, security_level='AUTH_PRIV', user_id=None, port=162, server=None):  # noqa: E501
        """Snmpv3Target - a model defined in Swagger"""  # noqa: E501
        self._security_level = None
        self._user_id = None
        self._port = None
        self._server = None
        self.discriminator = None
        if security_level is not None:
            self.security_level = security_level
        self.user_id = user_id
        if port is not None:
            self.port = port
        self.server = server

    @property
    def security_level(self):
        """Gets the security_level of this Snmpv3Target.  # noqa: E501

        Security level indicates whether SNMP communication involves authentication and privacy protocols for this user. Value \"AUTH_PRIV\" indicates both authentication and privacy protocols will be used for SNMP communication.  # noqa: E501

        :return: The security_level of this Snmpv3Target.  # noqa: E501
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """Sets the security_level of this Snmpv3Target.

        Security level indicates whether SNMP communication involves authentication and privacy protocols for this user. Value \"AUTH_PRIV\" indicates both authentication and privacy protocols will be used for SNMP communication.  # noqa: E501

        :param security_level: The security_level of this Snmpv3Target.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTH_PRIV"]  # noqa: E501
        if security_level not in allowed_values:
            raise ValueError(
                "Invalid value for `security_level` ({0}), must be one of {1}"  # noqa: E501
                .format(security_level, allowed_values)
            )

        self._security_level = security_level

    @property
    def user_id(self):
        """Gets the user_id of this Snmpv3Target.  # noqa: E501

        SNMP v3 user id used to notify target server. This SNMP v3 user should already be added in this profile.  # noqa: E501

        :return: The user_id of this Snmpv3Target.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Snmpv3Target.

        SNMP v3 user id used to notify target server. This SNMP v3 user should already be added in this profile.  # noqa: E501

        :param user_id: The user_id of this Snmpv3Target.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def port(self):
        """Gets the port of this Snmpv3Target.  # noqa: E501

        SNMP v3 target server's port.  # noqa: E501

        :return: The port of this Snmpv3Target.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Snmpv3Target.

        SNMP v3 target server's port.  # noqa: E501

        :param port: The port of this Snmpv3Target.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def server(self):
        """Gets the server of this Snmpv3Target.  # noqa: E501

        SNMP v3 target server's IP or FQDN.  # noqa: E501

        :return: The server of this Snmpv3Target.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this Snmpv3Target.

        SNMP v3 target server's IP or FQDN.  # noqa: E501

        :param server: The server of this Snmpv3Target.  # noqa: E501
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
        if issubclass(Snmpv3Target, dict):
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
        if not isinstance(other, Snmpv3Target):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other