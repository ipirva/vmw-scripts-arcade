# swagger_client.SystemAdministrationConfigurationFabricNodesServicesNodeManagementApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_appliance_management_service_action_restart**](SystemAdministrationConfigurationFabricNodesServicesNodeManagementApi.md#create_appliance_management_service_action_restart) | **POST** /node/services/node-mgmt?action&#x3D;restart | Restart the node management service
[**read_appliance_management_service**](SystemAdministrationConfigurationFabricNodesServicesNodeManagementApi.md#read_appliance_management_service) | **GET** /node/services/node-mgmt | Read appliance management service properties
[**read_appliance_management_service_status**](SystemAdministrationConfigurationFabricNodesServicesNodeManagementApi.md#read_appliance_management_service_status) | **GET** /node/services/node-mgmt/status | Read appliance management service status

# **create_appliance_management_service_action_restart**
> create_appliance_management_service_action_restart()

Restart the node management service

Restart the node management service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNodeManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart the node management service
    api_instance.create_appliance_management_service_action_restart()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNodeManagementApi->create_appliance_management_service_action_restart: %s\n" % e)
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

# **read_appliance_management_service**
> NodeServiceProperties read_appliance_management_service()

Read appliance management service properties

Read appliance management service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNodeManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read appliance management service properties
    api_response = api_instance.read_appliance_management_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNodeManagementApi->read_appliance_management_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_appliance_management_service_status**
> NodeServiceStatusProperties read_appliance_management_service_status()

Read appliance management service status

Read appliance management service status

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNodeManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read appliance management service status
    api_response = api_instance.read_appliance_management_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNodeManagementApi->read_appliance_management_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

