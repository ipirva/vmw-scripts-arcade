# EdgeClusterInterSiteStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_update_timestamp** | **int** | Timestamp when the edge cluster inter-site status was last updated.  | [optional] 
**overall_status** | **str** | Overall status of all edge nodes IBGP status in the edge cluster.  | [optional] 
**edge_cluster_name** | **str** | Name of the edge cluster whose status is being reported. | [optional] 
**member_status** | [**list[EdgeClusterMemberInterSiteStatus]**](EdgeClusterMemberInterSiteStatus.md) | Per edge node inter-site status. | [optional] 
**edge_cluster_id** | **str** | Id of the edge cluster whose status is being reported. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

