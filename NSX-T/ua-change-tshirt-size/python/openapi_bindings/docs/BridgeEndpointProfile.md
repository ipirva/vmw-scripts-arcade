# BridgeEndpointProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_mode** | **str** | Faileover mode can be preemmptive or non-preemptive | [optional] [default to 'PREEMPTIVE']
**edge_cluster_member_indexes** | **list[int]** | First index will be used as the preferred member | [optional] 
**high_availability_mode** | **str** | High avaialability mode can be active-active or active-standby | [optional] [default to 'ACTIVE_STANDBY']
**edge_cluster_id** | **str** | UUID of the edge cluster for this bridge endpoint | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

