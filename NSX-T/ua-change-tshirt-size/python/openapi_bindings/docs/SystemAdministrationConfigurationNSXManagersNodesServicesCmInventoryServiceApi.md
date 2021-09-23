# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cminventory_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi.md#create_cminventory_service_action_restart) | **POST** /node/services/cm-inventory?action&#x3D;restart | Restart, start or stop the manager service
[**create_cminventory_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi.md#create_cminventory_service_action_start) | **POST** /node/services/cm-inventory?action&#x3D;start | Restart, start or stop the manager service
[**create_cminventory_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi.md#create_cminventory_service_action_stop) | **POST** /node/services/cm-inventory?action&#x3D;stop | Restart, start or stop the manager service
[**read_cminventory_service**](SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi.md#read_cminventory_service) | **GET** /node/services/cm-inventory | Read cm inventory service properties
[**read_cminventory_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi.md#read_cminventory_service_status) | **GET** /node/services/cm-inventory/status | Read manager service status

# **create_cminventory_service_action_restart**
> NodeServiceStatusProperties create_cminventory_service_action_restart()

Restart, start or stop the manager service

Restart, start or stop the manager service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the manager service
    api_response = api_instance.create_cminventory_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi->create_cminventory_service_action_restart: %s\n" % e)
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

# **create_cminventory_service_action_start**
> NodeServiceStatusProperties create_cminventory_service_action_start()

Restart, start or stop the manager service

Restart, start or stop the manager service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the manager service
    api_response = api_instance.create_cminventory_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi->create_cminventory_service_action_start: %s\n" % e)
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

# **create_cminventory_service_action_stop**
> NodeServiceStatusProperties create_cminventory_service_action_stop()

Restart, start or stop the manager service

Restart, start or stop the manager service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the manager service
    api_response = api_instance.create_cminventory_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi->create_cminventory_service_action_stop: %s\n" % e)
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

# **read_cminventory_service**
> NodeServiceProperties read_cminventory_service()

Read cm inventory service properties

Read cm inventory service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read cm inventory service properties
    api_response = api_instance.read_cminventory_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi->read_cminventory_service: %s\n" % e)
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

# **read_cminventory_service_status**
> NodeServiceStatusProperties read_cminventory_service_status()

Read manager service status

Read manager service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read manager service status
    api_response = api_instance.read_cminventory_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesCmInventoryServiceApi->read_cminventory_service_status: %s\n" % e)
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

