# swagger_client.SystemAdministrationConfigurationFabricNodesLLDPApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_fabric_node_neighbor_properties**](SystemAdministrationConfigurationFabricNodesLLDPApi.md#list_fabric_node_neighbor_properties) | **GET** /lldp/fabric-nodes/{fabric-node-id}/interfaces | List LLDP Neighbor Properties of Fabric Node
[**list_neighbor_properties**](SystemAdministrationConfigurationFabricNodesLLDPApi.md#list_neighbor_properties) | **GET** /lldp/transport-nodes/{node-id}/interfaces | List LLDP Neighbor Properties of Transport Node
[**read_fabric_node_neighbor_properties**](SystemAdministrationConfigurationFabricNodesLLDPApi.md#read_fabric_node_neighbor_properties) | **GET** /lldp/fabric-nodes/{fabric-node-id}/interfaces/{interface-name} | Read LLDP Neighbor Properties of Fabric Node by Interface Name
[**read_neighbor_properties**](SystemAdministrationConfigurationFabricNodesLLDPApi.md#read_neighbor_properties) | **GET** /lldp/transport-nodes/{node-id}/interfaces/{interface-name} | Read LLDP Neighbor Properties of Transport Node by Interface Name 

# **list_fabric_node_neighbor_properties**
> InterfaceNeighborPropertyListResult list_fabric_node_neighbor_properties(fabric_node_id)

List LLDP Neighbor Properties of Fabric Node

List LLDP Neighbor Properties for all interfaces of Fabric Node 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesLLDPApi(swagger_client.ApiClient(configuration))
fabric_node_id = 'fabric_node_id_example' # str | ID of fabric node

try:
    # List LLDP Neighbor Properties of Fabric Node
    api_response = api_instance.list_fabric_node_neighbor_properties(fabric_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesLLDPApi->list_fabric_node_neighbor_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric_node_id** | **str**| ID of fabric node | 

### Return type

[**InterfaceNeighborPropertyListResult**](InterfaceNeighborPropertyListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_neighbor_properties**
> InterfaceNeighborPropertyListResult list_neighbor_properties(node_id)

List LLDP Neighbor Properties of Transport Node

List LLDP Neighbor Properties for all interfaces of Transport Node 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesLLDPApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node

try:
    # List LLDP Neighbor Properties of Transport Node
    api_response = api_instance.list_neighbor_properties(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesLLDPApi->list_neighbor_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 

### Return type

[**InterfaceNeighborPropertyListResult**](InterfaceNeighborPropertyListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_fabric_node_neighbor_properties**
> InterfaceNeighborProperties read_fabric_node_neighbor_properties(fabric_node_id, interface_name)

Read LLDP Neighbor Properties of Fabric Node by Interface Name

Read LLDP Neighbor Properties for a specific interface of Fabric Node 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesLLDPApi(swagger_client.ApiClient(configuration))
fabric_node_id = 'fabric_node_id_example' # str | ID of fabric node
interface_name = 'interface_name_example' # str | Interface name to read

try:
    # Read LLDP Neighbor Properties of Fabric Node by Interface Name
    api_response = api_instance.read_fabric_node_neighbor_properties(fabric_node_id, interface_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesLLDPApi->read_fabric_node_neighbor_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fabric_node_id** | **str**| ID of fabric node | 
 **interface_name** | **str**| Interface name to read | 

### Return type

[**InterfaceNeighborProperties**](InterfaceNeighborProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_neighbor_properties**
> InterfaceNeighborProperties read_neighbor_properties(node_id, interface_name)

Read LLDP Neighbor Properties of Transport Node by Interface Name 

Read LLDP Neighbor Properties for a specific interface of Transport Node 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesLLDPApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | ID of transport node
interface_name = 'interface_name_example' # str | Interface name to read

try:
    # Read LLDP Neighbor Properties of Transport Node by Interface Name 
    api_response = api_instance.read_neighbor_properties(node_id, interface_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesLLDPApi->read_neighbor_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| ID of transport node | 
 **interface_name** | **str**| Interface name to read | 

### Return type

[**InterfaceNeighborProperties**](InterfaceNeighborProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

