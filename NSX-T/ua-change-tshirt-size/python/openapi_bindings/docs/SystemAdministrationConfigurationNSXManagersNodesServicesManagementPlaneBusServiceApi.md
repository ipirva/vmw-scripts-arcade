# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rabbit_mq_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi.md#create_rabbit_mq_service_action_restart) | **POST** /node/services/mgmt-plane-bus?action&#x3D;restart | Restart, start or stop the Rabbit MQ service
[**create_rabbit_mq_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi.md#create_rabbit_mq_service_action_start) | **POST** /node/services/mgmt-plane-bus?action&#x3D;start | Restart, start or stop the Rabbit MQ service
[**create_rabbit_mq_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi.md#create_rabbit_mq_service_action_stop) | **POST** /node/services/mgmt-plane-bus?action&#x3D;stop | Restart, start or stop the Rabbit MQ service
[**read_rabbit_mq_service**](SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi.md#read_rabbit_mq_service) | **GET** /node/services/mgmt-plane-bus | Read Rabbit MQ service properties
[**read_rabbit_mq_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi.md#read_rabbit_mq_service_status) | **GET** /node/services/mgmt-plane-bus/status | Read Rabbit MQ service status

# **create_rabbit_mq_service_action_restart**
> NodeServiceStatusProperties create_rabbit_mq_service_action_restart()

Restart, start or stop the Rabbit MQ service

Restart, start or stop the Rabbit MQ service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the Rabbit MQ service
    api_response = api_instance.create_rabbit_mq_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi->create_rabbit_mq_service_action_restart: %s\n" % e)
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

# **create_rabbit_mq_service_action_start**
> NodeServiceStatusProperties create_rabbit_mq_service_action_start()

Restart, start or stop the Rabbit MQ service

Restart, start or stop the Rabbit MQ service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the Rabbit MQ service
    api_response = api_instance.create_rabbit_mq_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi->create_rabbit_mq_service_action_start: %s\n" % e)
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

# **create_rabbit_mq_service_action_stop**
> NodeServiceStatusProperties create_rabbit_mq_service_action_stop()

Restart, start or stop the Rabbit MQ service

Restart, start or stop the Rabbit MQ service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the Rabbit MQ service
    api_response = api_instance.create_rabbit_mq_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi->create_rabbit_mq_service_action_stop: %s\n" % e)
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

# **read_rabbit_mq_service**
> NodeServiceProperties read_rabbit_mq_service()

Read Rabbit MQ service properties

Read Rabbit MQ service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read Rabbit MQ service properties
    api_response = api_instance.read_rabbit_mq_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi->read_rabbit_mq_service: %s\n" % e)
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

# **read_rabbit_mq_service_status**
> NodeServiceStatusProperties read_rabbit_mq_service_status()

Read Rabbit MQ service status

Read Rabbit MQ service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read Rabbit MQ service status
    api_response = api_instance.read_rabbit_mq_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesManagementPlaneBusServiceApi->read_rabbit_mq_service_status: %s\n" % e)
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

