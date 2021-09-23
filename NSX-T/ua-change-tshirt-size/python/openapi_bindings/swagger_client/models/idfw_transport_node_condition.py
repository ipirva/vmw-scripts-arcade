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

class IdfwTransportNodeCondition(object):
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
        'status': 'str',
        'status_detail': 'str'
    }

    attribute_map = {
        'status': 'status',
        'status_detail': 'status_detail'
    }

    def __init__(self, status=None, status_detail=None):  # noqa: E501
        """IdfwTransportNodeCondition - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._status_detail = None
        self.discriminator = None
        self.status = status
        if status_detail is not None:
            self.status_detail = status_detail

    @property
    def status(self):
        """Gets the status of this IdfwTransportNodeCondition.  # noqa: E501

        Transport node status for IDFW compute collection.  # noqa: E501

        :return: The status of this IdfwTransportNodeCondition.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IdfwTransportNodeCondition.

        Transport node status for IDFW compute collection.  # noqa: E501

        :param status: The status of this IdfwTransportNodeCondition.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["UNKNOWN", "UP", "DOWN", "NOT_PREPARED", "IDFW_COMPONENT_NOT_INSTALLED", "DFW_DISABLED", "IDFW_DISABLED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_detail(self):
        """Gets the status_detail of this IdfwTransportNodeCondition.  # noqa: E501

        IDFW Compute collection's transport node condition.  # noqa: E501

        :return: The status_detail of this IdfwTransportNodeCondition.  # noqa: E501
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this IdfwTransportNodeCondition.

        IDFW Compute collection's transport node condition.  # noqa: E501

        :param status_detail: The status_detail of this IdfwTransportNodeCondition.  # noqa: E501
        :type: str
        """

        self._status_detail = status_detail

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
        if issubclass(IdfwTransportNodeCondition, dict):
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
        if not isinstance(other, IdfwTransportNodeCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
