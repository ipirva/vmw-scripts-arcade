# UpgradeUnitAggregateInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of upgrade unit | [optional] 
**pre_upgrade_checks** | [**UpgradeCheckListResults**](UpgradeCheckListResults.md) |  | [optional] 
**errors** | **list[str]** | List of errors occurred during upgrade of this upgrade unit | [optional] 
**display_name** | **str** | Name of the upgrade unit | [optional] 
**post_upgrade_checks** | [**UpgradeCheckListResults**](UpgradeCheckListResults.md) |  | [optional] 
**warnings** | **list[str]** | List of warnings indicating issues with the upgrade unit that may result in upgrade failure | [optional] 
**current_version** | **str** | This is component version e.g. if upgrade unit is of type edge, then this is edge version. | [optional] 
**group** | [**UpgradeUnitGroupInfo**](UpgradeUnitGroupInfo.md) |  | [optional] 
**percent_complete** | **float** | Indicator of upgrade progress in percentage | [optional] 
**type** | **str** | Upgrade unit type | [optional] 
**id** | **str** | Identifier of the upgrade unit | [optional] 
**metadata** | [**list[KeyValuePair]**](KeyValuePair.md) | Metadata about upgrade unit | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

