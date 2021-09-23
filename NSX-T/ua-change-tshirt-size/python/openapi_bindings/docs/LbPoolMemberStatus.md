# LbPoolMemberStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | UP means that pool member is enabled and monitors have marked the pool member as UP. If the pool member has no monitor configured, it would be treated as UP. DOWN means that pool member is enabled and monitors have marked the pool member as DOWN. DISABLED means that admin state of pool member is set to DISABLED. GRACEFUL_DISABLED means that admin state of pool member is set to GRACEFUL_DISABLED. UNUSED means that the pool member is not used when the IP list size of member group exceeds the maximum setting. The remaining IP addresses would not be used as available backend servers, hence mark the status as UNUSED. UNKNOWN means that the related pool is not associated to any enabled virtual servers, or no status reported from transport-nodes, the associated load balancer service may be working(or not working).  | 
**failure_cause** | **str** | If multiple active monitors are configured, the failure_cause contains failure cause for each monitors. Like \&quot;Monitor_1:failure_cause_1. Monitor_2:failure_cause_2.\&quot;  | [optional] 
**last_check_time** | **int** | If multiple active monitors are configured, the property value is the latest last_check_time among all the monitors.  | [optional] 
**ip_address** | **str** | Pool member IP address | 
**last_state_change_time** | **int** | If multiple active monitors are configured, the property value is the latest last_state_change_time among all the monitors.  | [optional] 
**port** | **str** | The port is configured in pool member. For virtual server port range case, pool member port must be null.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

