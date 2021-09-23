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

class IPSecVPNSessionStatistics(object):
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
        'ike_traffic_statistics': 'IPSecVPNIKETrafficStatistics',
        'display_name': 'str',
        'policy_statistics': 'list[IPSecVPNPolicyTrafficStatistics]',
        'partial_stats': 'bool',
        'ipsec_vpn_session_id': 'str',
        'last_update_timestamp': 'int',
        'ike_status': 'IPSecVPNIKESessionStatus',
        'aggregate_traffic_counters': 'IPSecVPNTrafficCounters'
    }

    attribute_map = {
        'ike_traffic_statistics': 'ike_traffic_statistics',
        'display_name': 'display_name',
        'policy_statistics': 'policy_statistics',
        'partial_stats': 'partial_stats',
        'ipsec_vpn_session_id': 'ipsec_vpn_session_id',
        'last_update_timestamp': 'last_update_timestamp',
        'ike_status': 'ike_status',
        'aggregate_traffic_counters': 'aggregate_traffic_counters'
    }

    def __init__(self, ike_traffic_statistics=None, display_name=None, policy_statistics=None, partial_stats=None, ipsec_vpn_session_id=None, last_update_timestamp=None, ike_status=None, aggregate_traffic_counters=None):  # noqa: E501
        """IPSecVPNSessionStatistics - a model defined in Swagger"""  # noqa: E501
        self._ike_traffic_statistics = None
        self._display_name = None
        self._policy_statistics = None
        self._partial_stats = None
        self._ipsec_vpn_session_id = None
        self._last_update_timestamp = None
        self._ike_status = None
        self._aggregate_traffic_counters = None
        self.discriminator = None
        if ike_traffic_statistics is not None:
            self.ike_traffic_statistics = ike_traffic_statistics
        if display_name is not None:
            self.display_name = display_name
        if policy_statistics is not None:
            self.policy_statistics = policy_statistics
        if partial_stats is not None:
            self.partial_stats = partial_stats
        if ipsec_vpn_session_id is not None:
            self.ipsec_vpn_session_id = ipsec_vpn_session_id
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        if ike_status is not None:
            self.ike_status = ike_status
        if aggregate_traffic_counters is not None:
            self.aggregate_traffic_counters = aggregate_traffic_counters

    @property
    def ike_traffic_statistics(self):
        """Gets the ike_traffic_statistics of this IPSecVPNSessionStatistics.  # noqa: E501


        :return: The ike_traffic_statistics of this IPSecVPNSessionStatistics.  # noqa: E501
        :rtype: IPSecVPNIKETrafficStatistics
        """
        return self._ike_traffic_statistics

    @ike_traffic_statistics.setter
    def ike_traffic_statistics(self, ike_traffic_statistics):
        """Sets the ike_traffic_statistics of this IPSecVPNSessionStatistics.


        :param ike_traffic_statistics: The ike_traffic_statistics of this IPSecVPNSessionStatistics.  # noqa: E501
        :type: IPSecVPNIKETrafficStatistics
        """

        self._ike_traffic_statistics = ike_traffic_statistics

    @property
    def display_name(self):
        """Gets the display_name of this IPSecVPNSessionStatistics.  # noqa: E501

        Display name of vpn session.  # noqa: E501

        :return: The display_name of this IPSecVPNSessionStatistics.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this IPSecVPNSessionStatistics.

        Display name of vpn session.  # noqa: E501

        :param display_name: The display_name of this IPSecVPNSessionStatistics.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def policy_statistics(self):
        """Gets the policy_statistics of this IPSecVPNSessionStatistics.  # noqa: E501

        Gives aggregate traffic statistics across all ipsec tunnels and individual tunnel statistics.  # noqa: E501

        :return: The policy_statistics of this IPSecVPNSessionStatistics.  # noqa: E501
        :rtype: list[IPSecVPNPolicyTrafficStatistics]
        """
        return self._policy_statistics

    @policy_statistics.setter
    def policy_statistics(self, policy_statistics):
        """Sets the policy_statistics of this IPSecVPNSessionStatistics.

        Gives aggregate traffic statistics across all ipsec tunnels and individual tunnel statistics.  # noqa: E501

        :param policy_statistics: The policy_statistics of this IPSecVPNSessionStatistics.  # noqa: E501
        :type: list[IPSecVPNPolicyTrafficStatistics]
        """

        self._policy_statistics = policy_statistics

    @property
    def partial_stats(self):
        """Gets the partial_stats of this IPSecVPNSessionStatistics.  # noqa: E501

        Partial statistics if true specifies that the statistics are only from active node.  # noqa: E501

        :return: The partial_stats of this IPSecVPNSessionStatistics.  # noqa: E501
        :rtype: bool
        """
        return self._partial_stats

    @partial_stats.setter
    def partial_stats(self, partial_stats):
        """Sets the partial_stats of this IPSecVPNSessionStatistics.

        Partial statistics if true specifies that the statistics are only from active node.  # noqa: E501

        :param partial_stats: The partial_stats of this IPSecVPNSessionStatistics.  # noqa: E501
        :type: bool
        """

        self._partial_stats = partial_stats

    @property
    def ipsec_vpn_session_id(self):
        """Gets the ipsec_vpn_session_id of this IPSecVPNSessionStatistics.  # noqa: E501

        UUID of vpn session.  # noqa: E501

        :return: The ipsec_vpn_session_id of this IPSecVPNSessionStatistics.  # noqa: E501
        :rtype: str
        """
        return self._ipsec_vpn_session_id

    @ipsec_vpn_session_id.setter
    def ipsec_vpn_session_id(self, ipsec_vpn_session_id):
        """Sets the ipsec_vpn_session_id of this IPSecVPNSessionStatistics.

        UUID of vpn session.  # noqa: E501

        :param ipsec_vpn_session_id: The ipsec_vpn_session_id of this IPSecVPNSessionStatistics.  # noqa: E501
        :type: str
        """

        self._ipsec_vpn_session_id = ipsec_vpn_session_id

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this IPSecVPNSessionStatistics.  # noqa: E501

        Timestamp when the data was last updated.  # noqa: E501

        :return: The last_update_timestamp of this IPSecVPNSessionStatistics.  # noqa: E501
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this IPSecVPNSessionStatistics.

        Timestamp when the data was last updated.  # noqa: E501

        :param last_update_timestamp: The last_update_timestamp of this IPSecVPNSessionStatistics.  # noqa: E501
        :type: int
        """

        self._last_update_timestamp = last_update_timestamp

    @property
    def ike_status(self):
        """Gets the ike_status of this IPSecVPNSessionStatistics.  # noqa: E501


        :return: The ike_status of this IPSecVPNSessionStatistics.  # noqa: E501
        :rtype: IPSecVPNIKESessionStatus
        """
        return self._ike_status

    @ike_status.setter
    def ike_status(self, ike_status):
        """Sets the ike_status of this IPSecVPNSessionStatistics.


        :param ike_status: The ike_status of this IPSecVPNSessionStatistics.  # noqa: E501
        :type: IPSecVPNIKESessionStatus
        """

        self._ike_status = ike_status

    @property
    def aggregate_traffic_counters(self):
        """Gets the aggregate_traffic_counters of this IPSecVPNSessionStatistics.  # noqa: E501


        :return: The aggregate_traffic_counters of this IPSecVPNSessionStatistics.  # noqa: E501
        :rtype: IPSecVPNTrafficCounters
        """
        return self._aggregate_traffic_counters

    @aggregate_traffic_counters.setter
    def aggregate_traffic_counters(self, aggregate_traffic_counters):
        """Sets the aggregate_traffic_counters of this IPSecVPNSessionStatistics.


        :param aggregate_traffic_counters: The aggregate_traffic_counters of this IPSecVPNSessionStatistics.  # noqa: E501
        :type: IPSecVPNTrafficCounters
        """

        self._aggregate_traffic_counters = aggregate_traffic_counters

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
        if issubclass(IPSecVPNSessionStatistics, dict):
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
        if not isinstance(other, IPSecVPNSessionStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
