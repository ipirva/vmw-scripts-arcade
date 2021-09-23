# PoolMember

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_concurrent_connections** | **int** | To ensure members are not overloaded, connections to a member can be capped by the load balancer. When a member reaches this limit, it is skipped during server selection. If it is not specified, it means that connections are unlimited.  | [optional] 
**admin_state** | **str** | member admin state | [optional] [default to 'ENABLED']
**backup_member** | **bool** | Backup servers are typically configured with a sorry page indicating to the user that the application is currently unavailable. While the pool is active (a specified minimum number of pool members are active) BACKUP members are skipped during server selection. When the pool is inactive, incoming connections are sent to only the BACKUP member(s).  | [optional] [default to False]
**weight** | **int** | Pool member weight is used for WEIGHTED_ROUND_ROBIN balancing algorithm. The weight value would be ignored in other algorithms.  | [optional] [default to 1]
**display_name** | **str** | pool member name | [optional] 
**ip_address** | **str** | pool member IP address | 
**port** | **str** | If port is specified, all connections will be sent to this port. Only single port is supported. If unset, the same port the client connected to will be used, it could be overrode by default_pool_member_port setting in virtual server. The port should not specified for port range case.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

