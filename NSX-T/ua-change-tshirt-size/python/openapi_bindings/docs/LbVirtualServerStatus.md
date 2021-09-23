# LbVirtualServerStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | UP means that all primary members in default pool are in UP status. For L7 virtual server, if there is no default pool, the virtual server would be treated as UP. PARTIALLY_UP means that some(not all) primary members in default pool are in UP status. The size of these active primary members should be larger than or equal to the certain number(min_active_members) which is defined in LbPool. When there are no backup members which are in the UP status, the number(min_active_members) would be ignored. PRIMARY_DOWN means that less than certain(min_active_members) primary members in default pool are in UP status but backup members are in UP status, the connections would be dispatched to backup members. DOWN means that all primary and backup members are in DOWN status. DETACHED means that the virtual server is not bound to any service. DISABLED means that the admin state of the virtual server is disabled. UNKNOWN means that no status reported from transport-nodes. The associated load balancer service may be working(or not working).  | [optional] 
**last_update_timestamp** | **int** | Timestamp when the data was last updated. | [optional] 
**virtual_server_id** | **str** | load balancer virtual server identifier | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

