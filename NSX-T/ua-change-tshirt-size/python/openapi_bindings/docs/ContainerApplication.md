# ContainerApplication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the container application. | [optional] 
**network_status** | **str** | Network status of container application. | [optional] 
**container_cluster_id** | **str** | Identifier of the container cluster this container application belongs to. | [optional] 
**origin_properties** | [**list[KeyValuePair]**](KeyValuePair.md) | Array of additional specific properties of container application in key-value format.  | [optional] 
**external_id** | **str** | Identifier of the container application on container cluster e.g. PCF app id, k8s service id.  | 
**container_project_id** | **str** | Identifier of the project which this container application belongs to. | [optional] 
**network_errors** | [**list[NetworkError]**](NetworkError.md) | List of network errors related to container application. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

