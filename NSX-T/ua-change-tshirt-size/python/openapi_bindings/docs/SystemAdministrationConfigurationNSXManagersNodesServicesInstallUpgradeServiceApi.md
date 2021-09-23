# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repository_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi.md#create_repository_service_action_restart) | **POST** /node/services/install-upgrade?action&#x3D;restart | Restart, start or stop the NSX install-upgrade service
[**create_repository_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi.md#create_repository_service_action_start) | **POST** /node/services/install-upgrade?action&#x3D;start | Restart, start or stop the NSX install-upgrade service
[**create_repository_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi.md#create_repository_service_action_stop) | **POST** /node/services/install-upgrade?action&#x3D;stop | Restart, start or stop the NSX install-upgrade service
[**read_repository_service**](SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi.md#read_repository_service) | **GET** /node/services/install-upgrade | Read NSX install-upgrade service properties
[**read_repository_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi.md#read_repository_service_status) | **GET** /node/services/install-upgrade/status | Read NSX install-upgrade service status
[**update_repository_service**](SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi.md#update_repository_service) | **PUT** /node/services/install-upgrade | Update NSX install-upgrade service properties
[**update_uc_state**](SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi.md#update_uc_state) | **PUT** /node/services/install-upgrade/uc-state | Update UC state properties

# **create_repository_service_action_restart**
> NodeServiceStatusProperties create_repository_service_action_restart()

Restart, start or stop the NSX install-upgrade service

Restart, start or stop the NSX install-upgrade service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX install-upgrade service
    api_response = api_instance.create_repository_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi->create_repository_service_action_restart: %s\n" % e)
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

# **create_repository_service_action_start**
> NodeServiceStatusProperties create_repository_service_action_start()

Restart, start or stop the NSX install-upgrade service

Restart, start or stop the NSX install-upgrade service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX install-upgrade service
    api_response = api_instance.create_repository_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi->create_repository_service_action_start: %s\n" % e)
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

# **create_repository_service_action_stop**
> NodeServiceStatusProperties create_repository_service_action_stop()

Restart, start or stop the NSX install-upgrade service

Restart, start or stop the NSX install-upgrade service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX install-upgrade service
    api_response = api_instance.create_repository_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi->create_repository_service_action_stop: %s\n" % e)
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

# **read_repository_service**
> NodeInstallUpgradeServiceProperties read_repository_service()

Read NSX install-upgrade service properties

Read NSX install-upgrade service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX install-upgrade service properties
    api_response = api_instance.read_repository_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi->read_repository_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeInstallUpgradeServiceProperties**](NodeInstallUpgradeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_repository_service_status**
> NodeServiceStatusProperties read_repository_service_status()

Read NSX install-upgrade service status

Read NSX install-upgrade service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX install-upgrade service status
    api_response = api_instance.read_repository_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi->read_repository_service_status: %s\n" % e)
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

# **update_repository_service**
> NodeInstallUpgradeServiceProperties update_repository_service(body)

Update NSX install-upgrade service properties

Update NSX install-upgrade service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeInstallUpgradeServiceProperties() # NodeInstallUpgradeServiceProperties | 

try:
    # Update NSX install-upgrade service properties
    api_response = api_instance.update_repository_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi->update_repository_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeInstallUpgradeServiceProperties**](NodeInstallUpgradeServiceProperties.md)|  | 

### Return type

[**NodeInstallUpgradeServiceProperties**](NodeInstallUpgradeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_uc_state**
> update_uc_state(body)

Update UC state properties

Update UC state properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.UcStateProperties() # UcStateProperties | 

try:
    # Update UC state properties
    api_instance.update_uc_state(body)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesInstallUpgradeServiceApi->update_uc_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UcStateProperties**](UcStateProperties.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

