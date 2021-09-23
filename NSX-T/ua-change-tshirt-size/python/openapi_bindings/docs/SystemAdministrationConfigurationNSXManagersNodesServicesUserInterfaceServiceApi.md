# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nsx_ui_service_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi.md#create_nsx_ui_service_service_action_restart) | **POST** /node/services/ui-service?action&#x3D;restart | Restart, Start and Stop the ui service
[**create_nsx_ui_service_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi.md#create_nsx_ui_service_service_action_start) | **POST** /node/services/ui-service?action&#x3D;start | Restart, Start and Stop the ui service
[**create_nsx_ui_service_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi.md#create_nsx_ui_service_service_action_stop) | **POST** /node/services/ui-service?action&#x3D;stop | Restart, Start and Stop the ui service
[**read_nsx_ui_service_service**](SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi.md#read_nsx_ui_service_service) | **GET** /node/services/ui-service | Read ui service properties
[**read_nsx_ui_service_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi.md#read_nsx_ui_service_service_status) | **GET** /node/services/ui-service/status | Read ui service status

# **create_nsx_ui_service_service_action_restart**
> NodeServiceStatusProperties create_nsx_ui_service_service_action_restart()

Restart, Start and Stop the ui service

Restart, Start and Stop the ui service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, Start and Stop the ui service
    api_response = api_instance.create_nsx_ui_service_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi->create_nsx_ui_service_service_action_restart: %s\n" % e)
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

# **create_nsx_ui_service_service_action_start**
> NodeServiceStatusProperties create_nsx_ui_service_service_action_start()

Restart, Start and Stop the ui service

Restart, Start and Stop the ui service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, Start and Stop the ui service
    api_response = api_instance.create_nsx_ui_service_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi->create_nsx_ui_service_service_action_start: %s\n" % e)
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

# **create_nsx_ui_service_service_action_stop**
> NodeServiceStatusProperties create_nsx_ui_service_service_action_stop()

Restart, Start and Stop the ui service

Restart, Start and Stop the ui service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, Start and Stop the ui service
    api_response = api_instance.create_nsx_ui_service_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi->create_nsx_ui_service_service_action_stop: %s\n" % e)
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

# **read_nsx_ui_service_service**
> NodeServiceProperties read_nsx_ui_service_service()

Read ui service properties

Read ui service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read ui service properties
    api_response = api_instance.read_nsx_ui_service_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi->read_nsx_ui_service_service: %s\n" % e)
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

# **read_nsx_ui_service_service_status**
> NodeServiceStatusProperties read_nsx_ui_service_service_status()

Read ui service status

Read ui service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read ui service status
    api_response = api_instance.read_nsx_ui_service_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesUserInterfaceServiceApi->read_nsx_ui_service_service_status: %s\n" % e)
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

