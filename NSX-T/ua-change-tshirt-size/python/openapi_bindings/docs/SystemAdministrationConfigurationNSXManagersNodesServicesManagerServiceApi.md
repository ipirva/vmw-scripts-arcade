# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_proton_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi.md#create_proton_service_action_restart) | **POST** /node/services/manager?action&#x3D;restart | Restart, start or stop the service
[**create_proton_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi.md#create_proton_service_action_start) | **POST** /node/services/manager?action&#x3D;start | Restart, start or stop the service
[**create_proton_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi.md#create_proton_service_action_stop) | **POST** /node/services/manager?action&#x3D;stop | Restart, start or stop the service
[**read_proton_service**](SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi.md#read_proton_service) | **GET** /node/services/manager | Read service properties
[**read_proton_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi.md#read_proton_service_status) | **GET** /node/services/manager/status | Read service status
[**reset_proton_service_logging_level_action_reset_manager_logging_levels**](SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi.md#reset_proton_service_logging_level_action_reset_manager_logging_levels) | **POST** /node/services/manager?action&#x3D;reset-manager-logging-levels | Reset the logging levels to default values
[**update_proton_service**](SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi.md#update_proton_service) | **PUT** /node/services/manager | Update service properties

# **create_proton_service_action_restart**
> NodeServiceStatusProperties create_proton_service_action_restart()

Restart, start or stop the service

Restart, start or stop the service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the service
    api_response = api_instance.create_proton_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi->create_proton_service_action_restart: %s\n" % e)
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

# **create_proton_service_action_start**
> NodeServiceStatusProperties create_proton_service_action_start()

Restart, start or stop the service

Restart, start or stop the service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the service
    api_response = api_instance.create_proton_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi->create_proton_service_action_start: %s\n" % e)
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

# **create_proton_service_action_stop**
> NodeServiceStatusProperties create_proton_service_action_stop()

Restart, start or stop the service

Restart, start or stop the service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the service
    api_response = api_instance.create_proton_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi->create_proton_service_action_stop: %s\n" % e)
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

# **read_proton_service**
> NodeProtonServiceProperties read_proton_service()

Read service properties

Read service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read service properties
    api_response = api_instance.read_proton_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi->read_proton_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeProtonServiceProperties**](NodeProtonServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_proton_service_status**
> NodeServiceStatusProperties read_proton_service_status()

Read service status

Read service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read service status
    api_response = api_instance.read_proton_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi->read_proton_service_status: %s\n" % e)
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

# **reset_proton_service_logging_level_action_reset_manager_logging_levels**
> reset_proton_service_logging_level_action_reset_manager_logging_levels()

Reset the logging levels to default values

Reset the logging levels to default values

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Reset the logging levels to default values
    api_instance.reset_proton_service_logging_level_action_reset_manager_logging_levels()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi->reset_proton_service_logging_level_action_reset_manager_logging_levels: %s\n" % e)
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

# **update_proton_service**
> NodeProtonServiceProperties update_proton_service(body)

Update service properties

Update service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeProtonServiceProperties() # NodeProtonServiceProperties | 

try:
    # Update service properties
    api_response = api_instance.update_proton_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesManagerServiceApi->update_proton_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeProtonServiceProperties**](NodeProtonServiceProperties.md)|  | 

### Return type

[**NodeProtonServiceProperties**](NodeProtonServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

