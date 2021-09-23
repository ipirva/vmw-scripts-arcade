# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_controller_server_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi.md#create_controller_server_service_action_restart) | **POST** /node/services/controller?action&#x3D;restart | Restart, start or stop the controller service
[**create_controller_server_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi.md#create_controller_server_service_action_start) | **POST** /node/services/controller?action&#x3D;start | Restart, start or stop the controller service
[**create_controller_server_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi.md#create_controller_server_service_action_stop) | **POST** /node/services/controller?action&#x3D;stop | Restart, start or stop the controller service
[**get_controller_profiler_status**](SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi.md#get_controller_profiler_status) | **GET** /node/services/controller/profiler | Get the status (Enabled/Disabled) of controller profiler
[**read_controller_server_certificate**](SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi.md#read_controller_server_certificate) | **GET** /node/services/controller/controller-certificate | Read controller server certificate properties
[**read_controller_server_service**](SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi.md#read_controller_server_service) | **GET** /node/services/controller | Read controller service properties
[**read_controller_server_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi.md#read_controller_server_service_status) | **GET** /node/services/controller/status | Read controller service status
[**set_controller_profiler**](SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi.md#set_controller_profiler) | **PUT** /node/services/controller/profiler | Enable or disable controller profiler

# **create_controller_server_service_action_restart**
> NodeServiceStatusProperties create_controller_server_service_action_restart()

Restart, start or stop the controller service

Restart, start or stop the controller service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the controller service
    api_response = api_instance.create_controller_server_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi->create_controller_server_service_action_restart: %s\n" % e)
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

# **create_controller_server_service_action_start**
> NodeServiceStatusProperties create_controller_server_service_action_start()

Restart, start or stop the controller service

Restart, start or stop the controller service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the controller service
    api_response = api_instance.create_controller_server_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi->create_controller_server_service_action_start: %s\n" % e)
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

# **create_controller_server_service_action_stop**
> NodeServiceStatusProperties create_controller_server_service_action_stop()

Restart, start or stop the controller service

Restart, start or stop the controller service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the controller service
    api_response = api_instance.create_controller_server_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi->create_controller_server_service_action_stop: %s\n" % e)
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

# **get_controller_profiler_status**
> ControllerProfilerProperties get_controller_profiler_status()

Get the status (Enabled/Disabled) of controller profiler

Get the status (Enabled/Disabled) of controller profiler

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Get the status (Enabled/Disabled) of controller profiler
    api_response = api_instance.get_controller_profiler_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi->get_controller_profiler_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ControllerProfilerProperties**](ControllerProfilerProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_controller_server_certificate**
> CertificateKeyPair read_controller_server_certificate()

Read controller server certificate properties

Read controller server certificate properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read controller server certificate properties
    api_response = api_instance.read_controller_server_certificate()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi->read_controller_server_certificate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CertificateKeyPair**](CertificateKeyPair.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_controller_server_service**
> NodeServiceProperties read_controller_server_service()

Read controller service properties

Read controller service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read controller service properties
    api_response = api_instance.read_controller_server_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi->read_controller_server_service: %s\n" % e)
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

# **read_controller_server_service_status**
> NodeServiceStatusProperties read_controller_server_service_status()

Read controller service status

Read controller service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read controller service status
    api_response = api_instance.read_controller_server_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi->read_controller_server_service_status: %s\n" % e)
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

# **set_controller_profiler**
> set_controller_profiler(body)

Enable or disable controller profiler

Enable or disable controller profiler

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ControllerProfilerProperties() # ControllerProfilerProperties | 

try:
    # Enable or disable controller profiler
    api_instance.set_controller_profiler(body)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesControllerServiceApi->set_controller_profiler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ControllerProfilerProperties**](ControllerProfilerProperties.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

