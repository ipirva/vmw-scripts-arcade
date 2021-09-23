# swagger_client.SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_edge_cluster**](SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi.md#create_edge_cluster) | **POST** /edge-clusters | Create Edge Cluster
[**delete_edge_cluster**](SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi.md#delete_edge_cluster) | **DELETE** /edge-clusters/{edge-cluster-id} | Delete Edge Cluster
[**get_edge_cluster_allocation_status**](SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi.md#get_edge_cluster_allocation_status) | **GET** /edge-clusters/{edge-cluster-id}/allocation-status | Get the Allocation details of an edge cluster
[**get_edge_cluster_state**](SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi.md#get_edge_cluster_state) | **GET** /edge-clusters/{edge-cluster-id}/state | Get the Realized State of a Edge Cluster
[**get_edge_cluster_status**](SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi.md#get_edge_cluster_status) | **GET** /edge-clusters/{edge-cluster-id}/status | Get the status for the Edge cluster of the given id
[**list_edge_clusters**](SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi.md#list_edge_clusters) | **GET** /edge-clusters | List Edge Clusters
[**read_edge_cluster**](SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi.md#read_edge_cluster) | **GET** /edge-clusters/{edge-cluster-id} | Read Edge Cluster
[**replace_edge_cluster_member_transport_node_replace_transport_node**](SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi.md#replace_edge_cluster_member_transport_node_replace_transport_node) | **POST** /edge-clusters/{edge-cluster-id}?action&#x3D;replace_transport_node | Replace the transport node in the specified member of the edge-cluster
[**update_edge_cluster**](SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi.md#update_edge_cluster) | **PUT** /edge-clusters/{edge-cluster-id} | Update Edge Cluster

# **create_edge_cluster**
> EdgeCluster create_edge_cluster(body)

Create Edge Cluster

Creates a new edge cluster. It only supports homogeneous members. The TransportNodes backed by EdgeNode are only allowed in cluster members. DeploymentType (VIRTUAL_MACHINE|PHYSICAL_MACHINE) of these EdgeNodes is recommended to be the same. EdgeCluster supports members of different deployment types. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi(swagger_client.ApiClient(configuration))
body = swagger_client.EdgeCluster() # EdgeCluster | 

try:
    # Create Edge Cluster
    api_response = api_instance.create_edge_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi->create_edge_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EdgeCluster**](EdgeCluster.md)|  | 

### Return type

[**EdgeCluster**](EdgeCluster.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_edge_cluster**
> delete_edge_cluster(edge_cluster_id)

Delete Edge Cluster

Deletes the specified edge cluster.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi(swagger_client.ApiClient(configuration))
edge_cluster_id = 'edge_cluster_id_example' # str | 

try:
    # Delete Edge Cluster
    api_instance.delete_edge_cluster(edge_cluster_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi->delete_edge_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_cluster_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edge_cluster_allocation_status**
> EdgeClusterAllocationStatus get_edge_cluster_allocation_status(edge_cluster_id)

Get the Allocation details of an edge cluster

Returns the allocation details of cluster and its members. Lists the edge node members, active and standby services of each node, utilization details of configured sub-pools. These allocation details can be monitored by customers to trigger migration of certain service contexts to different edge nodes, to balance the utilization of edge node resources. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi(swagger_client.ApiClient(configuration))
edge_cluster_id = 'edge_cluster_id_example' # str | 

try:
    # Get the Allocation details of an edge cluster
    api_response = api_instance.get_edge_cluster_allocation_status(edge_cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi->get_edge_cluster_allocation_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_cluster_id** | **str**|  | 

### Return type

[**EdgeClusterAllocationStatus**](EdgeClusterAllocationStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edge_cluster_state**
> EdgeClusterState get_edge_cluster_state(edge_cluster_id, barrier_id=barrier_id, request_id=request_id)

Get the Realized State of a Edge Cluster

Return realized state information of a edge cluster. Any configuration update that affects the edge cluster can use this API to get its realized state by passing a request_id returned by the configuration change operation. e.g. Update configuration of edge cluster. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi(swagger_client.ApiClient(configuration))
edge_cluster_id = 'edge_cluster_id_example' # str | 
barrier_id = 789 # int |  (optional)
request_id = 'request_id_example' # str | Realization request ID (optional)

try:
    # Get the Realized State of a Edge Cluster
    api_response = api_instance.get_edge_cluster_state(edge_cluster_id, barrier_id=barrier_id, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi->get_edge_cluster_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_cluster_id** | **str**|  | 
 **barrier_id** | **int**|  | [optional] 
 **request_id** | **str**| Realization request ID | [optional] 

### Return type

[**EdgeClusterState**](EdgeClusterState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_edge_cluster_status**
> EdgeClusterStatus get_edge_cluster_status(edge_cluster_id, source=source)

Get the status for the Edge cluster of the given id

Returns the aggregated status for the Edge cluster along with status of all edge nodes in the cluster. Query parameter \"source=realtime\" is the only supported source. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi(swagger_client.ApiClient(configuration))
edge_cluster_id = 'edge_cluster_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the status for the Edge cluster of the given id
    api_response = api_instance.get_edge_cluster_status(edge_cluster_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi->get_edge_cluster_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_cluster_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**EdgeClusterStatus**](EdgeClusterStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_edge_clusters**
> EdgeClusterListResult list_edge_clusters(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List Edge Clusters

Returns information about the configured edge clusters, which enable you to group together transport nodes of the type EdgeNode and apply fabric profiles to all members of the edge cluster. Each edge node can participate in only one edge cluster. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List Edge Clusters
    api_response = api_instance.list_edge_clusters(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi->list_edge_clusters: %s\n" % e)
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

[**EdgeClusterListResult**](EdgeClusterListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_edge_cluster**
> EdgeCluster read_edge_cluster(edge_cluster_id)

Read Edge Cluster

Returns information about the specified edge cluster.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi(swagger_client.ApiClient(configuration))
edge_cluster_id = 'edge_cluster_id_example' # str | 

try:
    # Read Edge Cluster
    api_response = api_instance.read_edge_cluster(edge_cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi->read_edge_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_cluster_id** | **str**|  | 

### Return type

[**EdgeCluster**](EdgeCluster.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_edge_cluster_member_transport_node_replace_transport_node**
> EdgeCluster replace_edge_cluster_member_transport_node_replace_transport_node(body, edge_cluster_id)

Replace the transport node in the specified member of the edge-cluster

Replace the transport node in the specified member of the edge-cluster. This is a disruptive action. This will move all the LogicalRouterPorts(uplink and routerLink) host on the old transport_node to the new transport_node. The transportNode cannot be present in another member of any edgeClusters. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi(swagger_client.ApiClient(configuration))
body = swagger_client.EdgeClusterMemberTransportNode() # EdgeClusterMemberTransportNode | 
edge_cluster_id = 'edge_cluster_id_example' # str | 

try:
    # Replace the transport node in the specified member of the edge-cluster
    api_response = api_instance.replace_edge_cluster_member_transport_node_replace_transport_node(body, edge_cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi->replace_edge_cluster_member_transport_node_replace_transport_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EdgeClusterMemberTransportNode**](EdgeClusterMemberTransportNode.md)|  | 
 **edge_cluster_id** | **str**|  | 

### Return type

[**EdgeCluster**](EdgeCluster.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_edge_cluster**
> EdgeCluster update_edge_cluster(body, edge_cluster_id)

Update Edge Cluster

Modifies the specified edge cluster. Modifiable parameters include the description, display_name, transport-node-id. If the optional fabric_profile_binding is included, resource_type and profile_id are required. User should do a GET on the edge-cluster and obtain the payload and retain the member_index of the existing members as returning in the GET output. For new member additions, the member_index cannot be defined by the user, user can read the system allocated index to the new member in the output of this API call or by doing a GET call. User cannot use this PUT api to replace the transport_node of an existing member because this is a disruption action, we have exposed a explicit API for doing so, refer to \"ReplaceEdgeClusterMemberTransportNode\" EdgeCluster only supports homogeneous members. The TransportNodes backed by EdgeNode are only allowed in cluster members. DeploymentType (VIRTUAL_MACHINE|PHYSICAL_MACHINE) of these EdgeNodes is recommended to be the same. EdgeCluster supports members of different deployment types. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi(swagger_client.ApiClient(configuration))
body = swagger_client.EdgeCluster() # EdgeCluster | 
edge_cluster_id = 'edge_cluster_id_example' # str | 

try:
    # Update Edge Cluster
    api_response = api_instance.update_edge_cluster(body, edge_cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersEdgeClustersApi->update_edge_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EdgeCluster**](EdgeCluster.md)|  | 
 **edge_cluster_id** | **str**|  | 

### Return type

[**EdgeCluster**](EdgeCluster.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

