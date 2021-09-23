# BaseServiceInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_failure_policy** | **str** | Failure policy of the service instance - if it has to be different from the service. By default the service instance inherits the FailurePolicy of the service it belongs to. | [optional] 
**transport_type** | **str** | Transport to be used by this service instance for deploying the Service-VM. This field is to be set Not Applicable(NA) if the service only caters to functionality EPP(Endpoint Protection). | 
**resource_type** | **str** | ServiceInstance is used when NSX handles the lifecyle of   appliance. Deployment and appliance related all the information is necessary. ByodServiceInstance is a custom instance to be used when NSX is not handling   the lifecycles of appliance/s. User will manage their own appliance (BYOD)   to connect with NSX. VirtualServiceInstance is a a custom instance to be used when NSX is not   handling the lifecycle of an appliance and when the user is not bringing   their own appliance.  | 
**service_id** | **str** | The Service to which the service instance is associated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

