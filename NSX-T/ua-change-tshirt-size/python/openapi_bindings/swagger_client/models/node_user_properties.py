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

class NodeUserProperties(Resource):
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
        'username': 'str',
        'status': 'str',
        'last_password_change': 'int',
        'full_name': 'str',
        'password_change_frequency': 'int',
        'password': 'str',
        'userid': 'int',
        'old_password': 'str'
    }
    if hasattr(Resource, "swagger_types"):
        swagger_types.update(Resource.swagger_types)

    attribute_map = {
        'username': 'username',
        'status': 'status',
        'last_password_change': 'last_password_change',
        'full_name': 'full_name',
        'password_change_frequency': 'password_change_frequency',
        'password': 'password',
        'userid': 'userid',
        'old_password': 'old_password'
    }
    if hasattr(Resource, "attribute_map"):
        attribute_map.update(Resource.attribute_map)

    def __init__(self, username=None, status=None, last_password_change=None, full_name=None, password_change_frequency=None, password=None, userid=None, old_password=None, *args, **kwargs):  # noqa: E501
        """NodeUserProperties - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._status = None
        self._last_password_change = None
        self._full_name = None
        self._password_change_frequency = None
        self._password = None
        self._userid = None
        self._old_password = None
        self.discriminator = None
        if username is not None:
            self.username = username
        if status is not None:
            self.status = status
        if last_password_change is not None:
            self.last_password_change = last_password_change
        if full_name is not None:
            self.full_name = full_name
        if password_change_frequency is not None:
            self.password_change_frequency = password_change_frequency
        if password is not None:
            self.password = password
        if userid is not None:
            self.userid = userid
        if old_password is not None:
            self.old_password = old_password
        Resource.__init__(self, *args, **kwargs)

    @property
    def username(self):
        """Gets the username of this NodeUserProperties.  # noqa: E501

        User login name (must be \"root\" if userid is 0)  # noqa: E501

        :return: The username of this NodeUserProperties.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this NodeUserProperties.

        User login name (must be \"root\" if userid is 0)  # noqa: E501

        :param username: The username of this NodeUserProperties.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def status(self):
        """Gets the status of this NodeUserProperties.  # noqa: E501

        Status of the user. This value can be ACTIVE indicating authentication attempts will be successful if the correct credentials are specified. The value can also be PASSWORD_EXPIRED indicating authentication attempts will fail because the user's password has expired and must be changed. Or, this value can be NOT_ACTIVATED indicating the user's password has not yet been set and must be set before the user can authenticate.  # noqa: E501

        :return: The status of this NodeUserProperties.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeUserProperties.

        Status of the user. This value can be ACTIVE indicating authentication attempts will be successful if the correct credentials are specified. The value can also be PASSWORD_EXPIRED indicating authentication attempts will fail because the user's password has expired and must be changed. Or, this value can be NOT_ACTIVATED indicating the user's password has not yet been set and must be set before the user can authenticate.  # noqa: E501

        :param status: The status of this NodeUserProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "PASSWORD_EXPIRED", "NOT_ACTIVATED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def last_password_change(self):
        """Gets the last_password_change of this NodeUserProperties.  # noqa: E501

        Number of days since password was last changed  # noqa: E501

        :return: The last_password_change of this NodeUserProperties.  # noqa: E501
        :rtype: int
        """
        return self._last_password_change

    @last_password_change.setter
    def last_password_change(self, last_password_change):
        """Sets the last_password_change of this NodeUserProperties.

        Number of days since password was last changed  # noqa: E501

        :param last_password_change: The last_password_change of this NodeUserProperties.  # noqa: E501
        :type: int
        """

        self._last_password_change = last_password_change

    @property
    def full_name(self):
        """Gets the full_name of this NodeUserProperties.  # noqa: E501

        Full name for the user  # noqa: E501

        :return: The full_name of this NodeUserProperties.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this NodeUserProperties.

        Full name for the user  # noqa: E501

        :param full_name: The full_name of this NodeUserProperties.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def password_change_frequency(self):
        """Gets the password_change_frequency of this NodeUserProperties.  # noqa: E501

        Number of days password is valid before it must be changed. This can be set to 0 to indicate no password change is required or a positive integer up to 9999. By default local user passwords must be changed every 90 days.  # noqa: E501

        :return: The password_change_frequency of this NodeUserProperties.  # noqa: E501
        :rtype: int
        """
        return self._password_change_frequency

    @password_change_frequency.setter
    def password_change_frequency(self, password_change_frequency):
        """Sets the password_change_frequency of this NodeUserProperties.

        Number of days password is valid before it must be changed. This can be set to 0 to indicate no password change is required or a positive integer up to 9999. By default local user passwords must be changed every 90 days.  # noqa: E501

        :param password_change_frequency: The password_change_frequency of this NodeUserProperties.  # noqa: E501
        :type: int
        """

        self._password_change_frequency = password_change_frequency

    @property
    def password(self):
        """Gets the password of this NodeUserProperties.  # noqa: E501

        Password for the user (optionally specified on PUT, unspecified on GET)  # noqa: E501

        :return: The password of this NodeUserProperties.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this NodeUserProperties.

        Password for the user (optionally specified on PUT, unspecified on GET)  # noqa: E501

        :param password: The password of this NodeUserProperties.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def userid(self):
        """Gets the userid of this NodeUserProperties.  # noqa: E501

        Numeric id for the user  # noqa: E501

        :return: The userid of this NodeUserProperties.  # noqa: E501
        :rtype: int
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this NodeUserProperties.

        Numeric id for the user  # noqa: E501

        :param userid: The userid of this NodeUserProperties.  # noqa: E501
        :type: int
        """

        self._userid = userid

    @property
    def old_password(self):
        """Gets the old_password of this NodeUserProperties.  # noqa: E501

        Old password for the user (required on PUT if password specified)  # noqa: E501

        :return: The old_password of this NodeUserProperties.  # noqa: E501
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this NodeUserProperties.

        Old password for the user (required on PUT if password specified)  # noqa: E501

        :param old_password: The old_password of this NodeUserProperties.  # noqa: E501
        :type: str
        """

        self._old_password = old_password

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
        if issubclass(NodeUserProperties, dict):
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
        if not isinstance(other, NodeUserProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
