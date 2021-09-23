# swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeTunnelsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tunnel**](SystemAdministrationConfigurationFabricNodesTransportNodeTunnelsApi.md#get_tunnel) | **GET** /transport-nodes/{node-id}/tunnels/{tunnel-name} | Tunnel properties
[**query_tunnels**](SystemAdministrationConfigurationFabricNodesTransportNodeTunnelsApi.md#query_tunnels) | **GET** /transport-nodes/{node-id}/tunnels | List of tunnels

# **get_tunnel**
> TunnelProperties get_tunnel(node_id, tunnel_name, source=source)

Tunnel properties

Tunnel properties

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeTunnelsApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node
tunnel_name = 'tunnel_name_example' # str | Tunnel name
source = 'source_example' # str | Data source type. (optional)

try:
    # Tunnel properties
    api_response = api_instance.get_tunnel(node_id, tunnel_name, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeTunnelsApi->get_tunnel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 
 **tunnel_name** | **str**| Tunnel name | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**TunnelProperties**](TunnelProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_tunnels**
> TunnelList query_tunnels(node_id, bfd_diagnostic_code=bfd_diagnostic_code, cursor=cursor, included_fields=included_fields, page_size=page_size, remote_node_id=remote_node_id, sort_ascending=sort_ascending, sort_by=sort_by, source=source, status=status)

List of tunnels

List of tunnels

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeTunnelsApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node
bfd_diagnostic_code = 'bfd_diagnostic_code_example' # str | BFD diagnostic code of Tunnel as defined in RFC 5880 (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
remote_node_id = 'remote_node_id_example' # str |  (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
source = 'source_example' # str | Data source type. (optional)
status = 'status_example' # str | Tunnel status (optional)

try:
    # List of tunnels
    api_response = api_instance.query_tunnels(node_id, bfd_diagnostic_code=bfd_diagnostic_code, cursor=cursor, included_fields=included_fields, page_size=page_size, remote_node_id=remote_node_id, sort_ascending=sort_ascending, sort_by=sort_by, source=source, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeTunnelsApi->query_tunnels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 
 **bfd_diagnostic_code** | **str**| BFD diagnostic code of Tunnel as defined in RFC 5880 | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **remote_node_id** | **str**|  | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **source** | **str**| Data source type. | [optional] 
 **status** | **str**| Tunnel status | [optional] 

### Return type

[**TunnelList**](TunnelList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

