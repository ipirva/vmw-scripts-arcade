# DhcpStatistics

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **int** | The total number of DHCP errors | 
**releases** | **int** | The total number of DHCP RELEASE packets | 
**informs** | **int** | The total number of DHCP INFORM packets | 
**declines** | **int** | The total number of DHCP DECLINE packets | 
**dhcp_server_id** | **str** | dhcp server uuid | 
**nacks** | **int** | The total number of DHCP NACK packets | 
**offers** | **int** | The total number of DHCP OFFER packets | 
**discovers** | **int** | The total number of DHCP DISCOVER packets | 
**acks** | **int** | The total number of DHCP ACK packets | 
**timestamp** | **int** | timestamp of the statistics | 
**requests** | **int** | The total number of DHCP REQUEST packets | 
**ip_pool_stats** | [**list[DhcpIpPoolUsage]**](DhcpIpPoolUsage.md) | The DHCP ip pool usage statistics | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

