# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_async_replicator_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi.md#create_async_replicator_service_action_restart) | **POST** /node/services/async_replicator?action&#x3D;restart | Restart, start or stop the Async Replicator service
[**create_async_replicator_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi.md#create_async_replicator_service_action_start) | **POST** /node/services/async_replicator?action&#x3D;start | Restart, start or stop the Async Replicator service
[**create_async_replicator_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi.md#create_async_replicator_service_action_stop) | **POST** /node/services/async_replicator?action&#x3D;stop | Restart, start or stop the Async Replicator service
[**read_async_replicator_service**](SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi.md#read_async_replicator_service) | **GET** /node/services/async_replicator | Read the Async Replicator service properties
[**read_async_replicator_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi.md#read_async_replicator_service_status) | **GET** /node/services/async_replicator/status | Read the Async Replicator service status

# **create_async_replicator_service_action_restart**
> NodeServiceStatusProperties create_async_replicator_service_action_restart()

Restart, start or stop the Async Replicator service

Restart, start or stop the Async Replicator service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the Async Replicator service
    api_response = api_instance.create_async_replicator_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi->create_async_replicator_service_action_restart: %s\n" % e)
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

# **create_async_replicator_service_action_start**
> NodeServiceStatusProperties create_async_replicator_service_action_start()

Restart, start or stop the Async Replicator service

Restart, start or stop the Async Replicator service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the Async Replicator service
    api_response = api_instance.create_async_replicator_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi->create_async_replicator_service_action_start: %s\n" % e)
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

# **create_async_replicator_service_action_stop**
> NodeServiceStatusProperties create_async_replicator_service_action_stop()

Restart, start or stop the Async Replicator service

Restart, start or stop the Async Replicator service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the Async Replicator service
    api_response = api_instance.create_async_replicator_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi->create_async_replicator_service_action_stop: %s\n" % e)
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

# **read_async_replicator_service**
> NodeAsyncReplicatorServiceProperties read_async_replicator_service()

Read the Async Replicator service properties

Read the Async Replicator service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read the Async Replicator service properties
    api_response = api_instance.read_async_replicator_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi->read_async_replicator_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeAsyncReplicatorServiceProperties**](NodeAsyncReplicatorServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_async_replicator_service_status**
> NodeServiceStatusProperties read_async_replicator_service_status()

Read the Async Replicator service status

Read the Async Replicator service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read the Async Replicator service status
    api_response = api_instance.read_async_replicator_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesAsyncReplicatorServiceApi->read_async_replicator_service_status: %s\n" % e)
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

