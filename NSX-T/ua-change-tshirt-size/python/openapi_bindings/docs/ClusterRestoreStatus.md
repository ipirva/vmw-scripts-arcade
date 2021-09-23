# ClusterRestoreStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**GlobalRestoreStatus**](GlobalRestoreStatus.md) |  | [optional] 
**step** | [**RestoreStep**](RestoreStep.md) |  | [optional] 
**endpoints** | [**list[ResourceLink]**](ResourceLink.md) | The list of allowed endpoints, based on the current state of the restore process  | [optional] 
**total_steps** | **int** | Total number of steps in the entire restore process | [optional] 
**restore_start_time** | **int** | Timestamp when restore was started in epoch millisecond | [optional] 
**restore_end_time** | **int** | Timestamp when restore was completed in epoch millisecond | [optional] 
**backup_timestamp** | **int** | Timestamp when backup was initiated in epoch millisecond | [optional] 
**id** | **str** | Unique id for backup request | [optional] 
**instructions** | [**list[InstructionInfo]**](InstructionInfo.md) | Instructions for users to reconcile Restore operations | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

