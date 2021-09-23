# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_search_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi.md#create_search_service_action_restart) | **POST** /node/services/search?action&#x3D;restart | Restart, start or stop the NSX Search service
[**create_search_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi.md#create_search_service_action_start) | **POST** /node/services/search?action&#x3D;start | Restart, start or stop the NSX Search service
[**create_search_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi.md#create_search_service_action_stop) | **POST** /node/services/search?action&#x3D;stop | Restart, start or stop the NSX Search service
[**read_search_service**](SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi.md#read_search_service) | **GET** /node/services/search | Read NSX Search service properties
[**read_search_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi.md#read_search_service_status) | **GET** /node/services/search/status | Read NSX Search service status

# **create_search_service_action_restart**
> NodeServiceStatusProperties create_search_service_action_restart()

Restart, start or stop the NSX Search service

Restart, start or stop the NSX Search service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Search service
    api_response = api_instance.create_search_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi->create_search_service_action_restart: %s\n" % e)
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

# **create_search_service_action_start**
> NodeServiceStatusProperties create_search_service_action_start()

Restart, start or stop the NSX Search service

Restart, start or stop the NSX Search service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Search service
    api_response = api_instance.create_search_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi->create_search_service_action_start: %s\n" % e)
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

# **create_search_service_action_stop**
> NodeServiceStatusProperties create_search_service_action_stop()

Restart, start or stop the NSX Search service

Restart, start or stop the NSX Search service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX Search service
    api_response = api_instance.create_search_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi->create_search_service_action_stop: %s\n" % e)
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

# **read_search_service**
> NodeServiceProperties read_search_service()

Read NSX Search service properties

Read NSX Search service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX Search service properties
    api_response = api_instance.read_search_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi->read_search_service: %s\n" % e)
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

# **read_search_service_status**
> NodeServiceStatusProperties read_search_service_status()

Read NSX Search service status

Read NSX Search service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX Search service status
    api_response = api_instance.read_search_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesSearchServiceApi->read_search_service_status: %s\n" % e)
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

