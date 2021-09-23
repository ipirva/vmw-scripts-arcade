# DhcpIpPool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_ranges** | [**list[IpPoolRange]**](IpPoolRange.md) | Ip-ranges to define dynamic ip allocation ranges. | 
**warning_threshold** | **int** | Warning threshold. Alert will be raised if the pool usage reaches the given threshold.  | [optional] [default to 80]
**error_threshold** | **int** | Error threshold. Alert will be raised if the pool usage reaches the given threshold.  | [optional] [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

