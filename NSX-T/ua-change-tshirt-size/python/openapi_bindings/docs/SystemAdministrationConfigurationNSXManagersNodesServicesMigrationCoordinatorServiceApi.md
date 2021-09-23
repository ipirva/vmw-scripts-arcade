# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_migration_coordinator_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi.md#create_migration_coordinator_service_action_restart) | **POST** /node/services/migration-coordinator?action&#x3D;restart | Restart, start or stop the migration coordinator service
[**create_migration_coordinator_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi.md#create_migration_coordinator_service_action_start) | **POST** /node/services/migration-coordinator?action&#x3D;start | Restart, start or stop the migration coordinator service
[**create_migration_coordinator_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi.md#create_migration_coordinator_service_action_stop) | **POST** /node/services/migration-coordinator?action&#x3D;stop | Restart, start or stop the migration coordinator service
[**read_migration_coordinator_service**](SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi.md#read_migration_coordinator_service) | **GET** /node/services/migration-coordinator | Read migration coordinator service properties
[**read_migration_coordinator_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi.md#read_migration_coordinator_service_status) | **GET** /node/services/migration-coordinator/status | Read migration coordinator service status

# **create_migration_coordinator_service_action_restart**
> NodeServiceStatusProperties create_migration_coordinator_service_action_restart()

Restart, start or stop the migration coordinator service

Restart, start or stop the migration coordinator service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the migration coordinator service
    api_response = api_instance.create_migration_coordinator_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi->create_migration_coordinator_service_action_restart: %s\n" % e)
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

# **create_migration_coordinator_service_action_start**
> NodeServiceStatusProperties create_migration_coordinator_service_action_start()

Restart, start or stop the migration coordinator service

Restart, start or stop the migration coordinator service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the migration coordinator service
    api_response = api_instance.create_migration_coordinator_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi->create_migration_coordinator_service_action_start: %s\n" % e)
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

# **create_migration_coordinator_service_action_stop**
> NodeServiceStatusProperties create_migration_coordinator_service_action_stop()

Restart, start or stop the migration coordinator service

Restart, start or stop the migration coordinator service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the migration coordinator service
    api_response = api_instance.create_migration_coordinator_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi->create_migration_coordinator_service_action_stop: %s\n" % e)
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

# **read_migration_coordinator_service**
> NodeServiceProperties read_migration_coordinator_service()

Read migration coordinator service properties

Read migration coordinator service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read migration coordinator service properties
    api_response = api_instance.read_migration_coordinator_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi->read_migration_coordinator_service: %s\n" % e)
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

# **read_migration_coordinator_service_status**
> NodeServiceStatusProperties read_migration_coordinator_service_status()

Read migration coordinator service status

Read migration coordinator service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read migration coordinator service status
    api_response = api_instance.read_migration_coordinator_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesMigrationCoordinatorServiceApi->read_migration_coordinator_service_status: %s\n" % e)
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

