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
from swagger_client.models.traceflow_observation_dropped import TraceflowObservationDropped  # noqa: F401,E501

class TraceflowObservationDroppedLogical(TraceflowObservationDropped):
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
        'service_path_index': 'int',
        'component_id': 'str'
    }
    if hasattr(TraceflowObservationDropped, "swagger_types"):
        swagger_types.update(TraceflowObservationDropped.swagger_types)

    attribute_map = {
        'service_path_index': 'service_path_index',
        'component_id': 'component_id'
    }
    if hasattr(TraceflowObservationDropped, "attribute_map"):
        attribute_map.update(TraceflowObservationDropped.attribute_map)

    def __init__(self, service_path_index=None, component_id=None, *args, **kwargs):  # noqa: E501
        """TraceflowObservationDroppedLogical - a model defined in Swagger"""  # noqa: E501
        self._service_path_index = None
        self._component_id = None
        self.discriminator = None
        if service_path_index is not None:
            self.service_path_index = service_path_index
        if component_id is not None:
            self.component_id = component_id
        TraceflowObservationDropped.__init__(self, *args, **kwargs)

    @property
    def service_path_index(self):
        """Gets the service_path_index of this TraceflowObservationDroppedLogical.  # noqa: E501

        The index of service path that is a chain of services represents the point where the traceflow packet was dropped.   # noqa: E501

        :return: The service_path_index of this TraceflowObservationDroppedLogical.  # noqa: E501
        :rtype: int
        """
        return self._service_path_index

    @service_path_index.setter
    def service_path_index(self, service_path_index):
        """Sets the service_path_index of this TraceflowObservationDroppedLogical.

        The index of service path that is a chain of services represents the point where the traceflow packet was dropped.   # noqa: E501

        :param service_path_index: The service_path_index of this TraceflowObservationDroppedLogical.  # noqa: E501
        :type: int
        """

        self._service_path_index = service_path_index

    @property
    def component_id(self):
        """Gets the component_id of this TraceflowObservationDroppedLogical.  # noqa: E501

        The id of the component that dropped the traceflow packet.  # noqa: E501

        :return: The component_id of this TraceflowObservationDroppedLogical.  # noqa: E501
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this TraceflowObservationDroppedLogical.

        The id of the component that dropped the traceflow packet.  # noqa: E501

        :param component_id: The component_id of this TraceflowObservationDroppedLogical.  # noqa: E501
        :type: str
        """

        self._component_id = component_id

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
        if issubclass(TraceflowObservationDroppedLogical, dict):
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
        if not isinstance(other, TraceflowObservationDroppedLogical):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
