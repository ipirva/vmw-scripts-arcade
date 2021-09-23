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

class MigrationUnitStatus(object):
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
        'errors': 'list[str]',
        'display_name': 'str',
        'id': 'str',
        'percent_complete': 'float'
    }

    attribute_map = {
        'status': 'status',
        'errors': 'errors',
        'display_name': 'display_name',
        'id': 'id',
        'percent_complete': 'percent_complete'
    }

    def __init__(self, status=None, errors=None, display_name=None, id=None, percent_complete=None):  # noqa: E501
        """MigrationUnitStatus - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._errors = None
        self._display_name = None
        self._id = None
        self._percent_complete = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if errors is not None:
            self.errors = errors
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if percent_complete is not None:
            self.percent_complete = percent_complete

    @property
    def status(self):
        """Gets the status of this MigrationUnitStatus.  # noqa: E501

        Status of migration unit  # noqa: E501

        :return: The status of this MigrationUnitStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MigrationUnitStatus.

        Status of migration unit  # noqa: E501

        :param status: The status of this MigrationUnitStatus.  # noqa: E501
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
    def errors(self):
        """Gets the errors of this MigrationUnitStatus.  # noqa: E501

        List of errors occurred during migration of this migration unit  # noqa: E501

        :return: The errors of this MigrationUnitStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this MigrationUnitStatus.

        List of errors occurred during migration of this migration unit  # noqa: E501

        :param errors: The errors of this MigrationUnitStatus.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

    @property
    def display_name(self):
        """Gets the display_name of this MigrationUnitStatus.  # noqa: E501

        Name of migration unit  # noqa: E501

        :return: The display_name of this MigrationUnitStatus.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this MigrationUnitStatus.

        Name of migration unit  # noqa: E501

        :param display_name: The display_name of this MigrationUnitStatus.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this MigrationUnitStatus.  # noqa: E501

        Identifier of migration unit  # noqa: E501

        :return: The id of this MigrationUnitStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MigrationUnitStatus.

        Identifier of migration unit  # noqa: E501

        :param id: The id of this MigrationUnitStatus.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def percent_complete(self):
        """Gets the percent_complete of this MigrationUnitStatus.  # noqa: E501

        Indicator of migration progress in percentage  # noqa: E501

        :return: The percent_complete of this MigrationUnitStatus.  # noqa: E501
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this MigrationUnitStatus.

        Indicator of migration progress in percentage  # noqa: E501

        :param percent_complete: The percent_complete of this MigrationUnitStatus.  # noqa: E501
        :type: float
        """

        self._percent_complete = percent_complete

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
        if issubclass(MigrationUnitStatus, dict):
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
        if not isinstance(other, MigrationUnitStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
