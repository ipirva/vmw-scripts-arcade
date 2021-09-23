# swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cluster_node_vm**](SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi.md#add_cluster_node_vm) | **POST** /cluster/nodes/deployments | Deploy and register a cluster node VM
[**delete_auto_deployed_cluster_node_vm_delete**](SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi.md#delete_auto_deployed_cluster_node_vm_delete) | **POST** /cluster/nodes/deployments/{node-id}?action&#x3D;delete | Attempt to delete an auto-deployed cluster node VM
[**get_repo_sync_status**](SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi.md#get_repo_sync_status) | **GET** /cluster/nodes/{node-id}/repo_sync/status | Synchronizes the repository data between nsx managers.
[**list_cluster_node_vm_deployment_requests**](SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi.md#list_cluster_node_vm_deployment_requests) | **GET** /cluster/nodes/deployments | Returns info for all cluster node VM auto-deployment attempts
[**perform_repo_sync_repo_sync**](SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi.md#perform_repo_sync_repo_sync) | **POST** /cluster/node?action&#x3D;repo_sync | Synchronizes the repository data between nsx managers.
[**read_cluster_node_vm_deployment_request**](SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi.md#read_cluster_node_vm_deployment_request) | **GET** /cluster/nodes/deployments/{node-id} | Returns info for a cluster-node VM auto-deployment attempt
[**read_cluster_node_vm_deployment_status**](SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi.md#read_cluster_node_vm_deployment_status) | **GET** /cluster/nodes/deployments/{node-id}/status | Returns the status of the VM creation/deletion

# **add_cluster_node_vm**
> ClusterNodeVMDeploymentRequestList add_cluster_node_vm(body)

Deploy and register a cluster node VM

Deploys a cluster node VM as specified by the deployment config. Once the VM is deployed and powered on, it will automatically join the existing cluster. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddClusterNodeVMInfo() # AddClusterNodeVMInfo | 

try:
    # Deploy and register a cluster node VM
    api_response = api_instance.add_cluster_node_vm(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi->add_cluster_node_vm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddClusterNodeVMInfo**](AddClusterNodeVMInfo.md)|  | 

### Return type

[**ClusterNodeVMDeploymentRequestList**](ClusterNodeVMDeploymentRequestList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auto_deployed_cluster_node_vm_delete**
> delete_auto_deployed_cluster_node_vm_delete(node_id, force_delete=force_delete)

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 
force_delete = true # bool | Delete by force (optional)

try:
    # Attempt to delete an auto-deployed cluster node VM
    api_instance.delete_auto_deployed_cluster_node_vm_delete(node_id, force_delete=force_delete)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi->delete_auto_deployed_cluster_node_vm_delete: %s\n" % e)
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

# **get_repo_sync_status**
> RepoSyncStatusReport get_repo_sync_status(node_id)

Synchronizes the repository data between nsx managers.

Returns the synchronization status for the manager represented by given <node-id>. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Synchronizes the repository data between nsx managers.
    api_response = api_instance.get_repo_sync_status(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi->get_repo_sync_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**RepoSyncStatusReport**](RepoSyncStatusReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_node_vm_deployment_requests**
> ClusterNodeVMDeploymentRequestList list_cluster_node_vm_deployment_requests()

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi(swagger_client.ApiClient(configuration))

try:
    # Returns info for all cluster node VM auto-deployment attempts
    api_response = api_instance.list_cluster_node_vm_deployment_requests()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi->list_cluster_node_vm_deployment_requests: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterNodeVMDeploymentRequestList**](ClusterNodeVMDeploymentRequestList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_repo_sync_repo_sync**
> perform_repo_sync_repo_sync()

Synchronizes the repository data between nsx managers.

Attempts to synchronize the repository partition on nsx manager. Repository partition contains packages required for the install and upgrade of nsx components.Normally there is no need to call this API explicitely by the user. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi(swagger_client.ApiClient(configuration))

try:
    # Synchronizes the repository data between nsx managers.
    api_instance.perform_repo_sync_repo_sync()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi->perform_repo_sync_repo_sync: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_node_vm_deployment_request**
> ClusterNodeVMDeploymentRequest read_cluster_node_vm_deployment_request(node_id)

Returns info for a cluster-node VM auto-deployment attempt

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Returns info for a cluster-node VM auto-deployment attempt
    api_response = api_instance.read_cluster_node_vm_deployment_request(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi->read_cluster_node_vm_deployment_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**ClusterNodeVMDeploymentRequest**](ClusterNodeVMDeploymentRequest.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_node_vm_deployment_status**
> ClusterNodeVMDeploymentStatusReport read_cluster_node_vm_deployment_status(node_id)

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | 

try:
    # Returns the status of the VM creation/deletion
    api_response = api_instance.read_cluster_node_vm_deployment_status(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersClustersClusterNodeDeploymentsApi->read_cluster_node_vm_deployment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**ClusterNodeVMDeploymentStatusReport**](ClusterNodeVMDeploymentStatusReport.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

