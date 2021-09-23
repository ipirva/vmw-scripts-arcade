# HealthCheckResultPerUplink

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uplink_name** | **str** | Name of the uplink. | [optional] 
**vlan_and_mtu_allowed** | [**list[HealthCheckVlanRange]**](HealthCheckVlanRange.md) | List of VLAN ID ranges which are allowed by VLAN and MTU settings.  | [optional] 
**vlan_disallowed** | [**list[HealthCheckVlanRange]**](HealthCheckVlanRange.md) | List of VLAN ID ranges which may be disallowed by VLAN settings.  | [optional] 
**mtu_disallowed** | [**list[HealthCheckVlanRange]**](HealthCheckVlanRange.md) | List of VLAN ID ranges which are allowed by VLAN settings but may be disallowed by MTU settings.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

