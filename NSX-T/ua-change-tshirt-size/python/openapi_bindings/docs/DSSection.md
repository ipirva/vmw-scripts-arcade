# DSSection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stateful** | **bool** | Stateful or Stateless nature of distributed service section is enforced on all rules inside the section. Layer3 sections can be stateful or stateless. Layer2 sections can only be stateless. | 
**is_default** | **bool** | It is a boolean flag which reflects whether a distributed service section is default section or not. Each Layer 3 and Layer 2 section will have at least and at most one default section. | [optional] 
**applied_tos** | [**list[ResourceReference]**](ResourceReference.md) | List of objects where the rules in this section will be enforced. This will take precedence over rule level appliedTo. | [optional] 
**rule_count** | **int** | Number of rules in this section. | [optional] 
**section_type** | **str** | Type of the rules which a section can contain. Only homogeneous sections are supported. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

