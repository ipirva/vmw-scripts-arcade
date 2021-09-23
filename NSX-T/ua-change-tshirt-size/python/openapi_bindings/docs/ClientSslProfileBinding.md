# ClientSslProfileBinding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_auth** | **str** | client authentication mode | [optional] [default to 'IGNORE']
**ssl_profile_id** | **str** | Client SSL profile defines reusable, application-independent client side SSL properties.  | [optional] 
**certificate_chain_depth** | **int** | authentication depth is used to set the verification depth in the client certificates chain.  | [optional] [default to 3]
**client_auth_ca_ids** | **list[str]** | If client auth type is REQUIRED, client certificate must be signed by one of the trusted Certificate Authorities (CAs), also referred to as root CAs, whose self signed certificates are specified.  | [optional] 
**default_certificate_id** | **str** | A default certificate should be specified which will be used if the server does not host multiple hostnames on the same IP address or if the client does not support SNI extension.  | 
**sni_certificate_ids** | **list[str]** | Client-side SSL profile binding allows multiple certificates, for different hostnames, to be bound to the same virtual server.  | [optional] 
**client_auth_crl_ids** | **list[str]** | A Certificate Revocation List (CRL) can be specified in the client-side SSL profile binding to disallow compromised client certificates.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

