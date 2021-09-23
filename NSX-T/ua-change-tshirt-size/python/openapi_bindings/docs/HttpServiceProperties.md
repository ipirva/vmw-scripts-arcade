# HttpServiceProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_api_concurrency_limit** | **int** | The maximum number of concurrent API requests that will be serviced. If the number of API requests being processed exceeds this limit, new API requests will be refused and a 503 Service Unavailable response will be returned to the client.  To disable API concurrency limiting, set this value to 0. | [optional] [default to 100]
**certificate** | [**Certificate**](Certificate.md) |  | [optional] 
**basic_authentication_enabled** | **bool** | Identifies whether basic authentication is enabled or disabled in API calls. | [optional] [default to True]
**cookie_based_authentication_enabled** | **bool** | Identifies whether cookie-based authentication is enabled or disabled in API calls. When cookie-based authentication is disabled, new sessions cannot be created via /api/session/create. | [optional] [default to True]
**cipher_suites** | [**list[CipherSuite]**](CipherSuite.md) | Cipher suites used to secure contents of connection | [optional] 
**redirect_host** | **str** | Host name or IP address to use for redirect location headers, or empty string to derive from current request | [optional] [default to '']
**session_timeout** | **int** | NSX session inactivity timeout, set to 0 to configure no timeout | [optional] 
**client_api_rate_limit** | **int** | The maximum number of API requests that will be serviced per second for a given authenticated client.  If more API requests are received than can be serviced, a 429 Too Many Requests HTTP response will be returned. To disable API rate limiting, set this value to 0. | [optional] [default to 100]
**client_api_concurrency_limit** | **int** | The maximum number of concurrent API requests that will be serviced for a given authenticated client.  If the number of API requests being processed exceeds this limit, new API requests will be refused and a 503 Service Unavailable response will be returned to the client. To disable API concurrency limiting, set this value to 0. | [optional] [default to 40]
**protocol_versions** | [**list[ProtocolVersion]**](ProtocolVersion.md) | TLS protocol versions | [optional] 
**connection_timeout** | **int** | NSX connection timeout, set to 0 to configure no timeout | [optional] 
**logging_level** | **str** | Service logging level | [optional] [default to 'INFO']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

