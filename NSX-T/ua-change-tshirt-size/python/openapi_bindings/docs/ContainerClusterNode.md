# ContainerClusterNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_status** | **str** | Network status of container cluster node. | [optional] 
**container_cluster_id** | **str** | External identifier of the container cluster. | [optional] 
**ip_addresses** | **list[str]** | List of IP addresses of container cluster node. | [optional] 
**origin_properties** | [**list[KeyValuePair]**](KeyValuePair.md) | Array of additional specific properties of container cluster node in key-value format.  | [optional] 
**external_id** | **str** | External identifier of the container cluster node in K8S/PAS.  | 
**network_errors** | [**list[NetworkError]**](NetworkError.md) | List of network errors related to container cluster node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

