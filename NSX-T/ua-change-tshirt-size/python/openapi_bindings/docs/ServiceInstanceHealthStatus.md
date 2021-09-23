# ServiceInstanceHealthStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_sva_mux_incompatible** | **bool** | Protocol version might be different in both Mux and SVA. | [optional] 
**connect_timestamp** | **str** | Latest timestamp when mux was connected to SVA. | [optional] 
**mux_incompatible_version** | **str** | Mux version when Mux and SVA are incompatible | [optional] 
**solution_version** | **str** | Version of third party partner solution application. | [optional] 
**sync_time** | **str** | Latest timestamp when health status is received. | [optional] 
**solution_status** | **str** | Status of third party partner solution application. | [optional] 
**is_stale** | **bool** | The parameter is set if the last received health status is older than the predefined interval.  | [optional] 
**mux_connected_status** | **str** | Status of multiplexer which forwards the events from guest virtual machines to the partner appliance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

