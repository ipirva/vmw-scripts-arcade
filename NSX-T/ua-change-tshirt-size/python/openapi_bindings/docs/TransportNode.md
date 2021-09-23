# TransportNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_switch_spec** | [**HostSwitchSpec**](HostSwitchSpec.md) |  | [optional] 
**node_id** | **str** | Unique Id of the fabric node | [optional] 
**node_deployment_info** | [**Node**](Node.md) |  | [optional] 
**maintenance_mode** | **str** | The property is read-only, used for querying result. User could update transport node maintenance mode by UpdateTransportNodeMaintenanceMode call. | [optional] 
**failure_domain_id** | **str** | Set failure domain of edge transport node which will help in auto placement of TIER1 logical routers, DHCP Servers and MDProxies, if failure domain based allocation is enabled in edge cluster API. It is only supported for edge transport node and not for host transport node. In case failure domain is not set by user explicitly, it will be always assigned with default system created failure domain.  | [optional] 
**remote_tunnel_endpoint** | [**TransportNodeRemoteTunnelEndpointConfig**](TransportNodeRemoteTunnelEndpointConfig.md) |  | [optional] 
**is_overridden** | **bool** | This flag is relevant to only those hosts which are part of a compute collection which has transport node profile (TNP) applied on it. If you change the transport node configuration and it is different than cluster level TNP then this flag will be set to true  | [optional] 
**transport_zone_endpoints** | [**list[TransportZoneEndPoint]**](TransportZoneEndPoint.md) | This is deprecated. TransportZoneEndPoints should be specified per host switch at StandardHostSwitch through Transport Node or Transport Node Profile configuration. This will ONLY include the TransportZoneEndpoints that were were specified here during the TransportNode configuration. If TransportZoneEndpoints are specified directly in {$ref: StandardHostSwitch}, such TransportZoneEndpoints will not be populated here.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

