# EdgeMemberAllocationStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated_services** | [**list[AllocatedService]**](AllocatedService.md) | List of services allocated on the edge node. | [optional] 
**node_display_name** | **str** | Display name of edge cluster member. Defaults to ID if not set.  | [optional] 
**member_index** | **int** | System generated index for transport node backed by edge node.  | [optional] 
**allocation_pools** | [**list[AllocationPool]**](AllocationPool.md) | Allocation details of pools defined on the edge node. | [optional] 
**node_id** | **str** | System allotted UUID of edge node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

