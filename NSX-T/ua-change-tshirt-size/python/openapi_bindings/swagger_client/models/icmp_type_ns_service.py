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
from swagger_client.models.ns_service_element import NSServiceElement  # noqa: F401,E501

class ICMPTypeNSService(NSServiceElement):
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
        'icmp_code': 'int',
        'icmp_type': 'int',
        'protocol': 'str'
    }
    if hasattr(NSServiceElement, "swagger_types"):
        swagger_types.update(NSServiceElement.swagger_types)

    attribute_map = {
        'icmp_code': 'icmp_code',
        'icmp_type': 'icmp_type',
        'protocol': 'protocol'
    }
    if hasattr(NSServiceElement, "attribute_map"):
        attribute_map.update(NSServiceElement.attribute_map)

    def __init__(self, icmp_code=None, icmp_type=None, protocol=None, *args, **kwargs):  # noqa: E501
        """ICMPTypeNSService - a model defined in Swagger"""  # noqa: E501
        self._icmp_code = None
        self._icmp_type = None
        self._protocol = None
        self.discriminator = None
        if icmp_code is not None:
            self.icmp_code = icmp_code
        if icmp_type is not None:
            self.icmp_type = icmp_type
        self.protocol = protocol
        NSServiceElement.__init__(self, *args, **kwargs)

    @property
    def icmp_code(self):
        """Gets the icmp_code of this ICMPTypeNSService.  # noqa: E501

        ICMP message code  # noqa: E501

        :return: The icmp_code of this ICMPTypeNSService.  # noqa: E501
        :rtype: int
        """
        return self._icmp_code

    @icmp_code.setter
    def icmp_code(self, icmp_code):
        """Sets the icmp_code of this ICMPTypeNSService.

        ICMP message code  # noqa: E501

        :param icmp_code: The icmp_code of this ICMPTypeNSService.  # noqa: E501
        :type: int
        """

        self._icmp_code = icmp_code

    @property
    def icmp_type(self):
        """Gets the icmp_type of this ICMPTypeNSService.  # noqa: E501

        ICMP message type  # noqa: E501

        :return: The icmp_type of this ICMPTypeNSService.  # noqa: E501
        :rtype: int
        """
        return self._icmp_type

    @icmp_type.setter
    def icmp_type(self, icmp_type):
        """Sets the icmp_type of this ICMPTypeNSService.

        ICMP message type  # noqa: E501

        :param icmp_type: The icmp_type of this ICMPTypeNSService.  # noqa: E501
        :type: int
        """

        self._icmp_type = icmp_type

    @property
    def protocol(self):
        """Gets the protocol of this ICMPTypeNSService.  # noqa: E501

        ICMP protocol type  # noqa: E501

        :return: The protocol of this ICMPTypeNSService.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ICMPTypeNSService.

        ICMP protocol type  # noqa: E501

        :param protocol: The protocol of this ICMPTypeNSService.  # noqa: E501
        :type: str
        """
        if protocol is None:
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501
        allowed_values = ["ICMPv4", "ICMPv6"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

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
        if issubclass(ICMPTypeNSService, dict):
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
        if not isinstance(other, ICMPTypeNSService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
