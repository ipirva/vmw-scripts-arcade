# FieldsPacketData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv6_header** | [**Ipv6Header**](Ipv6Header.md) |  | [optional] 
**arp_header** | [**ArpHeader**](ArpHeader.md) |  | [optional] 
**transport_header** | [**TransportProtocolHeader**](TransportProtocolHeader.md) |  | [optional] 
**ip_header** | [**Ipv4Header**](Ipv4Header.md) |  | [optional] 
**eth_header** | [**EthernetHeader**](EthernetHeader.md) |  | [optional] 
**payload** | **str** | Up to 1000 bytes of payload may be supplied (with a base64-encoded length of 1336 bytes.) Additional bytes of traceflow metadata will be appended to the payload. The payload contains any data the user wants to put after the transport header. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

