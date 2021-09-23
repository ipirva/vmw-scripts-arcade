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

class ServicePath(object):
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
        'reverse_path': 'UnidirectionalServicePath',
        'service_chain_uuid': 'str',
        'forward_path': 'UnidirectionalServicePath',
        'service_path_id': 'int',
        'service_chain_id': 'int'
    }

    attribute_map = {
        'reverse_path': 'reverse_path',
        'service_chain_uuid': 'service_chain_uuid',
        'forward_path': 'forward_path',
        'service_path_id': 'service_path_id',
        'service_chain_id': 'service_chain_id'
    }

    def __init__(self, reverse_path=None, service_chain_uuid=None, forward_path=None, service_path_id=None, service_chain_id=None):  # noqa: E501
        """ServicePath - a model defined in Swagger"""  # noqa: E501
        self._reverse_path = None
        self._service_chain_uuid = None
        self._forward_path = None
        self._service_path_id = None
        self._service_chain_id = None
        self.discriminator = None
        if reverse_path is not None:
            self.reverse_path = reverse_path
        if service_chain_uuid is not None:
            self.service_chain_uuid = service_chain_uuid
        if forward_path is not None:
            self.forward_path = forward_path
        if service_path_id is not None:
            self.service_path_id = service_path_id
        if service_chain_id is not None:
            self.service_chain_id = service_chain_id

    @property
    def reverse_path(self):
        """Gets the reverse_path of this ServicePath.  # noqa: E501


        :return: The reverse_path of this ServicePath.  # noqa: E501
        :rtype: UnidirectionalServicePath
        """
        return self._reverse_path

    @reverse_path.setter
    def reverse_path(self, reverse_path):
        """Sets the reverse_path of this ServicePath.


        :param reverse_path: The reverse_path of this ServicePath.  # noqa: E501
        :type: UnidirectionalServicePath
        """

        self._reverse_path = reverse_path

    @property
    def service_chain_uuid(self):
        """Gets the service_chain_uuid of this ServicePath.  # noqa: E501

        Uuid of a service chain.  # noqa: E501

        :return: The service_chain_uuid of this ServicePath.  # noqa: E501
        :rtype: str
        """
        return self._service_chain_uuid

    @service_chain_uuid.setter
    def service_chain_uuid(self, service_chain_uuid):
        """Sets the service_chain_uuid of this ServicePath.

        Uuid of a service chain.  # noqa: E501

        :param service_chain_uuid: The service_chain_uuid of this ServicePath.  # noqa: E501
        :type: str
        """

        self._service_chain_uuid = service_chain_uuid

    @property
    def forward_path(self):
        """Gets the forward_path of this ServicePath.  # noqa: E501


        :return: The forward_path of this ServicePath.  # noqa: E501
        :rtype: UnidirectionalServicePath
        """
        return self._forward_path

    @forward_path.setter
    def forward_path(self, forward_path):
        """Sets the forward_path of this ServicePath.


        :param forward_path: The forward_path of this ServicePath.  # noqa: E501
        :type: UnidirectionalServicePath
        """

        self._forward_path = forward_path

    @property
    def service_path_id(self):
        """Gets the service_path_id of this ServicePath.  # noqa: E501

        Unique identifier of a service path.  # noqa: E501

        :return: The service_path_id of this ServicePath.  # noqa: E501
        :rtype: int
        """
        return self._service_path_id

    @service_path_id.setter
    def service_path_id(self, service_path_id):
        """Sets the service_path_id of this ServicePath.

        Unique identifier of a service path.  # noqa: E501

        :param service_path_id: The service_path_id of this ServicePath.  # noqa: E501
        :type: int
        """

        self._service_path_id = service_path_id

    @property
    def service_chain_id(self):
        """Gets the service_chain_id of this ServicePath.  # noqa: E501

        A unique id of a service chain.  # noqa: E501

        :return: The service_chain_id of this ServicePath.  # noqa: E501
        :rtype: int
        """
        return self._service_chain_id

    @service_chain_id.setter
    def service_chain_id(self, service_chain_id):
        """Sets the service_chain_id of this ServicePath.

        A unique id of a service chain.  # noqa: E501

        :param service_chain_id: The service_chain_id of this ServicePath.  # noqa: E501
        :type: int
        """

        self._service_chain_id = service_chain_id

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
        if issubclass(ServicePath, dict):
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
        if not isinstance(other, ServicePath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other