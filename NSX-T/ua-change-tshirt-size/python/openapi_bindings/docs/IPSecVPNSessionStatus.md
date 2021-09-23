# IPSecVPNSessionStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipsec_vpn_session_id** | **str** | UUID of vpn session. | [optional] 
**display_name** | **str** | Display name of vpn session. | [optional] 
**failed_tunnels** | **int** | Number of failed tunnels. | [optional] 
**negotiated_tunnels** | **int** | Number of negotiated tunnels. | [optional] 
**session_status** | **str** | Gives session status consolidated using IKE status and tunnel status. It can be UP, DOWN, DEGRADED. If IKE and all tunnels are UP status will be UP, if all down it will be DOWN, otherwise it will be DEGRADED. | [optional] 
**last_update_timestamp** | **int** | Timestamp when the data was last updated. | [optional] 
**aggregate_traffic_counters** | [**IPSecVPNTrafficCounters**](IPSecVPNTrafficCounters.md) |  | [optional] 
**ike_status** | [**IPSecVPNIKESessionStatus**](IPSecVPNIKESessionStatus.md) |  | [optional] 
**total_tunnels** | **int** | Total number of tunnels. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

