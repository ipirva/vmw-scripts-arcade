# LbServiceUsage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_capacity** | **int** | Pool capacity means maximum number of pools which could be configured in the given load balancer service.  | [optional] 
**service_size** | **str** | The size of load balancer service | [optional] 
**severity** | **str** | The severity calculation is based on the largest usage percentage from virtual servers, pools, pool members and rules for one load balancer service.  | [optional] 
**pool_member_capacity** | **int** | Pool member capacity means maximum number of pool members which could be configured in the given load balancer service.  | [optional] 
**current_virtual_server_count** | **int** | The current number of virtual servers which have been configured in the given load balancer service.  | [optional] 
**usage_percentage** | **float** | The usage percentage is the largest usage percentage from virtual servers, pools and pool members for the load balancer service. If the property relax_scale_validation is set as true for LbService, it is possible that the value is larger than 100.0. For example, if SMALL LBS is deployed on MEDIUM edge node and configured with MEDIUM LBS virtual server scale number, LBS usage percentage is shown larger than 100.0.  | [optional] 
**service_id** | **str** | UUID of load balancer service | [optional] 
**current_pool_count** | **int** | The current number of pools which have been configured in the given load balancer service.  | [optional] 
**virtual_server_capacity** | **int** | Virtual server capacity means maximum number of virtual servers which could be configured in the given load balancer service.  | [optional] 
**current_pool_member_count** | **int** | The current number of pool members which have been configured in the given load balancer service.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

