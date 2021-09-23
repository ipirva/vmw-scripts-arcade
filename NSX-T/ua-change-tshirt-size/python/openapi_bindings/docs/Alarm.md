# Alarm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_reported_time** | **int** | Indicates when the corresponding Event instance was last reported in milliseconds since epoch.  | [optional] 
**status** | **str** | Indicate the status which the Alarm is in.  | 
**entity_id** | **str** | The entity that the Event instance applies to. Note entity_id may not be included in a response body. For example, the cpu_high Event may not return an entity_id.  | [optional] 
**event_type** | **str** | Name of Event, e.g. manager_cpu_usage_high, certificate_expired.  | [optional] 
**recommended_action** | **str** | Recommended action for Alarm. This is the same action as the corresponding Event identified by feature_name.event_type.  | [optional] 
**severity** | **str** | Severity of the Alarm.Can be one of - CRITICAL, HIGH, MEDIUM, LOW.  | [optional] 
**node_id** | **str** | The UUID of the node that the Event instance applies to.  | [optional] 
**feature_name** | **str** | Feature defining this Event, e.g. manager_health, certificates.  | [optional] 
**resolved_by** | **str** | User ID of the user that set the status value to RESOLVED. This value can be SYSTEM to indicate that the system resolved the Alarm, for example when the system determines CPU usage is no longer high and the cpu_high Alarm is no longer applicable. This property is only returned when the status value is RESOLVED.  | [optional] 
**id** | **str** | ID that uniquely identifies an Alarm.  | [optional] 
**event_type_display_name** | **str** | Display name of Event type.  | [optional] 
**node_display_name** | **str** | Display name of node that the event instance applies to.  | [optional] 
**summary** | **str** | Summary description of Alarm. This is the same summary description as the corresponding Event identified by feature_name.event_type.  | [optional] 
**alarm_source_type** | **str** | Type of alarm source of the Event instance. Can be one of - INTENT_PATH, ENTITY_ID.  | [optional] 
**description** | **str** | Detailed description of Alarm. This is the same detailed description as the corresponding Event identified by feature_name.event_type.  | [optional] 
**node_resource_type** | **str** | The resource type of node that the Event instance applies to eg. ClusterNodeConfig, HostNode, EdgeNode.  | [optional] 
**alarm_source** | **list[str]** | If alarm_source_type &#x3D; INTENT_PATH, this field will contain a list of intent paths for the entity that the event instance applies to. If alarm_source_type &#x3D; ENTITY_ID, this field will contain a list with a single item identifying the entity id that the event instance applies to.  | [optional] 
**feature_display_name** | **str** | Display name of feature defining this Event.  | [optional] 
**suppressed_by** | **str** | User ID of the user that set the status value to SUPPRESSED. This property is only returned when the status value is SUPPRESSED.  | [optional] 
**suppress_start_time** | **int** | Indicates when the Alarm was suppressed in milliseconds since epoch. This property is only returned when the status value is SUPPRESSED.  | [optional] 
**resolved_time** | **int** | Indicates when the Alarm was resolved in milliseconds since epoch. This property is only returned when the status value is RESOLVED.  | [optional] 
**entity_resource_type** | **str** | The entity type that the Event instance applies to.  | [optional] 
**suppress_duration** | **int** | The time period between suppress_start_time and suppress_start_time + suppress_duration (specified in hours) an Alarm is SUPPRESSED. This property is only returned when the status value is SUPPRESSED.  | [optional] 
**node_ip_addresses** | **list[str]** | IP addresses of node that the event instance applies to.  | [optional] 
**reoccurrences_while_suppressed** | **int** | The number of reoccurrences since this alarm has been SUPPRESSED.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

