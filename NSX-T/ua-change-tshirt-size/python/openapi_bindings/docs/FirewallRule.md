# FirewallRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | [**list[FirewallService]**](FirewallService.md) | List of the services. Null will be treated as any. | [optional] 
**context_profiles** | [**list[ResourceReference]**](ResourceReference.md) | NS Profile object which accepts attributes and sub-attributes of various network services (ex. L7 AppId, domain name, encryption algorithm) as key value pairs. | [optional] 
**extended_sources** | [**list[ResourceReference]**](ResourceReference.md) | List of NSGroups that have end point attributes like AD Groups(SID), process name, process hash etc. For Flash release, only NSGroups containing AD Groups are supported. | [optional] 
**section_id** | **str** | Section Id of the section to which this rule belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

