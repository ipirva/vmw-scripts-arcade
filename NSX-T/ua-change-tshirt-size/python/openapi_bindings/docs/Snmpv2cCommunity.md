# Snmpv2cCommunity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** | Access permissions for polling NSX nodes over SNMP v2c. | [optional] [default to 'READ_ONLY']
**community_name** | **str** | Unique, non-sensitive community name to identify community. | 
**community_string** | **str** | Community string. This is considered a shared secret and therefore sensitive information. This field is required when adding a community. When updating a community, do not include this field in the request. If this field is present in an update request, it will be considered as a new value for community string. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

