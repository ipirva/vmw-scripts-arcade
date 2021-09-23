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

class Alarm(ManagedResource):
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
        'last_reported_time': 'int',
        'status': 'str',
        'entity_id': 'str',
        'event_type': 'str',
        'recommended_action': 'str',
        'severity': 'str',
        'node_id': 'str',
        'feature_name': 'str',
        'resolved_by': 'str',
        'id': 'str',
        'event_type_display_name': 'str',
        'node_display_name': 'str',
        'summary': 'str',
        'alarm_source_type': 'str',
        'description': 'str',
        'node_resource_type': 'str',
        'alarm_source': 'list[str]',
        'feature_display_name': 'str',
        'suppressed_by': 'str',
        'suppress_start_time': 'int',
        'resolved_time': 'int',
        'entity_resource_type': 'str',
        'suppress_duration': 'int',
        'node_ip_addresses': 'list[str]',
        'reoccurrences_while_suppressed': 'int'
    }
    if hasattr(ManagedResource, "swagger_types"):
        swagger_types.update(ManagedResource.swagger_types)

    attribute_map = {
        'last_reported_time': 'last_reported_time',
        'status': 'status',
        'entity_id': 'entity_id',
        'event_type': 'event_type',
        'recommended_action': 'recommended_action',
        'severity': 'severity',
        'node_id': 'node_id',
        'feature_name': 'feature_name',
        'resolved_by': 'resolved_by',
        'id': 'id',
        'event_type_display_name': 'event_type_display_name',
        'node_display_name': 'node_display_name',
        'summary': 'summary',
        'alarm_source_type': 'alarm_source_type',
        'description': 'description',
        'node_resource_type': 'node_resource_type',
        'alarm_source': 'alarm_source',
        'feature_display_name': 'feature_display_name',
        'suppressed_by': 'suppressed_by',
        'suppress_start_time': 'suppress_start_time',
        'resolved_time': 'resolved_time',
        'entity_resource_type': 'entity_resource_type',
        'suppress_duration': 'suppress_duration',
        'node_ip_addresses': 'node_ip_addresses',
        'reoccurrences_while_suppressed': 'reoccurrences_while_suppressed'
    }
    if hasattr(ManagedResource, "attribute_map"):
        attribute_map.update(ManagedResource.attribute_map)

    def __init__(self, last_reported_time=None, status=None, entity_id=None, event_type=None, recommended_action=None, severity=None, node_id=None, feature_name=None, resolved_by=None, id=None, event_type_display_name=None, node_display_name=None, summary=None, alarm_source_type=None, description=None, node_resource_type=None, alarm_source=None, feature_display_name=None, suppressed_by=None, suppress_start_time=None, resolved_time=None, entity_resource_type=None, suppress_duration=None, node_ip_addresses=None, reoccurrences_while_suppressed=None, *args, **kwargs):  # noqa: E501
        """Alarm - a model defined in Swagger"""  # noqa: E501
        self._last_reported_time = None
        self._status = None
        self._entity_id = None
        self._event_type = None
        self._recommended_action = None
        self._severity = None
        self._node_id = None
        self._feature_name = None
        self._resolved_by = None
        self._id = None
        self._event_type_display_name = None
        self._node_display_name = None
        self._summary = None
        self._alarm_source_type = None
        self._description = None
        self._node_resource_type = None
        self._alarm_source = None
        self._feature_display_name = None
        self._suppressed_by = None
        self._suppress_start_time = None
        self._resolved_time = None
        self._entity_resource_type = None
        self._suppress_duration = None
        self._node_ip_addresses = None
        self._reoccurrences_while_suppressed = None
        self.discriminator = None
        if last_reported_time is not None:
            self.last_reported_time = last_reported_time
        self.status = status
        if entity_id is not None:
            self.entity_id = entity_id
        if event_type is not None:
            self.event_type = event_type
        if recommended_action is not None:
            self.recommended_action = recommended_action
        if severity is not None:
            self.severity = severity
        if node_id is not None:
            self.node_id = node_id
        if feature_name is not None:
            self.feature_name = feature_name
        if resolved_by is not None:
            self.resolved_by = resolved_by
        if id is not None:
            self.id = id
        if event_type_display_name is not None:
            self.event_type_display_name = event_type_display_name
        if node_display_name is not None:
            self.node_display_name = node_display_name
        if summary is not None:
            self.summary = summary
        if alarm_source_type is not None:
            self.alarm_source_type = alarm_source_type
        if description is not None:
            self.description = description
        if node_resource_type is not None:
            self.node_resource_type = node_resource_type
        if alarm_source is not None:
            self.alarm_source = alarm_source
        if feature_display_name is not None:
            self.feature_display_name = feature_display_name
        if suppressed_by is not None:
            self.suppressed_by = suppressed_by
        if suppress_start_time is not None:
            self.suppress_start_time = suppress_start_time
        if resolved_time is not None:
            self.resolved_time = resolved_time
        if entity_resource_type is not None:
            self.entity_resource_type = entity_resource_type
        if suppress_duration is not None:
            self.suppress_duration = suppress_duration
        if node_ip_addresses is not None:
            self.node_ip_addresses = node_ip_addresses
        if reoccurrences_while_suppressed is not None:
            self.reoccurrences_while_suppressed = reoccurrences_while_suppressed
        ManagedResource.__init__(self, *args, **kwargs)

    @property
    def last_reported_time(self):
        """Gets the last_reported_time of this Alarm.  # noqa: E501

        Indicates when the corresponding Event instance was last reported in milliseconds since epoch.   # noqa: E501

        :return: The last_reported_time of this Alarm.  # noqa: E501
        :rtype: int
        """
        return self._last_reported_time

    @last_reported_time.setter
    def last_reported_time(self, last_reported_time):
        """Sets the last_reported_time of this Alarm.

        Indicates when the corresponding Event instance was last reported in milliseconds since epoch.   # noqa: E501

        :param last_reported_time: The last_reported_time of this Alarm.  # noqa: E501
        :type: int
        """

        self._last_reported_time = last_reported_time

    @property
    def status(self):
        """Gets the status of this Alarm.  # noqa: E501

        Indicate the status which the Alarm is in.   # noqa: E501

        :return: The status of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Alarm.

        Indicate the status which the Alarm is in.   # noqa: E501

        :param status: The status of this Alarm.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["OPEN", "ACKNOWLEDGED", "SUPPRESSED", "RESOLVED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def entity_id(self):
        """Gets the entity_id of this Alarm.  # noqa: E501

        The entity that the Event instance applies to. Note entity_id may not be included in a response body. For example, the cpu_high Event may not return an entity_id.   # noqa: E501

        :return: The entity_id of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this Alarm.

        The entity that the Event instance applies to. Note entity_id may not be included in a response body. For example, the cpu_high Event may not return an entity_id.   # noqa: E501

        :param entity_id: The entity_id of this Alarm.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def event_type(self):
        """Gets the event_type of this Alarm.  # noqa: E501

        Name of Event, e.g. manager_cpu_usage_high, certificate_expired.   # noqa: E501

        :return: The event_type of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this Alarm.

        Name of Event, e.g. manager_cpu_usage_high, certificate_expired.   # noqa: E501

        :param event_type: The event_type of this Alarm.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def recommended_action(self):
        """Gets the recommended_action of this Alarm.  # noqa: E501

        Recommended action for Alarm. This is the same action as the corresponding Event identified by feature_name.event_type.   # noqa: E501

        :return: The recommended_action of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._recommended_action

    @recommended_action.setter
    def recommended_action(self, recommended_action):
        """Sets the recommended_action of this Alarm.

        Recommended action for Alarm. This is the same action as the corresponding Event identified by feature_name.event_type.   # noqa: E501

        :param recommended_action: The recommended_action of this Alarm.  # noqa: E501
        :type: str
        """

        self._recommended_action = recommended_action

    @property
    def severity(self):
        """Gets the severity of this Alarm.  # noqa: E501

        Severity of the Alarm.Can be one of - CRITICAL, HIGH, MEDIUM, LOW.   # noqa: E501

        :return: The severity of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Alarm.

        Severity of the Alarm.Can be one of - CRITICAL, HIGH, MEDIUM, LOW.   # noqa: E501

        :param severity: The severity of this Alarm.  # noqa: E501
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def node_id(self):
        """Gets the node_id of this Alarm.  # noqa: E501

        The UUID of the node that the Event instance applies to.   # noqa: E501

        :return: The node_id of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this Alarm.

        The UUID of the node that the Event instance applies to.   # noqa: E501

        :param node_id: The node_id of this Alarm.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def feature_name(self):
        """Gets the feature_name of this Alarm.  # noqa: E501

        Feature defining this Event, e.g. manager_health, certificates.   # noqa: E501

        :return: The feature_name of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._feature_name

    @feature_name.setter
    def feature_name(self, feature_name):
        """Sets the feature_name of this Alarm.

        Feature defining this Event, e.g. manager_health, certificates.   # noqa: E501

        :param feature_name: The feature_name of this Alarm.  # noqa: E501
        :type: str
        """

        self._feature_name = feature_name

    @property
    def resolved_by(self):
        """Gets the resolved_by of this Alarm.  # noqa: E501

        User ID of the user that set the status value to RESOLVED. This value can be SYSTEM to indicate that the system resolved the Alarm, for example when the system determines CPU usage is no longer high and the cpu_high Alarm is no longer applicable. This property is only returned when the status value is RESOLVED.   # noqa: E501

        :return: The resolved_by of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._resolved_by

    @resolved_by.setter
    def resolved_by(self, resolved_by):
        """Sets the resolved_by of this Alarm.

        User ID of the user that set the status value to RESOLVED. This value can be SYSTEM to indicate that the system resolved the Alarm, for example when the system determines CPU usage is no longer high and the cpu_high Alarm is no longer applicable. This property is only returned when the status value is RESOLVED.   # noqa: E501

        :param resolved_by: The resolved_by of this Alarm.  # noqa: E501
        :type: str
        """

        self._resolved_by = resolved_by

    @property
    def id(self):
        """Gets the id of this Alarm.  # noqa: E501

        ID that uniquely identifies an Alarm.   # noqa: E501

        :return: The id of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Alarm.

        ID that uniquely identifies an Alarm.   # noqa: E501

        :param id: The id of this Alarm.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def event_type_display_name(self):
        """Gets the event_type_display_name of this Alarm.  # noqa: E501

        Display name of Event type.   # noqa: E501

        :return: The event_type_display_name of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._event_type_display_name

    @event_type_display_name.setter
    def event_type_display_name(self, event_type_display_name):
        """Sets the event_type_display_name of this Alarm.

        Display name of Event type.   # noqa: E501

        :param event_type_display_name: The event_type_display_name of this Alarm.  # noqa: E501
        :type: str
        """

        self._event_type_display_name = event_type_display_name

    @property
    def node_display_name(self):
        """Gets the node_display_name of this Alarm.  # noqa: E501

        Display name of node that the event instance applies to.   # noqa: E501

        :return: The node_display_name of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._node_display_name

    @node_display_name.setter
    def node_display_name(self, node_display_name):
        """Sets the node_display_name of this Alarm.

        Display name of node that the event instance applies to.   # noqa: E501

        :param node_display_name: The node_display_name of this Alarm.  # noqa: E501
        :type: str
        """

        self._node_display_name = node_display_name

    @property
    def summary(self):
        """Gets the summary of this Alarm.  # noqa: E501

        Summary description of Alarm. This is the same summary description as the corresponding Event identified by feature_name.event_type.   # noqa: E501

        :return: The summary of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Alarm.

        Summary description of Alarm. This is the same summary description as the corresponding Event identified by feature_name.event_type.   # noqa: E501

        :param summary: The summary of this Alarm.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def alarm_source_type(self):
        """Gets the alarm_source_type of this Alarm.  # noqa: E501

        Type of alarm source of the Event instance. Can be one of - INTENT_PATH, ENTITY_ID.   # noqa: E501

        :return: The alarm_source_type of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._alarm_source_type

    @alarm_source_type.setter
    def alarm_source_type(self, alarm_source_type):
        """Sets the alarm_source_type of this Alarm.

        Type of alarm source of the Event instance. Can be one of - INTENT_PATH, ENTITY_ID.   # noqa: E501

        :param alarm_source_type: The alarm_source_type of this Alarm.  # noqa: E501
        :type: str
        """
        allowed_values = ["INTENT_PATH", "ENTITY_ID"]  # noqa: E501
        if alarm_source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `alarm_source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(alarm_source_type, allowed_values)
            )

        self._alarm_source_type = alarm_source_type

    @property
    def description(self):
        """Gets the description of this Alarm.  # noqa: E501

        Detailed description of Alarm. This is the same detailed description as the corresponding Event identified by feature_name.event_type.   # noqa: E501

        :return: The description of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Alarm.

        Detailed description of Alarm. This is the same detailed description as the corresponding Event identified by feature_name.event_type.   # noqa: E501

        :param description: The description of this Alarm.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def node_resource_type(self):
        """Gets the node_resource_type of this Alarm.  # noqa: E501

        The resource type of node that the Event instance applies to eg. ClusterNodeConfig, HostNode, EdgeNode.   # noqa: E501

        :return: The node_resource_type of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._node_resource_type

    @node_resource_type.setter
    def node_resource_type(self, node_resource_type):
        """Sets the node_resource_type of this Alarm.

        The resource type of node that the Event instance applies to eg. ClusterNodeConfig, HostNode, EdgeNode.   # noqa: E501

        :param node_resource_type: The node_resource_type of this Alarm.  # noqa: E501
        :type: str
        """

        self._node_resource_type = node_resource_type

    @property
    def alarm_source(self):
        """Gets the alarm_source of this Alarm.  # noqa: E501

        If alarm_source_type = INTENT_PATH, this field will contain a list of intent paths for the entity that the event instance applies to. If alarm_source_type = ENTITY_ID, this field will contain a list with a single item identifying the entity id that the event instance applies to.   # noqa: E501

        :return: The alarm_source of this Alarm.  # noqa: E501
        :rtype: list[str]
        """
        return self._alarm_source

    @alarm_source.setter
    def alarm_source(self, alarm_source):
        """Sets the alarm_source of this Alarm.

        If alarm_source_type = INTENT_PATH, this field will contain a list of intent paths for the entity that the event instance applies to. If alarm_source_type = ENTITY_ID, this field will contain a list with a single item identifying the entity id that the event instance applies to.   # noqa: E501

        :param alarm_source: The alarm_source of this Alarm.  # noqa: E501
        :type: list[str]
        """

        self._alarm_source = alarm_source

    @property
    def feature_display_name(self):
        """Gets the feature_display_name of this Alarm.  # noqa: E501

        Display name of feature defining this Event.   # noqa: E501

        :return: The feature_display_name of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._feature_display_name

    @feature_display_name.setter
    def feature_display_name(self, feature_display_name):
        """Sets the feature_display_name of this Alarm.

        Display name of feature defining this Event.   # noqa: E501

        :param feature_display_name: The feature_display_name of this Alarm.  # noqa: E501
        :type: str
        """

        self._feature_display_name = feature_display_name

    @property
    def suppressed_by(self):
        """Gets the suppressed_by of this Alarm.  # noqa: E501

        User ID of the user that set the status value to SUPPRESSED. This property is only returned when the status value is SUPPRESSED.   # noqa: E501

        :return: The suppressed_by of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._suppressed_by

    @suppressed_by.setter
    def suppressed_by(self, suppressed_by):
        """Sets the suppressed_by of this Alarm.

        User ID of the user that set the status value to SUPPRESSED. This property is only returned when the status value is SUPPRESSED.   # noqa: E501

        :param suppressed_by: The suppressed_by of this Alarm.  # noqa: E501
        :type: str
        """

        self._suppressed_by = suppressed_by

    @property
    def suppress_start_time(self):
        """Gets the suppress_start_time of this Alarm.  # noqa: E501

        Indicates when the Alarm was suppressed in milliseconds since epoch. This property is only returned when the status value is SUPPRESSED.   # noqa: E501

        :return: The suppress_start_time of this Alarm.  # noqa: E501
        :rtype: int
        """
        return self._suppress_start_time

    @suppress_start_time.setter
    def suppress_start_time(self, suppress_start_time):
        """Sets the suppress_start_time of this Alarm.

        Indicates when the Alarm was suppressed in milliseconds since epoch. This property is only returned when the status value is SUPPRESSED.   # noqa: E501

        :param suppress_start_time: The suppress_start_time of this Alarm.  # noqa: E501
        :type: int
        """

        self._suppress_start_time = suppress_start_time

    @property
    def resolved_time(self):
        """Gets the resolved_time of this Alarm.  # noqa: E501

        Indicates when the Alarm was resolved in milliseconds since epoch. This property is only returned when the status value is RESOLVED.   # noqa: E501

        :return: The resolved_time of this Alarm.  # noqa: E501
        :rtype: int
        """
        return self._resolved_time

    @resolved_time.setter
    def resolved_time(self, resolved_time):
        """Sets the resolved_time of this Alarm.

        Indicates when the Alarm was resolved in milliseconds since epoch. This property is only returned when the status value is RESOLVED.   # noqa: E501

        :param resolved_time: The resolved_time of this Alarm.  # noqa: E501
        :type: int
        """

        self._resolved_time = resolved_time

    @property
    def entity_resource_type(self):
        """Gets the entity_resource_type of this Alarm.  # noqa: E501

        The entity type that the Event instance applies to.   # noqa: E501

        :return: The entity_resource_type of this Alarm.  # noqa: E501
        :rtype: str
        """
        return self._entity_resource_type

    @entity_resource_type.setter
    def entity_resource_type(self, entity_resource_type):
        """Sets the entity_resource_type of this Alarm.

        The entity type that the Event instance applies to.   # noqa: E501

        :param entity_resource_type: The entity_resource_type of this Alarm.  # noqa: E501
        :type: str
        """

        self._entity_resource_type = entity_resource_type

    @property
    def suppress_duration(self):
        """Gets the suppress_duration of this Alarm.  # noqa: E501

        The time period between suppress_start_time and suppress_start_time + suppress_duration (specified in hours) an Alarm is SUPPRESSED. This property is only returned when the status value is SUPPRESSED.   # noqa: E501

        :return: The suppress_duration of this Alarm.  # noqa: E501
        :rtype: int
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        """Sets the suppress_duration of this Alarm.

        The time period between suppress_start_time and suppress_start_time + suppress_duration (specified in hours) an Alarm is SUPPRESSED. This property is only returned when the status value is SUPPRESSED.   # noqa: E501

        :param suppress_duration: The suppress_duration of this Alarm.  # noqa: E501
        :type: int
        """

        self._suppress_duration = suppress_duration

    @property
    def node_ip_addresses(self):
        """Gets the node_ip_addresses of this Alarm.  # noqa: E501

        IP addresses of node that the event instance applies to.   # noqa: E501

        :return: The node_ip_addresses of this Alarm.  # noqa: E501
        :rtype: list[str]
        """
        return self._node_ip_addresses

    @node_ip_addresses.setter
    def node_ip_addresses(self, node_ip_addresses):
        """Sets the node_ip_addresses of this Alarm.

        IP addresses of node that the event instance applies to.   # noqa: E501

        :param node_ip_addresses: The node_ip_addresses of this Alarm.  # noqa: E501
        :type: list[str]
        """

        self._node_ip_addresses = node_ip_addresses

    @property
    def reoccurrences_while_suppressed(self):
        """Gets the reoccurrences_while_suppressed of this Alarm.  # noqa: E501

        The number of reoccurrences since this alarm has been SUPPRESSED.   # noqa: E501

        :return: The reoccurrences_while_suppressed of this Alarm.  # noqa: E501
        :rtype: int
        """
        return self._reoccurrences_while_suppressed

    @reoccurrences_while_suppressed.setter
    def reoccurrences_while_suppressed(self, reoccurrences_while_suppressed):
        """Sets the reoccurrences_while_suppressed of this Alarm.

        The number of reoccurrences since this alarm has been SUPPRESSED.   # noqa: E501

        :param reoccurrences_while_suppressed: The reoccurrences_while_suppressed of this Alarm.  # noqa: E501
        :type: int
        """

        self._reoccurrences_while_suppressed = reoccurrences_while_suppressed

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
        if issubclass(Alarm, dict):
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
        if not isinstance(other, Alarm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
