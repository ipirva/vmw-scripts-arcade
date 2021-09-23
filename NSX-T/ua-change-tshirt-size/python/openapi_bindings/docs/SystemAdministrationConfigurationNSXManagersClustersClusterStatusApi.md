# swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_cluster_node_status**](SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi.md#read_cluster_node_status) | **GET** /cluster/nodes/{node-id}/status | Read cluster node runtime status
[**read_cluster_nodes_aggregate_status**](SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi.md#read_cluster_nodes_aggregate_status) | **GET** /cluster/nodes/status | Read cluster runtime status
[**read_cluster_status**](SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi.md#read_cluster_status) | **GET** /cluster/status | Read Cluster Status

# **read_cluster_node_status**
> ClusterNodeStatus read_cluster_node_status(node_id, source=source)

Read cluster node runtime status

Read aggregated runtime status of cluster node. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read cluster node runtime status
    api_response = api_instance.read_cluster_node_status(node_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi->read_cluster_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**ClusterNodeStatus**](ClusterNodeStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_nodes_aggregate_status**
> ClustersAggregateInfo read_cluster_nodes_aggregate_status()

Read cluster runtime status

Read aggregated runtime status of all cluster nodes. Deprecated. Use GET /cluster/status instead. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi(swagger_client.ApiClient(configuration))

try:
    # Read cluster runtime status
    api_response = api_instance.read_cluster_nodes_aggregate_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi->read_cluster_nodes_aggregate_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClustersAggregateInfo**](ClustersAggregateInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_status**
> ClusterStatus read_cluster_status()

Read Cluster Status

Returns status information for the NSX cluster control role and management role. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi(swagger_client.ApiClient(configuration))

try:
    # Read Cluster Status
    api_response = api_instance.read_cluster_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterStatusApi->read_cluster_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterStatus**](ClusterStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

