# BgpConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inter_sr_ibgp** | [**InterSRRoutingConfig**](InterSRRoutingConfig.md) |  | [optional] 
**as_number** | **int** | This is a deprecated property, Please use &#x27;as_num&#x27; instead. For VRF logical router, the as_number from parent logical router will be effective. | [optional] 
**route_aggregation** | [**list[BgpRouteAggregation]**](BgpRouteAggregation.md) | List of routes to be aggregated | [optional] 
**logical_router_id** | **str** | Logical router id | [optional] 
**graceful_restart** | **bool** | Flag to enable graceful restart. This field is deprecated, kindly use graceful_restart_config parameter for graceful restart configuration. If both parameters are set and consistent with each other [i.e. graceful_restart&#x3D;false and graceful_restart_mode&#x3D;HELPER_ONLY OR graceful_restart&#x3D;true and graceful_restart_mode&#x3D;GR_AND_HELPER] then this is allowed, but if inconsistent with each other then this is not allowed and validation error will be thrown. For VRF logical router, the settings from parent logical router will be effective.  | [optional] 
**as_num** | **str** | For VRF logical router, the as_num from parent logical router will be effective. | [optional] 
**enabled** | **bool** | While creation of BGP config this flag will be set to - true for Tier0 logical router with Active-Active high-availability mode - false for Tier0 logical router with Active-Standby high-availanility mode. User can change this value while updating the config. If this property is not specified in the payload, the default value will be considered as false irrespective of the high-availability mode.  | [optional] [default to False]
**graceful_restart_config** | [**GracefulRestartConfig**](GracefulRestartConfig.md) |  | [optional] 
**multipath_relax** | **bool** | For TIER0 logical router, default is true. For VRF logical router, the settings from parent logical router will be effective. | [optional] 
**ecmp** | **bool** | While creation of BGP config this flag will be set to true User can change this value while updating BGP config. If this property is not specified in the payload, the default value will be considered as true.  | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

