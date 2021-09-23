# TransportNodeRemoteTunnelEndpointConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**named_teaming_policy** | **str** | Specifying this field will override the default teaming policy of the host switch and will be used by remote tunnel endpoint traffic. | [optional] 
**host_switch_name** | **str** | The host switch name should reference an existing host switch specified in the transport node configuration. The name will be used to identify the host switch responsible for processing remote tunnel endpoint traffic. | 
**rtep_vlan** | **int** | The transport VLAN id used for tagging intersite overlay traffic between remote tunnel endpoints. | 
**ip_assignment_spec** | [**IpAssignmentSpec**](IpAssignmentSpec.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

