# swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bridge_cluster**](ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi.md#create_bridge_cluster) | **POST** /bridge-clusters | Create a Bridge Cluster
[**delete_bridge_cluster**](ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi.md#delete_bridge_cluster) | **DELETE** /bridge-clusters/{bridgecluster-id} | Delete a Bridge Cluster
[**get_bridge_cluster**](ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi.md#get_bridge_cluster) | **GET** /bridge-clusters/{bridgecluster-id} | Get Information about a bridge cluster
[**get_bridge_cluster_status**](ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi.md#get_bridge_cluster_status) | **GET** /bridge-clusters/{cluster-id}/status | Returns status of a specified Bridge Cluster
[**list_bridge_clusters**](ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi.md#list_bridge_clusters) | **GET** /bridge-clusters | List All Bridge Clusters
[**update_bridge_cluster**](ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi.md#update_bridge_cluster) | **PUT** /bridge-clusters/{bridgecluster-id} | Update a Bridge Cluster

# **create_bridge_cluster**
> BridgeCluster create_bridge_cluster(body)

Create a Bridge Cluster

Creates a bridge cluster. It is collection of transport nodes that will do the bridging for overlay network to vlan networks. Bridge cluster may have one or more transport nodes 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi(swagger_client.ApiClient(configuration))
body = swagger_client.BridgeCluster() # BridgeCluster | 

try:
    # Create a Bridge Cluster
    api_response = api_instance.create_bridge_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi->create_bridge_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BridgeCluster**](BridgeCluster.md)|  | 

### Return type

[**BridgeCluster**](BridgeCluster.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bridge_cluster**
> delete_bridge_cluster(bridgecluster_id)

Delete a Bridge Cluster

Removes the specified Bridge Cluster.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi(swagger_client.ApiClient(configuration))
bridgecluster_id = 'bridgecluster_id_example' # str | 

try:
    # Delete a Bridge Cluster
    api_instance.delete_bridge_cluster(bridgecluster_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi->delete_bridge_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridgecluster_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bridge_cluster**
> BridgeCluster get_bridge_cluster(bridgecluster_id)

Get Information about a bridge cluster

Returns information about a specified bridge cluster.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi(swagger_client.ApiClient(configuration))
bridgecluster_id = 'bridgecluster_id_example' # str | 

try:
    # Get Information about a bridge cluster
    api_response = api_instance.get_bridge_cluster(bridgecluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi->get_bridge_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridgecluster_id** | **str**|  | 

### Return type

[**BridgeCluster**](BridgeCluster.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bridge_cluster_status**
> BridgeClusterStatus get_bridge_cluster_status(cluster_id, source=source)

Returns status of a specified Bridge Cluster

Get the status for the Bridge Cluster of the given cluster id

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Returns status of a specified Bridge Cluster
    api_response = api_instance.get_bridge_cluster_status(cluster_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi->get_bridge_cluster_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**BridgeClusterStatus**](BridgeClusterStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bridge_clusters**
> BridgeClusterListResult list_bridge_clusters(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List All Bridge Clusters

Returns information about all configured bridge clusters 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List All Bridge Clusters
    api_response = api_instance.list_bridge_clusters(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi->list_bridge_clusters: %s\n" % e)
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

[**BridgeClusterListResult**](BridgeClusterListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bridge_cluster**
> BridgeCluster update_bridge_cluster(body, bridgecluster_id)

Update a Bridge Cluster

Modifies a existing bridge cluster. One of more transport nodes can be added or removed from the bridge cluster using this API. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi(swagger_client.ApiClient(configuration))
body = swagger_client.BridgeCluster() # BridgeCluster | 
bridgecluster_id = 'bridgecluster_id_example' # str | 

try:
    # Update a Bridge Cluster
    api_response = api_instance.update_bridge_cluster(body, bridgecluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeClustersApi->update_bridge_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BridgeCluster**](BridgeCluster.md)|  | 
 **bridgecluster_id** | **str**|  | 

### Return type

[**BridgeCluster**](BridgeCluster.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

