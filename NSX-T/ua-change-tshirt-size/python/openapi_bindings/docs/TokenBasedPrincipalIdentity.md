# TokenBasedPrincipalIdentity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Unique node-id of a principal. This is used primarily in the case where a cluster of nodes is used to make calls to the NSX Manager and the same &#x27;name&#x27; is used so that the nodes can access and modify the same data while still accessing NSX through their individual secret (certificate or JWT). In all other cases this can be any string.  | 
**name** | **str** | Name of the principal. This will be matched to the name provided in the token. | 
**is_protected** | **bool** | Indicator whether the entities created by this principal should be protected. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

