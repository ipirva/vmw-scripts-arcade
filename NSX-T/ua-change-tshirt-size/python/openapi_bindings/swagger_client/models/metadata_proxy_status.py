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

class MetadataProxyStatus(object):
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
        'proxy_status': 'str',
        'error_message': 'str',
        'transport_nodes': 'list[str]'
    }

    attribute_map = {
        'proxy_status': 'proxy_status',
        'error_message': 'error_message',
        'transport_nodes': 'transport_nodes'
    }

    def __init__(self, proxy_status=None, error_message=None, transport_nodes=None):  # noqa: E501
        """MetadataProxyStatus - a model defined in Swagger"""  # noqa: E501
        self._proxy_status = None
        self._error_message = None
        self._transport_nodes = None
        self.discriminator = None
        self.proxy_status = proxy_status
        if error_message is not None:
            self.error_message = error_message
        self.transport_nodes = transport_nodes

    @property
    def proxy_status(self):
        """Gets the proxy_status of this MetadataProxyStatus.  # noqa: E501

        UP means the metadata proxy is working fine on both transport-nodes(if have); DOWN means the metadata proxy is is down on both transport-nodes(if have), hence the metadata proxy will not repsonse any metadata request; Error means error happens on transport-node(s) or no status is reported from transport-node(s). The metadata proxy may be working (or not working); NO_BACK means metadata proxy is working in one of the transport node while not in the other transport-node (if have). Hence if the metadata proxy in the working transport-node goes down, the metadata proxy will go down.   # noqa: E501

        :return: The proxy_status of this MetadataProxyStatus.  # noqa: E501
        :rtype: str
        """
        return self._proxy_status

    @proxy_status.setter
    def proxy_status(self, proxy_status):
        """Sets the proxy_status of this MetadataProxyStatus.

        UP means the metadata proxy is working fine on both transport-nodes(if have); DOWN means the metadata proxy is is down on both transport-nodes(if have), hence the metadata proxy will not repsonse any metadata request; Error means error happens on transport-node(s) or no status is reported from transport-node(s). The metadata proxy may be working (or not working); NO_BACK means metadata proxy is working in one of the transport node while not in the other transport-node (if have). Hence if the metadata proxy in the working transport-node goes down, the metadata proxy will go down.   # noqa: E501

        :param proxy_status: The proxy_status of this MetadataProxyStatus.  # noqa: E501
        :type: str
        """
        if proxy_status is None:
            raise ValueError("Invalid value for `proxy_status`, must not be `None`")  # noqa: E501
        allowed_values = ["UP", "DOWN", "ERROR", "NO_BACKUP"]  # noqa: E501
        if proxy_status not in allowed_values:
            raise ValueError(
                "Invalid value for `proxy_status` ({0}), must be one of {1}"  # noqa: E501
                .format(proxy_status, allowed_values)
            )

        self._proxy_status = proxy_status

    @property
    def error_message(self):
        """Gets the error_message of this MetadataProxyStatus.  # noqa: E501

        Error message, if available  # noqa: E501

        :return: The error_message of this MetadataProxyStatus.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this MetadataProxyStatus.

        Error message, if available  # noqa: E501

        :param error_message: The error_message of this MetadataProxyStatus.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def transport_nodes(self):
        """Gets the transport_nodes of this MetadataProxyStatus.  # noqa: E501

        Order of the transport nodes is insensitive because Metadata Proxy is running in Active-Active mode among target transport nodes.   # noqa: E501

        :return: The transport_nodes of this MetadataProxyStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._transport_nodes

    @transport_nodes.setter
    def transport_nodes(self, transport_nodes):
        """Sets the transport_nodes of this MetadataProxyStatus.

        Order of the transport nodes is insensitive because Metadata Proxy is running in Active-Active mode among target transport nodes.   # noqa: E501

        :param transport_nodes: The transport_nodes of this MetadataProxyStatus.  # noqa: E501
        :type: list[str]
        """
        if transport_nodes is None:
            raise ValueError("Invalid value for `transport_nodes`, must not be `None`")  # noqa: E501

        self._transport_nodes = transport_nodes

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
        if issubclass(MetadataProxyStatus, dict):
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
        if not isinstance(other, MetadataProxyStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
