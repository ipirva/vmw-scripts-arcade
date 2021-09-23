# swagger_client.SystemAdministrationConfigurationNSXManagersAPIServicesTaskManagementApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_tasks**](SystemAdministrationConfigurationNSXManagersAPIServicesTaskManagementApi.md#list_tasks) | **GET** /tasks | Get information about all tasks
[**read_task_properties**](SystemAdministrationConfigurationNSXManagersAPIServicesTaskManagementApi.md#read_task_properties) | **GET** /tasks/{task-id} | Get information about the specified task
[**read_task_result**](SystemAdministrationConfigurationNSXManagersAPIServicesTaskManagementApi.md#read_task_result) | **GET** /tasks/{task-id}/response | Get the response of a task

# **list_tasks**
> TaskListResult list_tasks(cursor=cursor, included_fields=included_fields, page_size=page_size, request_uri=request_uri, sort_ascending=sort_ascending, sort_by=sort_by, status=status, user=user)

Get information about all tasks

Get information about all tasks

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersAPIServicesTaskManagementApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
request_uri = 'request_uri_example' # str | Request URI(s) to include in query result (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
status = 'status_example' # str | Status(es) to include in query result (optional)
user = 'user_example' # str | Names of users to include in query result (optional)

try:
    # Get information about all tasks
    api_response = api_instance.list_tasks(cursor=cursor, included_fields=included_fields, page_size=page_size, request_uri=request_uri, sort_ascending=sort_ascending, sort_by=sort_by, status=status, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersAPIServicesTaskManagementApi->list_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **request_uri** | **str**| Request URI(s) to include in query result | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **status** | **str**| Status(es) to include in query result | [optional] 
 **user** | **str**| Names of users to include in query result | [optional] 

### Return type

[**TaskListResult**](TaskListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_task_properties**
> TaskProperties read_task_properties(task_id)

Get information about the specified task

Get information about the specified task

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersAPIServicesTaskManagementApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | ID of task to read

try:
    # Get information about the specified task
    api_response = api_instance.read_task_properties(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersAPIServicesTaskManagementApi->read_task_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| ID of task to read | 

### Return type

[**TaskProperties**](TaskProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_task_result**
> object read_task_result(task_id)

Get the response of a task

Get the response of a task

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersAPIServicesTaskManagementApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | ID of task to read

try:
    # Get the response of a task
    api_response = api_instance.read_task_result(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersAPIServicesTaskManagementApi->read_task_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| ID of task to read | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

