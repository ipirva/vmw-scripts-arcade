# swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transport_node_with_deployment_info**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#create_transport_node_with_deployment_info) | **POST** /transport-nodes | Create a Transport Node
[**delete_transport_node_with_deployment_info**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#delete_transport_node_with_deployment_info) | **DELETE** /transport-nodes/{transport-node-id} | Delete a Transport Node
[**disable_flow_cache_disable_flow_cache**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#disable_flow_cache_disable_flow_cache) | **POST** /transport-nodes/{transport-node-id}?action&#x3D;disable_flow_cache | Disable flow cache for an edge transport node
[**enable_flow_cache_enable_flow_cache**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#enable_flow_cache_enable_flow_cache) | **POST** /transport-nodes/{transport-node-id}?action&#x3D;enable_flow_cache | Enable flow cache for an edge transport node
[**get_fabric_node_modules_of_transport_node**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#get_fabric_node_modules_of_transport_node) | **GET** /transport-nodes/{node-id}/modules | Get the module details of a transport node 
[**get_transport_node_state_with_deployment_info**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#get_transport_node_state_with_deployment_info) | **GET** /transport-nodes/{transport-node-id}/state | Get a Transport Node&#x27;s State
[**get_transport_node_with_deployment_info**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#get_transport_node_with_deployment_info) | **GET** /transport-nodes/{transport-node-id} | Get a Transport Node
[**invoke_delete_transport_node_central_api**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#invoke_delete_transport_node_central_api) | **DELETE** /transport-nodes/{target-node-id}/{target-uri} | Invoke DELETE request on target transport node
[**invoke_get_transport_node_central_api**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#invoke_get_transport_node_central_api) | **GET** /transport-nodes/{target-node-id}/{target-uri} | Invoke GET request on target transport node
[**invoke_post_transport_node_central_api**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#invoke_post_transport_node_central_api) | **POST** /transport-nodes/{target-node-id}/{target-uri} | Invoke POST request on target transport node
[**invoke_put_transport_node_central_api**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#invoke_put_transport_node_central_api) | **PUT** /transport-nodes/{target-node-id}/{target-uri} | Invoke PUT request on target transport node
[**list_transport_node_capabilities**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#list_transport_node_capabilities) | **GET** /transport-nodes/{transport-node-id}/capabilities | Return the list of capabilities of transport node
[**list_transport_nodes_by_state_with_deployment_info**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#list_transport_nodes_by_state_with_deployment_info) | **GET** /transport-nodes/state | List transport nodes by realized state
[**list_transport_nodes_with_deployment_info**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#list_transport_nodes_with_deployment_info) | **GET** /transport-nodes | List Transport Nodes
[**redeploy_edge_transport_node_redeploy**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#redeploy_edge_transport_node_redeploy) | **POST** /transport-nodes/{node-id}?action&#x3D;redeploy | Redeploys a new node that replaces the specified edge node.
[**refresh_transport_node**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#refresh_transport_node) | **POST** /transport-nodes/{transport-node-id}?action&#x3D;refresh_node_configuration&amp;resource_type&#x3D;EdgeNode | Refresh the node configuration for the Edge node.
[**restart_transport_node_inventory_sync_restart_inventory_sync**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#restart_transport_node_inventory_sync_restart_inventory_sync) | **POST** /transport-nodes/{transport-node-id}?action&#x3D;restart_inventory_sync | Restart the inventory sync for the node if it is paused currently.
[**restore_parent_cluster_configuration_restore_cluster_config**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#restore_parent_cluster_configuration_restore_cluster_config) | **POST** /transport-nodes/{transport-node-id}?action&#x3D;restore_cluster_config | Apply cluster level Transport Node Profile on overridden host
[**resync_transport_node_resync_host_config**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#resync_transport_node_resync_host_config) | **POST** /transport-nodes/{transportnode-id}?action&#x3D;resync_host_config | Resync a Transport Node
[**update_transport_node_maintenance_mode**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#update_transport_node_maintenance_mode) | **POST** /transport-nodes/{transportnode-id} | Update transport node maintenance mode
[**update_transport_node_with_deployment_info**](SystemAdministrationConfigurationFabricNodesTransportNodesApi.md#update_transport_node_with_deployment_info) | **PUT** /transport-nodes/{transport-node-id} | Update a Transport Node

# **create_transport_node_with_deployment_info**
> TransportNode create_transport_node_with_deployment_info(body)

Create a Transport Node

Transport nodes are hypervisor hosts and NSX Edges that will participate in an NSX-T overlay. For a hypervisor host, this means that it hosts VMs that will communicate over NSX-T logical switches. For NSX Edges, this means that it will have logical router uplinks and downlinks.  This API creates transport node for a host node (hypervisor) or edge node (router) in the transport network.  When you run this command for a host, NSX Manager attempts to install the NSX kernel modules, which are packaged as VIB, RPM, or DEB files. For the installation to succeed, you must provide the host login credentials and the host thumbprint.  To get the ESXi host thumbprint, SSH to the host and run the <b>openssl x509 -in /etc/vmware/ssl/rui.crt -fingerprint -sha256 -noout</b> command.  To generate host key thumbprint using SHA-256 algorithm please follow the steps below.  Log into the host, making sure that the connection is not vulnerable to a man in the middle attack. Check whether a public key already exists. Host public key is generally located at '/etc/ssh/ssh_host_rsa_key.pub'. If the key is not present then generate a new key by running the following command and follow the instructions.  <b>ssh-keygen -t rsa</b>  Now generate a SHA256 hash of the key using the following command. Please make sure to pass the appropriate file name if the public key is stored with a different file name other than the default 'id_rsa.pub'.  <b>awk '{print $2}' id_rsa.pub | base64 -d | sha256sum -b | sed 's/ .*$//' | xxd -r -p | base64</b> This api is deprecated as part of FN+TN unification. Please use Transport Node API to install NSX components on a node.  Additional documentation on creating a transport node can be found in the NSX-T Installation Guide.  In order for the transport node to forward packets, the host_switch_spec property must be specified.  Host switches (called bridges in OVS on KVM hypervisors) are the individual switches within the host virtual switch. Virtual machines are connected to the host switches.  When creating a transport node, you need to specify if the host switches are already manually preconfigured on the node, or if NSX should create and manage the host switches. You specify this choice by the type of host switches you pass in the host_switch_spec property of the TransportNode request payload.  For a KVM host, you can preconfigure the host switch, or you can have NSX Manager perform the configuration. For an ESXi host or NSX Edge node, NSX Manager always configures the host switch.  To preconfigure the host switches on a KVM host, pass an array of PreconfiguredHostSwitchSpec objects that describes those host switches. In the current NSX-T release, only one prefonfigured host switch can be specified.  See the PreconfiguredHostSwitchSpec schema definition for documentation on the properties that must be provided. Preconfigured host switches are only supported on KVM hosts, not on ESXi hosts or NSX Edge nodes.  To allow NSX to manage the host switch configuration on KVM hosts, ESXi hosts, or NSX Edge nodes, pass an array of StandardHostSwitchSpec objects in the host_switch_spec property, and NSX will automatically create host switches with the properties you provide. In the current NSX-T release, up to 16 host switches can be automatically managed. See the StandardHostSwitchSpec schema definition for documentation on the properties that must be provided.  Note: Previous versions of NSX-T also used a property named transport_zone_endpoints at TransportNode level. This property is deprecated which creates some combinations of new client along with old client payloads. Examples [1] & [2] show old/existing client request and response by populating transport_zone_endpoints property at TransportNode level. Example [3] shows TransportNode creation request/response by populating transport_zone_endpoints property at StandardHostSwitch level and other new properties.  The request should either provide node_deployement_info or node_id.  If the host node (hypervisor) or edge node (router) is already added in system then it can be converted to transport node by providing node_id in request.  If host node (hypervisor) or edge node (router) is not already present in system then information should be provided under node_deployment_info. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportNode() # TransportNode | 

try:
    # Create a Transport Node
    api_response = api_instance.create_transport_node_with_deployment_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->create_transport_node_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportNode**](TransportNode.md)|  | 

### Return type

[**TransportNode**](TransportNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transport_node_with_deployment_info**
> delete_transport_node_with_deployment_info(transport_node_id, force=force, unprepare_host=unprepare_host)

Delete a Transport Node

Deletes the specified transport node. Query param force can be used to force delete the host nodes. Force deletion of edge and public cloud gateway nodes is not supported.  It also removes the specified node (host or edge) from system. If unprepare_host option is set to false, then host will be deleted without uninstalling the NSX components from the host. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)
unprepare_host = true # bool | Uninstall NSX components from host while deleting (optional) (default to true)

try:
    # Delete a Transport Node
    api_instance.delete_transport_node_with_deployment_info(transport_node_id, force=force, unprepare_host=unprepare_host)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->delete_transport_node_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]
 **unprepare_host** | **bool**| Uninstall NSX components from host while deleting | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_flow_cache_disable_flow_cache**
> disable_flow_cache_disable_flow_cache(transport_node_id)

Disable flow cache for an edge transport node

Disable flow cache for edge transport node. Caution: This involves restart of the edge dataplane and hence may lead to network disruption. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Disable flow cache for an edge transport node
    api_instance.disable_flow_cache_disable_flow_cache(transport_node_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->disable_flow_cache_disable_flow_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_flow_cache_enable_flow_cache**
> enable_flow_cache_enable_flow_cache(transport_node_id)

Enable flow cache for an edge transport node

Enable flow cache for edge transport node. Caution: This involves restart of the edge dataplane and hence may lead to network disruption. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Enable flow cache for an edge transport node
    api_instance.enable_flow_cache_enable_flow_cache(transport_node_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->enable_flow_cache_enable_flow_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fabric_node_modules_of_transport_node**
> SoftwareModuleResult get_fabric_node_modules_of_transport_node(node_id)

Get the module details of a transport node 

Get the module details of a transport node 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Get the module details of a transport node 
    api_response = api_instance.get_fabric_node_modules_of_transport_node(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->get_fabric_node_modules_of_transport_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**SoftwareModuleResult**](SoftwareModuleResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_node_state_with_deployment_info**
> TransportNodeState get_transport_node_state_with_deployment_info(transport_node_id)

Get a Transport Node's State

Returns information about the current state of the transport node configuration and information about the associated hostswitch. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Get a Transport Node's State
    api_response = api_instance.get_transport_node_state_with_deployment_info(transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->get_transport_node_state_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

[**TransportNodeState**](TransportNodeState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_node_with_deployment_info**
> TransportNode get_transport_node_with_deployment_info(transport_node_id)

Get a Transport Node

Returns information about a specified transport node.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Get a Transport Node
    api_response = api_instance.get_transport_node_with_deployment_info(transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->get_transport_node_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

[**TransportNode**](TransportNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_delete_transport_node_central_api**
> invoke_delete_transport_node_central_api(target_node_id, target_uri)

Invoke DELETE request on target transport node

Invoke DELETE request on target transport node

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke DELETE request on target transport node
    api_instance.invoke_delete_transport_node_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->invoke_delete_transport_node_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_get_transport_node_central_api**
> invoke_get_transport_node_central_api(target_node_id, target_uri)

Invoke GET request on target transport node

Invoke GET request on target transport node

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke GET request on target transport node
    api_instance.invoke_get_transport_node_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->invoke_get_transport_node_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_post_transport_node_central_api**
> invoke_post_transport_node_central_api(target_node_id, target_uri)

Invoke POST request on target transport node

Invoke POST request on target transport node

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke POST request on target transport node
    api_instance.invoke_post_transport_node_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->invoke_post_transport_node_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_put_transport_node_central_api**
> invoke_put_transport_node_central_api(target_node_id, target_uri)

Invoke PUT request on target transport node

Invoke PUT request on target transport node

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
target_node_id = 'target_node_id_example' # str | Target node UUID
target_uri = 'target_uri_example' # str | URI of API to invoke on target node

try:
    # Invoke PUT request on target transport node
    api_instance.invoke_put_transport_node_central_api(target_node_id, target_uri)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->invoke_put_transport_node_central_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_node_id** | **str**| Target node UUID | 
 **target_uri** | **str**| URI of API to invoke on target node | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_node_capabilities**
> NodeCapabilitiesResult list_transport_node_capabilities(transport_node_id)

Return the list of capabilities of transport node

Returns information about capabilities of transport host node. Edge nodes do not have capabilities.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Return the list of capabilities of transport node
    api_response = api_instance.list_transport_node_capabilities(transport_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->list_transport_node_capabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

[**NodeCapabilitiesResult**](NodeCapabilitiesResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_nodes_by_state_with_deployment_info**
> TransportNodeStateListResult list_transport_nodes_by_state_with_deployment_info(mm_state=mm_state, status=status, vtep_ip=vtep_ip)

List transport nodes by realized state

Returns a list of transport node states that have realized state as provided as query parameter 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
mm_state = 'mm_state_example' # str | maintenance mode state (optional)
status = 'status_example' # str | Realized state of transport nodes (optional)
vtep_ip = 'vtep_ip_example' # str | Virtual tunnel endpoint ip address of transport node (optional)

try:
    # List transport nodes by realized state
    api_response = api_instance.list_transport_nodes_by_state_with_deployment_info(mm_state=mm_state, status=status, vtep_ip=vtep_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->list_transport_nodes_by_state_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mm_state** | **str**| maintenance mode state | [optional] 
 **status** | **str**| Realized state of transport nodes | [optional] 
 **vtep_ip** | **str**| Virtual tunnel endpoint ip address of transport node | [optional] 

### Return type

[**TransportNodeStateListResult**](TransportNodeStateListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transport_nodes_with_deployment_info**
> TransportNodeListResult list_transport_nodes_with_deployment_info(cursor=cursor, in_maintenance_mode=in_maintenance_mode, included_fields=included_fields, node_id=node_id, node_ip=node_ip, node_types=node_types, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, transport_zone_id=transport_zone_id)

List Transport Nodes

Returns information about all transport nodes along with underlying host or edge details. A transport node is a host or edge that contains hostswitches. A hostswitch can have virtual machines connected to them.  Because each transport node has hostswitches, transport nodes can also have virtual tunnel endpoints, which means that they can be part of the overlay. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
in_maintenance_mode = true # bool | maintenance mode flag (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
node_id = 'node_id_example' # str | node identifier (optional)
node_ip = 'node_ip_example' # str | Fabric node IP address (optional)
node_types = 'node_types_example' # str | a list of fabric node types separated by comma or a single type (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
transport_zone_id = 'transport_zone_id_example' # str | Transport zone identifier (optional)

try:
    # List Transport Nodes
    api_response = api_instance.list_transport_nodes_with_deployment_info(cursor=cursor, in_maintenance_mode=in_maintenance_mode, included_fields=included_fields, node_id=node_id, node_ip=node_ip, node_types=node_types, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, transport_zone_id=transport_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->list_transport_nodes_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **in_maintenance_mode** | **bool**| maintenance mode flag | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **node_id** | **str**| node identifier | [optional] 
 **node_ip** | **str**| Fabric node IP address | [optional] 
 **node_types** | **str**| a list of fabric node types separated by comma or a single type | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **transport_zone_id** | **str**| Transport zone identifier | [optional] 

### Return type

[**TransportNodeListResult**](TransportNodeListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeploy_edge_transport_node_redeploy**
> TransportNode redeploy_edge_transport_node_redeploy(body, node_id)

Redeploys a new node that replaces the specified edge node.

Redeploys an edge node at NSX Manager that replaces the edge node with identifier <node-id>. If NSX Manager can access the specified edge node, then the node is put into maintenance mode and then the associated VM is deleted. This is a means to reset all configuration on the edge node. The communication channel between NSX Manager and edge is established after this operation. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportNode() # TransportNode | 
node_id = 'node_id_example' # str | 

try:
    # Redeploys a new node that replaces the specified edge node.
    api_response = api_instance.redeploy_edge_transport_node_redeploy(body, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->redeploy_edge_transport_node_redeploy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportNode**](TransportNode.md)|  | 
 **node_id** | **str**|  | 

### Return type

[**TransportNode**](TransportNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_transport_node**
> refresh_transport_node(transport_node_id)

Refresh the node configuration for the Edge node.

The API is applicable for Edge transport nodes. If you update the VM configuration and find a discrepancy in VM configuration at NSX Manager, then use this API to refresh configuration at NSX Manager. It refreshes the VM configuration from sources external to MP. Sources include vSphere Server and the edge node. After this action, the API GET api/v1/transport-nodes will show refreshed data. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Refresh the node configuration for the Edge node.
    api_instance.refresh_transport_node(transport_node_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->refresh_transport_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_transport_node_inventory_sync_restart_inventory_sync**
> restart_transport_node_inventory_sync_restart_inventory_sync(transport_node_id)

Restart the inventory sync for the node if it is paused currently.

Restart the inventory sync for the node if it is currently internally paused. After this action the next inventory sync coming from the node is processed. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Restart the inventory sync for the node if it is paused currently.
    api_instance.restart_transport_node_inventory_sync_restart_inventory_sync(transport_node_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->restart_transport_node_inventory_sync_restart_inventory_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_parent_cluster_configuration_restore_cluster_config**
> restore_parent_cluster_configuration_restore_cluster_config(transport_node_id)

Apply cluster level Transport Node Profile on overridden host

A host can be overridden to have different configuration than Transport Node Profile(TNP) on cluster. This action will restore such overridden host back to cluster level TNP.  This API can be used in other case. When TNP is applied to a cluster, if any validation fails (e.g. VMs running on host) then existing transport node (TN) is not updated. In that case after the issue is resolved manually (e.g. VMs powered off), you can call this API to update TN as per cluster level TNP. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
transport_node_id = 'transport_node_id_example' # str | 

try:
    # Apply cluster level Transport Node Profile on overridden host
    api_instance.restore_parent_cluster_configuration_restore_cluster_config(transport_node_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->restore_parent_cluster_configuration_restore_cluster_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resync_transport_node_resync_host_config**
> resync_transport_node_resync_host_config(transportnode_id)

Resync a Transport Node

Resync the TransportNode configuration on a host. It is similar to updating the TransportNode with existing configuration, but force synce these configurations to the host (no backend optimizations). 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
transportnode_id = 'transportnode_id_example' # str | 

try:
    # Resync a Transport Node
    api_instance.resync_transport_node_resync_host_config(transportnode_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->resync_transport_node_resync_host_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transportnode_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transport_node_maintenance_mode**
> update_transport_node_maintenance_mode(transportnode_id, action=action)

Update transport node maintenance mode

Put transport node into maintenance mode or exit from maintenance mode.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
transportnode_id = 'transportnode_id_example' # str | 
action = 'action_example' # str |  (optional)

try:
    # Update transport node maintenance mode
    api_instance.update_transport_node_maintenance_mode(transportnode_id, action=action)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->update_transport_node_maintenance_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transportnode_id** | **str**|  | 
 **action** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transport_node_with_deployment_info**
> TransportNode update_transport_node_with_deployment_info(body, transport_node_id, esx_mgmt_if_migration_dest=esx_mgmt_if_migration_dest, if_id=if_id, ping_ip=ping_ip, skip_validation=skip_validation, vnic=vnic, vnic_migration_dest=vnic_migration_dest)

Update a Transport Node

Modifies the transport node information. The host_switch_name field must match the host_switch_name value specified in the transport zone (API: transport-zones). You must create the associated uplink profile (API: host-switch-profiles) before you can specify an uplink_name here. If the host is an ESX and has only one physical NIC being used by a vSphere standard switch, TransportNodeUpdateParameters should be used to migrate the management interface and the physical NIC into a logical switch that is in a transport zone this transport node will join or has already joined. If the migration is already done, TransportNodeUpdateParameters can also be used to migrate the management interface and the physical NIC back to a vSphere standard switch. In other cases, the TransportNodeUpdateParameters should NOT be used. When updating transport node you should follow pattern where you should fetch the existing transport node and then only modify the required properties keeping other properties as is.  It also modifies attributes of node (host or edge).  Note: Previous versions of NSX-T also used a property named transport_zone_endpoints at TransportNode level. This property is deprecated which creates some combinations of new client along with old client payloads. Examples [1] shows old/existing client request and response by populating transport_zone_endpoints property at TransportNode level. Example [2] shows TransportNode updating TransportNode from exmaple [1] request/response by adding a new StandardHostSwitch by populating transport_zone_endpoints at StandardHostSwitch level. TransportNode level transport_zone_endpoints will ONLY have TransportZoneEndpoints that were originally specified here during create/update operation and does not include TransportZoneEndpoints that were directly specified at StandardHostSwitch level. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesTransportNodesApi(swagger_client.ApiClient(configuration))
body = swagger_client.TransportNode() # TransportNode | 
transport_node_id = 'transport_node_id_example' # str | 
esx_mgmt_if_migration_dest = 'esx_mgmt_if_migration_dest_example' # str | The network ids to which the ESX vmk interfaces will be migrated (optional)
if_id = 'if_id_example' # str | The ESX vmk interfaces to migrate (optional)
ping_ip = 'ping_ip_example' # str | IP Addresses to ping right after ESX vmk interfaces were migrated. (optional)
skip_validation = false # bool | Whether to skip front-end validation for vmk/vnic/pnic migration (optional) (default to false)
vnic = 'vnic_example' # str | The ESX vmk interfaces and/or VM NIC to migrate (optional)
vnic_migration_dest = 'vnic_migration_dest_example' # str | The migration destinations of ESX vmk interfaces and/or VM NIC (optional)

try:
    # Update a Transport Node
    api_response = api_instance.update_transport_node_with_deployment_info(body, transport_node_id, esx_mgmt_if_migration_dest=esx_mgmt_if_migration_dest, if_id=if_id, ping_ip=ping_ip, skip_validation=skip_validation, vnic=vnic, vnic_migration_dest=vnic_migration_dest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesTransportNodesApi->update_transport_node_with_deployment_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransportNode**](TransportNode.md)|  | 
 **transport_node_id** | **str**|  | 
 **esx_mgmt_if_migration_dest** | **str**| The network ids to which the ESX vmk interfaces will be migrated | [optional] 
 **if_id** | **str**| The ESX vmk interfaces to migrate | [optional] 
 **ping_ip** | **str**| IP Addresses to ping right after ESX vmk interfaces were migrated. | [optional] 
 **skip_validation** | **bool**| Whether to skip front-end validation for vmk/vnic/pnic migration | [optional] [default to false]
 **vnic** | **str**| The ESX vmk interfaces and/or VM NIC to migrate | [optional] 
 **vnic_migration_dest** | **str**| The migration destinations of ESX vmk interfaces and/or VM NIC | [optional] 

### Return type

[**TransportNode**](TransportNode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

