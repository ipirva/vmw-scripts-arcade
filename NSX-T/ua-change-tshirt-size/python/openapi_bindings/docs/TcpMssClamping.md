# TcpMssClamping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_segment_size** | **int** | It defines the maximum amount of data that a host is willing to accept in a single TCP segment. This field is set in TCP header during connection establishment. To avoid packet fragmentation, you can set this field depending on uplink MTU and VPN overhead. This is optional field and in case it is left unconfigured, best possible MSS value will be calculated based on effective mtu of uplink interface. Supported MSS range is 108 to 8852. | [optional] 
**direction** | **str** | Specifies the traffic direction for which to apply MSS Clamping. | [optional] [default to 'NONE']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

