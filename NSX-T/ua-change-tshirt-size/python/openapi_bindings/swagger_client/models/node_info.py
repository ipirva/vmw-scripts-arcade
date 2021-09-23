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
from swagger_client.models.resource import Resource  # noqa: F401,E501

class NodeInfo(Resource):
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
        'type': 'str',
        'display_name': 'str',
        'id': 'str',
        'component_version': 'str'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        'type': 'type',
        'display_name': 'display_name',
        'id': 'id',
        'component_version': 'component_version'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, type=None, display_name=None, id=None, component_version=None, *args, **kwargs):  # noqa: E501
        """NodeInfo - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._display_name = None
        self._id = None
        self._component_version = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if component_version is not None:
            self.component_version = component_version
        Resource.__init__(self, *args, **kwargs)

    @property
    def type(self):
        """Gets the type of this NodeInfo.  # noqa: E501

        Node type  # noqa: E501

        :return: The type of this NodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodeInfo.

        Node type  # noqa: E501

        :param type: The type of this NodeInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def display_name(self):
        """Gets the display_name of this NodeInfo.  # noqa: E501

        Name of the node  # noqa: E501

        :return: The display_name of this NodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this NodeInfo.

        Name of the node  # noqa: E501

        :param display_name: The display_name of this NodeInfo.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this NodeInfo.  # noqa: E501

        Identifier of the node  # noqa: E501

        :return: The id of this NodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeInfo.

        Identifier of the node  # noqa: E501

        :param id: The id of this NodeInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def component_version(self):
        """Gets the component_version of this NodeInfo.  # noqa: E501

        Component version of the node  # noqa: E501

        :return: The component_version of this NodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._component_version

    @component_version.setter
    def component_version(self, component_version):
        """Sets the component_version of this NodeInfo.

        Component version of the node  # noqa: E501

        :param component_version: The component_version of this NodeInfo.  # noqa: E501
        :type: str
        """

        self._component_version = component_version

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
        if issubclass(NodeInfo, dict):
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
        if not isinstance(other, NodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other