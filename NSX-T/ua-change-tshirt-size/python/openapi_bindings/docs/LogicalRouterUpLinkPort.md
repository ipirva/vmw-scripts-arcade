# LogicalRouterUpLinkPort

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnets** | [**list[IPSubnet]**](IPSubnet.md) | Logical router port subnets | 
**linked_logical_switch_port_id** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**ndra_prefix_config** | [**list[NDRAPrefixConfig]**](NDRAPrefixConfig.md) | Configuration to override the neighbor discovery router advertisement prefix time parameters at the subnet level. Note that users are allowed to override the prefix time only for IPv6 subnets which are configured on the port.  | [optional] 
**igmp_config** | [**InterfaceIgmpLocalGroupConfig**](InterfaceIgmpLocalGroupConfig.md) |  | [optional] 
**edge_cluster_member_index** | **list[int]** | Member index of the edge node on the cluster | 
**urpf_mode** | **str** | Unicast Reverse Path Forwarding mode | [optional] [default to 'STRICT']
**mac_address** | **str** | MAC address | [optional] 
**pim_config** | [**InterfacePimConfig**](InterfacePimConfig.md) |  | [optional] 
**ndra_profile_id** | **str** | Identifier of Neighbor Discovery Router Advertisement profile associated with port. When NDRA profile id is associated at both the port level and logical router level, the profile id specified at port level takes the precedence.  | [optional] 
**mtu** | **int** | Maximum transmission unit specifies the size of the largest packet that a network protocol can transmit. If not specified, the global logical MTU set in the /api/v1/global-configs/RoutingGlobalConfig API will be used.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

