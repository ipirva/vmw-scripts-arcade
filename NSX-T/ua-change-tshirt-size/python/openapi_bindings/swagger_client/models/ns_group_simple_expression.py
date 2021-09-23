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
from swagger_client.models.ns_group_expression import NSGroupExpression  # noqa: F401,E501

class NSGroupSimpleExpression(NSGroupExpression):
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
        'target_resource': 'ResourceReference',
        'target_property': 'str',
        'target_type': 'str',
        'value': 'str',
        'op': 'str'
    }
    if hasattr(NSGroupExpression, "swagger_types"):
        swagger_types.update(NSGroupExpression.swagger_types)

    attribute_map = {
        'target_resource': 'target_resource',
        'target_property': 'target_property',
        'target_type': 'target_type',
        'value': 'value',
        'op': 'op'
    }
    if hasattr(NSGroupExpression, "attribute_map"):
        attribute_map.update(NSGroupExpression.attribute_map)

    def __init__(self, target_resource=None, target_property=None, target_type=None, value=None, op=None, *args, **kwargs):  # noqa: E501
        """NSGroupSimpleExpression - a model defined in Swagger"""  # noqa: E501
        self._target_resource = None
        self._target_property = None
        self._target_type = None
        self._value = None
        self._op = None
        self.discriminator = None
        if target_resource is not None:
            self.target_resource = target_resource
        self.target_property = target_property
        self.target_type = target_type
        self.value = value
        self.op = op
        NSGroupExpression.__init__(self, *args, **kwargs)

    @property
    def target_resource(self):
        """Gets the target_resource of this NSGroupSimpleExpression.  # noqa: E501


        :return: The target_resource of this NSGroupSimpleExpression.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._target_resource

    @target_resource.setter
    def target_resource(self, target_resource):
        """Sets the target_resource of this NSGroupSimpleExpression.


        :param target_resource: The target_resource of this NSGroupSimpleExpression.  # noqa: E501
        :type: ResourceReference
        """

        self._target_resource = target_resource

    @property
    def target_property(self):
        """Gets the target_property of this NSGroupSimpleExpression.  # noqa: E501

        Field of the resource on which this expression is evaluated  # noqa: E501

        :return: The target_property of this NSGroupSimpleExpression.  # noqa: E501
        :rtype: str
        """
        return self._target_property

    @target_property.setter
    def target_property(self, target_property):
        """Sets the target_property of this NSGroupSimpleExpression.

        Field of the resource on which this expression is evaluated  # noqa: E501

        :param target_property: The target_property of this NSGroupSimpleExpression.  # noqa: E501
        :type: str
        """
        if target_property is None:
            raise ValueError("Invalid value for `target_property`, must not be `None`")  # noqa: E501

        self._target_property = target_property

    @property
    def target_type(self):
        """Gets the target_type of this NSGroupSimpleExpression.  # noqa: E501

        Type of the resource on which this expression is evaluated  # noqa: E501

        :return: The target_type of this NSGroupSimpleExpression.  # noqa: E501
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this NSGroupSimpleExpression.

        Type of the resource on which this expression is evaluated  # noqa: E501

        :param target_type: The target_type of this NSGroupSimpleExpression.  # noqa: E501
        :type: str
        """
        if target_type is None:
            raise ValueError("Invalid value for `target_type`, must not be `None`")  # noqa: E501
        allowed_values = ["NSGroup", "IPSet", "MACSet", "LogicalSwitch", "LogicalPort", "VirtualMachine", "DirectoryGroup", "VirtualNetworkInterface", "TransportNode", "CloudNativeServiceInstance", "PhysicalServer", "LogicalRouter", "LogicalRouterPort"]  # noqa: E501
        if target_type not in allowed_values:
            raise ValueError(
                "Invalid value for `target_type` ({0}), must be one of {1}"  # noqa: E501
                .format(target_type, allowed_values)
            )

        self._target_type = target_type

    @property
    def value(self):
        """Gets the value of this NSGroupSimpleExpression.  # noqa: E501

        Value that satisfies this expression  # noqa: E501

        :return: The value of this NSGroupSimpleExpression.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this NSGroupSimpleExpression.

        Value that satisfies this expression  # noqa: E501

        :param value: The value of this NSGroupSimpleExpression.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def op(self):
        """Gets the op of this NSGroupSimpleExpression.  # noqa: E501

        All operators perform a case insensitive match.   # noqa: E501

        :return: The op of this NSGroupSimpleExpression.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this NSGroupSimpleExpression.

        All operators perform a case insensitive match.   # noqa: E501

        :param op: The op of this NSGroupSimpleExpression.  # noqa: E501
        :type: str
        """
        if op is None:
            raise ValueError("Invalid value for `op`, must not be `None`")  # noqa: E501
        allowed_values = ["EQUALS", "CONTAINS", "STARTSWITH", "ENDSWITH", "NOTEQUALS"]  # noqa: E501
        if op not in allowed_values:
            raise ValueError(
                "Invalid value for `op` ({0}), must be one of {1}"  # noqa: E501
                .format(op, allowed_values)
            )

        self._op = op

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
        if issubclass(NSGroupSimpleExpression, dict):
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
        if not isinstance(other, NSGroupSimpleExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other