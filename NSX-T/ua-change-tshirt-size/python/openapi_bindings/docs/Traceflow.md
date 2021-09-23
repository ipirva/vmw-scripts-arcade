# Traceflow

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_state** | **str** | Represents the traceflow operation state | [optional] 
**logical_counters** | [**TraceflowObservationCounters**](TraceflowObservationCounters.md) |  | [optional] 
**timeout** | **int** | Maximum time (in ms) the management plane will be waiting for this traceflow round. | [optional] 
**result_overflowed** | **bool** | A flag, when set true, indicates some observations were deleted from the result set. | [optional] 
**lport_id** | **str** | id of the source logical port used for injecting the traceflow packet | [optional] 
**counters** | [**TraceflowObservationCounters**](TraceflowObservationCounters.md) |  | [optional] 
**request_status** | **str** | The status of the traceflow RPC request. SUCCESS - The traceflow request is sent successfully. TIMEOUT - The traceflow request gets timeout. SOURCE_PORT_NOT_FOUND - The source port of the request cannot be found. DATA_PATH_NOT_READY - The datapath component cannot be ready to receive request. CONNECTION_ERROR - There is connection error on datapath component. UNKNOWN - The status of traceflow request cannot be determined. | [optional] 
**analysis** | **list[str]** | Traceflow result analysis notes | [optional] 
**id** | **str** | The id of the traceflow round | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

