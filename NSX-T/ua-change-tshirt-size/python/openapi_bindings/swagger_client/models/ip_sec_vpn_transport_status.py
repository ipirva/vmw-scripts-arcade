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
from swagger_client.models.l2_vpn_transport_tunnel_status import L2VPNTransportTunnelStatus  # noqa: F401,E501

class IPSecVPNTransportStatus(L2VPNTransportTunnelStatus):
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
        'status': 'IPSecVPNSessionStatus'
    }
    if hasattr(L2VPNTransportTunnelStatus, "swagger_types"):
        swagger_types.update(L2VPNTransportTunnelStatus.swagger_types)

    attribute_map = {
        'status': 'status'
    }
    if hasattr(L2VPNTransportTunnelStatus, "attribute_map"):
        attribute_map.update(L2VPNTransportTunnelStatus.attribute_map)

    def __init__(self, status=None, *args, **kwargs):  # noqa: E501
        """IPSecVPNTransportStatus - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self.discriminator = None
        if status is not None:
            self.status = status
        L2VPNTransportTunnelStatus.__init__(self, *args, **kwargs)

    @property
    def status(self):
        """Gets the status of this IPSecVPNTransportStatus.  # noqa: E501


        :return: The status of this IPSecVPNTransportStatus.  # noqa: E501
        :rtype: IPSecVPNSessionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IPSecVPNTransportStatus.


        :param status: The status of this IPSecVPNTransportStatus.  # noqa: E501
        :type: IPSecVPNSessionStatus
        """

        self._status = status

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
        if issubclass(IPSecVPNTransportStatus, dict):
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
        if not isinstance(other, IPSecVPNTransportStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
