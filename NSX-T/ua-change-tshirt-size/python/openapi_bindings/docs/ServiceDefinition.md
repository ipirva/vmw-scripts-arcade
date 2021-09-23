# ServiceDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_deployment_spec** | [**ServiceDeploymentSpec**](ServiceDeploymentSpec.md) |  | [optional] 
**service_capability** | [**ServiceCapability**](ServiceCapability.md) |  | [optional] 
**functionalities** | **list[str]** | The capabilities provided by the services. Needs to be one or more of the following | NG_FW - Next Generation Firewall | IDS_IPS - Intrusion Detection System / Intrusion Prevention System | NET_MON - Network Monitoring | HCX - Hybrid Cloud Exchange | BYOD - Bring Your Own Device | TLB -  Transparent Load Balancer | EPP - Endpoint Protection.(Third party AntiVirus partners using NXGI should use this functionality for the service) | 
**attachment_point** | **list[str]** | The point at which the service is deployed/attached for redirecting the traffic to the the partner appliance. Attachment Point is required if Service caters to any functionality other than EPP. | [optional] 
**service_manager_id** | **str** | ID of the service manager to which this service is attached with. This field is not set during creation of service. This field will be set explicitly when Service Manager is created successfully using this service.  | [optional] 
**vendor_id** | **str** | Id which is unique to a vendor or partner for which the service is created. | 
**on_failure_policy** | **str** | Failure policy for the service tells datapath, the action to take i.e to Allow or Block traffic during failure scenarios. For north-south ServiceInsertion, failure policy in the service instance takes precedence. For east-west ServiceInsertion, failure policy in the service chain takes precedence. BLOCK is not supported for Endpoint protection (EPP) functionality. | [optional] [default to 'ALLOW']
**transports** | **list[str]** | Transport Type of the service, which is the mechanism of redirecting the traffic to the the partner appliance. Transport type is required if Service caters to any functionality other than EPP. | [optional] 
**implementations** | **list[str]** | This indicates the insertion point of the service i.e whether the service will be used to protect North-South or East-West traffic in the datacenter. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

