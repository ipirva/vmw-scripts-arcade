# SwitchSecuritySwitchingProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bpdu_filter** | [**BpduFilter**](BpduFilter.md) |  | [optional] 
**rate_limits** | [**RateLimits**](RateLimits.md) |  | [optional] 
**ra_guard_enabled** | **bool** | RA Guard when enabled blocks unauthorized/rogue Router Advertisement (RA) packets. | [optional] [default to True]
**dhcp_filter** | [**DhcpFilter**](DhcpFilter.md) |  | [optional] 
**block_non_ip_traffic** | **bool** | A flag to block all traffic except IP/(G)ARP/BPDU | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

