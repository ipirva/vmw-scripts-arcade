# IPSecVPNPolicyRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | [**list[IPSecVPNPolicySubnet]**](IPSecVPNPolicySubnet.md) | List of local subnets. | [optional] 
**action** | **str** | PROTECT - Protect rules are defined per policy based IPSec VPN session. BYPASS - Bypass rules are defined per IPSec VPN service and affects all policy based IPSec VPN sessions. Bypass rules are prioritized over protect rules.  | [optional] [default to 'PROTECT']
**enabled** | **bool** | A flag to enable/disable the policy rule. | [optional] [default to True]
**logged** | **bool** | A flag to enable/disable the logging for the policy rule. | [optional] [default to False]
**id** | **str** | Unique policy id. | [optional] 
**destinations** | [**list[IPSecVPNPolicySubnet]**](IPSecVPNPolicySubnet.md) | List of peer subnets. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

