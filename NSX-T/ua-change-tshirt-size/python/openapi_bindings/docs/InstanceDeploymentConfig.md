# InstanceDeploymentConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_id** | **str** | Context Id or VCenter Id. | 
**vm_nic_infos** | [**list[VmNicInfo]**](VmNicInfo.md) | List of NIC information for VMs | 
**storage_id** | **str** | Storage Id. | 
**host_id** | **str** | The service VM will be deployed on the specified host in the specified server within the cluster if host_id is specified. Note: You must ensure that storage and specified networks are accessible by this host.  | [optional] 
**compute_id** | **str** | Resource Pool or Compute Id. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

