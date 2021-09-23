# Snmpv3User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priv_password** | **str** | Privacy password used for SNMP v3 communication. This field is required when adding a user. When updating a user, do not include this field in the request. If this field is present in an update request, it will be considered as a new value for privacy password. | [optional] 
**access** | **str** | Access permissions for polling NSX nodes over SNMP v3. | [optional] [default to 'READ_ONLY']
**auth_password** | **str** | Authentication password used for SNMP v3 communication. This field is required when adding a user. When updating a user, do not include this field in the request. If this field is present in an update request, it will be considered as a new value for authentication password. | [optional] 
**user_id** | **str** | Unique SNMP v3 user id. | 
**security_level** | **str** | Security level indicates whether SNMP communication involves authentication and privacy protocols for this user. Value \&quot;AUTH_PRIV\&quot; indicates both authentication and privacy protocols will be used for SNMP communication. | [optional] [default to 'AUTH_PRIV']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

