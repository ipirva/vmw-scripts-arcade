# MonitoringEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_threshold_fixed** | **bool** | Indicates if the threshold property is configurable via the API.  | [optional] 
**event_false_snmp_oid** | **str** | Optional field containing OID for SNMP trap sent when Event instance is False. This value is null if suppress_snmp_trap or suppress_clear_oid is True.  | [optional] 
**description_on_clear** | **str** | Description of Event when an Event instance transitions from True to False.  | [optional] 
**event_type** | **str** | Name of Event, e.g. manager_cpu_usage_high, certificate_expired.  | [optional] 
**recommended_action** | **str** | Recommended action for the alarm condition.  | [optional] 
**severity** | **str** | Severity of the Event.Can be one of - CRITICAL, HIGH, MEDIUM, LOW.  | [optional] 
**sensitivity** | **int** | Percentage of samples to consider and used in combination with threshold when determining whether an Event instance status is True or False. Event evaluation uses sampling to determine Event instance status. A higher sensitivity value specifies that more samples are used to ensure accuracy and ignore infrequent or rare spikes in sampled data.  | 
**is_disabled** | **bool** | Flag to indicate whether sampling for this Event is off or on.  | [optional] [default to False]
**suppress_alarm** | **bool** | Flag to suppress Alarm generation. Alarms are not generated for this Event when this is set to True.  | [optional] [default to False]
**summary** | **str** | Summary description of the event.  | [optional] 
**feature_display_name** | **str** | Display name of feature defining this Event.  | [optional] 
**entity_resource_type** | **str** | Resource Type of entity where this event is applicable eg. LogicalSwitch, LogicalPort etc.  | [optional] 
**feature_name** | **str** | Feature defining this Event, e.g. manager_health, certificates.  | [optional] 
**threshold** | **int** | Threshold to determine if a single sample is True. For example, if the configured threshold is 95% and the current CPU sample is 99%, then the current sample is considered True.  | 
**suppress_snmp_trap** | **bool** | Flag to suppress SNMP trap generation. SNMP traps are not sent for this Event when this is set to True.  | [optional] [default to False]
**event_type_display_name** | **str** | Display name of Event type.  | [optional] 
**is_sensitivity_fixed** | **bool** | Indicates if the sensitivity property is configurable via the API.  | [optional] 
**event_true_snmp_oid** | **str** | Optional field containing OID for SNMP trap sent when Event instance is True. This value is null if suppress_snmp_trap is True.  | [optional] 
**id** | **str** | Unique identifier in the form of feature_name.event_type.  | [optional] 
**node_types** | **list[str]** | Array identifying the nodes on which this Event is applicable. Can be one or more of the following values - nsx_public_cloud_gateway, nsx_edge, nsx_esx, nsx_kvm, nsx_manager.  | [optional] 
**description** | **str** | Detailed description of the event.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

