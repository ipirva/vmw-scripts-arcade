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

class SIDataCounter(object):
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
        'total': 'int',
        'multicast_broadcast': 'int',
        'dropped': 'int'
    }

    attribute_map = {
        'total': 'total',
        'multicast_broadcast': 'multicast_broadcast',
        'dropped': 'dropped'
    }

    def __init__(self, total=None, multicast_broadcast=None, dropped=None):  # noqa: E501
        """SIDataCounter - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._multicast_broadcast = None
        self._dropped = None
        self.discriminator = None
        self.total = total
        if multicast_broadcast is not None:
            self.multicast_broadcast = multicast_broadcast
        if dropped is not None:
            self.dropped = dropped

    @property
    def total(self):
        """Gets the total of this SIDataCounter.  # noqa: E501

        The total packets or bytes  # noqa: E501

        :return: The total of this SIDataCounter.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SIDataCounter.

        The total packets or bytes  # noqa: E501

        :param total: The total of this SIDataCounter.  # noqa: E501
        :type: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def multicast_broadcast(self):
        """Gets the multicast_broadcast of this SIDataCounter.  # noqa: E501

        The multicast and broadcast packets or bytes  # noqa: E501

        :return: The multicast_broadcast of this SIDataCounter.  # noqa: E501
        :rtype: int
        """
        return self._multicast_broadcast

    @multicast_broadcast.setter
    def multicast_broadcast(self, multicast_broadcast):
        """Sets the multicast_broadcast of this SIDataCounter.

        The multicast and broadcast packets or bytes  # noqa: E501

        :param multicast_broadcast: The multicast_broadcast of this SIDataCounter.  # noqa: E501
        :type: int
        """

        self._multicast_broadcast = multicast_broadcast

    @property
    def dropped(self):
        """Gets the dropped of this SIDataCounter.  # noqa: E501

        The dropped packets or bytes  # noqa: E501

        :return: The dropped of this SIDataCounter.  # noqa: E501
        :rtype: int
        """
        return self._dropped

    @dropped.setter
    def dropped(self, dropped):
        """Sets the dropped of this SIDataCounter.

        The dropped packets or bytes  # noqa: E501

        :param dropped: The dropped of this SIDataCounter.  # noqa: E501
        :type: int
        """

        self._dropped = dropped

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
        if issubclass(SIDataCounter, dict):
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
        if not isinstance(other, SIDataCounter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
