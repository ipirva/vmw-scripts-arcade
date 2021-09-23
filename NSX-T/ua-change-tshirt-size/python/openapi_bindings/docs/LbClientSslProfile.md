# LbClientSslProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_cache_enabled** | **bool** | SSL session caching allows SSL client and server to reuse previously negotiated security parameters avoiding the expensive public key operation during handshake.  | [optional] [default to True]
**session_cache_timeout** | **int** | Session cache timeout specifies how long the SSL session parameters are held on to and can be reused.  | [optional] [default to 300]
**cipher_group_label** | **str** | It is a label of cipher group which is mostly consumed by GUI.  | [optional] 
**is_fips** | **bool** | This flag is set to true when all the ciphers and protocols are FIPS compliant. It is set to false when one of the ciphers or protocols are not FIPS compliant..  | [optional] 
**is_secure** | **bool** | This flag is set to true when all the ciphers and protocols are secure. It is set to false when one of the ciphers or protocols is insecure.  | [optional] 
**prefer_server_ciphers** | **bool** | During SSL handshake as part of the SSL client Hello client sends an ordered list of ciphers that it can support (or prefers) and typically server selects the first one from the top of that list it can also support. For Perfect Forward Secrecy(PFS), server could override the client&#x27;s preference.  | [optional] [default to True]
**ciphers** | **list[str]** | supported SSL cipher list to client side | [optional] 
**protocols** | **list[str]** | SSL versions TLS1.1 and TLS1.2 are supported and enabled by default. SSLv2, SSLv3, and TLS1.0 are supported, but disabled by default.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

