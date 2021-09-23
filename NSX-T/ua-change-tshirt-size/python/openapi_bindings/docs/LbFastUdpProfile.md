# LbFastUdpProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idle_timeout** | **int** | Though UDP is a connectionless protocol, for the purposes of load balancing, all UDP packets with the same flow signature (source and destination IP/ports and IP protocol) received within the idle timeout period are considered to belong to the same connection and are sent to the same backend server. If no packets are received for idle timeout period, the connection (association between flow signature and the selected server) is cleaned up.  | [optional] [default to 300]
**flow_mirroring_enabled** | **bool** | If flow mirroring is enabled, all the flows to the bounded virtual server are mirrored to the standby node.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

