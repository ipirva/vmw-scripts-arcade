# swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_transport_nodes_status**](SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi.md#get_all_transport_nodes_status) | **GET** /transport-nodes/status | Get high-level summary of all transport nodes. The service layer does not support source &#x3D; realtime or cached.
[**get_pnic_statuses_for_transport_node**](SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi.md#get_pnic_statuses_for_transport_node) | **GET** /transport-nodes/{node-id}/pnic-bond-status | Get high-level summary of a transport node
[**get_transport_node_report**](SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi.md#get_transport_node_report) | **GET** /transport-zones/transport-node-status-report | Creates a status report of transport nodes of all the transport zones
[**get_transport_node_report_for_a_transport_zone**](SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi.md#get_transport_node_report_for_a_transport_zone) | **GET** /transport-zones/{zone-id}/transport-node-status-report | Creates a status report of transport nodes in a transport zone
[**get_transport_node_status**](SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi.md#get_transport_node_status) | **GET** /transport-nodes/{node-id}/status | Read status of a transport node
[**list_remote_transport_node_status**](SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi.md#list_remote_transport_node_status) | **GET** /transport-nodes/{node-id}/remote-transport-node-status | Read status of all transport nodes with tunnel connections to transport node 
[**list_transport_node_status**](SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi.md#list_transport_node_status) | **GET** /transport-zones/transport-node-status | Read status of all the transport nodes
[**list_transport_node_status_for_transport_zone**](SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi.md#list_transport_node_status_for_transport_zone) | **GET** /transport-zones/{zone-id}/transport-node-status | Read status of transport nodes in a transport zone

# **get_all_transport_nodes_status**
> HeatMapTransportZoneStatus get_all_transport_nodes_status(node_type=node_type)

Get high-level summary of all transport nodes. The service layer does not support source = realtime or cached.

Get high-level summary of all transport nodes. The service layer does not support source = realtime or cached.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi(swagger_client.ApiClient(configuration))
node_type = 'node_type_example' # str | Transport node type (optional)

try:
    # Get high-level summary of all transport nodes. The service layer does not support source = realtime or cached.
    api_response = api_instance.get_all_transport_nodes_status(node_type=node_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi->get_all_transport_nodes_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_type** | **str**| Transport node type | [optional] 

### Return type

[**HeatMapTransportZoneStatus**](HeatMapTransportZoneStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pnic_statuses_for_transport_node**
> PnicBondStatusListResult get_pnic_statuses_for_transport_node(node_id, status=status)

Get high-level summary of a transport node

Get high-level summary of a transport node

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node
status = 'status_example' # str | pNic/bond status (optional)

try:
    # Get high-level summary of a transport node
    api_response = api_instance.get_pnic_statuses_for_transport_node(node_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi->get_pnic_statuses_for_transport_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 
 **status** | **str**| pNic/bond status | [optional] 

### Return type

[**PnicBondStatusListResult**](PnicBondStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_node_report**
> get_transport_node_report(source=source, status=status)

Creates a status report of transport nodes of all the transport zones

You must provide the request header \"Accept:application/octet-stream\" when calling this API.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi(swagger_client.ApiClient(configuration))
source = 'source_example' # str | Data source type. (optional)
status = 'status_example' # str | Transport node (optional)

try:
    # Creates a status report of transport nodes of all the transport zones
    api_instance.get_transport_node_report(source=source, status=status)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi->get_transport_node_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Data source type. | [optional] 
 **status** | **str**| Transport node | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_node_report_for_a_transport_zone**
> get_transport_node_report_for_a_transport_zone(zone_id, source=source, status=status)

Creates a status report of transport nodes in a transport zone

You must provide the request header \"Accept:application/octet-stream\" when calling this API.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi(swagger_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | ID of transport zone
source = 'source_example' # str | Data source type. (optional)
status = 'status_example' # str | Transport node (optional)

try:
    # Creates a status report of transport nodes in a transport zone
    api_instance.get_transport_node_report_for_a_transport_zone(zone_id, source=source, status=status)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi->get_transport_node_report_for_a_transport_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| ID of transport zone | 
 **source** | **str**| Data source type. | [optional] 
 **status** | **str**| Transport node | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_node_status**
> TransportNodeStatus get_transport_node_status(node_id, source=source)

Read status of a transport node

Read status of a transport node

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node
source = 'source_example' # str | Data source type. (optional)

try:
    # Read status of a transport node
    api_response = api_instance.get_transport_node_status(node_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi->get_transport_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**TransportNodeStatus**](TransportNodeStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_remote_transport_node_status**
> TransportNodeStatusListResult list_remote_transport_node_status(node_id, bfd_diagnostic_code=bfd_diagnostic_code, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, tunnel_status=tunnel_status)

Read status of all transport nodes with tunnel connections to transport node 

Read status of all transport nodes with tunnel connections to transport node 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node
bfd_diagnostic_code = 'bfd_diagnostic_code_example' # str | BFD diagnostic code of Tunnel (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
tunnel_status = 'tunnel_status_example' # str | Tunnel Status (optional)

try:
    # Read status of all transport nodes with tunnel connections to transport node 
    api_response = api_instance.list_remote_transport_node_status(node_id, bfd_diagnostic_code=bfd_diagnostic_code, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, tunnel_status=tunnel_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi->list_remote_transport_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 
 **bfd_diagnostic_code** | **str**| BFD diagnostic code of Tunnel | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **tunnel_status** | **str**| Tunnel Status | [optional] 

### Return type

[**TransportNodeStatusListResult**](TransportNodeStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_node_status**
> TransportNodeStatusListResult list_transport_node_status(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, status=status)

Read status of all the transport nodes

Read status of all the transport nodes

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
status = 'status_example' # str | Transport node (optional)

try:
    # Read status of all the transport nodes
    api_response = api_instance.list_transport_node_status(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi->list_transport_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **status** | **str**| Transport node | [optional] 

### Return type

[**TransportNodeStatusListResult**](TransportNodeStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_node_status_for_transport_zone**
> TransportNodeStatusListResult list_transport_node_status_for_transport_zone(zone_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, status=status)

Read status of transport nodes in a transport zone

Read status of transport nodes in a transport zone

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi(swagger_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | ID of transport zone
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
status = 'status_example' # str | Transport node (optional)

try:
    # Read status of transport nodes in a transport zone
    api_response = api_instance.list_transport_node_status_for_transport_zone(zone_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, source=source, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeStatusApi->list_transport_node_status_for_transport_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| ID of transport zone | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **status** | **str**| Transport node | [optional] 

### Return type

[**TransportNodeStatusListResult**](TransportNodeStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

