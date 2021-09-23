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
from swagger_client.models.discovered_resource import DiscoveredResource  # noqa: F401,E501

class CloudNativeServiceInstance(DiscoveredResource):
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
        'service_type': 'str',
        'source': 'ResourceReference',
        'external_id': 'str'
    }
    if hasattr(DiscoveredResource, "swagger_types"):
        swagger_types.update(DiscoveredResource.swagger_types)

    attribute_map = {
        'service_type': 'service_type',
        'source': 'source',
        'external_id': 'external_id'
    }
    if hasattr(DiscoveredResource, "attribute_map"):
        attribute_map.update(DiscoveredResource.attribute_map)

    def __init__(self, service_type=None, source=None, external_id=None, *args, **kwargs):  # noqa: E501
        """CloudNativeServiceInstance - a model defined in Swagger"""  # noqa: E501
        self._service_type = None
        self._source = None
        self._external_id = None
        self.discriminator = None
        if service_type is not None:
            self.service_type = service_type
        if source is not None:
            self.source = source
        if external_id is not None:
            self.external_id = external_id
        DiscoveredResource.__init__(self, *args, **kwargs)

    @property
    def service_type(self):
        """Gets the service_type of this CloudNativeServiceInstance.  # noqa: E501

        Type of cloud native service.  # noqa: E501

        :return: The service_type of this CloudNativeServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this CloudNativeServiceInstance.

        Type of cloud native service.  # noqa: E501

        :param service_type: The service_type of this CloudNativeServiceInstance.  # noqa: E501
        :type: str
        """

        self._service_type = service_type

    @property
    def source(self):
        """Gets the source of this CloudNativeServiceInstance.  # noqa: E501


        :return: The source of this CloudNativeServiceInstance.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CloudNativeServiceInstance.


        :param source: The source of this CloudNativeServiceInstance.  # noqa: E501
        :type: ResourceReference
        """

        self._source = source

    @property
    def external_id(self):
        """Gets the external_id of this CloudNativeServiceInstance.  # noqa: E501

        Id of service instance fetched from public cloud.   # noqa: E501

        :return: The external_id of this CloudNativeServiceInstance.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CloudNativeServiceInstance.

        Id of service instance fetched from public cloud.   # noqa: E501

        :param external_id: The external_id of this CloudNativeServiceInstance.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

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
        if issubclass(CloudNativeServiceInstance, dict):
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
        if not isinstance(other, CloudNativeServiceInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
