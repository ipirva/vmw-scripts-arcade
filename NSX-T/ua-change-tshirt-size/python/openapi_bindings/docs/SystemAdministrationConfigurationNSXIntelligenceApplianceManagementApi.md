# swagger_client.SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_intelligence_upgrade_coordinator_service_action_restart**](SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi.md#create_intelligence_upgrade_coordinator_service_action_restart) | **POST** /node/services/intelligence-upgrade-coordinator?action&#x3D;restart | Restart, start or stop the intelligence upgrade coordinator service
[**create_intelligence_upgrade_coordinator_service_action_start**](SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi.md#create_intelligence_upgrade_coordinator_service_action_start) | **POST** /node/services/intelligence-upgrade-coordinator?action&#x3D;start | Restart, start or stop the intelligence upgrade coordinator service
[**create_intelligence_upgrade_coordinator_service_action_stop**](SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi.md#create_intelligence_upgrade_coordinator_service_action_stop) | **POST** /node/services/intelligence-upgrade-coordinator?action&#x3D;stop | Restart, start or stop the intelligence upgrade coordinator service
[**read_intelligence_upgrade_coordinator_service**](SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi.md#read_intelligence_upgrade_coordinator_service) | **GET** /node/services/intelligence-upgrade-coordinator | Read intelligence upgrade coordinator service properties
[**read_intelligence_upgrade_coordinator_service_status**](SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi.md#read_intelligence_upgrade_coordinator_service_status) | **GET** /node/services/intelligence-upgrade-coordinator/status | Read intelligence upgrade coordinator service status
[**update_async_replicator_service**](SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi.md#update_async_replicator_service) | **PUT** /node/services/async_replicator | Update the async_replicator service properties

# **create_intelligence_upgrade_coordinator_service_action_restart**
> NodeServiceStatusProperties create_intelligence_upgrade_coordinator_service_action_restart()

Restart, start or stop the intelligence upgrade coordinator service

Restart, start or stop the intelligence upgrade coordinator service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the intelligence upgrade coordinator service
    api_response = api_instance.create_intelligence_upgrade_coordinator_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi->create_intelligence_upgrade_coordinator_service_action_restart: %s\n" % e)
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

# **create_intelligence_upgrade_coordinator_service_action_start**
> NodeServiceStatusProperties create_intelligence_upgrade_coordinator_service_action_start()

Restart, start or stop the intelligence upgrade coordinator service

Restart, start or stop the intelligence upgrade coordinator service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the intelligence upgrade coordinator service
    api_response = api_instance.create_intelligence_upgrade_coordinator_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi->create_intelligence_upgrade_coordinator_service_action_start: %s\n" % e)
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

# **create_intelligence_upgrade_coordinator_service_action_stop**
> NodeServiceStatusProperties create_intelligence_upgrade_coordinator_service_action_stop()

Restart, start or stop the intelligence upgrade coordinator service

Restart, start or stop the intelligence upgrade coordinator service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the intelligence upgrade coordinator service
    api_response = api_instance.create_intelligence_upgrade_coordinator_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi->create_intelligence_upgrade_coordinator_service_action_stop: %s\n" % e)
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

# **read_intelligence_upgrade_coordinator_service**
> NodeServiceProperties read_intelligence_upgrade_coordinator_service()

Read intelligence upgrade coordinator service properties

Read intelligence upgrade coordinator service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read intelligence upgrade coordinator service properties
    api_response = api_instance.read_intelligence_upgrade_coordinator_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi->read_intelligence_upgrade_coordinator_service: %s\n" % e)
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

# **read_intelligence_upgrade_coordinator_service_status**
> NodeServiceStatusProperties read_intelligence_upgrade_coordinator_service_status()

Read intelligence upgrade coordinator service status

Read intelligence upgrade coordinator service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read intelligence upgrade coordinator service status
    api_response = api_instance.read_intelligence_upgrade_coordinator_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi->read_intelligence_upgrade_coordinator_service_status: %s\n" % e)
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

# **update_async_replicator_service**
> NodeAsyncReplicatorServiceProperties update_async_replicator_service(body)

Update the async_replicator service properties

Update the async_replicator service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeAsyncReplicatorServiceProperties() # NodeAsyncReplicatorServiceProperties | 

try:
    # Update the async_replicator service properties
    api_response = api_instance.update_async_replicator_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceApplianceManagementApi->update_async_replicator_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeAsyncReplicatorServiceProperties**](NodeAsyncReplicatorServiceProperties.md)|  | 

### Return type

[**NodeAsyncReplicatorServiceProperties**](NodeAsyncReplicatorServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

