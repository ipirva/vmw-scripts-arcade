# swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_logical_router**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#create_logical_router) | **POST** /logical-routers | Create a Logical Router
[**delete_logical_router**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#delete_logical_router) | **DELETE** /logical-routers/{logical-router-id} | Delete a Logical Router
[**get_bgp_neighbor_advertised_routes**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_bgp_neighbor_advertised_routes) | **GET** /logical-routers/{logical-router-id}/routing/bgp/neighbors/{neighbor-id}/advertised-routes | Get BGP neighbor advertised routes
[**get_bgp_neighbor_advertised_routes_in_csv_format_csv**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_bgp_neighbor_advertised_routes_in_csv_format_csv) | **GET** /logical-routers/{logical-router-id}/routing/bgp/neighbors/{neighbor-id}/advertised-routes?format&#x3D;csv | Get BGP neighbor advertised routes in CSV format 
[**get_bgp_neighbor_routes**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_bgp_neighbor_routes) | **GET** /logical-routers/{logical-router-id}/routing/bgp/neighbors/{neighbor-id}/routes | Get BGP neighbor learned routes
[**get_bgp_neighbor_routes_in_csv_format_csv**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_bgp_neighbor_routes_in_csv_format_csv) | **GET** /logical-routers/{logical-router-id}/routing/bgp/neighbors/{neighbor-id}/routes?format&#x3D;csv | Get BGP neighbor learned routes in CSV format 
[**get_bgp_neighbors_status**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_bgp_neighbors_status) | **GET** /logical-routers/{logical-router-id}/routing/bgp/neighbors/status | Get the status of all the BGP neighbors for the Logical Router of the given id
[**get_logical_router_forwarding_table**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_logical_router_forwarding_table) | **GET** /logical-routers/{logical-router-id}/routing/forwarding-table | Get FIB table on a specified node for a logical router
[**get_logical_router_forwarding_table_in_csv_format_csv**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_logical_router_forwarding_table_in_csv_format_csv) | **GET** /logical-routers/{logical-router-id}/routing/forwarding-table?format&#x3D;csv | Get FIB table on a specified node for a logical router
[**get_logical_router_route_table**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_logical_router_route_table) | **GET** /logical-routers/{logical-router-id}/routing/route-table | Get route table on a given node for a logical router
[**get_logical_router_route_table_in_csv_format_csv**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_logical_router_route_table_in_csv_format_csv) | **GET** /logical-routers/{logical-router-id}/routing/route-table?format&#x3D;csv | Get route table on a node for a logical router
[**get_logical_router_routing_table**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_logical_router_routing_table) | **GET** /logical-routers/{logical-router-id}/routing/routing-table | Get RIB table on a specified node for a logical router
[**get_logical_router_routing_table_in_csv_format_csv**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_logical_router_routing_table_in_csv_format_csv) | **GET** /logical-routers/{logical-router-id}/routing/routing-table?format&#x3D;csv | Get RIB table on a specified node for a logical router
[**get_logical_router_state**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_logical_router_state) | **GET** /logical-routers/{logical-router-id}/state | Get the Realized State of a Logical Router
[**get_logical_router_status**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_logical_router_status) | **GET** /logical-routers/{logical-router-id}/status | Get the status for the Logical Router of the given id
[**get_logical_service_router_cluster_state**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#get_logical_service_router_cluster_state) | **GET** /logical-routers/{logical-router-id}/service-cluster/state | Get the Realized State of a Logical Service Router Cluster
[**list_logical_routers**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#list_logical_routers) | **GET** /logical-routers | List Logical Routers
[**re_allocate_service_routers_reallocate**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#re_allocate_service_routers_reallocate) | **POST** /logical-routers/{logical-router-id}?action&#x3D;reallocate | Re allocate edge node placement of TIER1 service routers
[**re_process_logical_router_reprocess**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#re_process_logical_router_reprocess) | **POST** /logical-routers/{logical-router-id}?action&#x3D;reprocess | Reprocesses a logical router configuration and publish updates to controller
[**read_logical_router**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#read_logical_router) | **GET** /logical-routers/{logical-router-id} | Read Logical Router
[**update_logical_router**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi.md#update_logical_router) | **PUT** /logical-routers/{logical-router-id} | Update a Logical Router

# **create_logical_router**
> LogicalRouter create_logical_router(body)

Create a Logical Router

Creates a logical router. The required parameters are router_type (TIER0 or TIER1) and edge_cluster_id (TIER0 only). Optional parameters include internal and external transit network addresses. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
body = swagger_client.LogicalRouter() # LogicalRouter | 

try:
    # Create a Logical Router
    api_response = api_instance.create_logical_router(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->create_logical_router: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogicalRouter**](LogicalRouter.md)|  | 

### Return type

[**LogicalRouter**](LogicalRouter.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_logical_router**
> delete_logical_router(logical_router_id, cascade_delete_linked_ports=cascade_delete_linked_ports, force=force)

Delete a Logical Router

Deletes the specified logical router. You must delete associated logical router ports before you can delete a logical router. Otherwise use force delete which will delete all related ports and other entities associated with that LR. To force delete logical router pass force=true in query param. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
cascade_delete_linked_ports = false # bool | Flag to specify whether to delete related logical switch ports (optional) (default to false)
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete a Logical Router
    api_instance.delete_logical_router(logical_router_id, cascade_delete_linked_ports=cascade_delete_linked_ports, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->delete_logical_router: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **cascade_delete_linked_ports** | **bool**| Flag to specify whether to delete related logical switch ports | [optional] [default to false]
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bgp_neighbor_advertised_routes**
> BgpNeighborRouteDetails get_bgp_neighbor_advertised_routes(logical_router_id, neighbor_id)

Get BGP neighbor advertised routes

Returns routes advertised by BGP neighbor from all edge transport nodes on which this neighbor is currently enabled. It always returns realtime response. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
neighbor_id = 'neighbor_id_example' # str | 

try:
    # Get BGP neighbor advertised routes
    api_response = api_instance.get_bgp_neighbor_advertised_routes(logical_router_id, neighbor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_bgp_neighbor_advertised_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **neighbor_id** | **str**|  | 

### Return type

[**BgpNeighborRouteDetails**](BgpNeighborRouteDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bgp_neighbor_advertised_routes_in_csv_format_csv**
> BgpNeighborRouteDetailsInCsvFormat get_bgp_neighbor_advertised_routes_in_csv_format_csv(logical_router_id, neighbor_id)

Get BGP neighbor advertised routes in CSV format 

Returns routes advertised by BGP neighbor from all edge transport nodes on which this neighbor is currently enabled in CSV format. It always returns realtime response. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
neighbor_id = 'neighbor_id_example' # str | 

try:
    # Get BGP neighbor advertised routes in CSV format 
    api_response = api_instance.get_bgp_neighbor_advertised_routes_in_csv_format_csv(logical_router_id, neighbor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_bgp_neighbor_advertised_routes_in_csv_format_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **neighbor_id** | **str**|  | 

### Return type

[**BgpNeighborRouteDetailsInCsvFormat**](BgpNeighborRouteDetailsInCsvFormat.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bgp_neighbor_routes**
> BgpNeighborRouteDetails get_bgp_neighbor_routes(logical_router_id, neighbor_id)

Get BGP neighbor learned routes

Returns routes learned by BGP neighbor from all edge transport nodes on which this neighbor is currently enabled. It always returns realtime response. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
neighbor_id = 'neighbor_id_example' # str | 

try:
    # Get BGP neighbor learned routes
    api_response = api_instance.get_bgp_neighbor_routes(logical_router_id, neighbor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_bgp_neighbor_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **neighbor_id** | **str**|  | 

### Return type

[**BgpNeighborRouteDetails**](BgpNeighborRouteDetails.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bgp_neighbor_routes_in_csv_format_csv**
> BgpNeighborRouteDetailsInCsvFormat get_bgp_neighbor_routes_in_csv_format_csv(logical_router_id, neighbor_id)

Get BGP neighbor learned routes in CSV format 

Returns routes learned by BGP neighbor from all edge transport nodes on which this neighbor is currently enabled in CSV format. It always returns realtime response. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
neighbor_id = 'neighbor_id_example' # str | 

try:
    # Get BGP neighbor learned routes in CSV format 
    api_response = api_instance.get_bgp_neighbor_routes_in_csv_format_csv(logical_router_id, neighbor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_bgp_neighbor_routes_in_csv_format_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **neighbor_id** | **str**|  | 

### Return type

[**BgpNeighborRouteDetailsInCsvFormat**](BgpNeighborRouteDetailsInCsvFormat.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bgp_neighbors_status**
> BgpNeighborsStatusListResult get_bgp_neighbors_status(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, transport_node_id=transport_node_id)

Get the status of all the BGP neighbors for the Logical Router of the given id

Returns the status of all the BGP neighbors for the Logical Router of the given id. To get BGP neighbors status for the logical router from particular node, parameter \"transport_node_id=<transportnode_id>\" needs to be specified. Query parameter \"source=realtime\" is the only supported source.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
transport_node_id = 'transport_node_id_example' # str | Transport node id (optional)

try:
    # Get the status of all the BGP neighbors for the Logical Router of the given id
    api_response = api_instance.get_bgp_neighbors_status(logical_router_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, transport_node_id=transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_bgp_neighbors_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **transport_node_id** | **str**| Transport node id | [optional] 

### Return type

[**BgpNeighborsStatusListResult**](BgpNeighborsStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_router_forwarding_table**
> LogicalRouterRouteTable get_logical_router_forwarding_table(logical_router_id, transport_node_id, cursor=cursor, included_fields=included_fields, network_prefix=network_prefix, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source)

Get FIB table on a specified node for a logical router

Returns the FIB for the logical router on a node of the given transport-node-id. Query parameter \"transport_node_id=<transport-node-id>\" is required. To filter the result by network address, paramter \"network_prefix=<a.b.c.d/mask>\" needs to be specified. Query parameter \"source=realtime\" is the only supported source. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
transport_node_id = 'transport_node_id_example' # str | TransportNode Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
network_prefix = 'network_prefix_example' # str | IPv4 or IPv6 CIDR Block (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)

try:
    # Get FIB table on a specified node for a logical router
    api_response = api_instance.get_logical_router_forwarding_table(logical_router_id, transport_node_id, cursor=cursor, included_fields=included_fields, network_prefix=network_prefix, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_logical_router_forwarding_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **transport_node_id** | **str**| TransportNode Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **network_prefix** | **str**| IPv4 or IPv6 CIDR Block | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LogicalRouterRouteTable**](LogicalRouterRouteTable.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_router_forwarding_table_in_csv_format_csv**
> LogicalRouterRouteTableInCsvFormat get_logical_router_forwarding_table_in_csv_format_csv(logical_router_id, transport_node_id, network_prefix=network_prefix, source=source)

Get FIB table on a specified node for a logical router

Returns the FIB table in CSV format for the logical router on a node of the given transport-node-id. Query parameter \"transport_node_id=<transport-node-id>\" is required. To filter the result by network address, paramter \"network_prefix=<a.b.c.d/mask>\" needs to be specified. Query parameter \"source=realtime\" is the only supported source. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
transport_node_id = 'transport_node_id_example' # str | TransportNode Id
network_prefix = 'network_prefix_example' # str | IPv4 or IPv6 CIDR Block (optional)
source = 'source_example' # str | Data source type. (optional)

try:
    # Get FIB table on a specified node for a logical router
    api_response = api_instance.get_logical_router_forwarding_table_in_csv_format_csv(logical_router_id, transport_node_id, network_prefix=network_prefix, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_logical_router_forwarding_table_in_csv_format_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **transport_node_id** | **str**| TransportNode Id | 
 **network_prefix** | **str**| IPv4 or IPv6 CIDR Block | [optional] 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LogicalRouterRouteTableInCsvFormat**](LogicalRouterRouteTableInCsvFormat.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_router_route_table**
> LogicalRouterRouteTable get_logical_router_route_table(logical_router_id, transport_node_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source)

Get route table on a given node for a logical router

Deprecated - Please use /logical-routers/<logical-router-id>/routing/routing-table for RIB and /logical-routers/<logical-router-id>/routing/forwarding-table for FIB. Returns the route table for the logical router on a node of the given transport-node-id. Query parameter \"transport_node_id=<transport-node-id>\" is required. Query parameter \"source=realtime\" is the only supported source. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
transport_node_id = 'transport_node_id_example' # str | TransportNode Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)

try:
    # Get route table on a given node for a logical router
    api_response = api_instance.get_logical_router_route_table(logical_router_id, transport_node_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_logical_router_route_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **transport_node_id** | **str**| TransportNode Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LogicalRouterRouteTable**](LogicalRouterRouteTable.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_router_route_table_in_csv_format_csv**
> LogicalRouterRouteTableInCsvFormat get_logical_router_route_table_in_csv_format_csv(logical_router_id, transport_node_id, source=source)

Get route table on a node for a logical router

Deprecated - Please use /logical-routers/<logical-router-id>/routing/routing-table for RIB and /logical-routers/<logical-router-id>/routing/forwarding-table for FIB. Returns the route table in CSV format for the logical router on a node of the given transport-node-id. Query parameter \"transport_node_id=<transport-node-id>\" is required. Query parameter \"source=realtime\" is the only supported source. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
transport_node_id = 'transport_node_id_example' # str | TransportNode Id
source = 'source_example' # str | Data source type. (optional)

try:
    # Get route table on a node for a logical router
    api_response = api_instance.get_logical_router_route_table_in_csv_format_csv(logical_router_id, transport_node_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_logical_router_route_table_in_csv_format_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **transport_node_id** | **str**| TransportNode Id | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LogicalRouterRouteTableInCsvFormat**](LogicalRouterRouteTableInCsvFormat.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_router_routing_table**
> LogicalRouterRouteTable get_logical_router_routing_table(logical_router_id, transport_node_id, cursor=cursor, included_fields=included_fields, network_prefix=network_prefix, page_size=page_size, route_source=route_source, sort_ascending=sort_ascending, sort_by=sort_by, source=source, vrf_table=vrf_table)

Get RIB table on a specified node for a logical router

Returns the route table(RIB) for the logical router on a node of the given transport-node-id. Query parameter \"transport_node_id=<transport-node-id>\" is required. To filter the result by network address, parameter \"network_prefix=<a.b.c.d/mask>\" needs to be specified. To filter the result by route source, parameter \"route_source=<source_type>\" needs to be specified where source_type can be BGP, STATIC, CONNECTED, NSX_STATIC, TIER1_NAT or TIER0_NAT. It is also possible to filter the RIB table using both network address and route source filter together. Query parameter \"source=realtime\" is the only supported source. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
transport_node_id = 'transport_node_id_example' # str | TransportNode Id
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
network_prefix = 'network_prefix_example' # str | IPv4 or IPv6 CIDR Block (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
route_source = 'route_source_example' # str | Route source filter parameter (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
vrf_table = 'vrf_table_example' # str | VRF filter parameter (optional)

try:
    # Get RIB table on a specified node for a logical router
    api_response = api_instance.get_logical_router_routing_table(logical_router_id, transport_node_id, cursor=cursor, included_fields=included_fields, network_prefix=network_prefix, page_size=page_size, route_source=route_source, sort_ascending=sort_ascending, sort_by=sort_by, source=source, vrf_table=vrf_table)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_logical_router_routing_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **transport_node_id** | **str**| TransportNode Id | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **network_prefix** | **str**| IPv4 or IPv6 CIDR Block | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **route_source** | **str**| Route source filter parameter | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **vrf_table** | **str**| VRF filter parameter | [optional] 

### Return type

[**LogicalRouterRouteTable**](LogicalRouterRouteTable.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_router_routing_table_in_csv_format_csv**
> LogicalRouterRouteTableInCsvFormat get_logical_router_routing_table_in_csv_format_csv(logical_router_id, transport_node_id, network_prefix=network_prefix, route_source=route_source, source=source, vrf_table=vrf_table)

Get RIB table on a specified node for a logical router

Returns the route table in CSV format for the logical router on a node of the given transport-node-id. Query parameter \"transport_node_id=<transport-node-id>\" is required. To filter the result by network address, paramter \"network_prefix=<a.b.c.d/mask>\" needs to be specified. To filter the result by route source, parameter \"route_source=<source_type>\" needs to be specified where source_type can be BGP, STATIC, CONNECTED, NSX_STATIC, TIER1_NAT or TIER0_NAT. It is also possible to filter the RIB table using both network address and route source filter together. Query parameter \"source=realtime\" is the only supported source. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
transport_node_id = 'transport_node_id_example' # str | TransportNode Id
network_prefix = 'network_prefix_example' # str | IPv4 or IPv6 CIDR Block (optional)
route_source = 'route_source_example' # str | Route source filter parameter (optional)
source = 'source_example' # str | Data source type. (optional)
vrf_table = 'vrf_table_example' # str | VRF filter parameter (optional)

try:
    # Get RIB table on a specified node for a logical router
    api_response = api_instance.get_logical_router_routing_table_in_csv_format_csv(logical_router_id, transport_node_id, network_prefix=network_prefix, route_source=route_source, source=source, vrf_table=vrf_table)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_logical_router_routing_table_in_csv_format_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **transport_node_id** | **str**| TransportNode Id | 
 **network_prefix** | **str**| IPv4 or IPv6 CIDR Block | [optional] 
 **route_source** | **str**| Route source filter parameter | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **vrf_table** | **str**| VRF filter parameter | [optional] 

### Return type

[**LogicalRouterRouteTableInCsvFormat**](LogicalRouterRouteTableInCsvFormat.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_router_state**
> LogicalRouterState get_logical_router_state(logical_router_id, barrier_id=barrier_id, request_id=request_id)

Get the Realized State of a Logical Router

Return realized state information of a logical router. Any configuration update that affects the logical router can use this API to get its realized state by passing a request_id returned by the configuration change operation. e.g. Update configuration of logical router, static routes, etc. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
barrier_id = 789 # int |  (optional)
request_id = 'request_id_example' # str | Realization request ID (optional)

try:
    # Get the Realized State of a Logical Router
    api_response = api_instance.get_logical_router_state(logical_router_id, barrier_id=barrier_id, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_logical_router_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **barrier_id** | **int**|  | [optional] 
 **request_id** | **str**| Realization request ID | [optional] 

### Return type

[**LogicalRouterState**](LogicalRouterState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_router_status**
> LogicalRouterStatus get_logical_router_status(logical_router_id, source=source)

Get the status for the Logical Router of the given id

Returns status for the Logical Router of the given id.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the status for the Logical Router of the given id
    api_response = api_instance.get_logical_router_status(logical_router_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_logical_router_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LogicalRouterStatus**](LogicalRouterStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_service_router_cluster_state**
> LogicalServiceRouterClusterState get_logical_service_router_cluster_state(logical_router_id, barrier_id=barrier_id, request_id=request_id)

Get the Realized State of a Logical Service Router Cluster

Return realized state information of a logical service router cluster. Any configuration update that affects the logical service router cluster can use this API to get its realized state by passing a request_id returned by the configuration change operation. e.g. Update configuration of nat, bgp, bfd, etc.  What is a Service Router? When a service cannot be distributed is enabled on a Logical Router, a Service Router (SR) is instantiated. Some examples of services that are not distributed are NAT, DHCP server, Metadata Proxy, Edge Firewall, Load Balancer and so on. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 
barrier_id = 789 # int |  (optional)
request_id = 'request_id_example' # str | Realization request ID (optional)

try:
    # Get the Realized State of a Logical Service Router Cluster
    api_response = api_instance.get_logical_service_router_cluster_state(logical_router_id, barrier_id=barrier_id, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->get_logical_service_router_cluster_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 
 **barrier_id** | **int**|  | [optional] 
 **request_id** | **str**| Realization request ID | [optional] 

### Return type

[**LogicalServiceRouterClusterState**](LogicalServiceRouterClusterState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_logical_routers**
> LogicalRouterListResult list_logical_routers(cursor=cursor, included_fields=included_fields, page_size=page_size, router_type=router_type, sort_ascending=sort_ascending, sort_by=sort_by, vrfs_on_logical_router_id=vrfs_on_logical_router_id)

List Logical Routers

Returns information about all logical routers, including the UUID, internal and external transit network addresses, and the router type (TIER0 or TIER1). You can get information for only TIER0 routers or only the TIER1 routers by including the router_type query parameter. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
router_type = 'router_type_example' # str | Type of Logical Router (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
vrfs_on_logical_router_id = 'vrfs_on_logical_router_id_example' # str | List all VRFs on the specified logical router. (optional)

try:
    # List Logical Routers
    api_response = api_instance.list_logical_routers(cursor=cursor, included_fields=included_fields, page_size=page_size, router_type=router_type, sort_ascending=sort_ascending, sort_by=sort_by, vrfs_on_logical_router_id=vrfs_on_logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->list_logical_routers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **router_type** | **str**| Type of Logical Router | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **vrfs_on_logical_router_id** | **str**| List all VRFs on the specified logical router. | [optional] 

### Return type

[**LogicalRouterListResult**](LogicalRouterListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **re_allocate_service_routers_reallocate**
> LogicalRouter re_allocate_service_routers_reallocate(body, logical_router_id)

Re allocate edge node placement of TIER1 service routers

API to re allocate edge node placement for TIER1 logical router. You can re-allocate service routers of TIER1 in same edge cluster or different edge cluster. You can also place edge nodes manually and provide maximum two indices for HA mode ACTIVE_STANDBY. To re-allocate on new edge cluster you must have existing edge cluster for TIER1 logical router. This will be disruptive operation and all existing statistics of logical router will be remove. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceRouterAllocationConfig() # ServiceRouterAllocationConfig | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Re allocate edge node placement of TIER1 service routers
    api_response = api_instance.re_allocate_service_routers_reallocate(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->re_allocate_service_routers_reallocate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceRouterAllocationConfig**](ServiceRouterAllocationConfig.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**LogicalRouter**](LogicalRouter.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **re_process_logical_router_reprocess**
> re_process_logical_router_reprocess(logical_router_id)

Reprocesses a logical router configuration and publish updates to controller

Reprocess logical router configuration and configuration of related entities like logical router ports, static routing, etc. Any missing Updates are published to controller. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Reprocesses a logical router configuration and publish updates to controller
    api_instance.re_process_logical_router_reprocess(logical_router_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->re_process_logical_router_reprocess: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_logical_router**
> LogicalRouter read_logical_router(logical_router_id)

Read Logical Router

Returns information about the specified logical router.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Read Logical Router
    api_response = api_instance.read_logical_router(logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->read_logical_router: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_id** | **str**|  | 

### Return type

[**LogicalRouter**](LogicalRouter.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_logical_router**
> LogicalRouter update_logical_router(body, logical_router_id)

Update a Logical Router

Modifies the specified logical router. Modifiable attributes include the internal_transit_network, external_transit_networks, and edge_cluster_id (for TIER0 routers). 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi(swagger_client.ApiClient(configuration))
body = swagger_client.LogicalRouter() # LogicalRouter | 
logical_router_id = 'logical_router_id_example' # str | 

try:
    # Update a Logical Router
    api_response = api_instance.update_logical_router(body, logical_router_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRoutersApi->update_logical_router: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogicalRouter**](LogicalRouter.md)|  | 
 **logical_router_id** | **str**|  | 

### Return type

[**LogicalRouter**](LogicalRouter.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

