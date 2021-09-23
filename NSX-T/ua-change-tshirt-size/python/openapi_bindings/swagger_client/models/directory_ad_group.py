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
from swagger_client.models.directory_group import DirectoryGroup  # noqa: F401,E501

class DirectoryAdGroup(DirectoryGroup):
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
        'object_guid': 'str',
        'secure_id': 'str'
    }
    if hasattr(DirectoryGroup, "swagger_types"):
        swagger_types.update(DirectoryGroup.swagger_types)

    attribute_map = {
        'object_guid': 'object_guid',
        'secure_id': 'secure_id'
    }
    if hasattr(DirectoryGroup, "attribute_map"):
        attribute_map.update(DirectoryGroup.attribute_map)

    def __init__(self, object_guid=None, secure_id=None, *args, **kwargs):  # noqa: E501
        """DirectoryAdGroup - a model defined in Swagger"""  # noqa: E501
        self._object_guid = None
        self._secure_id = None
        self.discriminator = None
        self.object_guid = object_guid
        self.secure_id = secure_id
        DirectoryGroup.__init__(self, *args, **kwargs)

    @property
    def object_guid(self):
        """Gets the object_guid of this DirectoryAdGroup.  # noqa: E501

        GUID is a 128-bit value that is unique not only in the enterprise but also across the world. GUIDs are assigned to every object created by Active Directory, not just User and Group objects.  # noqa: E501

        :return: The object_guid of this DirectoryAdGroup.  # noqa: E501
        :rtype: str
        """
        return self._object_guid

    @object_guid.setter
    def object_guid(self, object_guid):
        """Sets the object_guid of this DirectoryAdGroup.

        GUID is a 128-bit value that is unique not only in the enterprise but also across the world. GUIDs are assigned to every object created by Active Directory, not just User and Group objects.  # noqa: E501

        :param object_guid: The object_guid of this DirectoryAdGroup.  # noqa: E501
        :type: str
        """
        if object_guid is None:
            raise ValueError("Invalid value for `object_guid`, must not be `None`")  # noqa: E501

        self._object_guid = object_guid

    @property
    def secure_id(self):
        """Gets the secure_id of this DirectoryAdGroup.  # noqa: E501

        A security identifier (SID) is a unique value of variable length used to identify a trustee. A SID consists of the following components - The revision level of the SID structure; A 48-bit identifier authority value that identifies the authority that issued the SID; A variable number of subauthority or relative identifier (RID) values that uniquely identify the trustee relative to the authority that issued the SID.  # noqa: E501

        :return: The secure_id of this DirectoryAdGroup.  # noqa: E501
        :rtype: str
        """
        return self._secure_id

    @secure_id.setter
    def secure_id(self, secure_id):
        """Sets the secure_id of this DirectoryAdGroup.

        A security identifier (SID) is a unique value of variable length used to identify a trustee. A SID consists of the following components - The revision level of the SID structure; A 48-bit identifier authority value that identifies the authority that issued the SID; A variable number of subauthority or relative identifier (RID) values that uniquely identify the trustee relative to the authority that issued the SID.  # noqa: E501

        :param secure_id: The secure_id of this DirectoryAdGroup.  # noqa: E501
        :type: str
        """
        if secure_id is None:
            raise ValueError("Invalid value for `secure_id`, must not be `None`")  # noqa: E501

        self._secure_id = secure_id

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
        if issubclass(DirectoryAdGroup, dict):
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
        if not isinstance(other, DirectoryAdGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
