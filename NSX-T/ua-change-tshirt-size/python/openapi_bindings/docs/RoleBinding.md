# RoleBinding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_source_type** | **str** | Identity source type | [optional] [default to 'VIDM']
**name** | **str** | User/Group&#x27;s name | [optional] 
**roles** | [**list[Role]**](Role.md) | Roles | [optional] 
**type** | **str** | Type | [optional] 
**stale** | **str** | Property &#x27;stale&#x27; can be considered to have these values - absent  - This type of rolebinding does not support stale property TRUE    - Rolebinding is stale in vIDM meaning the user is no longer present in vIDM FALSE   - Rolebinding is available in vIDM UNKNOWN - Rolebinding&#x27;s state of staleness in unknown Once rolebindings become stale, they can be deleted using the API POST /aaa/role-bindings?action&#x3D;delete_stale_bindings | [optional] 
**identity_source_id** | **str** | The ID of the external identity source that holds the referenced external entity. Currently, only external LDAP and OIDC servers are allowed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

