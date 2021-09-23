# ManagementClusterStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The current status of the management cluster | [optional] 
**offline_nodes** | [**list[ManagementPlaneBaseNodeInfo]**](ManagementPlaneBaseNodeInfo.md) | Current missing management plane nodes | [optional] 
**required_members_for_initialization** | [**list[ClusterInitializationNodeInfo]**](ClusterInitializationNodeInfo.md) | The details of the cluster nodes required for cluster initialization | [optional] 
**online_nodes** | [**list[ManagementPlaneBaseNodeInfo]**](ManagementPlaneBaseNodeInfo.md) | Current alive management plane nodes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

