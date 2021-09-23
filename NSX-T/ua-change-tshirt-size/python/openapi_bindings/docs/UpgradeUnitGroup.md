# UpgradeUnitGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag to indicate whether upgrade of this group is enabled or not | [optional] [default to True]
**upgrade_unit_count** | **int** | Number of upgrade units in the group | [optional] 
**type** | **str** | Component type | 
**upgrade_units** | [**list[UpgradeUnit]**](UpgradeUnit.md) | List of upgrade units in the group | [optional] 
**extended_configuration** | [**list[KeyValuePair]**](KeyValuePair.md) | Extended configuration for the group | [optional] 
**parallel** | **bool** | Upgrade method to specify whether the upgrade is to be performed in parallel or serially | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

