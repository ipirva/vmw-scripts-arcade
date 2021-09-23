# ServiceInsertionRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | [**list[ServiceInsertionService]**](ServiceInsertionService.md) | List of the services. Null will be treated as any. | [optional] 
**redirect_tos** | [**list[ResourceReference]**](ResourceReference.md) | A rule can be redirected to ServiceInstance, InstanceEndpoint for North/South Traffic. A rule can be redirected to ServiceChain for East/West Traffic. For REDIRECT action, redirect_tos is mandatory. For DO_NOT_REDIRECT action, redirect_tos is optional. | [optional] 
**section_id** | **str** | ID of the section to which this rule belongs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

