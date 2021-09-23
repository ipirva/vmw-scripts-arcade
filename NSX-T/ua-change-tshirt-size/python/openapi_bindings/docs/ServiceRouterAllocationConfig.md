# ServiceRouterAllocationConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_cluster_member_indices** | **list[int]** | For TIER 1 logical router, for manual placement of service router within the cluster, edge cluster member indices needs to be provided else same will be auto-allocated. You can provide maximum two indices for HA ACTIVE_STANDBY.  | [optional] 
**allocation_pool** | [**EdgeClusterMemberAllocationPool**](EdgeClusterMemberAllocationPool.md) |  | [optional] 
**edge_cluster_id** | **str** | To reallocate TIER1 logical router on new or existing edge cluster  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

