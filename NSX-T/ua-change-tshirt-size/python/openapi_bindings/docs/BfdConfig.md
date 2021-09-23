# BfdConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receive_interval** | **int** | the time interval (in milliseconds) between heartbeat packets for BFD when receiving heartbeats. | [optional] [default to 500]
**declare_dead_multiple** | **int** | Number of times a packet is missed before BFD declares the neighbor down. | [optional] [default to 3]
**enabled** | **bool** | Flag to enable BFD for this LogicalRouter | [optional] [default to False]
**logical_router_id** | **str** | Logical router id | [optional] 
**transmit_interval** | **int** | the time interval (in milliseconds) between heartbeat packets for BFD when sending heartbeats. | [optional] [default to 500]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

