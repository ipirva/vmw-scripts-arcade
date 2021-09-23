# DirectoryDomainSyncStats

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev_sync_status** | **str** | Directory domain previous sync status. It could be one of the following two states. | [optional] 
**avg_full_sync_time** | **int** | All the historical full sync are counted in calculating the average full sync time in milliseconds. | [optional] 
**prev_sync_type** | **str** | Directory domain previous sync type. It could be one of the following five states. Right after the directory domain is configured, this field is set to IDLE. | [optional] 
**num_full_sync** | **int** | number of successful historical full sync initiated either by system or by API request. | [optional] 
**current_state_begin_time** | **int** | Since what time the current state has begun. The time is expressed in millisecond epoch time. | [optional] 
**avg_delta_sync_time** | **int** | All the historical delta sync are counted in calculating the average delta sync time in milliseconds. | [optional] 
**prev_sync_error** | **str** | Directory domain previous sync status error if last status was failure. | [optional] 
**current_state** | **str** | Current running state of the directory domain in synchronization life cycle. It could be one of the following five states. SELECTIVE_FULL_SYNC and SELECTIVE_DELTA_SYNC are sync states for selective sync. | [optional] 
**num_delta_sync** | **int** | number of successful historical delta sync initiated either by system or by API request. | [optional] 
**prev_sync_end_time** | **int** | Directory domain previous sync ending time expressed in millisecond epoch time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

