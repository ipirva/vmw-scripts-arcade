# LbService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_log_enabled** | **bool** | Whether access log is enabled | [optional] 
**attachment** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**error_log_level** | **str** | Load balancer engine writes information about encountered issues of different severity levels to the error log. This setting is used to define the severity level of the error log.  | [optional] [default to 'INFO']
**virtual_server_ids** | **list[str]** | virtual servers can be associated to LbService(which is similar to physical/virtual load balancer), Lb virtual servers, pools and other entities could be defined independently, the virtual server identifier list here would be used to maintain the relationship of LbService and other Lb entities.  | [optional] 
**relax_scale_validation** | **bool** | If relax_scale_validation is true, the scale validations for virtual servers/pools/pool members/rules are relaxed for load balancer service. When load balancer service is deployed on edge nodes, the scale of virtual servers/pools/pool members for the load balancer service should not exceed the scale number of the largest load balancer size which could be configured on a certain edge form factor. For example, the largest load balancer size supported on a MEDIUM edge node is MEDIUM. So one SMALL load balancer deployed on MEDIUM edge nodes can support the scale number of MEDIUM load balancer. It is not recommended to enable active monitors if relax_scale_validation is true due to performance consideration. If relax_scale_validation is false, scale numbers should be validated for load balancer service.  | [optional] [default to False]
**enabled** | **bool** | Whether the load balancer service is enabled | [optional] [default to True]
**size** | **str** | The size of load balancer service | [optional] [default to 'SMALL']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

