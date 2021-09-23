# L2VPNSessionStatistics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traffic_statistics_per_logical_switch** | [**list[L2VPNPerLSTrafficStatistics]**](L2VPNPerLSTrafficStatistics.md) | Traffic statistics per logical switch. | [optional] 
**display_name** | **str** | L2VPN display name. | [optional] 
**partial_stats** | **bool** | Partial statistics is set to true if onle active node responds while standby does not. In case of both nodes responded statistics will be summed and partial stats will be false. If cluster has only active node, partial statistics will always be false. | [optional] 
**session_id** | **str** | Session identifier for L2VPN. | [optional] 
**tap_traffic_counters** | [**list[L2VPNTapTrafficStatistics]**](L2VPNTapTrafficStatistics.md) | Tunnel port traffic counters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

