# LogicalRouterDownLinkPort

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnets** | [**list[IPSubnet]**](IPSubnet.md) | Logical router port subnets | 
**linked_logical_switch_port_id** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**ndra_profile_id** | **str** | Identifier of Neighbor Discovery Router Advertisement profile associated with port. When NDRA profile id is associated at both the port level and logical router level, the profile id specified at port level takes the precedence.  | [optional] 
**mac_address** | **str** | MAC address | [optional] 
**urpf_mode** | **str** | Unicast Reverse Path Forwarding mode | [optional] [default to 'STRICT']
**routing_policies** | [**list[RoutingPolicy]**](RoutingPolicy.md) | Routing policies used to specify how the traffic, which matches the policy routes, will be processed.  | [optional] 
**enable_multicast** | **bool** | If this flag is set to true - it will enable multicast on the downlink interface. If this flag is set to false - it will disable multicast on the downlink interface. This is supported only on Tier0 downlinks. Default value for Tier0 downlink will be true.  | [optional] 
**ndra_prefix_config** | [**list[NDRAPrefixConfig]**](NDRAPrefixConfig.md) | Configuration to override the neighbor discovery router advertisement prefix time parameters at the subnet level. Note that users are allowed to override the prefix time only for IPv6 subnets which are configured on the port.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

