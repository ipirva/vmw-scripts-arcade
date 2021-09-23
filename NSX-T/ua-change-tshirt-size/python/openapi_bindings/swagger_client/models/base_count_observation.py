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
from swagger_client.models.count_observation import CountObservation  # noqa: F401,E501

class BaseCountObservation(CountObservation):
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
        'count': 'int',
        'port_id': 'str',
        'checkpoint_type': 'str'
    }
    if hasattr(CountObservation, "swagger_types"):
        swagger_types.update(CountObservation.swagger_types)

    attribute_map = {
        'count': 'count',
        'port_id': 'port_id',
        'checkpoint_type': 'checkpoint_type'
    }
    if hasattr(CountObservation, "attribute_map"):
        attribute_map.update(CountObservation.attribute_map)

    def __init__(self, count=None, port_id=None, checkpoint_type=None, *args, **kwargs):  # noqa: E501
        """BaseCountObservation - a model defined in Swagger"""  # noqa: E501
        self._count = None
        self._port_id = None
        self._checkpoint_type = None
        self.discriminator = None
        if count is not None:
            self.count = count
        if port_id is not None:
            self.port_id = port_id
        if checkpoint_type is not None:
            self.checkpoint_type = checkpoint_type
        CountObservation.__init__(self, *args, **kwargs)

    @property
    def count(self):
        """Gets the count of this BaseCountObservation.  # noqa: E501

        Packet count  # noqa: E501

        :return: The count of this BaseCountObservation.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BaseCountObservation.

        Packet count  # noqa: E501

        :param count: The count of this BaseCountObservation.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def port_id(self):
        """Gets the port_id of this BaseCountObservation.  # noqa: E501

        Port ID, which is either a logical port ID or an uplink name  # noqa: E501

        :return: The port_id of this BaseCountObservation.  # noqa: E501
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this BaseCountObservation.

        Port ID, which is either a logical port ID or an uplink name  # noqa: E501

        :param port_id: The port_id of this BaseCountObservation.  # noqa: E501
        :type: str
        """

        self._port_id = port_id

    @property
    def checkpoint_type(self):
        """Gets the checkpoint_type of this BaseCountObservation.  # noqa: E501

        Type of checkpoint  # noqa: E501

        :return: The checkpoint_type of this BaseCountObservation.  # noqa: E501
        :rtype: str
        """
        return self._checkpoint_type

    @checkpoint_type.setter
    def checkpoint_type(self, checkpoint_type):
        """Sets the checkpoint_type of this BaseCountObservation.

        Type of checkpoint  # noqa: E501

        :param checkpoint_type: The checkpoint_type of this BaseCountObservation.  # noqa: E501
        :type: str
        """

        self._checkpoint_type = checkpoint_type

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
        if issubclass(BaseCountObservation, dict):
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
        if not isinstance(other, BaseCountObservation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
