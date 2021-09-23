# InstanceRuntime

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_vm_id** | **str** | Service-VM/SVM id of deployed virtual-machine. | [optional] 
**deployment_status** | **str** | Service-Instance Runtime deployment status of the Service-VM. It shows the latest status during the process of deployment, redeploy, upgrade, and un-deployment of VM. | [optional] 
**vm_nic_info** | [**VmNicInfo**](VmNicInfo.md) |  | [optional] 
**maintenance_mode** | **str** | The maintenance mode indicates whether the corresponding service VM is in maintenance mode. The service VM will not be used to service new requests if it is in maintenance mode.  | [optional] 
**runtime_status** | **str** | Service-Instance Runtime status of the deployed Service-VM. | [optional] 
**error_message** | **str** | Error message for the Service Instance Runtime if any. | [optional] 
**service_instance_id** | **str** | Id of an instantiation of a registered service. | [optional] 
**runtime_health_status_by_partner** | **str** | Service-Instance runtime health status set by partner to indicate whether the service is running properly or not.  | [optional] 
**unhealthy_reason** | **str** | Reason provided by partner for the service being unhealthy. This could be due to various reasons such as connectivity lost as an example.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

