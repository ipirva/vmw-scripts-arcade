# LbHttpsMonitor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_status_codes** | **list[int]** | The HTTP response status code should be a valid HTTP status code.  | [optional] 
**server_auth_crl_ids** | **list[str]** | A Certificate Revocation List (CRL) can be specified in the server-side SSL profile binding to disallow compromised server certificates.  | [optional] 
**server_auth_ca_ids** | **list[str]** | If server auth type is REQUIRED, server certificate must be signed by one of the trusted Certificate Authorities (CAs), also referred to as root CAs, whose self signed certificates are specified.  | [optional] 
**server_auth** | **str** | server authentication mode | [optional] [default to 'IGNORE']
**request_body** | **str** | String to send as part of HTTP health check request body. Valid only for certain HTTP methods like POST.  | [optional] 
**response_body** | **str** | If HTTP response body match string (regular expressions not supported) is specified (using LbHttpMonitor.response_body) then the healthcheck HTTP response body is matched against the specified string and server is considered healthy only if there is a match. If the response body string is not specified, HTTP healthcheck is considered successful if the HTTP response status code is 2xx, but it can be configured to accept other status codes as successful.  | [optional] 
**ciphers** | **list[str]** | supported SSL cipher list to servers | [optional] 
**request_headers** | [**list[LbHttpRequestHeader]**](LbHttpRequestHeader.md) | Array of HTTP request headers | [optional] 
**client_certificate_id** | **str** | client certificate can be specified to support client authentication.  | [optional] 
**request_method** | **str** | the health check method for HTTP monitor type | [optional] [default to 'GET']
**is_fips** | **bool** | This flag is set to true when all the ciphers and protocols are FIPS compliant. It is set to false when one of the ciphers or protocols are not FIPS compliant..  | [optional] 
**certificate_chain_depth** | **int** | authentication depth is used to set the verification depth in the server certificates chain.  | [optional] [default to 3]
**is_secure** | **bool** | This flag is set to true when all the ciphers and protocols are secure. It is set to false when one of the ciphers or protocols is insecure.  | [optional] 
**request_url** | **str** | URL used for HTTP monitor | [optional] 
**cipher_group_label** | **str** | It is a label of cipher group which is mostly consumed by GUI.  | [optional] 
**request_version** | **str** | HTTP request version | [optional] [default to 'HTTP_VERSION_1_1']
**protocols** | **list[str]** | SSL versions TLS1.1 and TLS1.2 are supported and enabled by default. SSLv2, SSLv3, and TLS1.0 are supported, but disabled by default.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

