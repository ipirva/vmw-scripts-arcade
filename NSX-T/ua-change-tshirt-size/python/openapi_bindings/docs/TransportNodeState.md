# TransportNodeState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_progress_state** | [**TransportNodeDeploymentProgressState**](TransportNodeDeploymentProgressState.md) |  | [optional] 
**transport_node_id** | **str** | Unique Id of the TransportNode | [optional] 
**remote_tunnel_endpoint_state** | [**RemoteTunnelEndpointConfigState**](RemoteTunnelEndpointConfigState.md) |  | [optional] 
**host_switch_states** | [**list[HostSwitchState]**](HostSwitchState.md) | States of HostSwitches on the host | [optional] 
**maintenance_mode_state** | **str** | the present realized maintenance mode state | [optional] 
**node_deployment_state** | [**ConfigurationState**](ConfigurationState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

