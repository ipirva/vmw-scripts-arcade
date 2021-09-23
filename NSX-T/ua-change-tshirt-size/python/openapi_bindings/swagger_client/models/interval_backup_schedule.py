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
from swagger_client.models.backup_schedule import BackupSchedule  # noqa: F401,E501

class IntervalBackupSchedule(BackupSchedule):
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
        'seconds_between_backups': 'int'
    }
    if hasattr(BackupSchedule, "swagger_types"):
        swagger_types.update(BackupSchedule.swagger_types)

    attribute_map = {
        'seconds_between_backups': 'seconds_between_backups'
    }
    if hasattr(BackupSchedule, "attribute_map"):
        attribute_map.update(BackupSchedule.attribute_map)

    def __init__(self, seconds_between_backups=3600, *args, **kwargs):  # noqa: E501
        """IntervalBackupSchedule - a model defined in Swagger"""  # noqa: E501
        self._seconds_between_backups = None
        self.discriminator = None
        if seconds_between_backups is not None:
            self.seconds_between_backups = seconds_between_backups
        BackupSchedule.__init__(self, *args, **kwargs)

    @property
    def seconds_between_backups(self):
        """Gets the seconds_between_backups of this IntervalBackupSchedule.  # noqa: E501

        Time interval in seconds between two consecutive automated backups  # noqa: E501

        :return: The seconds_between_backups of this IntervalBackupSchedule.  # noqa: E501
        :rtype: int
        """
        return self._seconds_between_backups

    @seconds_between_backups.setter
    def seconds_between_backups(self, seconds_between_backups):
        """Sets the seconds_between_backups of this IntervalBackupSchedule.

        Time interval in seconds between two consecutive automated backups  # noqa: E501

        :param seconds_between_backups: The seconds_between_backups of this IntervalBackupSchedule.  # noqa: E501
        :type: int
        """

        self._seconds_between_backups = seconds_between_backups

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
        if issubclass(IntervalBackupSchedule, dict):
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
        if not isinstance(other, IntervalBackupSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other