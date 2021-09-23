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

class BFDProperties(object):
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
        'active': 'bool',
        'state': 'str',
        'remote_state': 'str',
        'remote_diagnostic': 'str',
        'forwarding': 'bool',
        'diagnostic': 'str'
    }

    attribute_map = {
        'active': 'active',
        'state': 'state',
        'remote_state': 'remote_state',
        'remote_diagnostic': 'remote_diagnostic',
        'forwarding': 'forwarding',
        'diagnostic': 'diagnostic'
    }

    def __init__(self, active=None, state=None, remote_state=None, remote_diagnostic=None, forwarding=None, diagnostic=None):  # noqa: E501
        """BFDProperties - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._state = None
        self._remote_state = None
        self._remote_diagnostic = None
        self._forwarding = None
        self._diagnostic = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if state is not None:
            self.state = state
        if remote_state is not None:
            self.remote_state = remote_state
        if remote_diagnostic is not None:
            self.remote_diagnostic = remote_diagnostic
        if forwarding is not None:
            self.forwarding = forwarding
        if diagnostic is not None:
            self.diagnostic = diagnostic

    @property
    def active(self):
        """Gets the active of this BFDProperties.  # noqa: E501

        True if tunnel is active in a gateway HA setup  # noqa: E501

        :return: The active of this BFDProperties.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this BFDProperties.

        True if tunnel is active in a gateway HA setup  # noqa: E501

        :param active: The active of this BFDProperties.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def state(self):
        """Gets the state of this BFDProperties.  # noqa: E501

        State of the BFD session  # noqa: E501

        :return: The state of this BFDProperties.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BFDProperties.

        State of the BFD session  # noqa: E501

        :param state: The state of this BFDProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN_STATE", "ADMIN_DOWN", "DOWN", "INIT", "UP"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def remote_state(self):
        """Gets the remote_state of this BFDProperties.  # noqa: E501

        State of the remote interface's BFD session  # noqa: E501

        :return: The remote_state of this BFDProperties.  # noqa: E501
        :rtype: str
        """
        return self._remote_state

    @remote_state.setter
    def remote_state(self, remote_state):
        """Sets the remote_state of this BFDProperties.

        State of the remote interface's BFD session  # noqa: E501

        :param remote_state: The remote_state of this BFDProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN_STATE", "ADMIN_DOWN", "DOWN", "INIT", "UP"]  # noqa: E501
        if remote_state not in allowed_values:
            raise ValueError(
                "Invalid value for `remote_state` ({0}), must be one of {1}"  # noqa: E501
                .format(remote_state, allowed_values)
            )

        self._remote_state = remote_state

    @property
    def remote_diagnostic(self):
        """Gets the remote_diagnostic of this BFDProperties.  # noqa: E501

        A short message indicating what the remote interface's BFD session thinks is wrong in case of a problem  # noqa: E501

        :return: The remote_diagnostic of this BFDProperties.  # noqa: E501
        :rtype: str
        """
        return self._remote_diagnostic

    @remote_diagnostic.setter
    def remote_diagnostic(self, remote_diagnostic):
        """Sets the remote_diagnostic of this BFDProperties.

        A short message indicating what the remote interface's BFD session thinks is wrong in case of a problem  # noqa: E501

        :param remote_diagnostic: The remote_diagnostic of this BFDProperties.  # noqa: E501
        :type: str
        """

        self._remote_diagnostic = remote_diagnostic

    @property
    def forwarding(self):
        """Gets the forwarding of this BFDProperties.  # noqa: E501

        True if the BFD session believes this interface may be used to forward traffic  # noqa: E501

        :return: The forwarding of this BFDProperties.  # noqa: E501
        :rtype: bool
        """
        return self._forwarding

    @forwarding.setter
    def forwarding(self, forwarding):
        """Sets the forwarding of this BFDProperties.

        True if the BFD session believes this interface may be used to forward traffic  # noqa: E501

        :param forwarding: The forwarding of this BFDProperties.  # noqa: E501
        :type: bool
        """

        self._forwarding = forwarding

    @property
    def diagnostic(self):
        """Gets the diagnostic of this BFDProperties.  # noqa: E501

        A short message indicating what the BFD session thinks is wrong in case of a problem  # noqa: E501

        :return: The diagnostic of this BFDProperties.  # noqa: E501
        :rtype: str
        """
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, diagnostic):
        """Sets the diagnostic of this BFDProperties.

        A short message indicating what the BFD session thinks is wrong in case of a problem  # noqa: E501

        :param diagnostic: The diagnostic of this BFDProperties.  # noqa: E501
        :type: str
        """

        self._diagnostic = diagnostic

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
        if issubclass(BFDProperties, dict):
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
        if not isinstance(other, BFDProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
