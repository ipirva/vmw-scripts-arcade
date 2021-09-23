# swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bridge_endpoint**](ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi.md#create_bridge_endpoint) | **POST** /bridge-endpoints | Create a Bridge Endpoint
[**delete_bridge_endpoint**](ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi.md#delete_bridge_endpoint) | **DELETE** /bridge-endpoints/{bridgeendpoint-id} | Delete a Bridge Endpoint
[**get_bridge_endpoint**](ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi.md#get_bridge_endpoint) | **GET** /bridge-endpoints/{bridgeendpoint-id} | Get Information about a bridge endpoint
[**get_bridge_endpoint_statistics**](ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi.md#get_bridge_endpoint_statistics) | **GET** /bridge-endpoints/{endpoint-id}/statistics | Returns statistics of a specified Bridge Endpoint
[**get_bridge_endpoint_status**](ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi.md#get_bridge_endpoint_status) | **GET** /bridge-endpoints/{endpoint-id}/status | Returns status of a specified Bridge Endpoint
[**list_bridge_endpoints**](ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi.md#list_bridge_endpoints) | **GET** /bridge-endpoints | List All Bridge Endpoints
[**update_bridge_endpoint**](ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi.md#update_bridge_endpoint) | **PUT** /bridge-endpoints/{bridgeendpoint-id} | Update a Bridge Endpoint

# **create_bridge_endpoint**
> BridgeEndpoint create_bridge_endpoint(body)

Create a Bridge Endpoint

Creates a Bridge Endpoint. It describes the physical attributes of the bridge like vlan. A logical port can be attached to a vif providing bridging functionality from the logical overlay network to the physical vlan network 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BridgeEndpoint() # BridgeEndpoint | 

try:
    # Create a Bridge Endpoint
    api_response = api_instance.create_bridge_endpoint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi->create_bridge_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BridgeEndpoint**](BridgeEndpoint.md)|  | 

### Return type

[**BridgeEndpoint**](BridgeEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bridge_endpoint**
> delete_bridge_endpoint(bridgeendpoint_id)

Delete a Bridge Endpoint

Deletes the specified Bridge Endpoint.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi(swagger_client.ApiClient(configuration))
bridgeendpoint_id = 'bridgeendpoint_id_example' # str | 

try:
    # Delete a Bridge Endpoint
    api_instance.delete_bridge_endpoint(bridgeendpoint_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi->delete_bridge_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridgeendpoint_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bridge_endpoint**
> BridgeEndpoint get_bridge_endpoint(bridgeendpoint_id)

Get Information about a bridge endpoint

Returns information about a specified bridge endpoint.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi(swagger_client.ApiClient(configuration))
bridgeendpoint_id = 'bridgeendpoint_id_example' # str | 

try:
    # Get Information about a bridge endpoint
    api_response = api_instance.get_bridge_endpoint(bridgeendpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi->get_bridge_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridgeendpoint_id** | **str**|  | 

### Return type

[**BridgeEndpoint**](BridgeEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bridge_endpoint_statistics**
> BridgeEndpointStatistics get_bridge_endpoint_statistics(endpoint_id, source=source)

Returns statistics of a specified Bridge Endpoint

Get the statistics for the Bridge Endpoint of the given Endpoint id (endpoint-id)

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi(swagger_client.ApiClient(configuration))
endpoint_id = 'endpoint_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Returns statistics of a specified Bridge Endpoint
    api_response = api_instance.get_bridge_endpoint_statistics(endpoint_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi->get_bridge_endpoint_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**BridgeEndpointStatistics**](BridgeEndpointStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bridge_endpoint_status**
> BridgeEndpointStatus get_bridge_endpoint_status(endpoint_id, source=source)

Returns status of a specified Bridge Endpoint

Get the status for the Bridge Endpoint of the given Endpoint id

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi(swagger_client.ApiClient(configuration))
endpoint_id = 'endpoint_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Returns status of a specified Bridge Endpoint
    api_response = api_instance.get_bridge_endpoint_status(endpoint_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi->get_bridge_endpoint_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**BridgeEndpointStatus**](BridgeEndpointStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bridge_endpoints**
> BridgeEndpointListResult list_bridge_endpoints(bridge_cluster_id=bridge_cluster_id, bridge_endpoint_profile_id=bridge_endpoint_profile_id, cursor=cursor, included_fields=included_fields, logical_switch_id=logical_switch_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, vlan_transport_zone_id=vlan_transport_zone_id)

List All Bridge Endpoints

Returns information about all configured bridge endoints 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi(swagger_client.ApiClient(configuration))
bridge_cluster_id = 'bridge_cluster_id_example' # str | Bridge Cluster Identifier (optional)
bridge_endpoint_profile_id = 'bridge_endpoint_profile_id_example' # str | Bridge endpoint profile used by the edge cluster (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
logical_switch_id = 'logical_switch_id_example' # str | Logical Switch Identifier (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
vlan_transport_zone_id = 'vlan_transport_zone_id_example' # str | VLAN transport zone id used by the edge cluster (optional)

try:
    # List All Bridge Endpoints
    api_response = api_instance.list_bridge_endpoints(bridge_cluster_id=bridge_cluster_id, bridge_endpoint_profile_id=bridge_endpoint_profile_id, cursor=cursor, included_fields=included_fields, logical_switch_id=logical_switch_id, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, vlan_transport_zone_id=vlan_transport_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi->list_bridge_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_cluster_id** | **str**| Bridge Cluster Identifier | [optional] 
 **bridge_endpoint_profile_id** | **str**| Bridge endpoint profile used by the edge cluster | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **logical_switch_id** | **str**| Logical Switch Identifier | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **vlan_transport_zone_id** | **str**| VLAN transport zone id used by the edge cluster | [optional] 

### Return type

[**BridgeEndpointListResult**](BridgeEndpointListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bridge_endpoint**
> BridgeEndpoint update_bridge_endpoint(body, bridgeendpoint_id)

Update a Bridge Endpoint

Modifies a existing bridge endpoint. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BridgeEndpoint() # BridgeEndpoint | 
bridgeendpoint_id = 'bridgeendpoint_id_example' # str | 

try:
    # Update a Bridge Endpoint
    api_response = api_instance.update_bridge_endpoint(body, bridgeendpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalBridgingBridgeEndpointsApi->update_bridge_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BridgeEndpoint**](BridgeEndpoint.md)|  | 
 **bridgeendpoint_id** | **str**|  | 

### Return type

[**BridgeEndpoint**](BridgeEndpoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

