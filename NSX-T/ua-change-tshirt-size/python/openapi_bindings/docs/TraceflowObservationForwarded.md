# TraceflowObservationForwarded

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uplink_name** | **str** | The name of the uplink the traceflow packet is forwarded on | [optional] 
**vtep_label** | **int** | The virtual tunnel endpoint label | [optional] 
**remote_ip_address** | **str** | IP address of the destination end of the tunnel | [optional] 
**context** | **int** | The 64bit tunnel context carried on the wire | [optional] 
**local_ip_address** | **str** | IP address of the source end of the tunnel | [optional] 
**dst_transport_node_id** | **str** | This field will not be always available. Use remote_ip_address when this field is not set. | [optional] 
**dst_transport_node_name** | **str** | The name of the transport node to which the traceflow packet is forwarded | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

