# swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_logical_router_port**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi.md#create_logical_router_port) | **POST** /logical-router-ports | Create a Logical Router Port
[**delete_logical_router_port**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi.md#delete_logical_router_port) | **DELETE** /logical-router-ports/{logical-router-port-id} | Delete a Logical Router Port
[**get_logical_router_port_arp_table**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi.md#get_logical_router_port_arp_table) | **GET** /logical-router-ports/{logical-router-port-id}/arp-table | Get the ARP table (IPv4) or Neighbor Discovery table (IPv6) for the Logical Router Port of the given id 
[**get_logical_router_port_arp_table_in_csv_format_csv**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi.md#get_logical_router_port_arp_table_in_csv_format_csv) | **GET** /logical-router-ports/{logical-router-port-id}/arp-table?format&#x3D;csv | Get the ARP table (IPv4) or Neighbor Discovery table (IPv6) for the Logical Router Port of the given id 
[**get_logical_router_port_state**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi.md#get_logical_router_port_state) | **GET** /logical-router-ports/{logical-router-port-id}/state | Get the Realized State of a Logical Router Port
[**get_logical_router_port_statistics**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi.md#get_logical_router_port_statistics) | **GET** /logical-router-ports/{logical-router-port-id}/statistics | Get the statistics of a specified logical router port on all or a specified node
[**get_logical_router_port_statistics_summary**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi.md#get_logical_router_port_statistics_summary) | **GET** /logical-router-ports/{logical-router-port-id}/statistics/summary | Get the statistics summary of a specified logical router port
[**list_logical_router_ports**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi.md#list_logical_router_ports) | **GET** /logical-router-ports | List Logical Router Ports
[**read_logical_router_port**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi.md#read_logical_router_port) | **GET** /logical-router-ports/{logical-router-port-id} | Read Logical Router Port
[**update_logical_router_port**](ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi.md#update_logical_router_port) | **PUT** /logical-router-ports/{logical-router-port-id} | Update a Logical Router Port

# **create_logical_router_port**
> LogicalRouterPort create_logical_router_port(body)

Create a Logical Router Port

Creates a logical router port. The required parameters include resource_type (LogicalRouterUpLinkPort, LogicalRouterDownLinkPort, LogicalRouterLinkPort, LogicalRouterLoopbackPort, LogicalRouterCentralizedServicePort); and logical_router_id (the router to which each logical router port is assigned). The service_bindings parameter is optional. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LogicalRouterPort() # LogicalRouterPort | 

try:
    # Create a Logical Router Port
    api_response = api_instance.create_logical_router_port(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi->create_logical_router_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogicalRouterPort**](LogicalRouterPort.md)|  | 

### Return type

[**LogicalRouterPort**](LogicalRouterPort.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_logical_router_port**
> delete_logical_router_port(logical_router_port_id, cascade_delete_linked_ports=cascade_delete_linked_ports, force=force)

Delete a Logical Router Port

Deletes the specified logical router port. You must delete logical router ports before you can delete the associated logical router. To Delete Tier0 router link port you must have to delete attached tier1 router link port, otherwise pass \"force=true\" as query param to force delete the Tier0 router link port. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi(swagger_client.ApiClient(configuration))
logical_router_port_id = 'logical_router_port_id_example' # str | 
cascade_delete_linked_ports = false # bool | Flag to specify whether to delete related logical switch ports (optional) (default to false)
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete a Logical Router Port
    api_instance.delete_logical_router_port(logical_router_port_id, cascade_delete_linked_ports=cascade_delete_linked_ports, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi->delete_logical_router_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_port_id** | **str**|  | 
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

# **get_logical_router_port_arp_table**
> LogicalRouterPortArpTable get_logical_router_port_arp_table(logical_router_port_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, transport_node_id=transport_node_id)

Get the ARP table (IPv4) or Neighbor Discovery table (IPv6) for the Logical Router Port of the given id 

Returns ARP table (IPv4) or Neighbor Discovery table (IPv6) for the Logical Router Port of the given id, on a node if a query parameter \"transport_node_id=<transport-node-id>\" is given. The transport_node_id parameter is mandatory if the router port is not uplink type. Query parameter \"source=realtime\" is the only supported source. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi(swagger_client.ApiClient(configuration))
logical_router_port_id = 'logical_router_port_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
transport_node_id = 'transport_node_id_example' # str | TransportNode Id (optional)

try:
    # Get the ARP table (IPv4) or Neighbor Discovery table (IPv6) for the Logical Router Port of the given id 
    api_response = api_instance.get_logical_router_port_arp_table(logical_router_port_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, transport_node_id=transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi->get_logical_router_port_arp_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_port_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **transport_node_id** | **str**| TransportNode Id | [optional] 

### Return type

[**LogicalRouterPortArpTable**](LogicalRouterPortArpTable.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_router_port_arp_table_in_csv_format_csv**
> LogicalRouterPortArpTableInCsvFormat get_logical_router_port_arp_table_in_csv_format_csv(logical_router_port_id, source=source, transport_node_id=transport_node_id)

Get the ARP table (IPv4) or Neighbor Discovery table (IPv6) for the Logical Router Port of the given id 

Returns ARP table (IPv4) or Neighbor Discovery table (IPv6) in CSV format for the Logical Router Port of the given id, on a node if a query parameter \"transport_node_id=<transport-node-id>\" is given. The transport_node_id parameter is mandatory if the router port is not uplink type. Query parameter \"source=realtime\" is the only supported source. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi(swagger_client.ApiClient(configuration))
logical_router_port_id = 'logical_router_port_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)
transport_node_id = 'transport_node_id_example' # str | TransportNode Id (optional)

try:
    # Get the ARP table (IPv4) or Neighbor Discovery table (IPv6) for the Logical Router Port of the given id 
    api_response = api_instance.get_logical_router_port_arp_table_in_csv_format_csv(logical_router_port_id, source=source, transport_node_id=transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi->get_logical_router_port_arp_table_in_csv_format_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_port_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 
 **transport_node_id** | **str**| TransportNode Id | [optional] 

### Return type

[**LogicalRouterPortArpTableInCsvFormat**](LogicalRouterPortArpTableInCsvFormat.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_router_port_state**
> LogicalRouterPortState get_logical_router_port_state(logical_router_port_id, barrier_id=barrier_id, request_id=request_id)

Get the Realized State of a Logical Router Port

Return realized state information of a logical router port. Any configuration update that affects the logical router port can use this API to get its realized state by passing a request_id returned by the configuration change operation. e.g. Update configuration of logical router ports, dhcp relays, etc. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi(swagger_client.ApiClient(configuration))
logical_router_port_id = 'logical_router_port_id_example' # str | 
barrier_id = 789 # int |  (optional)
request_id = 'request_id_example' # str | Realization request ID (optional)

try:
    # Get the Realized State of a Logical Router Port
    api_response = api_instance.get_logical_router_port_state(logical_router_port_id, barrier_id=barrier_id, request_id=request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi->get_logical_router_port_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_port_id** | **str**|  | 
 **barrier_id** | **int**|  | [optional] 
 **request_id** | **str**| Realization request ID | [optional] 

### Return type

[**LogicalRouterPortState**](LogicalRouterPortState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_router_port_statistics**
> LogicalRouterPortStatistics get_logical_router_port_statistics(logical_router_port_id, source=source, transport_node_id=transport_node_id)

Get the statistics of a specified logical router port on all or a specified node

Returns the statistics for the Logical Router Port. If query parameter \"transport_node_id=<transport-node-id>\" is given,  only the statistics from the given node for the logical router port will be returned. Otherwise the statistics from each node for the same logical router port will be returned. The transport_node_id is mandatory if the router port is not uplink type. The query parameter \"source=cached\" will be ignored and it will always return realtime statistics of the logical router port. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi(swagger_client.ApiClient(configuration))
logical_router_port_id = 'logical_router_port_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)
transport_node_id = 'transport_node_id_example' # str | TransportNode Id (optional)

try:
    # Get the statistics of a specified logical router port on all or a specified node
    api_response = api_instance.get_logical_router_port_statistics(logical_router_port_id, source=source, transport_node_id=transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi->get_logical_router_port_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_port_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 
 **transport_node_id** | **str**| TransportNode Id | [optional] 

### Return type

[**LogicalRouterPortStatistics**](LogicalRouterPortStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_router_port_statistics_summary**
> LogicalRouterPortStatisticsSummary get_logical_router_port_statistics_summary(logical_router_port_id, source=source)

Get the statistics summary of a specified logical router port

Returns the summation of statistics from all nodes for the Specified Logical Router Port. The query parameter \"source=realtime\" is not supported. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi(swagger_client.ApiClient(configuration))
logical_router_port_id = 'logical_router_port_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get the statistics summary of a specified logical router port
    api_response = api_instance.get_logical_router_port_statistics_summary(logical_router_port_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi->get_logical_router_port_statistics_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_port_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**LogicalRouterPortStatisticsSummary**](LogicalRouterPortStatisticsSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_logical_router_ports**
> LogicalRouterPortListResult list_logical_router_ports(cursor=cursor, included_fields=included_fields, logical_router_id=logical_router_id, logical_switch_id=logical_switch_id, page_size=page_size, resource_type=resource_type, sort_ascending=sort_ascending, sort_by=sort_by)

List Logical Router Ports

Returns information about all logical router ports. Information includes the resource_type (LogicalRouterUpLinkPort, LogicalRouterDownLinkPort, LogicalRouterLinkPort, LogicalRouterLoopbackPort, LogicalRouterCentralizedServicePort); logical_router_id (the router to which each logical router port is assigned); and any service_bindings (such as DHCP relay service). The GET request can include a query parameter (logical_router_id or logical_switch_id). 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
logical_router_id = 'logical_router_id_example' # str | Logical Router identifier (optional)
logical_switch_id = 'logical_switch_id_example' # str | Logical Switch identifier (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
resource_type = 'resource_type_example' # str | Resource types of logical router port (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List Logical Router Ports
    api_response = api_instance.list_logical_router_ports(cursor=cursor, included_fields=included_fields, logical_router_id=logical_router_id, logical_switch_id=logical_switch_id, page_size=page_size, resource_type=resource_type, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi->list_logical_router_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **logical_router_id** | **str**| Logical Router identifier | [optional] 
 **logical_switch_id** | **str**| Logical Switch identifier | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **resource_type** | **str**| Resource types of logical router port | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**LogicalRouterPortListResult**](LogicalRouterPortListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_logical_router_port**
> LogicalRouterPort read_logical_router_port(logical_router_port_id)

Read Logical Router Port

Returns information about the specified logical router port.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi(swagger_client.ApiClient(configuration))
logical_router_port_id = 'logical_router_port_id_example' # str | 

try:
    # Read Logical Router Port
    api_response = api_instance.read_logical_router_port(logical_router_port_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi->read_logical_router_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_router_port_id** | **str**|  | 

### Return type

[**LogicalRouterPort**](LogicalRouterPort.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_logical_router_port**
> LogicalRouterPort update_logical_router_port(body, logical_router_port_id)

Update a Logical Router Port

Modifies the specified logical router port. Required parameters include the resource_type and logical_router_id. Modifiable parameters include the resource_type (LogicalRouterUpLinkPort, LogicalRouterDownLinkPort, LogicalRouterLinkPort, LogicalRouterLoopbackPort, LogicalRouterCentralizedServicePort), logical_router_id (to reassign the port to a different router), and service_bindings. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LogicalRouterPort() # LogicalRouterPort | 
logical_router_port_id = 'logical_router_port_id_example' # str | 

try:
    # Update a Logical Router Port
    api_response = api_instance.update_logical_router_port(body, logical_router_port_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalRoutingAndServicesLogicalRouterPortsApi->update_logical_router_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogicalRouterPort**](LogicalRouterPort.md)|  | 
 **logical_router_port_id** | **str**|  | 

### Return type

[**LogicalRouterPort**](LogicalRouterPort.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

