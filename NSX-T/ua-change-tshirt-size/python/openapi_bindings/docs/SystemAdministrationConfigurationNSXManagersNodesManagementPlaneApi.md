# swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagementPlaneApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_management_plane_configuration**](SystemAdministrationConfigurationNSXManagersNodesManagementPlaneApi.md#delete_management_plane_configuration) | **DELETE** /node/management-plane | Delete management plane configuration for this node
[**read_management_plane_configuration**](SystemAdministrationConfigurationNSXManagersNodesManagementPlaneApi.md#read_management_plane_configuration) | **GET** /node/management-plane | Get management plane configuration for this node
[**update_management_plane_configuration**](SystemAdministrationConfigurationNSXManagersNodesManagementPlaneApi.md#update_management_plane_configuration) | **PUT** /node/management-plane | Update management plane configuration for this node

# **delete_management_plane_configuration**
> delete_management_plane_configuration()

Delete management plane configuration for this node

Delete the management plane configuration for this node.

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagementPlaneApi(swagger_client.ApiClient(configuration))

try:
    # Delete management plane configuration for this node
    api_instance.delete_management_plane_configuration()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesManagementPlaneApi->delete_management_plane_configuration: %s\n" % e)
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

# **read_management_plane_configuration**
> ManagementPlaneProperties read_management_plane_configuration()

Get management plane configuration for this node

Retrieve the management plane configuration for this node to identify the Manager node with which the controller service is communicating.

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagementPlaneApi(swagger_client.ApiClient(configuration))

try:
    # Get management plane configuration for this node
    api_response = api_instance.read_management_plane_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesManagementPlaneApi->read_management_plane_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ManagementPlaneProperties**](ManagementPlaneProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_management_plane_configuration**
> ManagementPlaneProperties update_management_plane_configuration(body)

Update management plane configuration for this node

Update the management plane configuration for this node.

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagementPlaneApi(swagger_client.ApiClient(configuration))
body = swagger_client.ManagementPlaneProperties() # ManagementPlaneProperties | 

try:
    # Update management plane configuration for this node
    api_response = api_instance.update_management_plane_configuration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesManagementPlaneApi->update_management_plane_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManagementPlaneProperties**](ManagementPlaneProperties.md)|  | 

### Return type

[**ManagementPlaneProperties**](ManagementPlaneProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

