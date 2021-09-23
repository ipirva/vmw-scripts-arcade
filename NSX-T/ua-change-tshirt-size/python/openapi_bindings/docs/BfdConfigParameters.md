# BfdConfigParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receive_interval** | **int** | The time interval (in milliseconds) between heartbeat packets for BFD when receiving heartbeats.| For edge cluster type of bare metal, this value should be &gt;&#x3D; 50ms.| For edge cluster type of virtual machine or hybrid, this value should be &gt;&#x3D; 500ms. | [optional] [default to 500]
**declare_dead_multiple** | **int** | Number of times a packet is missed before BFD declares the neighbor down. | [optional] [default to 3]
**transmit_interval** | **int** | The time interval (in milliseconds) between heartbeat packets for BFD when sending heartbeats.| For edge cluster type of bare metal, this value should be &gt;&#x3D; 300ms.| For edge cluster type of virtual machine or hybrid, this value should be &gt;&#x3D; 1000ms. | [optional] [default to 500]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

