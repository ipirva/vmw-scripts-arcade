# VdsTopology

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vds_status** | **str** | Status of the VDS configuration | [optional] 
**vmknic** | **list[str]** | Virtual network interfaces that will be moved from VLAN Logical switch to Distributed Virtual PortGroup | [optional] 
**transport_node_id** | **list[str]** | Transport node identifiers on which NVDS(s) being upgraded to VDS | 
**status_details** | **list[str]** | Details of the VDS configuration status | [optional] 
**vds_config** | [**DVSConfig**](DVSConfig.md) |  | [optional] 
**vds_name** | **str** | VDS name that will be created under above datacenter | 
**data_center_id** | **str** | Identifier of datacenter where VDS will be created | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

