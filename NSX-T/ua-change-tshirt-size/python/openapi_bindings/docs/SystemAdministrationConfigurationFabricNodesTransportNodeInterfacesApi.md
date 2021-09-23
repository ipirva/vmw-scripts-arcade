# swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_fabric_node_interfaces**](SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi.md#list_fabric_node_interfaces) | **GET** /fabric/nodes/{node-id}/network/interfaces | List the specified node&#x27;s Network Interfaces
[**list_transport_node_interfaces**](SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi.md#list_transport_node_interfaces) | **GET** /transport-nodes/{transport-node-id}/network/interfaces | List the specified transport node&#x27;s network interfaces
[**read_fabric_node_interface**](SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi.md#read_fabric_node_interface) | **GET** /fabric/nodes/{node-id}/network/interfaces/{interface-id} | Read the node&#x27;s Network Interface
[**read_transport_node_interface**](SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi.md#read_transport_node_interface) | **GET** /transport-nodes/{transport-node-id}/network/interfaces/{interface-id} | Read the transport node&#x27;s network interface
[**read_transport_node_interface_statistics**](SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi.md#read_transport_node_interface_statistics) | **GET** /transport-nodes/{transport-node-id}/network/interfaces/{interface-id}/stats | Read the NSX Manager&#x27;s Network Interface Statistics

# **list_fabric_node_interfaces**
> NodeInterfacePropertiesListResult list_fabric_node_interfaces(node_id, admin_status=admin_status, source=source)

List the specified node's Network Interfaces

Returns the number of interfaces on the node and detailed information about each interface. Interface information includes MTU, broadcast and host IP addresses, link and admin status, MAC address, network mask, and the IP configuration method (static or DHCP). This api is deprecated. Please use Transport Node API GET /transport-nodes/<transport-node-id>/network/interfaces to list node network interfaces for the corresponding TN. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
admin_status = 'admin_status_example' # str | Admin status of the interface (optional)
source = 'source_example' # str | Data source type. (optional)

try:
    # List the specified node's Network Interfaces
    api_response = api_instance.list_fabric_node_interfaces(node_id, admin_status=admin_status, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi->list_fabric_node_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **admin_status** | **str**| Admin status of the interface | [optional] 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NodeInterfacePropertiesListResult**](NodeInterfacePropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_node_interfaces**
> NodeInterfacePropertiesListResult list_transport_node_interfaces(transport_node_id, admin_status=admin_status, source=source)

List the specified transport node's network interfaces

Returns the number of interfaces on the node and detailed information about each interface. Interface information includes MTU, broadcast and host IP addresses, link and admin status, MAC address, network mask, and the IP configuration method (static or DHCP). 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 
admin_status = 'admin_status_example' # str | Admin status of the interface (optional)
source = 'source_example' # str | Data source type. (optional)

try:
    # List the specified transport node's network interfaces
    api_response = api_instance.list_transport_node_interfaces(transport_node_id, admin_status=admin_status, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi->list_transport_node_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 
 **admin_status** | **str**| Admin status of the interface | [optional] 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NodeInterfacePropertiesListResult**](NodeInterfacePropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_fabric_node_interface**
> NodeInterfaceProperties read_fabric_node_interface(node_id, interface_id, source=source)

Read the node's Network Interface

Returns detailed information about the specified interface. Interface information includes MTU, broadcast and host IP addresses, link and admin status, MAC address, network  mask, and the IP configuration method (static or DHCP). This api is deprecated as part of FN+TN unification. Please use Transport Node API GET /transport-nodes/<transport-node-id>/network/interfaces/<interface-id> to get interface details of a node. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
interface_id = 'interface_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read the node's Network Interface
    api_response = api_instance.read_fabric_node_interface(node_id, interface_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi->read_fabric_node_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **interface_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NodeInterfaceProperties**](NodeInterfaceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_transport_node_interface**
> NodeInterfaceProperties read_transport_node_interface(transport_node_id, interface_id, source=source)

Read the transport node's network interface

Returns detailed information about the specified interface. Interface information includes MTU, broadcast and host IP addresses, link and admin status, MAC address, network  mask, and the IP configuration method (static or DHCP). 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 
interface_id = 'interface_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read the transport node's network interface
    api_response = api_instance.read_transport_node_interface(transport_node_id, interface_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi->read_transport_node_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 
 **interface_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NodeInterfaceProperties**](NodeInterfaceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_transport_node_interface_statistics**
> NodeInterfaceStatisticsProperties read_transport_node_interface_statistics(transport_node_id, interface_id, source=source)

Read the NSX Manager's Network Interface Statistics

On the specified interface, returns the number of received (rx), transmitted (tx), and dropped packets; the number of bytes and errors received and transmitted on the interface; and the number of detected collisions. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 
interface_id = 'interface_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read the NSX Manager's Network Interface Statistics
    api_response = api_instance.read_transport_node_interface_statistics(transport_node_id, interface_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodeInterfacesApi->read_transport_node_interface_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 
 **interface_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NodeInterfaceStatisticsProperties**](NodeInterfaceStatisticsProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

