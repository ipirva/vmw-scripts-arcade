# VmToolsInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**vm_type** | **str** | Type of VM - Edge, Service or other. | [optional] 
**network_agent_version** | **str** | Version of network agent on the VM of a third party partner solution. | [optional] 
**host_local_id** | **str** | Id of the VM which is assigned locally by the host. It is the VM-moref on ESXi hosts, in other environments it is VM UUID. | [optional] 
**external_id** | **str** | Current external id of this virtual machine in the system. | [optional] 
**tools_version** | **str** | Version of VMTools installed on the VM. | [optional] 
**svm_connectivity** | **bool** | Endpoint Protection (Third party AV partner using NXGI) status on the VM. TRUE  - VM is configured and protected by EPP Service VM. FALSE - VM is either not configured for protection or VM is disconnected from EPP Service VM. | [optional] 
**file_agent_version** | **str** | Version of file agent on the VM of a third party partner solution. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

