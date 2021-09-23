# DVSConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The DVS name | 
**lacp_group_configs** | [**list[LacpGroupConfigInfo]**](LacpGroupConfigInfo.md) | It contains information about VMware specific multiple dynamic LACP groups.  | [optional] 
**host_infra_traffic_res** | [**list[ResourceAllocation]**](ResourceAllocation.md) | host_infra_traffic_res specifies bandwidth allocation for various traffic resources.  | [optional] 
**uplink_port_names** | **list[str]** | Names of uplink ports for this DVS. | 
**uuid** | **str** | The DVS uuid | [optional] 
**lldp_send_enabled** | **bool** | Enabled or disabled sending LLDP packets | [optional] [default to False]
**mtu** | **int** | Maximum Transmission Unit used for uplinks | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

