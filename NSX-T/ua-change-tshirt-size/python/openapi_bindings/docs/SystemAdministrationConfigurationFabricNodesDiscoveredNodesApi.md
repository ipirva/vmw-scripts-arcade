# swagger_client.SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transport_node_for_discovered_node_create_transport_node**](SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi.md#create_transport_node_for_discovered_node_create_transport_node) | **POST** /fabric/discovered-nodes/{node-ext-id}?action&#x3D;create_transport_node | Created Transport Node for Discovered Node
[**host_prep_discovered_node_hostprep**](SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi.md#host_prep_discovered_node_hostprep) | **POST** /fabric/discovered-nodes/{node-ext-id}?action&#x3D;hostprep | (Deprecated) Prepares discovered Node for NSX
[**list_discovered_nodes**](SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi.md#list_discovered_nodes) | **GET** /fabric/discovered-nodes | Return the List of Discovered Nodes
[**read_discovered_node**](SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi.md#read_discovered_node) | **GET** /fabric/discovered-nodes/{node-ext-id} | Return Discovered Node Information
[**reapply_tn_profile_on_discovered_node_reapply_cluster_config**](SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi.md#reapply_tn_profile_on_discovered_node_reapply_cluster_config) | **POST** /fabric/discovered-nodes/{node-ext-id}?action&#x3D;reapply_cluster_config | Apply cluster level config on Discovered Node

# **create_transport_node_for_discovered_node_create_transport_node**
> TransportNode create_transport_node_for_discovered_node_create_transport_node(body, node_ext_id)

Created Transport Node for Discovered Node

NSX components are installaed on host and transport node is created with given configurations.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportNode() # TransportNode | 
node_ext_id = 'node_ext_id_example' # str | 

try:
    # Created Transport Node for Discovered Node
    api_response = api_instance.create_transport_node_for_discovered_node_create_transport_node(body, node_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi->create_transport_node_for_discovered_node_create_transport_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportNode**](TransportNode.md)|  | 
 **node_ext_id** | **str**|  | 

### Return type

[**TransportNode**](TransportNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_prep_discovered_node_hostprep**
> Node host_prep_discovered_node_hostprep(node_ext_id)

(Deprecated) Prepares discovered Node for NSX

Prepares(hostprep) discovered node for NSX. NSX LCP bundles are installed on this discovered node. This API is deprecated. Use /fabric/discovered-nodes/<node-ext-id>?action=create_transport_node

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi(swagger_client.ApiClient(configuration))
node_ext_id = 'node_ext_id_example' # str | 

try:
    # (Deprecated) Prepares discovered Node for NSX
    api_response = api_instance.host_prep_discovered_node_hostprep(node_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi->host_prep_discovered_node_hostprep: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_ext_id** | **str**|  | 

### Return type

[**Node**](Node.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_discovered_nodes**
> DiscoveredNodeListResult list_discovered_nodes(cm_local_id=cm_local_id, cursor=cursor, display_name=display_name, external_id=external_id, has_parent=has_parent, included_fields=included_fields, ip_address=ip_address, node_id=node_id, node_type=node_type, origin_id=origin_id, page_size=page_size, parent_compute_collection=parent_compute_collection, sort_ascending=sort_ascending, sort_by=sort_by)

Return the List of Discovered Nodes

Returns information about all discovered nodes.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi(swagger_client.ApiClient(configuration))
cm_local_id = 'cm_local_id_example' # str | Local Id of the discovered node in the Compute Manager (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
display_name = 'display_name_example' # str | Display name of discovered node (optional)
external_id = 'external_id_example' # str | External id of the discovered node, ex. a mo-ref from VC (optional)
has_parent = 'has_parent_example' # str | Discovered node has a parent compute collection or is a standalone host (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
ip_address = 'ip_address_example' # str | IP address of the discovered node (optional)
node_id = 'node_id_example' # str | Id of the fabric node created from the discovered node (optional)
node_type = 'node_type_example' # str | Discovered Node type like HostNode (optional)
origin_id = 'origin_id_example' # str | Id of the compute manager from where this node was discovered (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
parent_compute_collection = 'parent_compute_collection_example' # str | External id of the compute collection to which this node belongs (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the List of Discovered Nodes
    api_response = api_instance.list_discovered_nodes(cm_local_id=cm_local_id, cursor=cursor, display_name=display_name, external_id=external_id, has_parent=has_parent, included_fields=included_fields, ip_address=ip_address, node_id=node_id, node_type=node_type, origin_id=origin_id, page_size=page_size, parent_compute_collection=parent_compute_collection, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi->list_discovered_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cm_local_id** | **str**| Local Id of the discovered node in the Compute Manager | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **display_name** | **str**| Display name of discovered node | [optional] 
 **external_id** | **str**| External id of the discovered node, ex. a mo-ref from VC | [optional] 
 **has_parent** | **str**| Discovered node has a parent compute collection or is a standalone host | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **ip_address** | **str**| IP address of the discovered node | [optional] 
 **node_id** | **str**| Id of the fabric node created from the discovered node | [optional] 
 **node_type** | **str**| Discovered Node type like HostNode | [optional] 
 **origin_id** | **str**| Id of the compute manager from where this node was discovered | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **parent_compute_collection** | **str**| External id of the compute collection to which this node belongs | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**DiscoveredNodeListResult**](DiscoveredNodeListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_discovered_node**
> DiscoveredNode read_discovered_node(node_ext_id)

Return Discovered Node Information

Returns information about a specific discovered node.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi(swagger_client.ApiClient(configuration))
node_ext_id = 'node_ext_id_example' # str | 

try:
    # Return Discovered Node Information
    api_response = api_instance.read_discovered_node(node_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi->read_discovered_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_ext_id** | **str**|  | 

### Return type

[**DiscoveredNode**](DiscoveredNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reapply_tn_profile_on_discovered_node_reapply_cluster_config**
> TransportNode reapply_tn_profile_on_discovered_node_reapply_cluster_config(node_ext_id)

Apply cluster level config on Discovered Node

When transport node profile (TNP) is applied to a cluster, if any validation fails (e.g. VMs running on host) then transport node (TN) is not created. In that case after the required action is taken (e.g. VMs powered off), you can call this API to try to create TN for that discovered node. Do not call this API if Transport Node already exists for the discovered node. In that case use API on transport node. /transport-nodes/<transport-node-id>?action=restore_cluster_config

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi(swagger_client.ApiClient(configuration))
node_ext_id = 'node_ext_id_example' # str | 

try:
    # Apply cluster level config on Discovered Node
    api_response = api_instance.reapply_tn_profile_on_discovered_node_reapply_cluster_config(node_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesDiscoveredNodesApi->reapply_tn_profile_on_discovered_node_reapply_cluster_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_ext_id** | **str**|  | 

### Return type

[**TransportNode**](TransportNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

