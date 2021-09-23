# ServiceDeploymentStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_issues** | [**list[ServiceDeploymentIssue]**](ServiceDeploymentIssue.md) | List of issue and detailed description of the issue in case of deployment failure. | [optional] 
**last_update_timestamp** | **int** | Timestamp when the data was last updated; unset if data source has never updated the data. | [optional] 
**deployment_status** | **str** | Deployment status of NXGI Partner Service-VM on a compute collection. It shows the latest status during the process of deployment, redeploy, upgrade, and un-deployment on a compute collection such as VC cluster. | [optional] 
**sva_current_version** | **str** | Currently deployed Service Virtual Appliance version. | [optional] 
**service_deployment_id** | **str** | Id of service deployment. | [optional] 
**sva_max_available_version** | **str** | Max available SVA version for upgrade | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

