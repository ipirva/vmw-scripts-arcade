# DistributedVirtualSwitch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovered_nodes** | [**list[DiscoveredNode]**](DiscoveredNode.md) | Array of discovered nodes connected to this switch. | [optional] 
**uplink_portgroup** | [**DistributedVirtualPortgroup**](DistributedVirtualPortgroup.md) |  | [optional] 
**uuid** | **str** | UUID of the switch | [optional] 
**origin_properties** | [**list[KeyValuePair]**](KeyValuePair.md) | Key-Value map of additional properties of switch | [optional] 
**lacp_group_configs** | [**list[LacpGroupConfigInfo]**](LacpGroupConfigInfo.md) | It contains information about VMware specific multiple dynamic LACP groups.  | [optional] 
**uplink_port_names** | **list[str]** | The uniform name of uplink ports on each host. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

