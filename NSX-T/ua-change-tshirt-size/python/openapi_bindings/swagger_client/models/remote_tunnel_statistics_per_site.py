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

class RemoteTunnelStatisticsPerSite(object):
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
        'stats_per_tunnel': 'list[RemoteTunnelStatistics]',
        'remote_site': 'ResourceReference',
        'rx': 'InterSitePortCounters',
        'tx': 'InterSitePortCounters'
    }

    attribute_map = {
        'stats_per_tunnel': 'stats_per_tunnel',
        'remote_site': 'remote_site',
        'rx': 'rx',
        'tx': 'tx'
    }

    def __init__(self, stats_per_tunnel=None, remote_site=None, rx=None, tx=None):  # noqa: E501
        """RemoteTunnelStatisticsPerSite - a model defined in Swagger"""  # noqa: E501
        self._stats_per_tunnel = None
        self._remote_site = None
        self._rx = None
        self._tx = None
        self.discriminator = None
        if stats_per_tunnel is not None:
            self.stats_per_tunnel = stats_per_tunnel
        if remote_site is not None:
            self.remote_site = remote_site
        if rx is not None:
            self.rx = rx
        if tx is not None:
            self.tx = tx

    @property
    def stats_per_tunnel(self):
        """Gets the stats_per_tunnel of this RemoteTunnelStatisticsPerSite.  # noqa: E501

        Statistics per remote tunnel.  # noqa: E501

        :return: The stats_per_tunnel of this RemoteTunnelStatisticsPerSite.  # noqa: E501
        :rtype: list[RemoteTunnelStatistics]
        """
        return self._stats_per_tunnel

    @stats_per_tunnel.setter
    def stats_per_tunnel(self, stats_per_tunnel):
        """Sets the stats_per_tunnel of this RemoteTunnelStatisticsPerSite.

        Statistics per remote tunnel.  # noqa: E501

        :param stats_per_tunnel: The stats_per_tunnel of this RemoteTunnelStatisticsPerSite.  # noqa: E501
        :type: list[RemoteTunnelStatistics]
        """

        self._stats_per_tunnel = stats_per_tunnel

    @property
    def remote_site(self):
        """Gets the remote_site of this RemoteTunnelStatisticsPerSite.  # noqa: E501


        :return: The remote_site of this RemoteTunnelStatisticsPerSite.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._remote_site

    @remote_site.setter
    def remote_site(self, remote_site):
        """Sets the remote_site of this RemoteTunnelStatisticsPerSite.


        :param remote_site: The remote_site of this RemoteTunnelStatisticsPerSite.  # noqa: E501
        :type: ResourceReference
        """

        self._remote_site = remote_site

    @property
    def rx(self):
        """Gets the rx of this RemoteTunnelStatisticsPerSite.  # noqa: E501


        :return: The rx of this RemoteTunnelStatisticsPerSite.  # noqa: E501
        :rtype: InterSitePortCounters
        """
        return self._rx

    @rx.setter
    def rx(self, rx):
        """Sets the rx of this RemoteTunnelStatisticsPerSite.


        :param rx: The rx of this RemoteTunnelStatisticsPerSite.  # noqa: E501
        :type: InterSitePortCounters
        """

        self._rx = rx

    @property
    def tx(self):
        """Gets the tx of this RemoteTunnelStatisticsPerSite.  # noqa: E501


        :return: The tx of this RemoteTunnelStatisticsPerSite.  # noqa: E501
        :rtype: InterSitePortCounters
        """
        return self._tx

    @tx.setter
    def tx(self, tx):
        """Sets the tx of this RemoteTunnelStatisticsPerSite.


        :param tx: The tx of this RemoteTunnelStatisticsPerSite.  # noqa: E501
        :type: InterSitePortCounters
        """

        self._tx = tx

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
        if issubclass(RemoteTunnelStatisticsPerSite, dict):
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
        if not isinstance(other, RemoteTunnelStatisticsPerSite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other