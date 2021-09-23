# NSGroupTagExpression

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_op** | **str** | Target_type VirtualMachine supports all specified operators for tag expression while LogicalSwitch and LogicalPort supports only EQUALS operator. All operators perform a case insensitive match.  | [optional] [default to 'EQUALS']
**scope** | **str** | The tag.scope attribute of the object | [optional] 
**scope_op** | **str** | Operator of the scope expression eg- tag.scope &#x3D; \&quot;S1\&quot;. | [optional] [default to 'EQUALS']
**tag** | **str** | The tag.tag attribute of the object | [optional] 
**target_type** | **str** | Type of the resource on which this expression is evaluated | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

