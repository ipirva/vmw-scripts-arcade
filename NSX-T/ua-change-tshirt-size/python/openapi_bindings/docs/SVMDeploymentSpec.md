# SVMDeploymentSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ovf_url** | **str** | Location of the partner VM OVF to be deployed. | 
**name** | **str** | Deployment Spec name for ease of use, since multiple DeploymentSpec can be specified. | [optional] 
**min_host_version** | **str** | Minimum host version supported by this ovf. If a host in the deployment cluster is having version less than this, then service deployment will not happen on that host. | [optional] [default to '6.5']
**service_form_factor** | **str** | Supported ServiceInsertion Form Factor for the OVF deployment. The default FormFactor is Medium. | [optional] [default to 'MEDIUM']
**host_type** | **str** | Host Type on which the specified OVF can be deployed. | 
**svm_version** | **str** | Partner needs to specify the Service VM version which will get deployed. | [optional] [default to '1.0']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

