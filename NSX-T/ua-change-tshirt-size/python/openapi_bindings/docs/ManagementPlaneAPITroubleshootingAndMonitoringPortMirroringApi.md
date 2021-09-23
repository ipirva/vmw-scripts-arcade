# swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_port_mirroring_sessions**](ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi.md#create_port_mirroring_sessions) | **POST** /mirror-sessions | Create a mirror session
[**delete_port_mirroring_session**](ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi.md#delete_port_mirroring_session) | **DELETE** /mirror-sessions/{mirror-session-id} | Delete the mirror session
[**get_mirror_stack_status**](ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi.md#get_mirror_stack_status) | **GET** /mirror-sessions/{mirror-session-id}/mirror-stack-status | Get the mirror stack status on given remote L3 mirror session
[**get_port_mirroring_session**](ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi.md#get_port_mirroring_session) | **GET** /mirror-sessions/{mirror-session-id} | Get the mirror session
[**list_port_mirroring_session**](ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi.md#list_port_mirroring_session) | **GET** /mirror-sessions | List all mirror sessions
[**update_port_mirroring_session**](ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi.md#update_port_mirroring_session) | **PUT** /mirror-sessions/{mirror-session-id} | Update the mirror session
[**verify_port_mirroring_session_verify**](ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi.md#verify_port_mirroring_session_verify) | **POST** /mirror-sessions/{mirror-session-id}?action&#x3D;verify | Verify whether the mirror session is still valid

# **create_port_mirroring_sessions**
> PortMirroringSession create_port_mirroring_sessions(body)

Create a mirror session

Create a mirror session

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi(swagger_client.ApiClient(configuration))
body = swagger_client.PortMirroringSession() # PortMirroringSession | 

try:
    # Create a mirror session
    api_response = api_instance.create_port_mirroring_sessions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi->create_port_mirroring_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PortMirroringSession**](PortMirroringSession.md)|  | 

### Return type

[**PortMirroringSession**](PortMirroringSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_port_mirroring_session**
> delete_port_mirroring_session(mirror_session_id)

Delete the mirror session

Delete the mirror session

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi(swagger_client.ApiClient(configuration))
mirror_session_id = 'mirror_session_id_example' # str | 

try:
    # Delete the mirror session
    api_instance.delete_port_mirroring_session(mirror_session_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi->delete_port_mirroring_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mirror_session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mirror_stack_status**
> MirrorStackStatusListResult get_mirror_stack_status(mirror_session_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get the mirror stack status on given remote L3 mirror session

Get the mirror stack status on given remote L3 mirror session

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi(swagger_client.ApiClient(configuration))
mirror_session_id = 'mirror_session_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get the mirror stack status on given remote L3 mirror session
    api_response = api_instance.get_mirror_stack_status(mirror_session_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi->get_mirror_stack_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mirror_session_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**MirrorStackStatusListResult**](MirrorStackStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port_mirroring_session**
> PortMirroringSession get_port_mirroring_session(mirror_session_id)

Get the mirror session

Get the mirror session

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi(swagger_client.ApiClient(configuration))
mirror_session_id = 'mirror_session_id_example' # str | 

try:
    # Get the mirror session
    api_response = api_instance.get_port_mirroring_session(mirror_session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi->get_port_mirroring_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mirror_session_id** | **str**|  | 

### Return type

[**PortMirroringSession**](PortMirroringSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_port_mirroring_session**
> PortMirroringSessionListResult list_port_mirroring_session(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List all mirror sessions

List all mirror sessions

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List all mirror sessions
    api_response = api_instance.list_port_mirroring_session(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi->list_port_mirroring_session: %s\n" % e)
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

[**PortMirroringSessionListResult**](PortMirroringSessionListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_port_mirroring_session**
> PortMirroringSession update_port_mirroring_session(body, mirror_session_id)

Update the mirror session

Update the mirror session

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi(swagger_client.ApiClient(configuration))
body = swagger_client.PortMirroringSession() # PortMirroringSession | 
mirror_session_id = 'mirror_session_id_example' # str | 

try:
    # Update the mirror session
    api_response = api_instance.update_port_mirroring_session(body, mirror_session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi->update_port_mirroring_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PortMirroringSession**](PortMirroringSession.md)|  | 
 **mirror_session_id** | **str**|  | 

### Return type

[**PortMirroringSession**](PortMirroringSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_port_mirroring_session_verify**
> verify_port_mirroring_session_verify(mirror_session_id)

Verify whether the mirror session is still valid

Verify whether all participants are on the same transport node

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi(swagger_client.ApiClient(configuration))
mirror_session_id = 'mirror_session_id_example' # str | 

try:
    # Verify whether the mirror session is still valid
    api_instance.verify_port_mirroring_session_verify(mirror_session_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringPortMirroringApi->verify_port_mirroring_session_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mirror_session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

