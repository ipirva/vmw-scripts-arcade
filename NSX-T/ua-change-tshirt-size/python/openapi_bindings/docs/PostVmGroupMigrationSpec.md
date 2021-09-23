# PostVmGroupMigrationSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_override** | **bool** | Flag to indicate whether to re-run the post migrate steps for the VM group if they are already run before. | [optional] [default to False]
**group_id** | **str** | User defined VM group id that must be unique among all VM groups ids and also should match the group id used in the pre VM group migrate API. | 
**failed_vm_instance_ids** | **list[str]** | List of instance uuids of VMs that failed to migrate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

