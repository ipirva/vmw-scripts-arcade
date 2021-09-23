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

class MigrationUnit(Resource):
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
        'group': 'ResourceReference',
        'warnings': 'list[str]',
        'current_version': 'str',
        'metadata': 'list[KeyValuePair]',
        'type': 'str',
        'id': 'str',
        'display_name': 'str'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        'group': 'group',
        'warnings': 'warnings',
        'current_version': 'current_version',
        'metadata': 'metadata',
        'type': 'type',
        'id': 'id',
        'display_name': 'display_name'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, group=None, warnings=None, current_version=None, metadata=None, type=None, id=None, display_name=None, *args, **kwargs):  # noqa: E501
        """MigrationUnit - a model defined in Swagger"""  # noqa: E501
        self._group = None
        self._warnings = None
        self._current_version = None
        self._metadata = None
        self._type = None
        self._id = None
        self._display_name = None
        self.discriminator = None
        if group is not None:
            self.group = group
        if warnings is not None:
            self.warnings = warnings
        if current_version is not None:
            self.current_version = current_version
        if metadata is not None:
            self.metadata = metadata
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name
        Resource.__init__(self, *args, **kwargs)

    @property
    def group(self):
        """Gets the group of this MigrationUnit.  # noqa: E501


        :return: The group of this MigrationUnit.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this MigrationUnit.


        :param group: The group of this MigrationUnit.  # noqa: E501
        :type: ResourceReference
        """

        self._group = group

    @property
    def warnings(self):
        """Gets the warnings of this MigrationUnit.  # noqa: E501

        List of warnings indicating issues with the migration unit that may result in migration failure  # noqa: E501

        :return: The warnings of this MigrationUnit.  # noqa: E501
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this MigrationUnit.

        List of warnings indicating issues with the migration unit that may result in migration failure  # noqa: E501

        :param warnings: The warnings of this MigrationUnit.  # noqa: E501
        :type: list[str]
        """

        self._warnings = warnings

    @property
    def current_version(self):
        """Gets the current_version of this MigrationUnit.  # noqa: E501

        This is component version e.g. if migration unit is of type HOST, then this is host version.  # noqa: E501

        :return: The current_version of this MigrationUnit.  # noqa: E501
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this MigrationUnit.

        This is component version e.g. if migration unit is of type HOST, then this is host version.  # noqa: E501

        :param current_version: The current_version of this MigrationUnit.  # noqa: E501
        :type: str
        """

        self._current_version = current_version

    @property
    def metadata(self):
        """Gets the metadata of this MigrationUnit.  # noqa: E501

        Metadata about migration unit  # noqa: E501

        :return: The metadata of this MigrationUnit.  # noqa: E501
        :rtype: list[KeyValuePair]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this MigrationUnit.

        Metadata about migration unit  # noqa: E501

        :param metadata: The metadata of this MigrationUnit.  # noqa: E501
        :type: list[KeyValuePair]
        """

        self._metadata = metadata

    @property
    def type(self):
        """Gets the type of this MigrationUnit.  # noqa: E501

        Migration unit type  # noqa: E501

        :return: The type of this MigrationUnit.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MigrationUnit.

        Migration unit type  # noqa: E501

        :param type: The type of this MigrationUnit.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this MigrationUnit.  # noqa: E501

        Identifier of the migration unit  # noqa: E501

        :return: The id of this MigrationUnit.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MigrationUnit.

        Identifier of the migration unit  # noqa: E501

        :param id: The id of this MigrationUnit.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this MigrationUnit.  # noqa: E501

        Name of the migration unit  # noqa: E501

        :return: The display_name of this MigrationUnit.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this MigrationUnit.

        Name of the migration unit  # noqa: E501

        :param display_name: The display_name of this MigrationUnit.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

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
        if issubclass(MigrationUnit, dict):
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
        if not isinstance(other, MigrationUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
