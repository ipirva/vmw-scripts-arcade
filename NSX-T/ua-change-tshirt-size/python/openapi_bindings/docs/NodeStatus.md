# NodeStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mpa_connectivity_status** | **str** | Indicates the fabric node&#x27;s MP&amp;lt;-&amp;gt;MPA channel connectivity status, UP, DOWN, UNKNOWN. | [optional] 
**lcp_connectivity_status_details** | [**list[ControlConnStatus]**](ControlConnStatus.md) | Details, if any, about the current LCP&amp;lt;-&amp;gt;CCP channel connectivity status of the fabric node. | [optional] 
**mpa_connectivity_status_details** | **str** | Details, if any, about the current MP&amp;lt;-&amp;gt;MPA channel connectivity status of the fabric node. | [optional] 
**external_id** | **str** | HostNode external id | [optional] 
**software_version** | **str** | Software version of the fabric node. | [optional] 
**maintenance_mode** | **str** | Indicates the fabric node&#x27;s status of maintenance mode, OFF, ENTERING, ON, EXITING. | [optional] 
**inventory_sync_paused** | **bool** | Is true if inventory sync is paused else false | [optional] 
**system_status** | [**NodeStatusProperties**](NodeStatusProperties.md) |  | [optional] 
**inventory_sync_reenable_time** | **int** | Inventory sync auto re-enable target time, in epoch milis | [optional] 
**lcp_connectivity_status** | **str** | Indicates the fabric node&#x27;s LCP&amp;lt;-&amp;gt;CCP channel connectivity status, UP, DOWN, DEGRADED, UNKNOWN. | [optional] [default to 'UNKNOWN']
**last_heartbeat_timestamp** | **int** | Timestamp of the last heartbeat status change, in epoch milliseconds. | [optional] 
**last_sync_time** | **int** | Timestamp of the last successful update of Inventory, in epoch milliseconds. | [optional] 
**host_node_deployment_status** | **str** | This enum specifies the current nsx install state for host node or current deployment and ready state for edge node. The ready status &#x27;NODE_READY&#x27; indicates whether edge node is ready to become a transport node. The status &#x27;EDGE_CONFIG_ERROR&#x27; indicates that edge hardware or underlying host is not supported. After all fabric level operations are done for an edge node, this value indicates transport node related configuration issues and state as relevant.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

