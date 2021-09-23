# NicInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnet_mask** | **str** | Subnet mask associated with the NIC metadata. | [optional] 
**gateway_address** | **str** | Gateway address associated with the NIC metadata. | [optional] 
**ip_allocation_type** | **str** | IP allocation type with values STATIC, DHCP, or NONE indicating that IP address is not required. | [optional] 
**nic_metadata** | [**NicMetadata**](NicMetadata.md) |  | [optional] 
**network_id** | **str** | Network Id associated with the NIC metadata. It can be a moref, or a logical switch ID. If it is to be taken from &#x27;Agent VM Settings&#x27;, then it should be empty. | [optional] 
**ip_pool_id** | **str** | If the nic should get IP using a static IP pool then IP pool id should be provided here. | [optional] 
**ip_address** | **str** | IP address associated with the NIC metadata. Required only when assigning IP statically for a deployment that is for a single VM instance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

