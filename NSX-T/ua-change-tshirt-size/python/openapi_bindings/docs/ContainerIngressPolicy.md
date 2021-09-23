# ContainerIngressPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_status** | **str** | Network status of container ingress. | [optional] 
**container_cluster_id** | **str** | Identifier of the container cluster this ingress policy belongs to. | [optional] 
**container_application_ids** | **list[str]** | List of identifiers of the container application , on which ingress policy is applied. e.g. IDs of all services on which the ingress is applied in kubernetes.  | [optional] 
**origin_properties** | [**list[KeyValuePair]**](KeyValuePair.md) | Array of additional specific properties of container ingress in key-value format.  | [optional] 
**external_id** | **str** | Identifier of the container ingress policy. | 
**container_project_id** | **str** | Identifier of the project which this container ingress belongs to. | [optional] 
**network_errors** | [**list[NetworkError]**](NetworkError.md) | List of network errors related to container ingress. | [optional] 
**spec** | **str** | Container ingress policy specification. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

