# StaticHopBfdPeer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_addresses** | **list[str]** | BFD peers will be created from all these source addresses to this neighbour. | [optional] 
**bfd_config** | [**BfdConfigParameters**](BfdConfigParameters.md) |  | [optional] 
**enabled** | **bool** | Indicate BFD peer is enabled or disabled. Default is true. | [optional] [default to True]
**peer_ip_address** | **str** | IP address of BFD peer. This should be same as next hop IP address. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

