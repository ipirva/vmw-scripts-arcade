# swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cluster_node**](SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi.md#add_cluster_node) | **POST** /cluster/nodes | Add a controller to the cluster
[**delete_cluster_node_config**](SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi.md#delete_cluster_node_config) | **DELETE** /cluster/nodes/{node-id} | Remove a controller from the cluster
[**detach_cluster_node_remove_node**](SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi.md#detach_cluster_node_remove_node) | **POST** /cluster/{node-id}?action&#x3D;remove_node | Detach a node from the Cluster
[**get_backup_ui_frames_info**](SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi.md#get_backup_ui_frames_info) | **GET** /cluster/backups/ui_frames | Get backup frames for UI
[**get_cluster_node_config**](SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi.md#get_cluster_node_config) | **GET** /cluster/{node-id} | Read cluster node configuration
[**invoke_delete_cluster_central_api**](SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi.md#invoke_delete_cluster_central_api) | **DELETE** /cluster/{target-node-id}/{target-uri} | Invoke DELETE request on target cluster node
[**invoke_get_cluster_central_api**](SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi.md#invoke_get_cluster_central_api) | **GET** /cluster/{target-node-id}/{target-uri} | Invoke GET request on target cluster node
[**invoke_post_cluster_central_api**](SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi.md#invoke_post_cluster_central_api) | **POST** /cluster/{target-node-id}/{target-uri} | Invoke POST request on target cluster node
[**invoke_put_cluster_central_api**](SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi.md#invoke_put_cluster_central_api) | **PUT** /cluster/{target-node-id}/{target-uri} | Invoke PUT request on target cluster node
[**join_cluster_join_cluster**](SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi.md#join_cluster_join_cluster) | **POST** /cluster?action&#x3D;join_cluster | Join this node to a NSX Cluster
[**list_cluster_node_configs**](SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi.md#list_cluster_node_configs) | **GET** /cluster/nodes | List Cluster Node Configurations
[**read_cluster_config**](SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi.md#read_cluster_config) | **GET** /cluster | Read Cluster Configuration
[**read_cluster_node_config**](SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi.md#read_cluster_node_config) | **GET** /cluster/nodes/{node-id} | Read Cluster Node Configuration

# **add_cluster_node**
> ClusterNodeConfig add_cluster_node(body, action)

Add a controller to the cluster

Add a new controller to the NSX cluster. Deprecated. Use POST /cluster?action=join_cluster to join a node to cluster. The controller comes with the new node. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddClusterNodeSpec() # AddClusterNodeSpec | 
action = 'action_example' # str | 

try:
    # Add a controller to the cluster
    api_response = api_instance.add_cluster_node(body, action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi->add_cluster_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddClusterNodeSpec**](AddClusterNodeSpec.md)|  | 
 **action** | **str**|  | 

### Return type

[**ClusterNodeConfig**](ClusterNodeConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_node_config**
> delete_cluster_node_config(node_id)

Remove a controller from the cluster

Removes the specified controller from the NSX cluster. Before you can remove a controller from the cluster, you must shut down the controller service with the \"stop service controller\" command. Deprecated. Use POST /cluster/<node-id>?action=remove_node to detach a node from cluster. The controller is removed with the node. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Remove a controller from the cluster
    api_instance.delete_cluster_node_config(node_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi->delete_cluster_node_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_cluster_node_remove_node**
> ClusterConfiguration detach_cluster_node_remove_node(node_id, force=force, graceful_shutdown=graceful_shutdown, ignore_repository_ip_check=ignore_repository_ip_check)

Detach a node from the Cluster

Detach a node from the Cluster

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | UUID of the node
force = 'force_example' # str |  (optional)
graceful_shutdown = 'false' # str |  (optional) (default to false)
ignore_repository_ip_check = 'false' # str |  (optional) (default to false)

try:
    # Detach a node from the Cluster
    api_response = api_instance.detach_cluster_node_remove_node(node_id, force=force, graceful_shutdown=graceful_shutdown, ignore_repository_ip_check=ignore_repository_ip_check)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi->detach_cluster_node_remove_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| UUID of the node | 
 **force** | **str**|  | [optional] 
 **graceful_shutdown** | **str**|  | [optional] [default to false]
 **ignore_repository_ip_check** | **str**|  | [optional] [default to false]

### Return type

[**ClusterConfiguration**](ClusterConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_ui_frames_info**
> BackupUiFramesInfoList get_backup_ui_frames_info(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, ui_tab_type=ui_tab_type)

Get backup frames for UI

Returns list of backup frames and some metadata to be used by UI. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
ui_tab_type = 'LOCAL_MANAGER_TAB' # str |  (optional) (default to LOCAL_MANAGER_TAB)

try:
    # Get backup frames for UI
    api_response = api_instance.get_backup_ui_frames_info(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, ui_tab_type=ui_tab_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi->get_backup_ui_frames_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **ui_tab_type** | **str**|  | [optional] [default to LOCAL_MANAGER_TAB]

### Return type

[**BackupUiFramesInfoList**](BackupUiFramesInfoList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_node_config**
> ClusterNodeInfo get_cluster_node_config(node_id)

Read cluster node configuration

Returns information about the specified NSX cluster node.

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Read cluster node configuration
    api_response = api_instance.get_cluster_node_config(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi->get_cluster_node_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**ClusterNodeInfo**](ClusterNodeInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_delete_cluster_central_api**
> invoke_delete_cluster_central_api(target_node_id, target_uri)

Invoke DELETE request on target cluster node

Invoke DELETE request on target cluster node

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID or keyword self
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke DELETE request on target cluster node
    api_instance.invoke_delete_cluster_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi->invoke_delete_cluster_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID or keyword self | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_get_cluster_central_api**
> invoke_get_cluster_central_api(target_node_id, target_uri)

Invoke GET request on target cluster node

Invoke GET request on target cluster node

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID or keyword self
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke GET request on target cluster node
    api_instance.invoke_get_cluster_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi->invoke_get_cluster_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID or keyword self | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_post_cluster_central_api**
> invoke_post_cluster_central_api(target_node_id, target_uri)

Invoke POST request on target cluster node

Invoke POST request on target cluster node

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID or keyword self
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke POST request on target cluster node
    api_instance.invoke_post_cluster_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi->invoke_post_cluster_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID or keyword self | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_put_cluster_central_api**
> invoke_put_cluster_central_api(target_node_id, target_uri)

Invoke PUT request on target cluster node

Invoke PUT request on target cluster node

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID or keyword self
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke PUT request on target cluster node
    api_instance.invoke_put_cluster_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi->invoke_put_cluster_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID or keyword self | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_cluster_join_cluster**
> ClusterConfiguration join_cluster_join_cluster(body)

Join this node to a NSX Cluster

Join this node to a NSX Cluster

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.JoinClusterParameters() # JoinClusterParameters | 

try:
    # Join this node to a NSX Cluster
    api_response = api_instance.join_cluster_join_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi->join_cluster_join_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JoinClusterParameters**](JoinClusterParameters.md)|  | 

### Return type

[**ClusterConfiguration**](ClusterConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_node_configs**
> ClusterNodeConfigListResult list_cluster_node_configs(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List Cluster Node Configurations

Returns information about all NSX cluster nodes. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List Cluster Node Configurations
    api_response = api_instance.list_cluster_node_configs(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi->list_cluster_node_configs: %s\n" % e)
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

[**ClusterNodeConfigListResult**](ClusterNodeConfigListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_config**
> ClusterConfig read_cluster_config()

Read Cluster Configuration

Returns information about the NSX cluster configuration. An NSX cluster has two functions or purposes, commonly referred to as \"roles.\" These two roles are control and management. Each NSX installation has a single cluster. Separate NSX clusters do not share data. In other words, a given data-plane node is attached to only one cluster, not to multiple clusters. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Read Cluster Configuration
    api_response = api_instance.read_cluster_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi->read_cluster_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterConfig**](ClusterConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_node_config**
> ClusterNodeConfig read_cluster_node_config(node_id)

Read Cluster Node Configuration

Returns information about the specified NSX cluster node. Deprecated. Use GET /cluster/<node-id> to get cluster node configuration. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Read Cluster Node Configuration
    api_response = api_instance.read_cluster_node_config(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterConfigurationApi->read_cluster_node_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**ClusterNodeConfig**](ClusterNodeConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

