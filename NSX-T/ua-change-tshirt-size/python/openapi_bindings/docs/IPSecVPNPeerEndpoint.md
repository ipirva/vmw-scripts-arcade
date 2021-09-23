# IPSecVPNPeerEndpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**psk** | **str** | IPSec Pre-shared key. Maximum length of this field is 128 characters. | [optional] 
**peer_id** | **str** | Peer identifier. | 
**ipsec_tunnel_profile_id** | **str** | Tunnel profile id to be used. By default it will point to system default profile. | [optional] 
**authentication_mode** | **str** | Authentication mode used for the peer authentication. For PSK (Pre Shared Key) authentication mode, &#x27;psk&#x27; property is mandatory and for the CERTIFICATE authentication mode, &#x27;peer_id&#x27; property is mandatory. | [optional] [default to 'PSK']
**peer_address** | **str** | IPV4 address of peer endpoint on remote site. | 
**connection_initiation_mode** | **str** | Connection initiation mode used by local endpoint to establish ike connection with peer endpoint. INITIATOR - In this mode local endpoint initiates tunnel setup and will also respond to incoming tunnel setup requests from peer gateway. RESPOND_ONLY - In this mode, local endpoint shall only respond to incoming tunnel setup requests. It shall not initiate the tunnel setup. ON_DEMAND - In this mode local endpoint will initiate tunnel creation once first packet matching the policy rule is received and will also respond to incoming initiation request.  | [optional] [default to 'INITIATOR']
**dpd_profile_id** | **str** | Dead peer detection (DPD) profile id. Default will be set according to system default policy. | [optional] 
**ike_profile_id** | **str** | IKE profile id to be used. Default will be set according to system default policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

