# SnmpServiceProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v3_auth_protocol** | **str** | SNMP v3 auth protocol | [default to 'SHA1']
**communities** | **list[str]** | SNMP v1, v2c community strings | [optional] 
**v3_configured** | **bool** | SNMP v3 is configured or not | [optional] 
**v3_priv_protocol** | **str** | SNMP v3 private protocol | [default to 'AES128']
**v3_users** | [**list[SnmpV3User]**](SnmpV3User.md) | SNMP v3 users information | [optional] 
**v2_configured** | **bool** | SNMP v2 is configured or not | [optional] 
**start_on_boot** | **bool** | Start when system boots | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

