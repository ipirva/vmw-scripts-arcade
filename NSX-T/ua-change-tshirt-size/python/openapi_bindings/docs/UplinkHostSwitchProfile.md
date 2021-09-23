# UplinkHostSwitchProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lags** | [**list[Lag]**](Lag.md) | list of LACP group | [optional] 
**transport_vlan** | **int** | VLAN used for tagging Overlay traffic of associated HostSwitch | [optional] [default to 0]
**teaming** | [**TeamingPolicy**](TeamingPolicy.md) |  | 
**overlay_encap** | **str** | The protocol used to encapsulate overlay traffic | [optional] [default to 'GENEVE']
**named_teamings** | [**list[NamedTeamingPolicy]**](NamedTeamingPolicy.md) | List of named uplink teaming policies that can be used by logical switches | [optional] 
**mtu** | **int** | Maximum Transmission Unit used for uplinks | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

