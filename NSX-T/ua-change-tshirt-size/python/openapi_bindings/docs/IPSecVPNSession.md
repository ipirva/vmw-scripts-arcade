# IPSecVPNSession

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peer_endpoint_id** | **str** | Peer endpoint identifier. | 
**ipsec_vpn_service_id** | **str** | Identifier of VPN Service linked with local endpoint. | [optional] 
**local_endpoint_id** | **str** | Local endpoint identifier. | 
**tcp_mss_clamping** | [**TcpMssClamping**](TcpMssClamping.md) |  | [optional] 
**enabled** | **bool** | Enable/Disable IPSec VPN session. | [optional] [default to True]
**resource_type** | **str** | A Policy Based VPN requires to define protect rules that match   local and peer subnets. IPSec security associations is   negotiated for each pair of local and peer subnet. A Route Based VPN is more flexible, more powerful and recommended over   policy based VPN. IP Tunnel port is created and all traffic routed via   tunnel port is protected. Routes can be configured statically   or can be learned through BGP. A route based VPN is must for establishing   redundant VPN session to remote site.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

