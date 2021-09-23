# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_boot_manager_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi.md#create_cluster_boot_manager_service_action_restart) | **POST** /node/services/cluster_manager?action&#x3D;restart | Restart, start or stop the cluster boot manager service
[**create_cluster_boot_manager_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi.md#create_cluster_boot_manager_service_action_start) | **POST** /node/services/cluster_manager?action&#x3D;start | Restart, start or stop the cluster boot manager service
[**create_cluster_boot_manager_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi.md#create_cluster_boot_manager_service_action_stop) | **POST** /node/services/cluster_manager?action&#x3D;stop | Restart, start or stop the cluster boot manager service
[**read_cluster_boot_manager_service**](SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi.md#read_cluster_boot_manager_service) | **GET** /node/services/cluster_manager | Read cluster boot manager service properties
[**read_cluster_boot_manager_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi.md#read_cluster_boot_manager_service_status) | **GET** /node/services/cluster_manager/status | Read cluster boot manager service status

# **create_cluster_boot_manager_service_action_restart**
> NodeServiceStatusProperties create_cluster_boot_manager_service_action_restart()

Restart, start or stop the cluster boot manager service

Restart, start or stop the cluster boot manager service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the cluster boot manager service
    api_response = api_instance.create_cluster_boot_manager_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi->create_cluster_boot_manager_service_action_restart: %s\n" % e)
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

# **create_cluster_boot_manager_service_action_start**
> NodeServiceStatusProperties create_cluster_boot_manager_service_action_start()

Restart, start or stop the cluster boot manager service

Restart, start or stop the cluster boot manager service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the cluster boot manager service
    api_response = api_instance.create_cluster_boot_manager_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi->create_cluster_boot_manager_service_action_start: %s\n" % e)
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

# **create_cluster_boot_manager_service_action_stop**
> NodeServiceStatusProperties create_cluster_boot_manager_service_action_stop()

Restart, start or stop the cluster boot manager service

Restart, start or stop the cluster boot manager service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the cluster boot manager service
    api_response = api_instance.create_cluster_boot_manager_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi->create_cluster_boot_manager_service_action_stop: %s\n" % e)
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

# **read_cluster_boot_manager_service**
> NodeServiceProperties read_cluster_boot_manager_service()

Read cluster boot manager service properties

Read cluster boot manager service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read cluster boot manager service properties
    api_response = api_instance.read_cluster_boot_manager_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi->read_cluster_boot_manager_service: %s\n" % e)
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

# **read_cluster_boot_manager_service_status**
> NodeServiceStatusProperties read_cluster_boot_manager_service_status()

Read cluster boot manager service status

Read cluster boot manager service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read cluster boot manager service status
    api_response = api_instance.read_cluster_boot_manager_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesClusterManagerServiceApi->read_cluster_boot_manager_service_status: %s\n" % e)
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

