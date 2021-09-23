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

class NvdsUpgradeStatusSummary(object):
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
        'precheck_id': 'str',
        'migration_state': 'list[NvdsUpgradeHostState]',
        'precheck_issue': 'list[NvdsUpgradeConfigIssue]',
        'precheck_status': 'str'
    }

    attribute_map = {
        'precheck_id': 'precheck_id',
        'migration_state': 'migration_state',
        'precheck_issue': 'precheck_issue',
        'precheck_status': 'precheck_status'
    }

    def __init__(self, precheck_id=None, migration_state=None, precheck_issue=None, precheck_status=None):  # noqa: E501
        """NvdsUpgradeStatusSummary - a model defined in Swagger"""  # noqa: E501
        self._precheck_id = None
        self._migration_state = None
        self._precheck_issue = None
        self._precheck_status = None
        self.discriminator = None
        if precheck_id is not None:
            self.precheck_id = precheck_id
        if migration_state is not None:
            self.migration_state = migration_state
        if precheck_issue is not None:
            self.precheck_issue = precheck_issue
        if precheck_status is not None:
            self.precheck_status = precheck_status

    @property
    def precheck_id(self):
        """Gets the precheck_id of this NvdsUpgradeStatusSummary.  # noqa: E501

        Tracking ID of nvds upgrade precheck  # noqa: E501

        :return: The precheck_id of this NvdsUpgradeStatusSummary.  # noqa: E501
        :rtype: str
        """
        return self._precheck_id

    @precheck_id.setter
    def precheck_id(self, precheck_id):
        """Sets the precheck_id of this NvdsUpgradeStatusSummary.

        Tracking ID of nvds upgrade precheck  # noqa: E501

        :param precheck_id: The precheck_id of this NvdsUpgradeStatusSummary.  # noqa: E501
        :type: str
        """

        self._precheck_id = precheck_id

    @property
    def migration_state(self):
        """Gets the migration_state of this NvdsUpgradeStatusSummary.  # noqa: E501

        Overall state of migration across all TransportNodes  # noqa: E501

        :return: The migration_state of this NvdsUpgradeStatusSummary.  # noqa: E501
        :rtype: list[NvdsUpgradeHostState]
        """
        return self._migration_state

    @migration_state.setter
    def migration_state(self, migration_state):
        """Sets the migration_state of this NvdsUpgradeStatusSummary.

        Overall state of migration across all TransportNodes  # noqa: E501

        :param migration_state: The migration_state of this NvdsUpgradeStatusSummary.  # noqa: E501
        :type: list[NvdsUpgradeHostState]
        """

        self._migration_state = migration_state

    @property
    def precheck_issue(self):
        """Gets the precheck_issue of this NvdsUpgradeStatusSummary.  # noqa: E501

        Config issue in pre-check  # noqa: E501

        :return: The precheck_issue of this NvdsUpgradeStatusSummary.  # noqa: E501
        :rtype: list[NvdsUpgradeConfigIssue]
        """
        return self._precheck_issue

    @precheck_issue.setter
    def precheck_issue(self, precheck_issue):
        """Sets the precheck_issue of this NvdsUpgradeStatusSummary.

        Config issue in pre-check  # noqa: E501

        :param precheck_issue: The precheck_issue of this NvdsUpgradeStatusSummary.  # noqa: E501
        :type: list[NvdsUpgradeConfigIssue]
        """

        self._precheck_issue = precheck_issue

    @property
    def precheck_status(self):
        """Gets the precheck_status of this NvdsUpgradeStatusSummary.  # noqa: E501

        Overall status of pre-check  # noqa: E501

        :return: The precheck_status of this NvdsUpgradeStatusSummary.  # noqa: E501
        :rtype: str
        """
        return self._precheck_status

    @precheck_status.setter
    def precheck_status(self, precheck_status):
        """Sets the precheck_status of this NvdsUpgradeStatusSummary.

        Overall status of pre-check  # noqa: E501

        :param precheck_status: The precheck_status of this NvdsUpgradeStatusSummary.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "FAILED", "PENDING_TOPOLOGY", "APPLYING_TOPOLOGY", "APPLY_TOPOLOGY_FAILED", "READY"]  # noqa: E501
        if precheck_status not in allowed_values:
            raise ValueError(
                "Invalid value for `precheck_status` ({0}), must be one of {1}"  # noqa: E501
                .format(precheck_status, allowed_values)
            )

        self._precheck_status = precheck_status

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
        if issubclass(NvdsUpgradeStatusSummary, dict):
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
        if not isinstance(other, NvdsUpgradeStatusSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other