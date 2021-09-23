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

class TnNodeStackSpanStatus(object):
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
        'tn_node_name': 'str',
        'vmknic_status': 'str',
        'dedicated_stack_status': 'str',
        'tn_node_id': 'str',
        'detail': 'str',
        'last_updated_time': 'int'
    }

    attribute_map = {
        'tn_node_name': 'tn_node_name',
        'vmknic_status': 'vmknic_status',
        'dedicated_stack_status': 'dedicated_stack_status',
        'tn_node_id': 'tn_node_id',
        'detail': 'detail',
        'last_updated_time': 'last_updated_time'
    }

    def __init__(self, tn_node_name=None, vmknic_status=None, dedicated_stack_status=None, tn_node_id=None, detail=None, last_updated_time=None):  # noqa: E501
        """TnNodeStackSpanStatus - a model defined in Swagger"""  # noqa: E501
        self._tn_node_name = None
        self._vmknic_status = None
        self._dedicated_stack_status = None
        self._tn_node_id = None
        self._detail = None
        self._last_updated_time = None
        self.discriminator = None
        self.tn_node_name = tn_node_name
        self.vmknic_status = vmknic_status
        self.dedicated_stack_status = dedicated_stack_status
        if tn_node_id is not None:
            self.tn_node_id = tn_node_id
        self.detail = detail
        self.last_updated_time = last_updated_time

    @property
    def tn_node_name(self):
        """Gets the tn_node_name of this TnNodeStackSpanStatus.  # noqa: E501

        For L3PortMirrorSession configured mirror stack, show the TN node friendly name which spaned in L3PortMirrorSession.   # noqa: E501

        :return: The tn_node_name of this TnNodeStackSpanStatus.  # noqa: E501
        :rtype: str
        """
        return self._tn_node_name

    @tn_node_name.setter
    def tn_node_name(self, tn_node_name):
        """Sets the tn_node_name of this TnNodeStackSpanStatus.

        For L3PortMirrorSession configured mirror stack, show the TN node friendly name which spaned in L3PortMirrorSession.   # noqa: E501

        :param tn_node_name: The tn_node_name of this TnNodeStackSpanStatus.  # noqa: E501
        :type: str
        """
        if tn_node_name is None:
            raise ValueError("Invalid value for `tn_node_name`, must not be `None`")  # noqa: E501

        self._tn_node_name = tn_node_name

    @property
    def vmknic_status(self):
        """Gets the vmknic_status of this TnNodeStackSpanStatus.  # noqa: E501

        Show the vmknic health status, if the vmknic has been bouned to mirror stack, it will show SUCCESS or it will show FAILED.   # noqa: E501

        :return: The vmknic_status of this TnNodeStackSpanStatus.  # noqa: E501
        :rtype: str
        """
        return self._vmknic_status

    @vmknic_status.setter
    def vmknic_status(self, vmknic_status):
        """Sets the vmknic_status of this TnNodeStackSpanStatus.

        Show the vmknic health status, if the vmknic has been bouned to mirror stack, it will show SUCCESS or it will show FAILED.   # noqa: E501

        :param vmknic_status: The vmknic_status of this TnNodeStackSpanStatus.  # noqa: E501
        :type: str
        """
        if vmknic_status is None:
            raise ValueError("Invalid value for `vmknic_status`, must not be `None`")  # noqa: E501
        allowed_values = ["UNKNOWN", "SUCCESS", "FAILED"]  # noqa: E501
        if vmknic_status not in allowed_values:
            raise ValueError(
                "Invalid value for `vmknic_status` ({0}), must be one of {1}"  # noqa: E501
                .format(vmknic_status, allowed_values)
            )

        self._vmknic_status = vmknic_status

    @property
    def dedicated_stack_status(self):
        """Gets the dedicated_stack_status of this TnNodeStackSpanStatus.  # noqa: E501

        Show the dedicated mirror stack health status, if the TN node has the mirror stack, it will show SUCCESS or it will show FAILED.   # noqa: E501

        :return: The dedicated_stack_status of this TnNodeStackSpanStatus.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_stack_status

    @dedicated_stack_status.setter
    def dedicated_stack_status(self, dedicated_stack_status):
        """Sets the dedicated_stack_status of this TnNodeStackSpanStatus.

        Show the dedicated mirror stack health status, if the TN node has the mirror stack, it will show SUCCESS or it will show FAILED.   # noqa: E501

        :param dedicated_stack_status: The dedicated_stack_status of this TnNodeStackSpanStatus.  # noqa: E501
        :type: str
        """
        if dedicated_stack_status is None:
            raise ValueError("Invalid value for `dedicated_stack_status`, must not be `None`")  # noqa: E501
        allowed_values = ["UNKNOWN", "SUCCESS", "FAILED"]  # noqa: E501
        if dedicated_stack_status not in allowed_values:
            raise ValueError(
                "Invalid value for `dedicated_stack_status` ({0}), must be one of {1}"  # noqa: E501
                .format(dedicated_stack_status, allowed_values)
            )

        self._dedicated_stack_status = dedicated_stack_status

    @property
    def tn_node_id(self):
        """Gets the tn_node_id of this TnNodeStackSpanStatus.  # noqa: E501

        For L3PortMirrorSession configured mirror stack, show the TN node UUID which spaned in L3PortMirrorSession.   # noqa: E501

        :return: The tn_node_id of this TnNodeStackSpanStatus.  # noqa: E501
        :rtype: str
        """
        return self._tn_node_id

    @tn_node_id.setter
    def tn_node_id(self, tn_node_id):
        """Sets the tn_node_id of this TnNodeStackSpanStatus.

        For L3PortMirrorSession configured mirror stack, show the TN node UUID which spaned in L3PortMirrorSession.   # noqa: E501

        :param tn_node_id: The tn_node_id of this TnNodeStackSpanStatus.  # noqa: E501
        :type: str
        """

        self._tn_node_id = tn_node_id

    @property
    def detail(self):
        """Gets the detail of this TnNodeStackSpanStatus.  # noqa: E501

        Give the detail info for mirror stack and vmknic health status. If the stack or vmknic is FAILED, detail info will tell user reason why the stauts is FAILED. So that user can correct their configuration.   # noqa: E501

        :return: The detail of this TnNodeStackSpanStatus.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this TnNodeStackSpanStatus.

        Give the detail info for mirror stack and vmknic health status. If the stack or vmknic is FAILED, detail info will tell user reason why the stauts is FAILED. So that user can correct their configuration.   # noqa: E501

        :param detail: The detail of this TnNodeStackSpanStatus.  # noqa: E501
        :type: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

    @property
    def last_updated_time(self):
        """Gets the last_updated_time of this TnNodeStackSpanStatus.  # noqa: E501

        TN miror stack status will be updated periodically, this item indicates the lastest timestamp of TN node stack status is updated.   # noqa: E501

        :return: The last_updated_time of this TnNodeStackSpanStatus.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, last_updated_time):
        """Sets the last_updated_time of this TnNodeStackSpanStatus.

        TN miror stack status will be updated periodically, this item indicates the lastest timestamp of TN node stack status is updated.   # noqa: E501

        :param last_updated_time: The last_updated_time of this TnNodeStackSpanStatus.  # noqa: E501
        :type: int
        """
        if last_updated_time is None:
            raise ValueError("Invalid value for `last_updated_time`, must not be `None`")  # noqa: E501

        self._last_updated_time = last_updated_time

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
        if issubclass(TnNodeStackSpanStatus, dict):
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
        if not isinstance(other, TnNodeStackSpanStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
