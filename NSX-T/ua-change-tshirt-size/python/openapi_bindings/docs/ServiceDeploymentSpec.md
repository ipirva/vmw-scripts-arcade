# ServiceDeploymentSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_specs** | [**list[SVMDeploymentSpec]**](SVMDeploymentSpec.md) | Deployment Specs holds information required to deploy the Service-VMs. i.e. OVF url where the partner Service-VM OVF is hosted. The host type on which the OVF can be deployed, Form factor to name a few. | [optional] 
**nic_metadata_list** | [**list[NicMetadata]**](NicMetadata.md) | NIC metadata associated with the deployment spec. | [optional] 
**deployment_template** | [**list[DeploymentTemplate]**](DeploymentTemplate.md) | Deployment Template holds the attributes specific to partner for which the service is created. These attributes are opaque to NSX Manager. | 
**svm_version** | **str** | Partner needs to specify the Service VM version which will get deployed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

