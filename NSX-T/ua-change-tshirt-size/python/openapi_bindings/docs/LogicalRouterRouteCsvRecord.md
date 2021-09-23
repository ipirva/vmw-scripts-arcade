# LogicalRouterRouteCsvRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lr_component_id** | **str** | Logical router component(Service Router/Distributed Router) id | [optional] 
**next_hop** | **str** | The IP of the next hop | [optional] 
**lr_component_type** | **str** | Logical router component(Service Router/Distributed Router) type | [optional] 
**network** | **str** | CIDR network address | 
**route_type** | **str** | Route type (USER, CONNECTED, NSX_INTERNAL,..) | 
**logical_router_port_id** | **str** | The id of the logical router port which is used as the next hop | [optional] 
**admin_distance** | **int** | The admin distance of the next hop | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

