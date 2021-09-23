# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi.md#create_policy_service_action_restart) | **POST** /node/services/policy?action&#x3D;restart | Restart, start or stop the service
[**create_policy_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi.md#create_policy_service_action_start) | **POST** /node/services/policy?action&#x3D;start | Restart, start or stop the service
[**create_policy_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi.md#create_policy_service_action_stop) | **POST** /node/services/policy?action&#x3D;stop | Restart, start or stop the service
[**read_policy_service**](SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi.md#read_policy_service) | **GET** /node/services/policy | Read service properties
[**read_policy_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi.md#read_policy_service_status) | **GET** /node/services/policy/status | Read service status
[**reset_policy_service_logging_level_action_reset_manager_logging_levels**](SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi.md#reset_policy_service_logging_level_action_reset_manager_logging_levels) | **POST** /node/services/policy?action&#x3D;reset-manager-logging-levels | Reset the logging levels to default values
[**update_policy_service**](SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi.md#update_policy_service) | **PUT** /node/services/policy | Update service properties

# **create_policy_service_action_restart**
> NodeServiceStatusProperties create_policy_service_action_restart()

Restart, start or stop the service

Restart, start or stop the service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the service
    api_response = api_instance.create_policy_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi->create_policy_service_action_restart: %s\n" % e)
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

# **create_policy_service_action_start**
> NodeServiceStatusProperties create_policy_service_action_start()

Restart, start or stop the service

Restart, start or stop the service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the service
    api_response = api_instance.create_policy_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi->create_policy_service_action_start: %s\n" % e)
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

# **create_policy_service_action_stop**
> NodeServiceStatusProperties create_policy_service_action_stop()

Restart, start or stop the service

Restart, start or stop the service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the service
    api_response = api_instance.create_policy_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi->create_policy_service_action_stop: %s\n" % e)
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

# **read_policy_service**
> NodePolicyServiceProperties read_policy_service()

Read service properties

Read service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read service properties
    api_response = api_instance.read_policy_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi->read_policy_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodePolicyServiceProperties**](NodePolicyServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_policy_service_status**
> NodeServiceStatusProperties read_policy_service_status()

Read service status

Read service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read service status
    api_response = api_instance.read_policy_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi->read_policy_service_status: %s\n" % e)
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

# **reset_policy_service_logging_level_action_reset_manager_logging_levels**
> reset_policy_service_logging_level_action_reset_manager_logging_levels()

Reset the logging levels to default values

Reset the logging levels to default values

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi(swagger_client.ApiClient(configuration))

try:
    # Reset the logging levels to default values
    api_instance.reset_policy_service_logging_level_action_reset_manager_logging_levels()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi->reset_policy_service_logging_level_action_reset_manager_logging_levels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_service**
> NodePolicyServiceProperties update_policy_service(body)

Update service properties

Update service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodePolicyServiceProperties() # NodePolicyServiceProperties | 

try:
    # Update service properties
    api_response = api_instance.update_policy_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesPolicyServiceApi->update_policy_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodePolicyServiceProperties**](NodePolicyServiceProperties.md)|  | 

### Return type

[**NodePolicyServiceProperties**](NodePolicyServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

