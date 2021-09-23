# swagger_client.SystemAdministrationConfigurationFabricNodesServicesLogInsightApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_liagent_service_action_restart**](SystemAdministrationConfigurationFabricNodesServicesLogInsightApi.md#create_liagent_service_action_restart) | **POST** /node/services/liagent?action&#x3D;restart | Restart, start or stop the liagent service
[**create_liagent_service_action_start**](SystemAdministrationConfigurationFabricNodesServicesLogInsightApi.md#create_liagent_service_action_start) | **POST** /node/services/liagent?action&#x3D;start | Restart, start or stop the liagent service
[**create_liagent_service_action_stop**](SystemAdministrationConfigurationFabricNodesServicesLogInsightApi.md#create_liagent_service_action_stop) | **POST** /node/services/liagent?action&#x3D;stop | Restart, start or stop the liagent service
[**read_liagent_service**](SystemAdministrationConfigurationFabricNodesServicesLogInsightApi.md#read_liagent_service) | **GET** /node/services/liagent | Read liagent service properties
[**read_liagent_service_status**](SystemAdministrationConfigurationFabricNodesServicesLogInsightApi.md#read_liagent_service_status) | **GET** /node/services/liagent/status | Read liagent service status

# **create_liagent_service_action_restart**
> NodeServiceStatusProperties create_liagent_service_action_restart()

Restart, start or stop the liagent service

Restart, start or stop the liagent service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesLogInsightApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the liagent service
    api_response = api_instance.create_liagent_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesLogInsightApi->create_liagent_service_action_restart: %s\n" % e)
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

# **create_liagent_service_action_start**
> NodeServiceStatusProperties create_liagent_service_action_start()

Restart, start or stop the liagent service

Restart, start or stop the liagent service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesLogInsightApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the liagent service
    api_response = api_instance.create_liagent_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesLogInsightApi->create_liagent_service_action_start: %s\n" % e)
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

# **create_liagent_service_action_stop**
> NodeServiceStatusProperties create_liagent_service_action_stop()

Restart, start or stop the liagent service

Restart, start or stop the liagent service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesLogInsightApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the liagent service
    api_response = api_instance.create_liagent_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesLogInsightApi->create_liagent_service_action_stop: %s\n" % e)
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

# **read_liagent_service**
> NodeServiceProperties read_liagent_service()

Read liagent service properties

Read liagent service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesLogInsightApi(swagger_client.ApiClient(configuration))

try:
    # Read liagent service properties
    api_response = api_instance.read_liagent_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesLogInsightApi->read_liagent_service: %s\n" % e)
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

# **read_liagent_service_status**
> NodeServiceStatusProperties read_liagent_service_status()

Read liagent service status

Read liagent service status

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesLogInsightApi(swagger_client.ApiClient(configuration))

try:
    # Read liagent service status
    api_response = api_instance.read_liagent_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesLogInsightApi->read_liagent_service_status: %s\n" % e)
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

