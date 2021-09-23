# AddControllerNodeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mpa_msg_client_info** | [**MsgClientInfo**](MsgClientInfo.md) |  | 
**host_msg_client_info** | [**MsgClientInfo**](MsgClientInfo.md) |  | 
**clustering_params** | [**ClusteringInfo**](ClusteringInfo.md) |  | [optional] 
**node_id** | **str** | Only use this if an id for the node already exists with MP. If not specified, then the node_id will be set to a random id. | [optional] 
**control_plane_server_certificate** | **str** | Deprecated. Do not supply a value for this property. | [optional] 
**type** | **str** | must be set to AddControllerNodeSpec | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

