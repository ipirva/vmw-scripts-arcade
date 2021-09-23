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
from swagger_client.models.managed_resource import ManagedResource  # noqa: F401,E501

class LiveTraceStatus(ManagedResource):
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
        'filter': 'LiveTraceFilterData',
        'operation_state': 'str',
        'timeout': 'int',
        'source_lport': 'str',
        'request_status': 'str',
        'actions': 'LiveTraceActionConfig'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'filter': 'filter',
        'operation_state': 'operation_state',
        'timeout': 'timeout',
        'source_lport': 'source_lport',
        'request_status': 'request_status',
        'actions': 'actions'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, filter=None, operation_state=None, timeout=None, source_lport=None, request_status=None, actions=None, *args, **kwargs):  # noqa: E501
        """LiveTraceStatus - a model defined in Swagger"""  # noqa: E501
        self._filter = None
        self._operation_state = None
        self._timeout = None
        self._source_lport = None
        self._request_status = None
        self._actions = None
        self.discriminator = None
        if filter is not None:
            self.filter = filter
        if operation_state is not None:
            self.operation_state = operation_state
        if timeout is not None:
            self.timeout = timeout
        if source_lport is not None:
            self.source_lport = source_lport
        if request_status is not None:
            self.request_status = request_status
        if actions is not None:
            self.actions = actions
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def filter(self):
        """Gets the filter of this LiveTraceStatus.  # noqa: E501


        :return: The filter of this LiveTraceStatus.  # noqa: E501
        :rtype: LiveTraceFilterData
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this LiveTraceStatus.


        :param filter: The filter of this LiveTraceStatus.  # noqa: E501
        :type: LiveTraceFilterData
        """

        self._filter = filter

    @property
    def operation_state(self):
        """Gets the operation_state of this LiveTraceStatus.  # noqa: E501

        The operation state of live trace. IN_PROGRESS - collecting the session results. FINISHED - session results collect complete. PARTIAL_FINISHED - some ssession results may be lost. CANCELED - session cancelled by exception. TIMEOUT - session result is incomplete until timeout.   # noqa: E501

        :return: The operation_state of this LiveTraceStatus.  # noqa: E501
        :rtype: str
        """
        return self._operation_state

    @operation_state.setter
    def operation_state(self, operation_state):
        """Sets the operation_state of this LiveTraceStatus.

        The operation state of live trace. IN_PROGRESS - collecting the session results. FINISHED - session results collect complete. PARTIAL_FINISHED - some ssession results may be lost. CANCELED - session cancelled by exception. TIMEOUT - session result is incomplete until timeout.   # noqa: E501

        :param operation_state: The operation_state of this LiveTraceStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "FINISHED", "PARTIAL_FINISHED", "CANCELED", "TIMEOUT"]  # noqa: E501
        if operation_state not in allowed_values:
            raise ValueError(
                "Invalid value for `operation_state` ({0}), must be one of {1}"  # noqa: E501
                .format(operation_state, allowed_values)
            )

        self._operation_state = operation_state

    @property
    def timeout(self):
        """Gets the timeout of this LiveTraceStatus.  # noqa: E501

        Timeout in seconds for livetrace session  # noqa: E501

        :return: The timeout of this LiveTraceStatus.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this LiveTraceStatus.

        Timeout in seconds for livetrace session  # noqa: E501

        :param timeout: The timeout of this LiveTraceStatus.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def source_lport(self):
        """Gets the source_lport of this LiveTraceStatus.  # noqa: E501

        The source logical port  # noqa: E501

        :return: The source_lport of this LiveTraceStatus.  # noqa: E501
        :rtype: str
        """
        return self._source_lport

    @source_lport.setter
    def source_lport(self, source_lport):
        """Sets the source_lport of this LiveTraceStatus.

        The source logical port  # noqa: E501

        :param source_lport: The source_lport of this LiveTraceStatus.  # noqa: E501
        :type: str
        """

        self._source_lport = source_lport

    @property
    def request_status(self):
        """Gets the request_status of this LiveTraceStatus.  # noqa: E501

        The status of a live trace request. SUCCESS_DELIVERED - The request is delivered successfully. LCP_FAILURE - nsx-cfgagent fails to realize the request. INVALID_FILTER - filter data invalid. DATAPATH_FAILURE - DP fails to realize the request. TIMEOUT - The response to the request is not received within timeout. CONNECTION_ERROR - There is connection error with host component. UNKNOWN - The status of request cannot be determined.   # noqa: E501

        :return: The request_status of this LiveTraceStatus.  # noqa: E501
        :rtype: str
        """
        return self._request_status

    @request_status.setter
    def request_status(self, request_status):
        """Sets the request_status of this LiveTraceStatus.

        The status of a live trace request. SUCCESS_DELIVERED - The request is delivered successfully. LCP_FAILURE - nsx-cfgagent fails to realize the request. INVALID_FILTER - filter data invalid. DATAPATH_FAILURE - DP fails to realize the request. TIMEOUT - The response to the request is not received within timeout. CONNECTION_ERROR - There is connection error with host component. UNKNOWN - The status of request cannot be determined.   # noqa: E501

        :param request_status: The request_status of this LiveTraceStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS_DELIVERED", "LCP_FAILURE", "INVALID_FILTER", "DATAPATH_FAILURE", "CONNECTION_ERROR", "TIMEOUT", "UNKNOWN"]  # noqa: E501
        if request_status not in allowed_values:
            raise ValueError(
                "Invalid value for `request_status` ({0}), must be one of {1}"  # noqa: E501
                .format(request_status, allowed_values)
            )

        self._request_status = request_status

    @property
    def actions(self):
        """Gets the actions of this LiveTraceStatus.  # noqa: E501


        :return: The actions of this LiveTraceStatus.  # noqa: E501
        :rtype: LiveTraceActionConfig
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this LiveTraceStatus.


        :param actions: The actions of this LiveTraceStatus.  # noqa: E501
        :type: LiveTraceActionConfig
        """

        self._actions = actions

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
        if issubclass(LiveTraceStatus, dict):
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
        if not isinstance(other, LiveTraceStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
