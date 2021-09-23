# LbSslModeSelectionAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssl_mode** | **str** | SSL Passthrough: LB establishes a TCP connection with client and another connection with selected backend server. LB won&#x27;t inspect the stream data between client and backend server, but just pass it through. Backend server exchanges SSL connection with client. SSL Offloading: LB terminiates the connections from client, and establishes SSL connection with it. After receiving the HTTP request, LB connects the selected backend server and talk with it via HTTP without SSL. LB estalishes new connection to selected backend server for each HTTP request, in case server_keep_alive or multiplexing are NOT configured. SSL End-to-End: LB terminiates the connections from client, and establishes SSL connection with it. After receiving the HTTP request, LB connects the selected backend server and talk with it via HTTPS. LB estalishes new SSL connection to selected backend server for each HTTP request, in case server_keep_alive or multiplexing are NOT configured.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

