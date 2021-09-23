# TaskProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Current status of the task | [optional] 
**async_response_available** | **bool** | True if response for asynchronous request is available | [optional] 
**description** | **str** | Description of the task | [optional] 
**start_time** | **int** | The start time of the task in epoch milliseconds | [optional] 
**cancelable** | **bool** | True if this task can be canceled | [optional] 
**request_method** | **str** | HTTP request method | [optional] 
**user** | **str** | Name of the user who created this task | [optional] 
**progress** | **int** | Task progress if known, from 0 to 100 | [optional] 
**message** | **str** | A message describing the disposition of the task | [optional] 
**request_uri** | **str** | URI of the method invocation that spawned this task | [optional] 
**id** | **str** | Identifier for this task | [optional] 
**end_time** | **int** | The end time of the task in epoch milliseconds | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

