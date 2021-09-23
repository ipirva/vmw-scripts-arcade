# L2VpnTunnelEncapsulation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_endpoint_ip** | **str** | IP Address of the tunnel port. For hub, the IP is allocated from L2VpnService logical_tap_ip_pool. All sessions on same L2VpnService get the same local_endpoint_ip. For spoke, the IP must be provided. | [optional] 
**protocol** | **str** | Encapsulation protocol used by the tunnel | [optional] [default to 'GRE']
**peer_endpoint_ip** | **str** | IP Address of the peer tunnel port. For hub, the IP is allocated from L2VpnService logical_tap_ip_pool. For spoke, the IP must be provided. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

