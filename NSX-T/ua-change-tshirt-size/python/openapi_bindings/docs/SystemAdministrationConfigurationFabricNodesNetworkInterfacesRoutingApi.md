# swagger_client.SystemAdministrationConfigurationFabricNodesNetworkInterfacesRoutingApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_node_network_route**](SystemAdministrationConfigurationFabricNodesNetworkInterfacesRoutingApi.md#create_node_network_route) | **POST** /node/network/routes | Create node network route
[**delete_node_network_route**](SystemAdministrationConfigurationFabricNodesNetworkInterfacesRoutingApi.md#delete_node_network_route) | **DELETE** /node/network/routes/{route-id} | Delete node network route
[**list_node_network_routes**](SystemAdministrationConfigurationFabricNodesNetworkInterfacesRoutingApi.md#list_node_network_routes) | **GET** /node/network/routes | List node network routes
[**read_node_network_route**](SystemAdministrationConfigurationFabricNodesNetworkInterfacesRoutingApi.md#read_node_network_route) | **GET** /node/network/routes/{route-id} | Read node network route

# **create_node_network_route**
> NodeRouteProperties create_node_network_route(body)

Create node network route

Add a route to the node routing table. For static routes, the route_type, interface_id, netmask, and destination are required parameters. For default routes, the route_type, gateway address, and interface_id are required. For blackhole routes, the route_type and destination are required. All other parameters are optional. When you add a static route, the scope and route_id are created automatically. When you add a default or blackhole route, the route_id is created automatically. The route_id is read-only, meaning that it cannot be modified. All other properties can be modified by deleting and readding the route. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesNetworkInterfacesRoutingApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeRouteProperties() # NodeRouteProperties | 

try:
    # Create node network route
    api_response = api_instance.create_node_network_route(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesNetworkInterfacesRoutingApi->create_node_network_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeRouteProperties**](NodeRouteProperties.md)|  | 

### Return type

[**NodeRouteProperties**](NodeRouteProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_network_route**
> delete_node_network_route(route_id)

Delete node network route

Delete a route from the node routing table. You can modify an existing route by deleting it and then posting the modified version of the route. To verify, remove the route ID from the URI, issue a GET request, and note the absense of the deleted route. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesNetworkInterfacesRoutingApi(swagger_client.ApiClient(configuration))
route_id = 'route_id_example' # str | ID of route to delete

try:
    # Delete node network route
    api_instance.delete_node_network_route(route_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesNetworkInterfacesRoutingApi->delete_node_network_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **str**| ID of route to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_network_routes**
> NodeRoutePropertiesListResult list_node_network_routes()

List node network routes

Returns detailed information about each route in the node routing table. Route information includes the route type (default, static, and so on), a unique route identifier, the route metric, the protocol from which the route was learned, the route source (which is the preferred egress interface), the route destination, and the route scope. The route scope refers to the distance to the destination network: The \"host\" scope leads to a destination address on the node, such as a loopback address; the \"link\" scope leads to a destination on the local network; and the \"global\" scope leads to addresses that are more than one hop away. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesNetworkInterfacesRoutingApi(swagger_client.ApiClient(configuration))

try:
    # List node network routes
    api_response = api_instance.list_node_network_routes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesNetworkInterfacesRoutingApi->list_node_network_routes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeRoutePropertiesListResult**](NodeRoutePropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_network_route**
> NodeRouteProperties read_node_network_route(route_id)

Read node network route

Returns detailed information about a specified route in the node routing table. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesNetworkInterfacesRoutingApi(swagger_client.ApiClient(configuration))
route_id = 'route_id_example' # str | ID of route to read

try:
    # Read node network route
    api_response = api_instance.read_node_network_route(route_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesNetworkInterfacesRoutingApi->read_node_network_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **str**| ID of route to read | 

### Return type

[**NodeRouteProperties**](NodeRouteProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

