# ServiceInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_spec_name** | **str** | Name of the deployment spec to be used by this service instance. | 
**instance_deployment_template** | [**DeploymentTemplate**](DeploymentTemplate.md) |  | 
**implementation_type** | **str** | Implementation to be used by this service instance for deploying the Service-VM. | 
**attachment_point** | **str** | Attachment point to be used by this service instance for deploying the Service-VM. | 
**instance_deployment_config** | [**InstanceDeploymentConfig**](InstanceDeploymentConfig.md) |  | [optional] 
**deployment_mode** | **str** | Deployment mode specifies where the partner appliance will be deployed in HA or non-HA i.e standalone mode. | [default to 'ACTIVE_STANDBY']
**deployed_to** | [**list[ResourceReference]**](ResourceReference.md) | List of resource references where service instance be deployed. Ex. Tier 0 Logical Router in case of N-S ServiceInsertion. | 
**service_deployment_id** | **str** | Id of the Service Deployment using which the instances were deployed. Its available only for instances that were deployed using service deployment API. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

