# LbTcpMonitor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receive** | **str** | Expected data, if specified, can be anywhere in the response and it has to be a string, regular expressions are not supported.  | [optional] 
**send** | **str** | If both send and receive are not specified, then just a TCP connection is established (3-way handshake) to validate server is healthy, no data is sent.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

