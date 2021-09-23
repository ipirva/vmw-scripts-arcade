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

class LbServiceInstanceDetailPerStatus(object):
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
        'instance_number': 'int',
        'instance_details': 'list[LbServiceInstanceDetail]'
    }

    attribute_map = {
        'status': 'status',
        'instance_number': 'instance_number',
        'instance_details': 'instance_details'
    }

    def __init__(self, status=None, instance_number=None, instance_details=None):  # noqa: E501
        """LbServiceInstanceDetailPerStatus - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._instance_number = None
        self._instance_details = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if instance_number is not None:
            self.instance_number = instance_number
        if instance_details is not None:
            self.instance_details = instance_details

    @property
    def status(self):
        """Gets the status of this LbServiceInstanceDetailPerStatus.  # noqa: E501

        The type of load balancer instance status.   # noqa: E501

        :return: The status of this LbServiceInstanceDetailPerStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LbServiceInstanceDetailPerStatus.

        The type of load balancer instance status.   # noqa: E501

        :param status: The status of this LbServiceInstanceDetailPerStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["READY", "CONFLICT", "NOT_READY"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def instance_number(self):
        """Gets the instance_number of this LbServiceInstanceDetailPerStatus.  # noqa: E501

        It means the total number of instances in this status type for the given transport node.   # noqa: E501

        :return: The instance_number of this LbServiceInstanceDetailPerStatus.  # noqa: E501
        :rtype: int
        """
        return self._instance_number

    @instance_number.setter
    def instance_number(self, instance_number):
        """Sets the instance_number of this LbServiceInstanceDetailPerStatus.

        It means the total number of instances in this status type for the given transport node.   # noqa: E501

        :param instance_number: The instance_number of this LbServiceInstanceDetailPerStatus.  # noqa: E501
        :type: int
        """

        self._instance_number = instance_number

    @property
    def instance_details(self):
        """Gets the instance_details of this LbServiceInstanceDetailPerStatus.  # noqa: E501

        The detailed information of the load balancer instance. This field will be only returned on realtime status API.   # noqa: E501

        :return: The instance_details of this LbServiceInstanceDetailPerStatus.  # noqa: E501
        :rtype: list[LbServiceInstanceDetail]
        """
        return self._instance_details

    @instance_details.setter
    def instance_details(self, instance_details):
        """Sets the instance_details of this LbServiceInstanceDetailPerStatus.

        The detailed information of the load balancer instance. This field will be only returned on realtime status API.   # noqa: E501

        :param instance_details: The instance_details of this LbServiceInstanceDetailPerStatus.  # noqa: E501
        :type: list[LbServiceInstanceDetail]
        """

        self._instance_details = instance_details

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
        if issubclass(LbServiceInstanceDetailPerStatus, dict):
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
        if not isinstance(other, LbServiceInstanceDetailPerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
