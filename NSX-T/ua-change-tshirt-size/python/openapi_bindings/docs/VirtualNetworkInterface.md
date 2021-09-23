# VirtualNetworkInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_address** | **str** | MAC address of the virtual network interface. | 
**owner_vm_type** | **str** | Owner virtual machine type; Edge, Service VM or other. | [optional] 
**device_key** | **str** | Device key of the virtual network interface. | 
**host_id** | **str** | Id of the host on which the vm exists. | 
**owner_vm_id** | **str** | Id of the vm to which this virtual network interface belongs. | 
**vm_local_id_on_host** | **str** | Id of the vm unique within the host. | 
**external_id** | **str** | External Id of the virtual network inferface. | 
**lport_attachment_id** | **str** | LPort Attachment Id of the virtual network interface. | [optional] 
**ip_address_info** | [**list[IpAddressInfo]**](IpAddressInfo.md) | IP Addresses of the the virtual network interface, from various sources. | [optional] 
**device_name** | **str** | Device name of the virtual network interface. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

