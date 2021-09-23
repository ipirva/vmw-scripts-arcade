# Ipv4Header

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_ip** | **str** | The source ip address. | [optional] 
**flags** | **int** | IP flags | [optional] [default to 0]
**dst_ip** | **str** | The destination ip address. | [optional] 
**src_subnet_prefix_len** | **int** | This is used together with src_ip to calculate dst_ip for broadcast when dst_ip is not given; not used in all other cases. | [optional] 
**ttl** | **int** | Time to live (ttl) | [optional] [default to 64]
**protocol** | **int** | IP protocol - defaults to ICMP | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

