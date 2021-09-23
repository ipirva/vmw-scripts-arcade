# IpPool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnets** | [**list[IpPoolSubnet]**](IpPoolSubnet.md) | Subnets can be IPv4 or IPv6 and they should not overlap. The maximum number will not exceed 5 subnets. | [optional] 
**pool_usage** | [**PoolUsage**](PoolUsage.md) |  | [optional] 
**ip_release_delay** | **int** | Delay in milliseconds, while releasing allocated IP address from IP pool (Default is 2 mins). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

