# swagger_client.SystemAdministrationConfigurationFabricNodesPhysicalServersApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_physical_server**](SystemAdministrationConfigurationFabricNodesPhysicalServersApi.md#get_physical_server) | **GET** /fabric/physical-servers/{physical-server-id} | Return a specific physical server
[**list_physical_servers**](SystemAdministrationConfigurationFabricNodesPhysicalServersApi.md#list_physical_servers) | **GET** /fabric/physical-servers | Return the list of physical servers

# **get_physical_server**
> PhysicalServer get_physical_server(physical_server_id)

Return a specific physical server

Returns information about physical/bare metal server based on given transport node id.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesPhysicalServersApi(swagger_client.ApiClient(configuration))
physical_server_id = 'physical_server_id_example' # str | 

try:
    # Return a specific physical server
    api_response = api_instance.get_physical_server(physical_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesPhysicalServersApi->get_physical_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **physical_server_id** | **str**|  | 

### Return type

[**PhysicalServer**](PhysicalServer.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_physical_servers**
> PhysicalServerListResult list_physical_servers(cursor=cursor, display_name=display_name, included_fields=included_fields, os_type=os_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return the list of physical servers

Returns information of all physical/bare metal servers registered as TN.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesPhysicalServersApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
display_name = 'display_name_example' # str | Display Name of the physical server (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
os_type = 'os_type_example' # str | OS type of the physical server (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the list of physical servers
    api_response = api_instance.list_physical_servers(cursor=cursor, display_name=display_name, included_fields=included_fields, os_type=os_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesPhysicalServersApi->list_physical_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **display_name** | **str**| Display Name of the physical server | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **os_type** | **str**| OS type of the physical server | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**PhysicalServerListResult**](PhysicalServerListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

