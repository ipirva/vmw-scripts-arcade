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

class LiveTraceActionConfig(object):
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
        'trace_config': 'TraceActionConfig',
        'pktcap_config': 'PktcapActionConfig',
        'count_config': 'CountActionConfig'
    }

    attribute_map = {
        'trace_config': 'trace_config',
        'pktcap_config': 'pktcap_config',
        'count_config': 'count_config'
    }

    def __init__(self, trace_config=None, pktcap_config=None, count_config=None):  # noqa: E501
        """LiveTraceActionConfig - a model defined in Swagger"""  # noqa: E501
        self._trace_config = None
        self._pktcap_config = None
        self._count_config = None
        self.discriminator = None
        if trace_config is not None:
            self.trace_config = trace_config
        if pktcap_config is not None:
            self.pktcap_config = pktcap_config
        if count_config is not None:
            self.count_config = count_config

    @property
    def trace_config(self):
        """Gets the trace_config of this LiveTraceActionConfig.  # noqa: E501


        :return: The trace_config of this LiveTraceActionConfig.  # noqa: E501
        :rtype: TraceActionConfig
        """
        return self._trace_config

    @trace_config.setter
    def trace_config(self, trace_config):
        """Sets the trace_config of this LiveTraceActionConfig.


        :param trace_config: The trace_config of this LiveTraceActionConfig.  # noqa: E501
        :type: TraceActionConfig
        """

        self._trace_config = trace_config

    @property
    def pktcap_config(self):
        """Gets the pktcap_config of this LiveTraceActionConfig.  # noqa: E501


        :return: The pktcap_config of this LiveTraceActionConfig.  # noqa: E501
        :rtype: PktcapActionConfig
        """
        return self._pktcap_config

    @pktcap_config.setter
    def pktcap_config(self, pktcap_config):
        """Sets the pktcap_config of this LiveTraceActionConfig.


        :param pktcap_config: The pktcap_config of this LiveTraceActionConfig.  # noqa: E501
        :type: PktcapActionConfig
        """

        self._pktcap_config = pktcap_config

    @property
    def count_config(self):
        """Gets the count_config of this LiveTraceActionConfig.  # noqa: E501


        :return: The count_config of this LiveTraceActionConfig.  # noqa: E501
        :rtype: CountActionConfig
        """
        return self._count_config

    @count_config.setter
    def count_config(self, count_config):
        """Sets the count_config of this LiveTraceActionConfig.


        :param count_config: The count_config of this LiveTraceActionConfig.  # noqa: E501
        :type: CountActionConfig
        """

        self._count_config = count_config

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
        if issubclass(LiveTraceActionConfig, dict):
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
        if not isinstance(other, LiveTraceActionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
