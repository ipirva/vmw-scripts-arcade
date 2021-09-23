# LbHttpProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_buffering** | **bool** | When buffering is disabled, the response is passed to a client synchronously, immediately as it is received. When buffering is enabled, LB receives a response from the backend server as soon as possible, saving it into the buffers.  | [optional] [default to False]
**response_timeout** | **int** | If server doesn&#x27;t send any packet within this time, the connection is closed.  | [optional] [default to 60]
**request_body_size** | **int** | If it is not specified, it means that request body size is unlimited.  | [optional] 
**ntlm** | **bool** | NTLM is an authentication protocol that can be used over HTTP. If the flag is set to true, LB will use NTLM challenge/response methodology. This property is deprecated. Please use the property server_keep_alive in order to keep the backend server connection alive for the client connection. When create a new profile, if both ntlm and server_keep_alive are set as different values, ERROR will be reported. When update an existing profile, if either ntlm or server_keep_alive value is changed, both of them are updated with the changed value.  | [optional] 
**request_header_size** | **int** | A request with header equal to or below this size is guaranteed to be processed. A request with header larger than request_header_size will be processed up to 32K bytes on best effort basis.  | [optional] [default to 1024]
**http_redirect_to_https** | **bool** | Certain secure applications may want to force communication over SSL, but instead of rejecting non-SSL connections, they may choose to redirect the client automatically to use SSL.  | [optional] [default to False]
**response_header_size** | **int** | A response with header larger than response_header_size will be dropped.  | [optional] [default to 4096]
**idle_timeout** | **int** | It is used to specify the HTTP application idle timeout, it means that how long the load balancer will keep the connection idle to wait for the client to send the next keep-alive request. It is not a TCP socket setting.  | [optional] [default to 15]
**server_keep_alive** | **bool** | If server_keep_alive is true, it means the backend connection will keep alive for the client connection. Every client connection is tied 1:1 with the corresponding server-side connection. If server_keep_alive is false, it means the backend connection won&#x27;t keep alive for the client connection. The default value is false. If server_keep_alive is not specified for API input, its value in API output will be the same with the property ntlm.  | [optional] 
**http_redirect_to** | **str** | If a website is temporarily down or has moved, incoming requests for that virtual server can be temporarily redirected to a URL  | [optional] 
**x_forwarded_for** | **str** | When X-Forwareded-For is configured, X-Forwarded-Proto and X-Forwarded-Port information is added automatically. The two additional header information can be also modified or deleted in load balancer rules.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

