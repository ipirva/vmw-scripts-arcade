# swagger_client.SystemAdministrationLifecycleManagementMigrationNodesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_migration_nodes**](SystemAdministrationLifecycleManagementMigrationNodesApi.md#get_migration_nodes) | **GET** /migration/nodes | Get list of nodes across all types
[**get_migration_nodes_summary**](SystemAdministrationLifecycleManagementMigrationNodesApi.md#get_migration_nodes_summary) | **GET** /migration/nodes-summary | Get summary of nodes

# **get_migration_nodes**
> NodeInfoListResult get_migration_nodes(component_type=component_type, component_version=component_version, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get list of nodes across all types

Get list of nodes. If request parameter component type is specified, then all nodes for that component will be returned. If request parameter component version is specified, then all nodes at that version will be returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationNodesApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which nodes will be filtered (optional)
component_version = 'component_version_example' # str | Component version based on which nodes will be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get list of nodes across all types
    api_response = api_instance.get_migration_nodes(component_type=component_type, component_version=component_version, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationNodesApi->get_migration_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type based on which nodes will be filtered | [optional] 
 **component_version** | **str**| Component version based on which nodes will be filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**NodeInfoListResult**](NodeInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_nodes_summary**
> NodeSummaryList get_migration_nodes_summary()

Get summary of nodes

Get summary of nodes, which includes node count for each type and component version.

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationNodesApi(swagger_client.ApiClient(configuration))

try:
    # Get summary of nodes
    api_response = api_instance.get_migration_nodes_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationNodesApi->get_migration_nodes_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSummaryList**](NodeSummaryList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

