# NDRAProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ra_mode** | **str** | RA Mode | [default to 'SLAAC_DNS_THROUGH_RA']
**ra_config** | [**RAConfig**](RAConfig.md) |  | 
**retransmit_interval** | **int** | The time, in milliseconds, between retransmitted neighbour solicitation messages.  | [optional] [default to 1000]
**dns_config** | [**RaDNSConfig**](RaDNSConfig.md) |  | [optional] 
**reachable_timer** | **int** | Neighbour reachable time duration in milliseconds. A value of 0 means unspecified.  | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

