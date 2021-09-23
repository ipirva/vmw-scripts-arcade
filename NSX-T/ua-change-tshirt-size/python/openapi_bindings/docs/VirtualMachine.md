# VirtualMachine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**local_id_on_host** | **str** | Id of the vm unique within the host. | 
**type** | **str** | Virtual Machine type; Edge, Service VM or other. | [optional] 
**guest_info** | [**GuestInfo**](GuestInfo.md) |  | [optional] 
**power_state** | **str** | Current power state of this virtual machine in the system. | 
**compute_ids** | **list[str]** | List of external compute ids of the virtual machine in the format &#x27;id-type-key:value&#x27; , list of external compute ids [&#x27;uuid:xxxx-xxxx-xxxx-xxxx&#x27;, &#x27;moIdOnHost:moref-11&#x27;, &#x27;instanceUuid:xxxx-xxxx-xxxx-xxxx&#x27;] | 
**host_id** | **str** | Id of the host in which this virtual machine exists. | [optional] 
**external_id** | **str** | Current external id of this virtual machine in the system. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

