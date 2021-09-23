# Snmpv3Target

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security_level** | **str** | Security level indicates whether SNMP communication involves authentication and privacy protocols for this user. Value \&quot;AUTH_PRIV\&quot; indicates both authentication and privacy protocols will be used for SNMP communication. | [optional] [default to 'AUTH_PRIV']
**user_id** | **str** | SNMP v3 user id used to notify target server. This SNMP v3 user should already be added in this profile. | 
**port** | **int** | SNMP v3 target server&#x27;s port. | [optional] [default to 162]
**server** | **str** | SNMP v3 target server&#x27;s IP or FQDN. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

