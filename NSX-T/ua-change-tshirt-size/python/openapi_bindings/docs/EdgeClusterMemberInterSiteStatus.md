# EdgeClusterMemberInterSiteStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport_node** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**established_bgp_sessions** | **int** | Total number of current established inter-site IBGP sessions. | [optional] 
**status** | **str** | Edge node IBGP status | [optional] 
**total_bgp_sessions** | **int** | Total number of inter-site IBGP sessions. | [optional] 
**neighbor_status** | [**list[BgpNeighborStatusLiteDto]**](BgpNeighborStatusLiteDto.md) | Inter-site BGP neighbor status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

