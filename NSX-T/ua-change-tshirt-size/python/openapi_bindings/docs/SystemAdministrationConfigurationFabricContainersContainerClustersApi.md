# swagger_client.SystemAdministrationConfigurationFabricContainersContainerClustersApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_container_cluster**](SystemAdministrationConfigurationFabricContainersContainerClustersApi.md#get_container_cluster) | **GET** /fabric/container-clusters/{container-cluster-id} | Return a container cluster
[**get_container_cluster_node**](SystemAdministrationConfigurationFabricContainersContainerClustersApi.md#get_container_cluster_node) | **GET** /fabric/container-cluster-nodes/{container-cluster-node-id} | Return a container cluster node
[**get_container_ingress_policy**](SystemAdministrationConfigurationFabricContainersContainerClustersApi.md#get_container_ingress_policy) | **GET** /fabric/container-ingress-policies/{ingress-policy-id} | Returns an ingress policy spec
[**get_container_network_policy**](SystemAdministrationConfigurationFabricContainersContainerClustersApi.md#get_container_network_policy) | **GET** /fabric/container-network-policies/{network-policy-id} | Return a network policy spec
[**list_container_cluster_nodes**](SystemAdministrationConfigurationFabricContainersContainerClustersApi.md#list_container_cluster_nodes) | **GET** /fabric/container-cluster-nodes | Return the list of container cluster nodes
[**list_container_clusters**](SystemAdministrationConfigurationFabricContainersContainerClustersApi.md#list_container_clusters) | **GET** /fabric/container-clusters | Return the List of Container Clusters
[**list_container_ingress_policies**](SystemAdministrationConfigurationFabricContainersContainerClustersApi.md#list_container_ingress_policies) | **GET** /fabric/container-ingress-policies | Return the List of Container Ingress Policies
[**list_container_network_policies**](SystemAdministrationConfigurationFabricContainersContainerClustersApi.md#list_container_network_policies) | **GET** /fabric/container-network-policies | Return the List of Container Network Policies

# **get_container_cluster**
> ContainerCluster get_container_cluster(container_cluster_id)

Return a container cluster

Returns information about a specific container cluster

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricContainersContainerClustersApi(swagger_client.ApiClient(configuration))
container_cluster_id = 'container_cluster_id_example' # str | 

try:
    # Return a container cluster
    api_response = api_instance.get_container_cluster(container_cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricContainersContainerClustersApi->get_container_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_cluster_id** | **str**|  | 

### Return type

[**ContainerCluster**](ContainerCluster.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_cluster_node**
> ContainerClusterNode get_container_cluster_node(container_cluster_node_id)

Return a container cluster node

Returns information about a specific container cluster node.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricContainersContainerClustersApi(swagger_client.ApiClient(configuration))
container_cluster_node_id = 'container_cluster_node_id_example' # str | 

try:
    # Return a container cluster node
    api_response = api_instance.get_container_cluster_node(container_cluster_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricContainersContainerClustersApi->get_container_cluster_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_cluster_node_id** | **str**|  | 

### Return type

[**ContainerClusterNode**](ContainerClusterNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_ingress_policy**
> ContainerIngressPolicy get_container_ingress_policy(ingress_policy_id)

Returns an ingress policy spec

Returns information about a specific ingress policy.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricContainersContainerClustersApi(swagger_client.ApiClient(configuration))
ingress_policy_id = 'ingress_policy_id_example' # str | 

try:
    # Returns an ingress policy spec
    api_response = api_instance.get_container_ingress_policy(ingress_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricContainersContainerClustersApi->get_container_ingress_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingress_policy_id** | **str**|  | 

### Return type

[**ContainerIngressPolicy**](ContainerIngressPolicy.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_network_policy**
> ContainerNetworkPolicy get_container_network_policy(network_policy_id)

Return a network policy spec

Returns information about a specific network policy.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricContainersContainerClustersApi(swagger_client.ApiClient(configuration))
network_policy_id = 'network_policy_id_example' # str | 

try:
    # Return a network policy spec
    api_response = api_instance.get_container_network_policy(network_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricContainersContainerClustersApi->get_container_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_policy_id** | **str**|  | 

### Return type

[**ContainerNetworkPolicy**](ContainerNetworkPolicy.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_container_cluster_nodes**
> ContainerClusterNodeListResult list_container_cluster_nodes(container_cluster_id=container_cluster_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return the list of container cluster nodes

Returns information about all container cluster nodes.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricContainersContainerClustersApi(swagger_client.ApiClient(configuration))
container_cluster_id = 'container_cluster_id_example' # str | Identifier of the container cluster (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the list of container cluster nodes
    api_response = api_instance.list_container_cluster_nodes(container_cluster_id=container_cluster_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricContainersContainerClustersApi->list_container_cluster_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_cluster_id** | **str**| Identifier of the container cluster | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ContainerClusterNodeListResult**](ContainerClusterNodeListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_container_clusters**
> ContainerClusterListResult list_container_clusters(cluster_type=cluster_type, cursor=cursor, included_fields=included_fields, infra_type=infra_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return the List of Container Clusters

Returns information about all Container Clusters.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricContainersContainerClustersApi(swagger_client.ApiClient(configuration))
cluster_type = 'cluster_type_example' # str | Type of container cluster (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
infra_type = 'infra_type_example' # str | Type of infrastructure (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the List of Container Clusters
    api_response = api_instance.list_container_clusters(cluster_type=cluster_type, cursor=cursor, included_fields=included_fields, infra_type=infra_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricContainersContainerClustersApi->list_container_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_type** | **str**| Type of container cluster | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **infra_type** | **str**| Type of infrastructure | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ContainerClusterListResult**](ContainerClusterListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_container_ingress_policies**
> ContainerIngressPolicyListResult list_container_ingress_policies(container_cluster_id=container_cluster_id, container_project_id=container_project_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return the List of Container Ingress Policies

Returns information about all ingress policies.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricContainersContainerClustersApi(swagger_client.ApiClient(configuration))
container_cluster_id = 'container_cluster_id_example' # str | Identifier of the container cluster (optional)
container_project_id = 'container_project_id_example' # str | Identifier of the container project (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the List of Container Ingress Policies
    api_response = api_instance.list_container_ingress_policies(container_cluster_id=container_cluster_id, container_project_id=container_project_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricContainersContainerClustersApi->list_container_ingress_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_cluster_id** | **str**| Identifier of the container cluster | [optional] 
 **container_project_id** | **str**| Identifier of the container project | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ContainerIngressPolicyListResult**](ContainerIngressPolicyListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_container_network_policies**
> ContainerNetworkPolicyListResult list_container_network_policies(container_cluster_id=container_cluster_id, container_project_id=container_project_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Return the List of Container Network Policies

Returns information about all network policies.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricContainersContainerClustersApi(swagger_client.ApiClient(configuration))
container_cluster_id = 'container_cluster_id_example' # str | Identifier of the container cluster (optional)
container_project_id = 'container_project_id_example' # str | Identifier of the container project (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the List of Container Network Policies
    api_response = api_instance.list_container_network_policies(container_cluster_id=container_cluster_id, container_project_id=container_project_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricContainersContainerClustersApi->list_container_network_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_cluster_id** | **str**| Identifier of the container cluster | [optional] 
 **container_project_id** | **str**| Identifier of the container project | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ContainerNetworkPolicyListResult**](ContainerNetworkPolicyListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

