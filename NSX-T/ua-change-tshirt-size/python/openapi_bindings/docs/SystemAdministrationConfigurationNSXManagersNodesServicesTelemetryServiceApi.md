# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_phonehome_coordinator_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi.md#create_phonehome_coordinator_service_action_restart) | **POST** /node/services/telemetry?action&#x3D;restart | Restart, start or stop Telemetry service
[**create_phonehome_coordinator_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi.md#create_phonehome_coordinator_service_action_start) | **POST** /node/services/telemetry?action&#x3D;start | Restart, start or stop Telemetry service
[**create_phonehome_coordinator_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi.md#create_phonehome_coordinator_service_action_stop) | **POST** /node/services/telemetry?action&#x3D;stop | Restart, start or stop Telemetry service
[**read_phonehome_coordinator_service**](SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi.md#read_phonehome_coordinator_service) | **GET** /node/services/telemetry | Read Telemetry service properties
[**read_phonehome_coordinator_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi.md#read_phonehome_coordinator_service_status) | **GET** /node/services/telemetry/status | Read Telemetry service status

# **create_phonehome_coordinator_service_action_restart**
> NodeServiceStatusProperties create_phonehome_coordinator_service_action_restart()

Restart, start or stop Telemetry service

Restart, start or stop Telemetry service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop Telemetry service
    api_response = api_instance.create_phonehome_coordinator_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi->create_phonehome_coordinator_service_action_restart: %s\n" % e)
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

# **create_phonehome_coordinator_service_action_start**
> NodeServiceStatusProperties create_phonehome_coordinator_service_action_start()

Restart, start or stop Telemetry service

Restart, start or stop Telemetry service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop Telemetry service
    api_response = api_instance.create_phonehome_coordinator_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi->create_phonehome_coordinator_service_action_start: %s\n" % e)
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

# **create_phonehome_coordinator_service_action_stop**
> NodeServiceStatusProperties create_phonehome_coordinator_service_action_stop()

Restart, start or stop Telemetry service

Restart, start or stop Telemetry service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop Telemetry service
    api_response = api_instance.create_phonehome_coordinator_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi->create_phonehome_coordinator_service_action_stop: %s\n" % e)
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

# **read_phonehome_coordinator_service**
> NodeServiceProperties read_phonehome_coordinator_service()

Read Telemetry service properties

Read Telemetry service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read Telemetry service properties
    api_response = api_instance.read_phonehome_coordinator_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi->read_phonehome_coordinator_service: %s\n" % e)
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

# **read_phonehome_coordinator_service_status**
> NodeServiceStatusProperties read_phonehome_coordinator_service_status()

Read Telemetry service status

Read Telemetry service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read Telemetry service status
    api_response = api_instance.read_phonehome_coordinator_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesTelemetryServiceApi->read_phonehome_coordinator_service_status: %s\n" % e)
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

