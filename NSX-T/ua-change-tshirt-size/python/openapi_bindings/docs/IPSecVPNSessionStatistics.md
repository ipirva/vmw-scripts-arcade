# IPSecVPNSessionStatistics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ike_traffic_statistics** | [**IPSecVPNIKETrafficStatistics**](IPSecVPNIKETrafficStatistics.md) |  | [optional] 
**display_name** | **str** | Display name of vpn session. | [optional] 
**policy_statistics** | [**list[IPSecVPNPolicyTrafficStatistics]**](IPSecVPNPolicyTrafficStatistics.md) | Gives aggregate traffic statistics across all ipsec tunnels and individual tunnel statistics. | [optional] 
**partial_stats** | **bool** | Partial statistics if true specifies that the statistics are only from active node. | [optional] 
**ipsec_vpn_session_id** | **str** | UUID of vpn session. | [optional] 
**last_update_timestamp** | **int** | Timestamp when the data was last updated. | [optional] 
**ike_status** | [**IPSecVPNIKESessionStatus**](IPSecVPNIKESessionStatus.md) |  | [optional] 
**aggregate_traffic_counters** | [**IPSecVPNTrafficCounters**](IPSecVPNTrafficCounters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

