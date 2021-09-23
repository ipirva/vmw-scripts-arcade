# PBRRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Flag to disable rule. Disabled will only be persisted but never provisioned/realized. | [optional] [default to False]
**sources** | [**list[ResourceReference]**](ResourceReference.md) | List of sources. Null will be treated as any. | [optional] 
**rule_tag** | **str** | User level field which will be printed in CLI and packet logs. | [optional] 
**services** | [**list[PBRService]**](PBRService.md) | List of the services. Null will be treated as any. | [optional] 
**notes** | **str** | User notes specific to the rule. | [optional] 
**applied_tos** | [**list[ResourceReference]**](ResourceReference.md) | List of object where rule will be enforced. field overrides this one. Null will be treated as any. | [optional] 
**logged** | **bool** | Flag to enable packet logging. Default is disabled. | [optional] [default to False]
**action** | **str** | Action enforced on the packets which matches the PBR rule. | 
**destinations** | [**list[ResourceReference]**](ResourceReference.md) | List of the destinations. Null will be treated as any. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

