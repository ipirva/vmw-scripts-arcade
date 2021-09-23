# DnsForwarderStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | UP means the DNS forwarder is working correctly on the active transport node and the stand-by transport node (if present). Failover will occur if either node goes down. DOWN means the DNS forwarder is down on both active transport node and standby node (if present). The DNS forwarder does not function in this situation. Error means there is some error on one or both transport node, or no status was reported from one or both transport nodes. The dns forwarder may be working (or not working). NO_BACKUP means dns forwarder is working in only one transport node, either because it is down on the standby node, or no standby is configured. An forwarder outage will occur if the active node goes down.  | [optional] 
**timestamp** | **int** | Time stamp of the current status, in ms | [optional] 
**standby_node** | **str** | Uuid of stand_by transport node. null if non-HA mode | [optional] 
**extra_message** | **str** | Extra message, if available | [optional] 
**active_node** | **str** | Uuid of active transport node | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

