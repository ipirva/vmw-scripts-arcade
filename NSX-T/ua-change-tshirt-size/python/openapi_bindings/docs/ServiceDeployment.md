# ServiceDeployment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**perimeter** | **str** | This indicates the deployment perimeter, such as a VC cluster or a host. | [optional] [default to 'HOST']
**deployment_spec_name** | **str** | Name of the deployment spec to be used for deployment, which specifies the OVF provided by the partner and the form factor. | 
**deployment_mode** | **str** | Mode of deployment. Currently, only stand alone deployment is supported. It is a single VM deployed through this deployment spec. In future, HA configurations will be supported here. | [optional] [default to 'STAND_ALONE']
**instance_deployment_template** | [**DeploymentTemplate**](DeploymentTemplate.md) |  | 
**service_deployment_config** | [**ServiceDeploymentConfig**](ServiceDeploymentConfig.md) |  | 
**service_id** | **str** | The Service to which the service deployment is associated. | [optional] 
**clustered_deployment_count** | **int** | Number of instances in case of clustered deployment. | [optional] [default to 1]
**deployed_to** | [**list[ResourceReference]**](ResourceReference.md) | List of resource references where service instance be deployed. Ex. Tier 0 Logical Router in case of N-S ServiceInsertion. Service Attachment in case of E-W ServiceInsertion. | [optional] 
**deployment_type** | **str** | Specifies whether the service VM should be deployed on each host such that it provides partner service locally on the host, or whether the service VMs can be deployed as a cluster. If deployment_type is CLUSTERED, then the clustered_deployment_count should be provided. | [optional] [default to 'CLUSTERED']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

