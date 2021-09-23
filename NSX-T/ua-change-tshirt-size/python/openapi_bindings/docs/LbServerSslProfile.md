# LbServerSslProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_cache_enabled** | **bool** | SSL session caching allows SSL client and server to reuse previously negotiated security parameters avoiding the expensive public key operation during handshake.  | [optional] [default to True]
**is_fips** | **bool** | This flag is set to true when all the ciphers and protocols are FIPS compliant. It is set to false when one of the ciphers or protocols are not FIPS compliant.  | [optional] 
**cipher_group_label** | **str** | It is a label of cipher group which is mostly consumed by GUI.  | [optional] 
**is_secure** | **bool** | This flag is set to true when all the ciphers and protocols are secure. It is set to false when one of the ciphers or protocols is insecure.  | [optional] 
**ciphers** | **list[str]** | supported SSL cipher list to client side | [optional] 
**protocols** | **list[str]** | SSL versions TLS1.1 and TLS1.2 are supported and enabled by default. SSLv2, SSLv3, and TLS1.0 are supported, but disabled by default.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

