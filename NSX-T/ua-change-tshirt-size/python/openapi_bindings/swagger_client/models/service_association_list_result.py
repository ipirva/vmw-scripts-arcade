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
from swagger_client.models.list_result import ListResult  # noqa: F401,E501

class ServiceAssociationListResult(ListResult):
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
        'service_type': 'str'
    }
    if hasattr(ListResult, "swagger_types"):
        swagger_types.update(ListResult.swagger_types)

    attribute_map = {
        'service_type': 'service_type'
    }
    if hasattr(ListResult, "attribute_map"):
        attribute_map.update(ListResult.attribute_map)

    discriminator_value_class_map = {
          'IpfixServiceAssociationListResult': 'IpfixServiceAssociationListResult',
'FireWallServiceAssociationListResult': 'FireWallServiceAssociationListResult'    }

    def __init__(self, service_type=None, *args, **kwargs):  # noqa: E501
        """ServiceAssociationListResult - a model defined in Swagger"""  # noqa: E501
        self._service_type = None
        self.discriminator = 'service_type'
        self.service_type = service_type
        ListResult.__init__(self, *args, **kwargs)

    @property
    def service_type(self):
        """Gets the service_type of this ServiceAssociationListResult.  # noqa: E501


        :return: The service_type of this ServiceAssociationListResult.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this ServiceAssociationListResult.


        :param service_type: The service_type of this ServiceAssociationListResult.  # noqa: E501
        :type: str
        """
        if service_type is None:
            raise ValueError("Invalid value for `service_type`, must not be `None`")  # noqa: E501
        allowed_values = ["FireWallServiceAssociationListResult", "IpfixServiceAssociationListResult"]  # noqa: E501
        if service_type not in allowed_values:
            raise ValueError(
                "Invalid value for `service_type` ({0}), must be one of {1}"  # noqa: E501
                .format(service_type, allowed_values)
            )

        self._service_type = service_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(ServiceAssociationListResult, dict):
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
        if not isinstance(other, ServiceAssociationListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other