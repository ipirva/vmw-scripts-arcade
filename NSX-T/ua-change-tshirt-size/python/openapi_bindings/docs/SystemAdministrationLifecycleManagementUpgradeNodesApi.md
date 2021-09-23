# swagger_client.SystemAdministrationLifecycleManagementUpgradeNodesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_upgrade_task_**](SystemAdministrationLifecycleManagementUpgradeNodesApi.md#execute_upgrade_task_) | **POST** /node/upgrade/performtask?action&#x3D;[^/]+ | Execute upgrade task
[**get_node_upgrade_status_summary**](SystemAdministrationLifecycleManagementUpgradeNodesApi.md#get_node_upgrade_status_summary) | **GET** /node/upgrade/status-summary | Get upgrade status summary
[**get_nodes**](SystemAdministrationLifecycleManagementUpgradeNodesApi.md#get_nodes) | **GET** /upgrade/nodes | Get list of nodes across all types
[**get_nodes_summary**](SystemAdministrationLifecycleManagementUpgradeNodesApi.md#get_nodes_summary) | **GET** /upgrade/nodes-summary | Get summary of nodes
[**get_upgrade_progress_status**](SystemAdministrationLifecycleManagementUpgradeNodesApi.md#get_upgrade_progress_status) | **GET** /node/upgrade/progress-status | Get upgrade progress status
[**get_upgrade_task_status**](SystemAdministrationLifecycleManagementUpgradeNodesApi.md#get_upgrade_task_status) | **GET** /node/upgrade | Get upgrade task status
[**get_version_whitelist**](SystemAdministrationLifecycleManagementUpgradeNodesApi.md#get_version_whitelist) | **GET** /upgrade/version-whitelist | Get the version whitelist
[**get_version_whitelist_by_component**](SystemAdministrationLifecycleManagementUpgradeNodesApi.md#get_version_whitelist_by_component) | **GET** /upgrade/version-whitelist/{component_type} | Get the version whitelist for the specified component
[**update_version_whitelist**](SystemAdministrationLifecycleManagementUpgradeNodesApi.md#update_version_whitelist) | **PUT** /upgrade/version-whitelist/{component_type} | Update the version whitelist for the specified component type

# **execute_upgrade_task_**
> UpgradeTaskProperties execute_upgrade_task_(body)

Execute upgrade task

Execute upgrade task. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpgradeTaskProperties() # UpgradeTaskProperties | 

try:
    # Execute upgrade task
    api_response = api_instance.execute_upgrade_task_(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeNodesApi->execute_upgrade_task_: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeTaskProperties**](UpgradeTaskProperties.md)|  | 

### Return type

[**UpgradeTaskProperties**](UpgradeTaskProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_upgrade_status_summary**
> UpgradeStatusSummary get_node_upgrade_status_summary()

Get upgrade status summary

Get status summary of node upgrade, if upgrade bundle is present. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeNodesApi(swagger_client.ApiClient(configuration))

try:
    # Get upgrade status summary
    api_response = api_instance.get_node_upgrade_status_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeNodesApi->get_node_upgrade_status_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UpgradeStatusSummary**](UpgradeStatusSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes**
> NodeInfoListResult get_nodes(component_type=component_type, component_version=component_version, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeNodesApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which nodes will be filtered (optional)
component_version = 'component_version_example' # str | Component version based on which nodes will be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get list of nodes across all types
    api_response = api_instance.get_nodes(component_type=component_type, component_version=component_version, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeNodesApi->get_nodes: %s\n" % e)
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

# **get_nodes_summary**
> NodeSummaryList get_nodes_summary()

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeNodesApi(swagger_client.ApiClient(configuration))

try:
    # Get summary of nodes
    api_response = api_instance.get_nodes_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeNodesApi->get_nodes_summary: %s\n" % e)
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

# **get_upgrade_progress_status**
> UpgradeProgressStatus get_upgrade_progress_status()

Get upgrade progress status

Get progress status of last upgrade step, if upgrade bundle is present. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeNodesApi(swagger_client.ApiClient(configuration))

try:
    # Get upgrade progress status
    api_response = api_instance.get_upgrade_progress_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeNodesApi->get_upgrade_progress_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UpgradeProgressStatus**](UpgradeProgressStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_task_status**
> UpgradeTaskProperties get_upgrade_task_status(bundle_name=bundle_name, upgrade_task_id=upgrade_task_id)

Get upgrade task status

Get upgrade task status for the given task of the given bundle. Both bundle_name and task_id must be provided, otherwise you will receive a 404 NOT FOUND response. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeNodesApi(swagger_client.ApiClient(configuration))
bundle_name = 'bundle_name_example' # str | Bundle Name (optional)
upgrade_task_id = 'upgrade_task_id_example' # str | Upgrade Task ID (optional)

try:
    # Get upgrade task status
    api_response = api_instance.get_upgrade_task_status(bundle_name=bundle_name, upgrade_task_id=upgrade_task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeNodesApi->get_upgrade_task_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_name** | **str**| Bundle Name | [optional] 
 **upgrade_task_id** | **str**| Upgrade Task ID | [optional] 

### Return type

[**UpgradeTaskProperties**](UpgradeTaskProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_whitelist**
> AcceptableComponentVersionList get_version_whitelist()

Get the version whitelist

Get whitelist of versions for different components

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeNodesApi(swagger_client.ApiClient(configuration))

try:
    # Get the version whitelist
    api_response = api_instance.get_version_whitelist()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeNodesApi->get_version_whitelist: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AcceptableComponentVersionList**](AcceptableComponentVersionList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_whitelist_by_component**
> AcceptableComponentVersion get_version_whitelist_by_component(component_type)

Get the version whitelist for the specified component

Get whitelist of versions for a component. Component can include HOST, EDGE, CCP, MP

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeNodesApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | 

try:
    # Get the version whitelist for the specified component
    api_response = api_instance.get_version_whitelist_by_component(component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeNodesApi->get_version_whitelist_by_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**|  | 

### Return type

[**AcceptableComponentVersion**](AcceptableComponentVersion.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version_whitelist**
> update_version_whitelist(body, component_type)

Update the version whitelist for the specified component type

Update the version whitelist for the specified component type (HOST, EDGE, CCP, MP).

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.VersionList() # VersionList | 
component_type = 'component_type_example' # str | 

try:
    # Update the version whitelist for the specified component type
    api_instance.update_version_whitelist(body, component_type)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeNodesApi->update_version_whitelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VersionList**](VersionList.md)|  | 
 **component_type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

