# Ipv6Header

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_ip** | **str** | The source ip address. | [optional] 
**dst_ip** | **str** | The destination ip address. | [optional] 
**next_header** | **int** | Identifies the type of header immediately following the IPv6 header. | [optional] [default to 58]
**hop_limit** | **int** | Decremented by 1 by each node that forwards the packets. The packet is discarded if Hop Limit is decremented to zero. | [optional] [default to 64]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

