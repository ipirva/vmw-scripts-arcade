# LogicalRouterCentralizedServicePort

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked_logical_switch_port_id** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**subnets** | [**list[IPSubnet]**](IPSubnet.md) | Logical router port subnets | [optional] 
**enable_netx** | **bool** | Port is exclusively used for N-S service insertion | [optional] [default to False]
**urpf_mode** | **str** | Unicast Reverse Path Forwarding mode | [optional] [default to 'STRICT']
**ndra_profile_id** | **str** | Identifier of Neighbor Discovery Router Advertisement profile associated with port. When NDRA profile id is associated at both the port level and logical router level, the profile id specified at port level takes the precedence.  | [optional] 
**mtu** | **int** | Maximum transmission unit specifies the size of the largest packet that a network protocol can transmit. If not specified, the global logical MTU set in the /api/v1/global-configs/RoutingGlobalConfig API will be used.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

