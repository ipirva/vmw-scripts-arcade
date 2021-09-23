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

class NatStatisticsPerLogicalRouter(object):
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
        'per_transport_node_statistics': 'list[NatStatisticsPerTransportNode]',
        'statistics_across_all_nodes': 'NatCounters',
        'logical_router_id': 'str'
    }

    attribute_map = {
        'last_update_timestamp': 'last_update_timestamp',
        'per_transport_node_statistics': 'per_transport_node_statistics',
        'statistics_across_all_nodes': 'statistics_across_all_nodes',
        'logical_router_id': 'logical_router_id'
    }

    def __init__(self, last_update_timestamp=None, per_transport_node_statistics=None, statistics_across_all_nodes=None, logical_router_id=None):  # noqa: E501
        """NatStatisticsPerLogicalRouter - a model defined in Swagger"""  # noqa: E501
        self._last_update_timestamp = None
        self._per_transport_node_statistics = None
        self._statistics_across_all_nodes = None
        self._logical_router_id = None
        self.discriminator = None
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        if per_transport_node_statistics is not None:
            self.per_transport_node_statistics = per_transport_node_statistics
        if statistics_across_all_nodes is not None:
            self.statistics_across_all_nodes = statistics_across_all_nodes
        if logical_router_id is not None:
            self.logical_router_id = logical_router_id

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this NatStatisticsPerLogicalRouter.  # noqa: E501

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :return: The last_update_timestamp of this NatStatisticsPerLogicalRouter.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this NatStatisticsPerLogicalRouter.

        Timestamp when the data was last updated; unset if data source has never updated the data.  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this NatStatisticsPerLogicalRouter.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def per_transport_node_statistics(self):
        """Gets the per_transport_node_statistics of this NatStatisticsPerLogicalRouter.  # noqa: E501

        Detailed per node statistics  # noqa: E501

        :return: The per_transport_node_statistics of this NatStatisticsPerLogicalRouter.  # noqa: E501
        :rtype: list[NatStatisticsPerTransportNode]
        """
        return self._per_transport_node_statistics

    @per_transport_node_statistics.setter
    def per_transport_node_statistics(self, per_transport_node_statistics):
        """Sets the per_transport_node_statistics of this NatStatisticsPerLogicalRouter.

        Detailed per node statistics  # noqa: E501

        :param per_transport_node_statistics: The per_transport_node_statistics of this NatStatisticsPerLogicalRouter.  # noqa: E501
        :type: list[NatStatisticsPerTransportNode]
        """

        self._per_transport_node_statistics = per_transport_node_statistics

    @property
    def statistics_across_all_nodes(self):
        """Gets the statistics_across_all_nodes of this NatStatisticsPerLogicalRouter.  # noqa: E501


        :return: The statistics_across_all_nodes of this NatStatisticsPerLogicalRouter.  # noqa: E501
        :rtype: NatCounters
        """
        return self._statistics_across_all_nodes

    @statistics_across_all_nodes.setter
    def statistics_across_all_nodes(self, statistics_across_all_nodes):
        """Sets the statistics_across_all_nodes of this NatStatisticsPerLogicalRouter.


        :param statistics_across_all_nodes: The statistics_across_all_nodes of this NatStatisticsPerLogicalRouter.  # noqa: E501
        :type: NatCounters
        """

        self._statistics_across_all_nodes = statistics_across_all_nodes

    @property
    def logical_router_id(self):
        """Gets the logical_router_id of this NatStatisticsPerLogicalRouter.  # noqa: E501

        Id for the logical router  # noqa: E501

        :return: The logical_router_id of this NatStatisticsPerLogicalRouter.  # noqa: E501
        :rtype: str
        """
        return self._logical_router_id

    @logical_router_id.setter
    def logical_router_id(self, logical_router_id):
        """Sets the logical_router_id of this NatStatisticsPerLogicalRouter.

        Id for the logical router  # noqa: E501

        :param logical_router_id: The logical_router_id of this NatStatisticsPerLogicalRouter.  # noqa: E501
        :type: str
        """

        self._logical_router_id = logical_router_id

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
        if issubclass(NatStatisticsPerLogicalRouter, dict):
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
        if not isinstance(other, NatStatisticsPerLogicalRouter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
