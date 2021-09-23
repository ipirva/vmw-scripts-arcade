# swagger_client.SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pace_cluster_node_vm**](SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi.md#add_pace_cluster_node_vm) | **POST** /intelligence/nodes/deployments | Deploy and register a Intelligence cluster node VM
[**delete_auto_deployed_pace_cluster_node_vm_delete**](SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi.md#delete_auto_deployed_pace_cluster_node_vm_delete) | **POST** /intelligence/nodes/deployments/{node-id}?action&#x3D;delete | Attempt to delete an auto-deployed cluster node VM
[**list_pace_cluster_node_vm_deployment_requests**](SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi.md#list_pace_cluster_node_vm_deployment_requests) | **GET** /intelligence/nodes/deployments | Returns info for all cluster node VM auto-deployment attempts
[**read_pace_cluster_node_vm_deployment_request**](SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi.md#read_pace_cluster_node_vm_deployment_request) | **GET** /intelligence/nodes/deployments/{node-id} | Returns info for a Intelligence cluster node VM auto-deployment attempt
[**read_pace_cluster_node_vm_deployment_status**](SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi.md#read_pace_cluster_node_vm_deployment_status) | **GET** /intelligence/nodes/deployments/{node-id}/status | Returns the status of the VM creation/deletion

# **add_pace_cluster_node_vm**
> IntelligenceClusterNodeVMDeploymentRequestList add_pace_cluster_node_vm(body)

Deploy and register a Intelligence cluster node VM

Deploys a Intelligence cluster node VM as specified by the deployment config. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddIntelligenceClusterNodeVMInfo() # AddIntelligenceClusterNodeVMInfo | 

try:
    # Deploy and register a Intelligence cluster node VM
    api_response = api_instance.add_pace_cluster_node_vm(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi->add_pace_cluster_node_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddIntelligenceClusterNodeVMInfo**](AddIntelligenceClusterNodeVMInfo.md)|  | 

### Return type

[**IntelligenceClusterNodeVMDeploymentRequestList**](IntelligenceClusterNodeVMDeploymentRequestList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auto_deployed_pace_cluster_node_vm_delete**
> delete_auto_deployed_pace_cluster_node_vm_delete(node_id, force_delete=force_delete)

Attempt to delete an auto-deployed cluster node VM

Attempts to unregister and undeploy a specified auto-deployed cluster node VM. If it is a member of a cluster, then the VM will be automatically detached from the cluster before being unregistered and undeployed. Alternatively, if the original deployment attempt failed or the VM is not found, cleans up the deployment information associated with the deployment attempt. Note: If a VM has been successfully auto-deployed, then the associated deployment information will not be deleted unless and until the VM is successfully deleted. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
force_delete = true # bool | Delete by force (optional)

try:
    # Attempt to delete an auto-deployed cluster node VM
    api_instance.delete_auto_deployed_pace_cluster_node_vm_delete(node_id, force_delete=force_delete)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi->delete_auto_deployed_pace_cluster_node_vm_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **force_delete** | **bool**| Delete by force | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pace_cluster_node_vm_deployment_requests**
> IntelligenceClusterNodeVMDeploymentRequestList list_pace_cluster_node_vm_deployment_requests()

Returns info for all cluster node VM auto-deployment attempts

Returns request information for every attempted deployment of a cluster node VM. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi(swagger_client.ApiClient(configuration))

try:
    # Returns info for all cluster node VM auto-deployment attempts
    api_response = api_instance.list_pace_cluster_node_vm_deployment_requests()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi->list_pace_cluster_node_vm_deployment_requests: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IntelligenceClusterNodeVMDeploymentRequestList**](IntelligenceClusterNodeVMDeploymentRequestList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_pace_cluster_node_vm_deployment_request**
> IntelligenceClusterNodeVMDeploymentRequest read_pace_cluster_node_vm_deployment_request(node_id)

Returns info for a Intelligence cluster node VM auto-deployment attempt

Returns deployment request information for a specific attempted deployment of a cluster node VM. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Returns info for a Intelligence cluster node VM auto-deployment attempt
    api_response = api_instance.read_pace_cluster_node_vm_deployment_request(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi->read_pace_cluster_node_vm_deployment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**IntelligenceClusterNodeVMDeploymentRequest**](IntelligenceClusterNodeVMDeploymentRequest.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_pace_cluster_node_vm_deployment_status**
> IntelligenceClusterNodeVMDeploymentStatusReport read_pace_cluster_node_vm_deployment_status(node_id)

Returns the status of the VM creation/deletion

Returns the current deployment or undeployment status for a VM along with any other relevant current information, such as error messages. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Returns the status of the VM creation/deletion
    api_response = api_instance.read_pace_cluster_node_vm_deployment_status(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceDeploymentsApi->read_pace_cluster_node_vm_deployment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**IntelligenceClusterNodeVMDeploymentStatusReport**](IntelligenceClusterNodeVMDeploymentStatusReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

