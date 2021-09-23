# swagger_client.SystemAdministrationMonitoringSystemHealthPluginsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plugin_file**](SystemAdministrationMonitoringSystemHealthPluginsApi.md#create_plugin_file) | **POST** /systemhealth/plugins/{plugin-id}/files/{file-name}/data | Upload a plugin File to MP
[**create_system_health_plugin**](SystemAdministrationMonitoringSystemHealthPluginsApi.md#create_system_health_plugin) | **POST** /systemhealth/plugins | Create a system health plugin
[**delete_system_health_plugin**](SystemAdministrationMonitoringSystemHealthPluginsApi.md#delete_system_health_plugin) | **DELETE** /systemhealth/plugins/{plugin-id} | Delete an existing system health plugin
[**list_all_system_health_plugins**](SystemAdministrationMonitoringSystemHealthPluginsApi.md#list_all_system_health_plugins) | **GET** /systemhealth/plugins | Show all the system health plugin
[**show_system_health_plugin**](SystemAdministrationMonitoringSystemHealthPluginsApi.md#show_system_health_plugin) | **GET** /systemhealth/plugins/{plugin-id} | Show the details of a system health plugin
[**show_system_health_plugin_on_node**](SystemAdministrationMonitoringSystemHealthPluginsApi.md#show_system_health_plugin_on_node) | **GET** /systemhealth/plugins/status/{node-id} | Show the installed system health plugin list

# **create_plugin_file**
> PluginFileProperties create_plugin_file(file_name, plugin_id)

Upload a plugin File to MP

Upload a plugin File to MP

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthPluginsApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | Plugin filename
plugin_id = 'plugin_id_example' # str | Plugin ID

try:
    # Upload a plugin File to MP
    api_response = api_instance.create_plugin_file(file_name, plugin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthPluginsApi->create_plugin_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Plugin filename | 
 **plugin_id** | **str**| Plugin ID | 

### Return type

[**PluginFileProperties**](PluginFileProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_system_health_plugin**
> SystemHealthPluginProfile create_system_health_plugin(body)

Create a system health plugin

Create a system health plugin. 

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthPluginsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SystemHealthPluginProfile() # SystemHealthPluginProfile | 

try:
    # Create a system health plugin
    api_response = api_instance.create_system_health_plugin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthPluginsApi->create_system_health_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemHealthPluginProfile**](SystemHealthPluginProfile.md)|  | 

### Return type

[**SystemHealthPluginProfile**](SystemHealthPluginProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_system_health_plugin**
> delete_system_health_plugin(plugin_id)

Delete an existing system health plugin

Delete an existing system health plugin by ID.

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthPluginsApi(swagger_client.ApiClient(configuration))
plugin_id = 'plugin_id_example' # str | 

try:
    # Delete an existing system health plugin
    api_instance.delete_system_health_plugin(plugin_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthPluginsApi->delete_system_health_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_system_health_plugins**
> SystemHealthPluginProfileList list_all_system_health_plugins(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Show all the system health plugin

Show all the system health plugins. 

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthPluginsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Show all the system health plugin
    api_response = api_instance.list_all_system_health_plugins(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthPluginsApi->list_all_system_health_plugins: %s\n" % e)
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

[**SystemHealthPluginProfileList**](SystemHealthPluginProfileList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_system_health_plugin**
> SystemHealthPluginProfile show_system_health_plugin(plugin_id)

Show the details of a system health plugin

Show the details of a system health plugin. 

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthPluginsApi(swagger_client.ApiClient(configuration))
plugin_id = 'plugin_id_example' # str | 

try:
    # Show the details of a system health plugin
    api_response = api_instance.show_system_health_plugin(plugin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthPluginsApi->show_system_health_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**|  | 

### Return type

[**SystemHealthPluginProfile**](SystemHealthPluginProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_system_health_plugin_on_node**
> PluginStatusList show_system_health_plugin_on_node(node_id)

Show the installed system health plugin list

Show all the installed system health plugins on given node 

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthPluginsApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Show the installed system health plugin list
    api_response = api_instance.show_system_health_plugin_on_node(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthPluginsApi->show_system_health_plugin_on_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**PluginStatusList**](PluginStatusList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

