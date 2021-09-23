# ComponentUpgradeStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Upgrade status of component | [optional] 
**pre_upgrade_status** | [**UpgradeChecksExecutionStatus**](UpgradeChecksExecutionStatus.md) |  | [optional] 
**details** | **str** | Details about the upgrade status | [optional] 
**component_type** | **str** | Component type for the upgrade status | [optional] 
**node_count_at_target_version** | **int** | Number of nodes of the type and at the component version | [optional] 
**target_component_version** | **str** | Target component version | [optional] 
**percent_complete** | **float** | Indicator of upgrade progress in percentage | [optional] 
**can_skip** | **bool** | Can the upgrade of the remaining units in this component be skipped | [optional] 
**current_version_node_summary** | [**NodeSummaryList**](NodeSummaryList.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

