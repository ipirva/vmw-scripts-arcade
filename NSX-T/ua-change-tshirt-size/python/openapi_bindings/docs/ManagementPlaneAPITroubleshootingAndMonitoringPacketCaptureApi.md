# swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_packet_capture_session**](ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi.md#create_packet_capture_session) | **POST** /pktcap/session | Create an new packet capture session
[**delete_all_capture_sessions_delete**](ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi.md#delete_all_capture_sessions_delete) | **POST** /pktcap/sessions?action&#x3D;delete | Delete all the packet capture sessions
[**delete_packet_capture_session_delete**](ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi.md#delete_packet_capture_session_delete) | **POST** /pktcap/session/{session-id}?action&#x3D;delete | Delete the packet capture session by session id.
[**get_capture_file**](ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi.md#get_capture_file) | **GET** /pktcap/session/{session-id}/capturefile | Get packet capture file
[**list_packet_capture_sessions**](ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi.md#list_packet_capture_sessions) | **GET** /pktcap/sessions | Get the information of all packet capture sessions
[**read_packet_capture_session**](ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi.md#read_packet_capture_session) | **GET** /pktcap/session/{session-id} | Get the status of packet capture session
[**restart_packet_capture_session_restart**](ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi.md#restart_packet_capture_session_restart) | **POST** /pktcap/session/{session-id}?action&#x3D;restart | Restart the packet capture session
[**terminate_packet_capture_session_terminate**](ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi.md#terminate_packet_capture_session_terminate) | **POST** /pktcap/session/{session-id}?action&#x3D;terminate | Terminate the packet capture session by session id

# **create_packet_capture_session**
> PacketCaptureSession create_packet_capture_session(body)

Create an new packet capture session

Create an new packet capture session on given node with specified options 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi(swagger_client.ApiClient(configuration))
body = swagger_client.PacketCaptureRequest() # PacketCaptureRequest | 

try:
    # Create an new packet capture session
    api_response = api_instance.create_packet_capture_session(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi->create_packet_capture_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PacketCaptureRequest**](PacketCaptureRequest.md)|  | 

### Return type

[**PacketCaptureSession**](PacketCaptureSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_capture_sessions_delete**
> PacketCaptureSessionList delete_all_capture_sessions_delete()

Delete all the packet capture sessions

Delete all the packet capture sessions. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi(swagger_client.ApiClient(configuration))

try:
    # Delete all the packet capture sessions
    api_response = api_instance.delete_all_capture_sessions_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi->delete_all_capture_sessions_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PacketCaptureSessionList**](PacketCaptureSessionList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_packet_capture_session_delete**
> PacketCaptureSession delete_packet_capture_session_delete(session_id)

Delete the packet capture session by session id.

Before calling this method, terminate any running capture session. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | Packet capture session id

try:
    # Delete the packet capture session by session id.
    api_response = api_instance.delete_packet_capture_session_delete(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi->delete_packet_capture_session_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Packet capture session id | 

### Return type

[**PacketCaptureSession**](PacketCaptureSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_capture_file**
> get_capture_file(session_id)

Get packet capture file

You must provide the request header \"Accept:application/octet-stream\" when calling this API. The capture file can only be found in MP which receives the capture request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | Packet capture session id

try:
    # Get packet capture file
    api_instance.get_capture_file(session_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi->get_capture_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Packet capture session id | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packet_capture_sessions**
> PacketCaptureSessionList list_packet_capture_sessions()

Get the information of all packet capture sessions

Get the information of all packet capture sessions. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi(swagger_client.ApiClient(configuration))

try:
    # Get the information of all packet capture sessions
    api_response = api_instance.list_packet_capture_sessions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi->list_packet_capture_sessions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PacketCaptureSessionList**](PacketCaptureSessionList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_packet_capture_session**
> PacketCaptureSession read_packet_capture_session(session_id)

Get the status of packet capture session

Get the packet capture status information by session id. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | Packet capture session id

try:
    # Get the status of packet capture session
    api_response = api_instance.read_packet_capture_session(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi->read_packet_capture_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Packet capture session id | 

### Return type

[**PacketCaptureSession**](PacketCaptureSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_packet_capture_session_restart**
> PacketCaptureSession restart_packet_capture_session_restart(session_id)

Restart the packet capture session

Restart the packet capture session 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | Packet capture session id

try:
    # Restart the packet capture session
    api_response = api_instance.restart_packet_capture_session_restart(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi->restart_packet_capture_session_restart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Packet capture session id | 

### Return type

[**PacketCaptureSession**](PacketCaptureSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_packet_capture_session_terminate**
> PacketCaptureSession terminate_packet_capture_session_terminate(session_id)

Terminate the packet capture session by session id

Terminate the packet capture session by session id. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | Packet capture session id

try:
    # Terminate the packet capture session by session id
    api_response = api_instance.terminate_packet_capture_session_terminate(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPacketCaptureApi->terminate_packet_capture_session_terminate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Packet capture session id | 

### Return type

[**PacketCaptureSession**](PacketCaptureSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

