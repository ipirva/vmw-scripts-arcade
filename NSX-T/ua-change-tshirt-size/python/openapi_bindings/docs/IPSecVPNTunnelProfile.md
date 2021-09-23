# IPSecVPNTunnelProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encapsulation_mode** | **str** | Encapsulation Mode to be used for encryption of packet. Tunnel mode protects internal routing information by encrypting IP header of original packet. | [optional] [default to 'TUNNEL_MODE']
**transform_protocol** | **str** | IPSec transform specifies IPSec security protocol. | [optional] [default to 'ESP']
**digest_algorithms** | **list[str]** | Algorithm to be used for message digest. Default digest algorithm is implicitly covered by default encryption algorithm \&quot;AES_GCM_128\&quot;. | [optional] 
**encryption_algorithms** | **list[str]** | Encryption algorithm to encrypt/decrypt the messages exchanged between IPSec VPN initiator and responder during tunnel negotiation. Default is AES_GCM_128. | [optional] 
**enable_perfect_forward_secrecy** | **bool** | If true, perfect forward secrecy (PFS) is enabled. | [optional] [default to True]
**dh_groups** | **list[str]** | Diffie-Hellman group to be used if PFS is enabled. Default is GROUP14. | [optional] 
**df_policy** | **str** | Defragmentation policy helps to handle defragmentation bit present in the inner packet. COPY copies the defragmentation bit from the inner IP packet into the outer packet. CLEAR ignores the defragmentation bit present in the inner packet. | [optional] [default to 'COPY']
**sa_life_time** | **int** | SA life time specifies the expiry time of security association. Default is 3600 seconds.  | [optional] [default to 3600]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

