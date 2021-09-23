# IPSecVPNService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ike_log_level** | **str** | Log level for internet key exchange (IKE). | [optional] [default to 'INFO']
**logical_router_id** | **str** | Logical router id. | 
**ipsec_ha_sync** | **bool** | Enable/disable IPSec HA state sync. IPSec HA state sync can be disabled in case there are performance issues with the state sync messages. Default is to enable HA Sync.  | [optional] [default to True]
**bypass_rules** | [**list[IPSecVPNPolicyRule]**](IPSecVPNPolicyRule.md) | Bypass policy rules are configured using VPN service. Bypass rules always have higher priority over protect rules and they affect all policy based vpn sessions associated with the IPSec VPN service. Protect rules are defined per policy based vpn session.  | [optional] 
**enabled** | **bool** | If true, enable VPN services for given logical router. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

