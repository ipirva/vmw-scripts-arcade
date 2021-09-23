# StaticRouteNextHop

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blackhole_action** | **str** | Action to be taken on matching packets for NULL routes. | [optional] 
**administrative_distance** | **int** | Administrative Distance for the next hop IP | [optional] [default to 1]
**ip_address** | **str** | Next Hop IP | [optional] 
**bfd_enabled** | **bool** | Status of bfd for this next hop where bfd_enabled &#x3D; true indicate bfd is enabled for this next hop and bfd_enabled &#x3D; false indicate bfd peer is disabled or not configured for this next hop. | [optional] [default to False]
**logical_router_port_id** | [**ResourceReference**](ResourceReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

