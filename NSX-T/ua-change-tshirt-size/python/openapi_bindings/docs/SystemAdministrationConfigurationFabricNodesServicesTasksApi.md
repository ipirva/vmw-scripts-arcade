# swagger_client.SystemAdministrationConfigurationFabricNodesServicesTasksApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_appliance_management_task_cancel**](SystemAdministrationConfigurationFabricNodesServicesTasksApi.md#cancel_appliance_management_task_cancel) | **POST** /node/tasks/{task-id}?action&#x3D;cancel | Cancel specified task
[**delete_appliance_management_task**](SystemAdministrationConfigurationFabricNodesServicesTasksApi.md#delete_appliance_management_task) | **DELETE** /node/tasks/{task-id} | Delete task
[**list_appliance_management_tasks**](SystemAdministrationConfigurationFabricNodesServicesTasksApi.md#list_appliance_management_tasks) | **GET** /node/tasks | List appliance management tasks
[**read_appliance_management_task_properties**](SystemAdministrationConfigurationFabricNodesServicesTasksApi.md#read_appliance_management_task_properties) | **GET** /node/tasks/{task-id} | Read task properties
[**read_async_appliance_management_task_response**](SystemAdministrationConfigurationFabricNodesServicesTasksApi.md#read_async_appliance_management_task_response) | **GET** /node/tasks/{task-id}/response | Read asynchronous task response

# **cancel_appliance_management_task_cancel**
> cancel_appliance_management_task_cancel(task_id)

Cancel specified task

Cancel specified task

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesTasksApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | ID of task to delete

try:
    # Cancel specified task
    api_instance.cancel_appliance_management_task_cancel(task_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesTasksApi->cancel_appliance_management_task_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| ID of task to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_appliance_management_task**
> delete_appliance_management_task(task_id)

Delete task

Delete task

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesTasksApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | ID of task to delete

try:
    # Delete task
    api_instance.delete_appliance_management_task(task_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesTasksApi->delete_appliance_management_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| ID of task to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_appliance_management_tasks**
> ApplianceManagementTaskListResult list_appliance_management_tasks(fields=fields, request_method=request_method, request_path=request_path, request_uri=request_uri, status=status, user=user)

List appliance management tasks

List appliance management tasks

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesTasksApi(swagger_client.ApiClient(configuration))
fields = 'fields_example' # str | Fields to include in query results (optional)
request_method = 'request_method_example' # str | Request method(s) to include in query result (optional)
request_path = 'request_path_example' # str | Request URI path(s) to include in query result (optional)
request_uri = 'request_uri_example' # str | Request URI(s) to include in query result (optional)
status = 'status_example' # str | Status(es) to include in query result (optional)
user = 'user_example' # str | Names of users to include in query result (optional)

try:
    # List appliance management tasks
    api_response = api_instance.list_appliance_management_tasks(fields=fields, request_method=request_method, request_path=request_path, request_uri=request_uri, status=status, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesTasksApi->list_appliance_management_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Fields to include in query results | [optional] 
 **request_method** | **str**| Request method(s) to include in query result | [optional] 
 **request_path** | **str**| Request URI path(s) to include in query result | [optional] 
 **request_uri** | **str**| Request URI(s) to include in query result | [optional] 
 **status** | **str**| Status(es) to include in query result | [optional] 
 **user** | **str**| Names of users to include in query result | [optional] 

### Return type

[**ApplianceManagementTaskListResult**](ApplianceManagementTaskListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_appliance_management_task_properties**
> ApplianceManagementTaskProperties read_appliance_management_task_properties(task_id, suppress_redirect=suppress_redirect)

Read task properties

Read task properties

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesTasksApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | ID of task to read
suppress_redirect = false # bool | Suppress redirect status if applicable (optional) (default to false)

try:
    # Read task properties
    api_response = api_instance.read_appliance_management_task_properties(task_id, suppress_redirect=suppress_redirect)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesTasksApi->read_appliance_management_task_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| ID of task to read | 
 **suppress_redirect** | **bool**| Suppress redirect status if applicable | [optional] [default to false]

### Return type

[**ApplianceManagementTaskProperties**](ApplianceManagementTaskProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_async_appliance_management_task_response**
> read_async_appliance_management_task_response(task_id)

Read asynchronous task response

Read asynchronous task response

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesTasksApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | ID of task to read

try:
    # Read asynchronous task response
    api_instance.read_async_appliance_management_task_response(task_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesTasksApi->read_async_appliance_management_task_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| ID of task to read | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

