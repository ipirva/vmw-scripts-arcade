# LbVariablePersistenceOnAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable_hash_enabled** | **bool** | The property is used to enable a hash operation for variable value when composing the persistence key.  | [optional] [default to False]
**variable_name** | **str** | The property is the name of variable to be used. It specifies which variable&#x27;s value of a HTTP Request will be used in the key of persistence entry. The variable can be a system embedded variable such as \&quot;_cookie_JSESSIONID\&quot;, a customized variable defined in LbVariableAssignmentAction or a captured variable in regular expression such as \&quot;article\&quot;.  | 
**persistence_profile_id** | **str** | If the persistence profile UUID is not specified, a default persistence table is created per virtual server. Currently, only LbGenericPersistenceProfile is supported.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

