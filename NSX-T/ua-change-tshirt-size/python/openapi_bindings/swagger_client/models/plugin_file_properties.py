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

class PluginFileProperties(Resource):
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
        'file_name': 'str',
        'plugin_id': 'str'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        'status': 'status',
        'file_name': 'file_name',
        'plugin_id': 'plugin_id'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, status=None, file_name=None, plugin_id=None, *args, **kwargs):  # noqa: E501
        """PluginFileProperties - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._file_name = None
        self._plugin_id = None
        self.discriminator = None
        self.status = status
        self.file_name = file_name
        self.plugin_id = plugin_id
        Resource.__init__(self, *args, **kwargs)

    @property
    def status(self):
        """Gets the status of this PluginFileProperties.  # noqa: E501

        Upload status  # noqa: E501

        :return: The status of this PluginFileProperties.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PluginFileProperties.

        Upload status  # noqa: E501

        :param status: The status of this PluginFileProperties.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def file_name(self):
        """Gets the file_name of this PluginFileProperties.  # noqa: E501

        File name  # noqa: E501

        :return: The file_name of this PluginFileProperties.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this PluginFileProperties.

        File name  # noqa: E501

        :param file_name: The file_name of this PluginFileProperties.  # noqa: E501
        :type: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def plugin_id(self):
        """Gets the plugin_id of this PluginFileProperties.  # noqa: E501

        Plugin id  # noqa: E501

        :return: The plugin_id of this PluginFileProperties.  # noqa: E501
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this PluginFileProperties.

        Plugin id  # noqa: E501

        :param plugin_id: The plugin_id of this PluginFileProperties.  # noqa: E501
        :type: str
        """
        if plugin_id is None:
            raise ValueError("Invalid value for `plugin_id`, must not be `None`")  # noqa: E501

        self._plugin_id = plugin_id

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
        if issubclass(PluginFileProperties, dict):
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
        if not isinstance(other, PluginFileProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other