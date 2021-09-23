# ServiceDeploymentConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_id** | **str** | Moref of the datastore in VC. If it is to be taken from &#x27;Agent VM Settings&#x27;, then it should be empty. | [optional] 
**host_id** | **str** | The service VM will be deployed on the specified host in the specified server within the cluster if host_id is specified. Note: You must ensure that storage and specified networks are accessible       by this host.  | [optional] 
**compute_collection_id** | **str** | Resource Pool or cluster Id. | 
**vm_nic_info** | [**VmNicInfo**](VmNicInfo.md) |  | [optional] 
**compute_manager_id** | **str** | Context Id or VCenter Id. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

