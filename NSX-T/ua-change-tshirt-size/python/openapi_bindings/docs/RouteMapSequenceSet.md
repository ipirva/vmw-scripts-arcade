# RouteMapSequenceSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefer_global_v6_next_hop** | **bool** | For incoming and import route_maps on receiving both v6 global and v6 link-local address for the route, prefer to use the global address as the next hop. By default, it prefers the link-local next hop.  | [optional] [default to False]
**local_preference** | **int** | Local preference indicates the degree of preference for one BGP route over other BGP routes. The path/route with highest local preference value is preferred/selected. If local preference value is not specified then it will be considered as 100 by default.  | [optional] 
**weight** | **int** | Weight used to select certain path | [optional] 
**large_community** | **str** | Set large BGP community, community value shoud be in aa:bb:nn format where aa, bb, nn are unsigned integers with range [1-4294967295]. | [optional] 
**as_path_prepend** | **str** | As Path Prepending to influence path selection | [optional] 
**community** | **str** | Set normal BGP community either well-known community name or community value in aa:nn(2byte:2byte) format.  | [optional] 
**multi_exit_discriminator** | **int** | Multi Exit Discriminator (MED) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

