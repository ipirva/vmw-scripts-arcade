# DiscoveredNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stateless** | **bool** | The stateless property describes whether host persists its state across reboot or not. If state persists, value is set as false otherwise true. | [optional] 
**parent_compute_collection** | **str** | External id of the compute collection to which this node belongs | [optional] 
**certificate** | **str** | Certificate of the discovered node | [optional] 
**origin_id** | **str** | Id of the compute manager from where this node was discovered | [optional] 
**ip_addresses** | **list[str]** | IP Addresses of the the discovered node. | [optional] 
**hardware_id** | **str** | Hardware Id is generated using system hardware info. It is used to retrieve fabric node of the esx. | [optional] 
**os_version** | **str** | OS version of the discovered node | [optional] 
**node_type** | **str** | Discovered Node type like Host | [optional] 
**os_type** | **str** | OS type of the discovered node | [optional] 
**origin_properties** | [**list[KeyValuePair]**](KeyValuePair.md) | Key-Value map of additional specific properties of discovered node in the Compute Manager  | [optional] 
**external_id** | **str** | External id of the discovered node, ex. a mo-ref from VC | [optional] 
**cm_local_id** | **str** | Local Id of the discovered node in the Compute Manager | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

