# ContainerCluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_status** | **str** | Network status of container cluster. | [optional] 
**infrastructure** | [**ContainerInfrastructureInfo**](ContainerInfrastructureInfo.md) |  | [optional] 
**cluster_type** | **str** | Type of the container cluster. In case of creating container cluster first time, it is expected to pass the valid cluster-type. In case of update, if there is no change in cluster-type, then this field can be omitted in the request.  | [optional] 
**origin_properties** | [**list[KeyValuePair]**](KeyValuePair.md) | Array of additional specific properties of container cluster in key-value format.  | [optional] 
**external_id** | **str** | External identifier of the container cluster. | [optional] 
**network_errors** | [**list[NetworkError]**](NetworkError.md) | List of network errors related to container cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

