# LiveTraceStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**LiveTraceFilterData**](LiveTraceFilterData.md) |  | [optional] 
**operation_state** | **str** | The operation state of live trace. IN_PROGRESS - collecting the session results. FINISHED - session results collect complete. PARTIAL_FINISHED - some ssession results may be lost. CANCELED - session cancelled by exception. TIMEOUT - session result is incomplete until timeout.  | [optional] 
**timeout** | **int** | Timeout in seconds for livetrace session | [optional] 
**source_lport** | **str** | The source logical port | [optional] 
**request_status** | **str** | The status of a live trace request. SUCCESS_DELIVERED - The request is delivered successfully. LCP_FAILURE - nsx-cfgagent fails to realize the request. INVALID_FILTER - filter data invalid. DATAPATH_FAILURE - DP fails to realize the request. TIMEOUT - The response to the request is not received within timeout. CONNECTION_ERROR - There is connection error with host component. UNKNOWN - The status of request cannot be determined.  | [optional] 
**actions** | [**LiveTraceActionConfig**](LiveTraceActionConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

