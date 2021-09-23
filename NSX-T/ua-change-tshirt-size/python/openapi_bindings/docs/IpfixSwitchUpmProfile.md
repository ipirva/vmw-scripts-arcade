# IpfixSwitchUpmProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** | This priority field is used to resolve conflicts in logical ports/switch  which inherit multiple switch IPFIX profiles from NSGroups.  Override rule is : for multiple profiles inherited from NSGroups, the one with highest priority (lowest number) overrides others; the profile directly applied to logical switch overrides profiles inherited from NSGroup; the profile directly applied to logical port overides profiles inherited from logical switch and/or nsgroup;  The IPFIX exporter will send records to collectors of final effective profile only.  | 
**collector_profile** | **str** | Each IPFIX switching profile can have its own collector profile.  | 
**idle_timeout** | **int** | The time in seconds after a flow is expired if no more packets matching this flow are received by the cache.  | [optional] [default to 300]
**max_flows** | **int** | The maximum number of flow entries in each exporter flow cache.  | [optional] [default to 16384]
**observation_domain_id** | **int** | An identifier that is unique to the exporting process and used to meter the Flows.  | 
**active_timeout** | **int** | The time in seconds after a flow is expired even if more packets matching this Flow are received by the cache.  | [optional] [default to 300]
**export_overlay_flow** | **bool** | It controls whether sample result includes overlay flow info.  | [optional] [default to True]
**applied_tos** | [**AppliedTos**](AppliedTos.md) |  | [optional] 
**packet_sample_probability** | **float** | The probability in percentage that a packet is sampled. The value should be  in range (0,100] and can only have three decimal places at most. The probability  is equal for every packet.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

