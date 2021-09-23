# Snmpv2cTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**community_name** | **str** | Unique non-sensitive community name to identify community. | 
**community_string** | **str** | Community string (shared secret). This field is required when adding a community target. When updating a community target, do not include this field in the request. If this field is present in an update request, it will be considered as a new value for community string. | [optional] 
**port** | **int** | SNMP v2c target server&#x27;s port number. | [optional] [default to 162]
**server** | **str** | SNMP v2c target server&#x27;s IP or FQDN. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

