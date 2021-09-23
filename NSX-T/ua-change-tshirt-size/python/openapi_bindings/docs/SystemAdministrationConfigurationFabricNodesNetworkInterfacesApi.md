# swagger_client.SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_node_interfaces**](SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi.md#list_node_interfaces) | **GET** /node/network/interfaces | List the Node&#x27;s Network Interfaces
[**read_network_interface_statistics**](SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi.md#read_network_interface_statistics) | **GET** /node/network/interfaces/{interface-id}/stats | Read the Node&#x27;s Network Interface Statistics
[**read_network_properties**](SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi.md#read_network_properties) | **GET** /node/network | Read network configuration properties
[**read_node_interface**](SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi.md#read_node_interface) | **GET** /node/network/interfaces/{interface-id} | Read the Node&#x27;s Network Interface
[**update_node_interface**](SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi.md#update_node_interface) | **PUT** /node/network/interfaces/{interface-id} | Update the Node&#x27;s Network Interface

# **list_node_interfaces**
> NodeNetworkInterfacePropertiesListResult list_node_interfaces()

List the Node's Network Interfaces

Returns the number of interfaces on the node appliance and detailed information about each interface. Interface information includes MTU, broadcast and host IP addresses, link and admin status, MAC address, network mask, and the IP configuration method (static or DHCP). 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi(swagger_client.ApiClient(configuration))

try:
    # List the Node's Network Interfaces
    api_response = api_instance.list_node_interfaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi->list_node_interfaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeNetworkInterfacePropertiesListResult**](NodeNetworkInterfacePropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_network_interface_statistics**
> NodeInterfaceStatisticsProperties read_network_interface_statistics(interface_id)

Read the Node's Network Interface Statistics

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi(swagger_client.ApiClient(configuration))
interface_id = 'interface_id_example' # str | ID of interface to read

try:
    # Read the Node's Network Interface Statistics
    api_response = api_instance.read_network_interface_statistics(interface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi->read_network_interface_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_id** | **str**| ID of interface to read | 

### Return type

[**NodeInterfaceStatisticsProperties**](NodeInterfaceStatisticsProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_network_properties**
> NodeNetworkProperties read_network_properties()

Read network configuration properties

Read network configuration properties

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi(swagger_client.ApiClient(configuration))

try:
    # Read network configuration properties
    api_response = api_instance.read_network_properties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi->read_network_properties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeNetworkProperties**](NodeNetworkProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_interface**
> NodeNetworkInterfaceProperties read_node_interface(interface_id)

Read the Node's Network Interface

Returns detailed information about the specified interface. Interface information includes MTU, broadcast and host IP addresses, link and admin status, MAC address, network  mask, and the IP configuration method. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi(swagger_client.ApiClient(configuration))
interface_id = 'interface_id_example' # str | ID of interface to read

try:
    # Read the Node's Network Interface
    api_response = api_instance.read_node_interface(interface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi->read_node_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_id** | **str**| ID of interface to read | 

### Return type

[**NodeNetworkInterfaceProperties**](NodeNetworkInterfaceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_interface**
> NodeNetworkInterfaceProperties update_node_interface(body, interface_id)

Update the Node's Network Interface

Updates the specified interface properties. You cannot change the properties <code>ip_configuration</code>, <code>ip_addresses</code>, or <code>plane</code>. NSX Manager must have a static IP address. You must use NSX CLI to configure a controller or an edge node. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeNetworkInterfaceProperties() # NodeNetworkInterfaceProperties | 
interface_id = 'interface_id_example' # str | ID of interface to update

try:
    # Update the Node's Network Interface
    api_response = api_instance.update_node_interface(body, interface_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesNetworkInterfacesApi->update_node_interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeNetworkInterfaceProperties**](NodeNetworkInterfaceProperties.md)|  | 
 **interface_id** | **str**| ID of interface to update | 

### Return type

[**NodeNetworkInterfaceProperties**](NodeNetworkInterfaceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

