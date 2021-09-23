# swagger_client.SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_edge_cluster_inter_site_status**](SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi.md#get_edge_cluster_inter_site_status) | **GET** /edge-clusters/{edge-cluster-id}/inter-site/status | Get inter-site status of the edge cluster
[**get_inter_site_edge_node_bgp_neighbor_advertised_routes**](SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi.md#get_inter_site_edge_node_bgp_neighbor_advertised_routes) | **GET** /transport-nodes/{edge-node-id}/inter-site/bgp/neighbors/{neighbor-id}/advertised-routes | Get BGP neighbor advertised routes on edge transport node
[**get_inter_site_edge_node_bgp_neighbor_routes**](SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi.md#get_inter_site_edge_node_bgp_neighbor_routes) | **GET** /transport-nodes/{edge-node-id}/inter-site/bgp/neighbors/{neighbor-id}/routes | Get BGP neighbor learned routes on edge transport node
[**get_inter_site_edge_node_bgp_summary**](SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi.md#get_inter_site_edge_node_bgp_summary) | **GET** /transport-nodes/{edge-node-id}/inter-site/bgp/summary | Get inter-site BGP summary of edge node
[**get_inter_site_edge_node_statistics**](SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi.md#get_inter_site_edge_node_statistics) | **GET** /transport-nodes/{edge-node-id}/inter-site/statistics | Get inter-site statistics of edge node
[**list_inter_site_edge_node_bgp_neighbors**](SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi.md#list_inter_site_edge_node_bgp_neighbors) | **GET** /transport-nodes/{edge-node-id}/inter-site/bgp/neighbors | Paginated list of BGP Neighbors on edge transport node

# **get_edge_cluster_inter_site_status**
> EdgeClusterInterSiteStatus get_edge_cluster_inter_site_status(edge_cluster_id)

Get inter-site status of the edge cluster

Returns the aggregated status for the Edge cluster along with status of all edge nodes in the cluster. It always returns cached response. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi(swagger_client.ApiClient(configuration))
edge_cluster_id = 'edge_cluster_id_example' # str | 

try:
    # Get inter-site status of the edge cluster
    api_response = api_instance.get_edge_cluster_inter_site_status(edge_cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi->get_edge_cluster_inter_site_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_cluster_id** | **str**|  | 

### Return type

[**EdgeClusterInterSiteStatus**](EdgeClusterInterSiteStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inter_site_edge_node_bgp_neighbor_advertised_routes**
> BgpNeighborRouteDetails get_inter_site_edge_node_bgp_neighbor_advertised_routes(edge_node_id, neighbor_id)

Get BGP neighbor advertised routes on edge transport node

Returns routes advertised by BGP neighbor from the given edge transport node. It always returns realtime response. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi(swagger_client.ApiClient(configuration))
edge_node_id = 'edge_node_id_example' # str | 
neighbor_id = 'neighbor_id_example' # str | 

try:
    # Get BGP neighbor advertised routes on edge transport node
    api_response = api_instance.get_inter_site_edge_node_bgp_neighbor_advertised_routes(edge_node_id, neighbor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi->get_inter_site_edge_node_bgp_neighbor_advertised_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_node_id** | **str**|  | 
 **neighbor_id** | **str**|  | 

### Return type

[**BgpNeighborRouteDetails**](BgpNeighborRouteDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inter_site_edge_node_bgp_neighbor_routes**
> BgpNeighborRouteDetails get_inter_site_edge_node_bgp_neighbor_routes(edge_node_id, neighbor_id)

Get BGP neighbor learned routes on edge transport node

Returns routes learned by BGP neighbor from the given edge transport node. It always returns realtime response. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi(swagger_client.ApiClient(configuration))
edge_node_id = 'edge_node_id_example' # str | 
neighbor_id = 'neighbor_id_example' # str | 

try:
    # Get BGP neighbor learned routes on edge transport node
    api_response = api_instance.get_inter_site_edge_node_bgp_neighbor_routes(edge_node_id, neighbor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi->get_inter_site_edge_node_bgp_neighbor_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_node_id** | **str**|  | 
 **neighbor_id** | **str**|  | 

### Return type

[**BgpNeighborRouteDetails**](BgpNeighborRouteDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inter_site_edge_node_bgp_summary**
> InterSiteBgpSummary get_inter_site_edge_node_bgp_summary(edge_node_id)

Get inter-site BGP summary of edge node

Returns BGP summary for all configured neighbors in tunnel VRF on the given egde node. It always returns realtime response. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi(swagger_client.ApiClient(configuration))
edge_node_id = 'edge_node_id_example' # str | 

try:
    # Get inter-site BGP summary of edge node
    api_response = api_instance.get_inter_site_edge_node_bgp_summary(edge_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi->get_inter_site_edge_node_bgp_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_node_id** | **str**|  | 

### Return type

[**InterSiteBgpSummary**](InterSiteBgpSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inter_site_edge_node_statistics**
> NodeInterSiteStatistics get_inter_site_edge_node_statistics(edge_node_id)

Get inter-site statistics of edge node

Returns RTEP to RTEP tunnel port statistics of the given edge node. It always returns realtime response. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi(swagger_client.ApiClient(configuration))
edge_node_id = 'edge_node_id_example' # str | 

try:
    # Get inter-site statistics of edge node
    api_response = api_instance.get_inter_site_edge_node_statistics(edge_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi->get_inter_site_edge_node_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_node_id** | **str**|  | 

### Return type

[**NodeInterSiteStatistics**](NodeInterSiteStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inter_site_edge_node_bgp_neighbors**
> BgpNeighborListResult list_inter_site_edge_node_bgp_neighbors(edge_node_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Paginated list of BGP Neighbors on edge transport node

Paginated list of BGP Neighbors on edge transport node. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi(swagger_client.ApiClient(configuration))
edge_node_id = 'edge_node_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Paginated list of BGP Neighbors on edge transport node
    api_response = api_instance.list_inter_site_edge_node_bgp_neighbors(edge_node_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricEdgeClustersInterSitesApi->list_inter_site_edge_node_bgp_neighbors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_node_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**BgpNeighborListResult**](BgpNeighborListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

