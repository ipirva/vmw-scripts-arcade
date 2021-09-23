# ClusterNodeVMDeploymentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_config** | [**ClusterNodeVMDeploymentConfig**](ClusterNodeVMDeploymentConfig.md) |  | 
**vm_id** | **str** | ID of the VM maintained internally and used to recognize it. Note: This is automatically generated and cannot be modified.  | [optional] 
**user_settings** | [**NodeUserSettings**](NodeUserSettings.md) |  | [optional] 
**roles** | **list[str]** | List of cluster node role (or roles) which the VM should take on. They specify what type (or types) of cluster node which the new VM should act as. Currently both CONTROLLER and MANAGER must be provided, since this permutation is the only one supported now.  | 
**form_factor** | **str** | Specifies the desired \&quot;size\&quot; of the VM  | [optional] [default to 'MEDIUM']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

