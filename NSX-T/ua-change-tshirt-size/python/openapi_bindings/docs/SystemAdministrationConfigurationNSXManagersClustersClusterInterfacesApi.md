# swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterInterfacesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_cluster_node_interfaces**](SystemAdministrationConfigurationNSXManagersClustersClusterInterfacesApi.md#list_cluster_node_interfaces) | **GET** /cluster/nodes/{node-id}/network/interfaces | List the specified node&#x27;s Network Interfaces
[**read_cluster_node_interface**](SystemAdministrationConfigurationNSXManagersClustersClusterInterfacesApi.md#read_cluster_node_interface) | **GET** /cluster/nodes/{node-id}/network/interfaces/{interface-id} | Read the node&#x27;s Network Interface

# **list_cluster_node_interfaces**
> NodeInterfacePropertiesListResult list_cluster_node_interfaces(node_id, source=source)

List the specified node's Network Interfaces

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterInterfacesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # List the specified node's Network Interfaces
    api_response = api_instance.list_cluster_node_interfaces(node_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterInterfacesApi->list_cluster_node_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**NodeInterfacePropertiesListResult**](NodeInterfacePropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_node_interface**
> NodeInterfaceProperties read_cluster_node_interface(node_id, interface_id, source=source)

Read the node's Network Interface

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterInterfacesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
interface_id = 'interface_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read the node's Network Interface
    api_response = api_instance.read_cluster_node_interface(node_id, interface_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterInterfacesApi->read_cluster_node_interface: %s\n" % e)
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

