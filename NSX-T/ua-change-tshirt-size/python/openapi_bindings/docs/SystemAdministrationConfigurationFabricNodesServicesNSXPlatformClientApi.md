# swagger_client.SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_platform_client_service_action_restart**](SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi.md#create_platform_client_service_action_restart) | **POST** /node/services/nsx-platform-client?action&#x3D;restart | Restart, start or stop the NSX Platform Client service
[**create_platform_client_service_action_start**](SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi.md#create_platform_client_service_action_start) | **POST** /node/services/nsx-platform-client?action&#x3D;start | Restart, start or stop the NSX Platform Client service
[**create_platform_client_service_action_stop**](SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi.md#create_platform_client_service_action_stop) | **POST** /node/services/nsx-platform-client?action&#x3D;stop | Restart, start or stop the NSX Platform Client service
[**read_platform_client_service**](SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi.md#read_platform_client_service) | **GET** /node/services/nsx-platform-client | Read NSX Platform Client service properties
[**read_platform_client_service_status**](SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi.md#read_platform_client_service_status) | **GET** /node/services/nsx-platform-client/status | Read NSX Platform Client service status

# **create_platform_client_service_action_restart**
> NodeServiceStatusProperties create_platform_client_service_action_restart()

Restart, start or stop the NSX Platform Client service

Restart, start or stop the NSX Platform Client service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Platform Client service
    api_response = api_instance.create_platform_client_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi->create_platform_client_service_action_restart: %s\n" % e)
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

# **create_platform_client_service_action_start**
> NodeServiceStatusProperties create_platform_client_service_action_start()

Restart, start or stop the NSX Platform Client service

Restart, start or stop the NSX Platform Client service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Platform Client service
    api_response = api_instance.create_platform_client_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi->create_platform_client_service_action_start: %s\n" % e)
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

# **create_platform_client_service_action_stop**
> NodeServiceStatusProperties create_platform_client_service_action_stop()

Restart, start or stop the NSX Platform Client service

Restart, start or stop the NSX Platform Client service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Platform Client service
    api_response = api_instance.create_platform_client_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi->create_platform_client_service_action_stop: %s\n" % e)
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

# **read_platform_client_service**
> NodeServiceProperties read_platform_client_service()

Read NSX Platform Client service properties

Read NSX Platform Client service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX Platform Client service properties
    api_response = api_instance.read_platform_client_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi->read_platform_client_service: %s\n" % e)
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

# **read_platform_client_service_status**
> NodeServiceStatusProperties read_platform_client_service_status()

Read NSX Platform Client service status

Read NSX Platform Client service status

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX Platform Client service status
    api_response = api_instance.read_platform_client_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNSXPlatformClientApi->read_platform_client_service_status: %s\n" % e)
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

