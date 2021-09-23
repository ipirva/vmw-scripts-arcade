# PortMirroringFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_action** | **str** | If set to MIRROR, packets will be mirrored. If set to DO_NOT_MIRROR, packets will not be mirrored. | [optional] [default to 'MIRROR']
**ip_protocol** | **str** | The transport protocols of TCP or UDP, used to match the transport protocol of a packet. If not provided, no filtering by IP protocols is performed. | [optional] 
**src_ips** | [**IPAddresses**](IPAddresses.md) |  | [optional] 
**dst_ips** | [**IPAddresses**](IPAddresses.md) |  | [optional] 
**dst_ports** | **str** | Destination port in the form of a port or port range, used to match the destination port of a packet. If not provided, no filtering by destination port is performed. | [optional] 
**src_ports** | **str** | Source port in the form of a port or port range, used to match the source port of a packet. If not provided, no filtering by source port is performed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

