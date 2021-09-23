# swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagerNetworkInterfacesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_cluster_node_interface_statistics**](SystemAdministrationConfigurationNSXManagersNodesManagerNetworkInterfacesApi.md#read_cluster_node_interface_statistics) | **GET** /cluster/nodes/{node-id}/network/interfaces/{interface-id}/stats | Read the NSX Manager/Controller&#x27;s Network Interface Statistics
[**read_fabric_node_interface_statistics**](SystemAdministrationConfigurationNSXManagersNodesManagerNetworkInterfacesApi.md#read_fabric_node_interface_statistics) | **GET** /fabric/nodes/{node-id}/network/interfaces/{interface-id}/stats | Read the NSX Manager&#x27;s Network Interface Statistics

# **read_cluster_node_interface_statistics**
> NodeInterfaceStatisticsProperties read_cluster_node_interface_statistics(node_id, interface_id, source=source)

Read the NSX Manager/Controller's Network Interface Statistics

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagerNetworkInterfacesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
interface_id = 'interface_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read the NSX Manager/Controller's Network Interface Statistics
    api_response = api_instance.read_cluster_node_interface_statistics(node_id, interface_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesManagerNetworkInterfacesApi->read_cluster_node_interface_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
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

# **read_fabric_node_interface_statistics**
> NodeInterfaceStatisticsProperties read_fabric_node_interface_statistics(node_id, interface_id, source=source)

Read the NSX Manager's Network Interface Statistics

On the specified interface, returns the number of received (rx), transmitted (tx), and dropped packets; the number of bytes and errors received and transmitted on the interface; and the number of detected collisions. This api is deprecated as part of FN+TN unification. Please use /transport-nodes/<transportnode-id>/network/interfaces/<interface-id>/stats to read network interface statistics with contraint FN is converted to TN. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagerNetworkInterfacesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
interface_id = 'interface_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Read the NSX Manager's Network Interface Statistics
    api_response = api_instance.read_fabric_node_interface_statistics(node_id, interface_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesManagerNetworkInterfacesApi->read_fabric_node_interface_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
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

