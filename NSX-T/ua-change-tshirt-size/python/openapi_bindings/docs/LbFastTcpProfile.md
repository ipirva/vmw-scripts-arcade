# LbFastTcpProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_timeout** | **int** | It is used to specify how long a closing TCP connection (both FINs received or a RST is received) should be kept for this application before cleaning up the connection.  | [optional] [default to 8]
**idle_timeout** | **int** | It is used to configure how long an idle TCP connection in ESTABLISHED state should be kept for this application before cleaning up.  | [optional] [default to 1800]
**ha_flow_mirroring_enabled** | **bool** | If flow mirroring is enabled, all the flows to the bounded virtual server are mirrored to the standby node.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

