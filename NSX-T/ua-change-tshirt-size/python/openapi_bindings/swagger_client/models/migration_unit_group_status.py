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

class MigrationUnitGroupStatus(object):
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
        'failed_count': 'int',
        'migration_unit_count': 'int',
        'group_id': 'str',
        'percent_complete': 'float',
        'group_name': 'str'
    }

    attribute_map = {
        'status': 'status',
        'failed_count': 'failed_count',
        'migration_unit_count': 'migration_unit_count',
        'group_id': 'group_id',
        'percent_complete': 'percent_complete',
        'group_name': 'group_name'
    }

    def __init__(self, status=None, failed_count=None, migration_unit_count=None, group_id=None, percent_complete=None, group_name=None):  # noqa: E501
        """MigrationUnitGroupStatus - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._failed_count = None
        self._migration_unit_count = None
        self._group_id = None
        self._percent_complete = None
        self._group_name = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if failed_count is not None:
            self.failed_count = failed_count
        if migration_unit_count is not None:
            self.migration_unit_count = migration_unit_count
        if group_id is not None:
            self.group_id = group_id
        if percent_complete is not None:
            self.percent_complete = percent_complete
        if group_name is not None:
            self.group_name = group_name

    @property
    def status(self):
        """Gets the status of this MigrationUnitGroupStatus.  # noqa: E501

        Migration status of migration unit group  # noqa: E501

        :return: The status of this MigrationUnitGroupStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MigrationUnitGroupStatus.

        Migration status of migration unit group  # noqa: E501

        :param status: The status of this MigrationUnitGroupStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILED", "IN_PROGRESS", "NOT_STARTED", "PAUSED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def failed_count(self):
        """Gets the failed_count of this MigrationUnitGroupStatus.  # noqa: E501

        Number of nodes in the migration unit group that failed migration  # noqa: E501

        :return: The failed_count of this MigrationUnitGroupStatus.  # noqa: E501
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        """Sets the failed_count of this MigrationUnitGroupStatus.

        Number of nodes in the migration unit group that failed migration  # noqa: E501

        :param failed_count: The failed_count of this MigrationUnitGroupStatus.  # noqa: E501
        :type: int
        """

        self._failed_count = failed_count

    @property
    def migration_unit_count(self):
        """Gets the migration_unit_count of this MigrationUnitGroupStatus.  # noqa: E501

        Number of migration units in the group  # noqa: E501

        :return: The migration_unit_count of this MigrationUnitGroupStatus.  # noqa: E501
        :rtype: int
        """
        return self._migration_unit_count

    @migration_unit_count.setter
    def migration_unit_count(self, migration_unit_count):
        """Sets the migration_unit_count of this MigrationUnitGroupStatus.

        Number of migration units in the group  # noqa: E501

        :param migration_unit_count: The migration_unit_count of this MigrationUnitGroupStatus.  # noqa: E501
        :type: int
        """

        self._migration_unit_count = migration_unit_count

    @property
    def group_id(self):
        """Gets the group_id of this MigrationUnitGroupStatus.  # noqa: E501

        Identifier for migration unit group  # noqa: E501

        :return: The group_id of this MigrationUnitGroupStatus.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this MigrationUnitGroupStatus.

        Identifier for migration unit group  # noqa: E501

        :param group_id: The group_id of this MigrationUnitGroupStatus.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def percent_complete(self):
        """Gets the percent_complete of this MigrationUnitGroupStatus.  # noqa: E501

        Indicator of migration progress in percentage  # noqa: E501

        :return: The percent_complete of this MigrationUnitGroupStatus.  # noqa: E501
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this MigrationUnitGroupStatus.

        Indicator of migration progress in percentage  # noqa: E501

        :param percent_complete: The percent_complete of this MigrationUnitGroupStatus.  # noqa: E501
        :type: float
        """

        self._percent_complete = percent_complete

    @property
    def group_name(self):
        """Gets the group_name of this MigrationUnitGroupStatus.  # noqa: E501

        Name of the migration unit group  # noqa: E501

        :return: The group_name of this MigrationUnitGroupStatus.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this MigrationUnitGroupStatus.

        Name of the migration unit group  # noqa: E501

        :param group_name: The group_name of this MigrationUnitGroupStatus.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

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
        if issubclass(MigrationUnitGroupStatus, dict):
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
        if not isinstance(other, MigrationUnitGroupStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
