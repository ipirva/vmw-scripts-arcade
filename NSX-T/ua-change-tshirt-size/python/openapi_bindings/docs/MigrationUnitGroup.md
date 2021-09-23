# MigrationUnitGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_unit_count** | **int** | Number of migration units in the group | [optional] 
**migration_units** | [**list[MigrationUnit]**](MigrationUnit.md) | List of migration units in the group | [optional] 
**enabled** | **bool** | Flag to indicate whether migration of this group is enabled or not | [optional] [default to True]
**type** | **str** | Component type | 
**parallel** | **bool** | Migration method to specify whether the migration is to be performed in parallel or serially | [optional] [default to True]
**extended_configuration** | [**list[KeyValuePair]**](KeyValuePair.md) | Extended configuration for the group | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

