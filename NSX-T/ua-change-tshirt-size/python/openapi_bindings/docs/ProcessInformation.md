# ProcessInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_id** | **str** | Display the process id. | [optional] 
**shared_memory_size** | **float** | The amount of shared memory available to a process, not all of which is typically resident. It simply reflects memory that could be potentially shared with other processes.  | [optional] 
**command** | **str** | Display the command line used to start the process. | [optional] 
**memory_usage** | **float** | A process&#x27;s currently used share of available physical memory.  | [optional] 
**virtual_memory_size** | **float** | The total amount of virtual memory used by the process. It includes all code, data and shared libraries plus pages that have been swapped out and pages that have been mapped but not used.  | [optional] 
**resident_memory_size** | **float** | The non-swapped physical memoery a task is using. | [optional] 
**nice_value** | **str** | A negative nice value means higher priority, whereas a positive nice value means lower priority. Zero in this field simply means priority will not be adjusted in determining a process&#x27;s dispatch-ability.  | [optional] 
**cpu_usage** | **float** | The process&#x27;s share of the elapsed CPU time since the last screen update, expressed as a percentage of total CPU time.  | [optional] 
**user** | **str** | Display the process user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

