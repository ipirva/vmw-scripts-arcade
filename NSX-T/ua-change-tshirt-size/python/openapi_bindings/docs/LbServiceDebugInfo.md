# LbServiceDebugInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pools** | [**list[LbPool]**](LbPool.md) | The pools which are associated to the given load balancer service would be included. The pools could be defined in virtual server default pool, sorry pool or load balancer rule action.  | [optional] 
**persistence_profiles** | [**list[LbPersistenceProfile]**](LbPersistenceProfile.md) | The persistence profiles are associated to virtual servers  | [optional] 
**virtual_servers** | [**list[LbVirtualServer]**](LbVirtualServer.md) | The virtual servers which are associated to the given load balancer service would be included.  | [optional] 
**client_ssl_profiles** | [**list[LbClientSslProfile]**](LbClientSslProfile.md) | The client SSL profiles are associated to virtual servers  | [optional] 
**server_ssl_profiles** | [**list[LbServerSslProfile]**](LbServerSslProfile.md) | The server SSL profiles are associated to virtual servers  | [optional] 
**service** | [**LbService**](LbService.md) |  | [optional] 
**rules** | [**list[LbRule]**](LbRule.md) | The load balancer rules are associated to virtual servers  | [optional] 
**application_profiles** | [**list[LbAppProfile]**](LbAppProfile.md) | The application profiles are associated to virtual servers  | [optional] 
**monitors** | [**list[LbMonitor]**](LbMonitor.md) | The load balancer monitors are associated to pools.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

