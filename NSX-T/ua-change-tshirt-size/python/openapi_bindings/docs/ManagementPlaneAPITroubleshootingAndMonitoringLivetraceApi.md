# swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_live_trace**](ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi.md#create_live_trace) | **POST** /livetraces | Create a livetrace session
[**delete_live_trace**](ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi.md#delete_live_trace) | **DELETE** /livetraces/{livetrace-session-id} | Delete a livetrace session
[**get_forward_pkt_cap_file_proxy**](ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi.md#get_forward_pkt_cap_file_proxy) | **GET** /livetraces/{livetrace-session-id}/proxy/forward/capturefile | Get forward packet capture file proxy
[**get_live_trace_result**](ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi.md#get_live_trace_result) | **GET** /livetraces/{livetrace-session-id}/results | Get the result of a livetrace session
[**get_live_trace_status**](ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi.md#get_live_trace_status) | **GET** /livetraces/{livetrace-session-id} | Get the status of a livetrace session
[**get_reverse_pkt_cap_file_proxy**](ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi.md#get_reverse_pkt_cap_file_proxy) | **GET** /livetraces/{livetrace-session-id}/proxy/reverse/capturefile | Get reverse packet capture file proxy
[**list_live_trace**](ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi.md#list_live_trace) | **GET** /livetraces | List all livetrace sessions

# **create_live_trace**
> LiveTraceStatus create_live_trace(body)

Create a livetrace session

Create a livetrace session

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi(swagger_client.ApiClient(configuration))
body = swagger_client.LiveTraceRequest() # LiveTraceRequest | 

try:
    # Create a livetrace session
    api_response = api_instance.create_live_trace(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi->create_live_trace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LiveTraceRequest**](LiveTraceRequest.md)|  | 

### Return type

[**LiveTraceStatus**](LiveTraceStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_live_trace**
> delete_live_trace(livetrace_session_id)

Delete a livetrace session

Delete a livetrace session

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi(swagger_client.ApiClient(configuration))
livetrace_session_id = 'livetrace_session_id_example' # str | 

try:
    # Delete a livetrace session
    api_instance.delete_live_trace(livetrace_session_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi->delete_live_trace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **livetrace_session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forward_pkt_cap_file_proxy**
> get_forward_pkt_cap_file_proxy(livetrace_session_id)

Get forward packet capture file proxy

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi(swagger_client.ApiClient(configuration))
livetrace_session_id = 'livetrace_session_id_example' # str | Livetrace session ID

try:
    # Get forward packet capture file proxy
    api_instance.get_forward_pkt_cap_file_proxy(livetrace_session_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi->get_forward_pkt_cap_file_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **livetrace_session_id** | **str**| Livetrace session ID | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_trace_result**
> LiveTraceResult get_live_trace_result(livetrace_session_id, action_type=action_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get the result of a livetrace session

Get the result of a livetrace session

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi(swagger_client.ApiClient(configuration))
livetrace_session_id = 'livetrace_session_id_example' # str | 
action_type = 'action_type_example' # str | The type of observations that will be listed. (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get the result of a livetrace session
    api_response = api_instance.get_live_trace_result(livetrace_session_id, action_type=action_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi->get_live_trace_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **livetrace_session_id** | **str**|  | 
 **action_type** | **str**| The type of observations that will be listed. | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**LiveTraceResult**](LiveTraceResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_trace_status**
> LiveTraceStatus get_live_trace_status(livetrace_session_id)

Get the status of a livetrace session

Get the status of a livetrace session

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi(swagger_client.ApiClient(configuration))
livetrace_session_id = 'livetrace_session_id_example' # str | 

try:
    # Get the status of a livetrace session
    api_response = api_instance.get_live_trace_status(livetrace_session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi->get_live_trace_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **livetrace_session_id** | **str**|  | 

### Return type

[**LiveTraceStatus**](LiveTraceStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reverse_pkt_cap_file_proxy**
> get_reverse_pkt_cap_file_proxy(livetrace_session_id)

Get reverse packet capture file proxy

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi(swagger_client.ApiClient(configuration))
livetrace_session_id = 'livetrace_session_id_example' # str | Livetrace session ID

try:
    # Get reverse packet capture file proxy
    api_instance.get_reverse_pkt_cap_file_proxy(livetrace_session_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi->get_reverse_pkt_cap_file_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **livetrace_session_id** | **str**| Livetrace session ID | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_live_trace**
> LiveTraceListResult list_live_trace(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List all livetrace sessions

List all livetrace sessions

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List all livetrace sessions
    api_response = api_instance.list_live_trace(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringLivetraceApi->list_live_trace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**LiveTraceListResult**](LiveTraceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

