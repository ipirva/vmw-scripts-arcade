# UpgradeUnitGroupAggregateInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Upgrade status of upgrade unit group | [optional] 
**upgrade_unit_count** | **int** | Number of upgrade units in the group | [optional] 
**failed_count** | **int** | Number of nodes in the upgrade unit group that failed upgrade | [optional] 
**post_upgrade_status** | [**UpgradeChecksExecutionStatus**](UpgradeChecksExecutionStatus.md) |  | [optional] 
**enabled** | **bool** | Flag to indicate whether upgrade of this group is enabled or not | [optional] [default to True]
**upgrade_units** | [**list[UpgradeUnit]**](UpgradeUnit.md) | List of upgrade units in the group | [optional] 
**extended_configuration** | [**list[KeyValuePair]**](KeyValuePair.md) | Extended configuration for the group | [optional] 
**percent_complete** | **float** | Indicator of upgrade progress in percentage | [optional] 
**type** | **str** | Component type | 
**parallel** | **bool** | Upgrade method to specify whether the upgrade is to be performed in parallel or serially | [optional] [default to True]
**group_level_failure** | **list[str]** | Reports failures that occured at the group or cluster level. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

