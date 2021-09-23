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
from swagger_client.models.list_result import ListResult  # noqa: F401,E501

class MacAddressListResult(ListResult):
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
        'last_update_timestamp': 'int',
        'logical_switch_id': 'str',
        'results': 'list[MacTableEntry]',
        'transport_node_id': 'str'
    }
    if hasattr(ListResult, "swagger_types"):
        swagger_types.update(ListResult.swagger_types)

    attribute_map = {
        'last_update_timestamp': 'last_update_timestamp',
        'logical_switch_id': 'logical_switch_id',
        'results': 'results',
        'transport_node_id': 'transport_node_id'
    }
    if hasattr(ListResult, "attribute_map"):
        attribute_map.update(ListResult.attribute_map)

    def __init__(self, last_update_timestamp=None, logical_switch_id=None, results=None, transport_node_id=None, *args, **kwargs):  # noqa: E501
        """MacAddressListResult - a model defined in Swagger"""  # noqa: E501
        self._last_update_timestamp = None
        self._logical_switch_id = None
        self._results = None
        self._transport_node_id = None
        self.discriminator = None
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        if logical_switch_id is not None:
            self.logical_switch_id = logical_switch_id
        if results is not None:
            self.results = results
        if transport_node_id is not None:
            self.transport_node_id = transport_node_id
        ListResult.__init__(self, *args, **kwargs)

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this MacAddressListResult.  # noqa: E501

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :return: The last_update_timestamp of this MacAddressListResult.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this MacAddressListResult.

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this MacAddressListResult.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def logical_switch_id(self):
        """Gets the logical_switch_id of this MacAddressListResult.  # noqa: E501

        The id of the logical Switch  # noqa: E501

        :return: The logical_switch_id of this MacAddressListResult.  # noqa: E501
        :rtype: str
        """
        return self._logical_switch_id

    @logical_switch_id.setter
    def logical_switch_id(self, logical_switch_id):
        """Sets the logical_switch_id of this MacAddressListResult.

        The id of the logical Switch  # noqa: E501

        :param logical_switch_id: The logical_switch_id of this MacAddressListResult.  # noqa: E501
        :type: str
        """

        self._logical_switch_id = logical_switch_id

    @property
    def results(self):
        """Gets the results of this MacAddressListResult.  # noqa: E501


        :return: The results of this MacAddressListResult.  # noqa: E501
        :rtype: list[MacTableEntry]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this MacAddressListResult.


        :param results: The results of this MacAddressListResult.  # noqa: E501
        :type: list[MacTableEntry]
        """

        self._results = results

    @property
    def transport_node_id(self):
        """Gets the transport_node_id of this MacAddressListResult.  # noqa: E501

        Transport node identifier  # noqa: E501

        :return: The transport_node_id of this MacAddressListResult.  # noqa: E501
        :rtype: str
        """
        return self._transport_node_id

    @transport_node_id.setter
    def transport_node_id(self, transport_node_id):
        """Sets the transport_node_id of this MacAddressListResult.

        Transport node identifier  # noqa: E501

        :param transport_node_id: The transport_node_id of this MacAddressListResult.  # noqa: E501
        :type: str
        """

        self._transport_node_id = transport_node_id

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
        if issubclass(MacAddressListResult, dict):
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
        if not isinstance(other, MacAddressListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
