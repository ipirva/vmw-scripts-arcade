# L2VpnService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_full_mesh** | **bool** | Full mesh topology auto disables traffic replication between connected peers. However, this property is deprecated. Please refer enable_hub property instead to control client to client forwarding via the server. The value of enable_full_mesh will not be used anymore. If enable_hub is not provided explicitly, the default value of it will be used.  | [optional] [default to False]
**enable_hub** | **bool** | This property only applies in SERVER mode. If set to true, traffic from any client will be replicated to all other clients. If set to false, traffic received from clients is only replicated to the local VPN endpoint.  | [optional] [default to False]
**logical_router_id** | **str** | Logical router id | 
**mode** | **str** | Specify an L2VPN service mode as SERVER or CLIENT. L2VPN service in SERVER mode requires user to configure L2VPN session explicitly. L2VPN service in CLIENT mode can use peercode generated from SERVER to configure L2VPN session.  | [optional] [default to 'SERVER']
**logical_tap_ip_pool** | **list[str]** | IP Pool to allocate local and peer endpoint IPs for L2VpnSession logical Tap. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

