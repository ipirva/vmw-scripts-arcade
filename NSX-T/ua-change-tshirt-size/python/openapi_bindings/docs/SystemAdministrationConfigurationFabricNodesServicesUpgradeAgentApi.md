# swagger_client.SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nsx_upgrade_agent_service_action_restart**](SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi.md#create_nsx_upgrade_agent_service_action_restart) | **POST** /node/services/nsx-upgrade-agent?action&#x3D;restart | Restart, start or stop the NSX upgrade agent service
[**create_nsx_upgrade_agent_service_action_start**](SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi.md#create_nsx_upgrade_agent_service_action_start) | **POST** /node/services/nsx-upgrade-agent?action&#x3D;start | Restart, start or stop the NSX upgrade agent service
[**create_nsx_upgrade_agent_service_action_stop**](SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi.md#create_nsx_upgrade_agent_service_action_stop) | **POST** /node/services/nsx-upgrade-agent?action&#x3D;stop | Restart, start or stop the NSX upgrade agent service
[**read_nsx_upgrade_agent_service**](SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi.md#read_nsx_upgrade_agent_service) | **GET** /node/services/nsx-upgrade-agent | Read NSX upgrade Agent service properties
[**read_nsx_upgrade_agent_service_status**](SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi.md#read_nsx_upgrade_agent_service_status) | **GET** /node/services/nsx-upgrade-agent/status | Read Nsx upgrade agent service status

# **create_nsx_upgrade_agent_service_action_restart**
> NodeServiceStatusProperties create_nsx_upgrade_agent_service_action_restart()

Restart, start or stop the NSX upgrade agent service

Restart, start or stop the NSX upgrade agent service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX upgrade agent service
    api_response = api_instance.create_nsx_upgrade_agent_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi->create_nsx_upgrade_agent_service_action_restart: %s\n" % e)
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

# **create_nsx_upgrade_agent_service_action_start**
> NodeServiceStatusProperties create_nsx_upgrade_agent_service_action_start()

Restart, start or stop the NSX upgrade agent service

Restart, start or stop the NSX upgrade agent service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX upgrade agent service
    api_response = api_instance.create_nsx_upgrade_agent_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi->create_nsx_upgrade_agent_service_action_start: %s\n" % e)
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

# **create_nsx_upgrade_agent_service_action_stop**
> NodeServiceStatusProperties create_nsx_upgrade_agent_service_action_stop()

Restart, start or stop the NSX upgrade agent service

Restart, start or stop the NSX upgrade agent service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX upgrade agent service
    api_response = api_instance.create_nsx_upgrade_agent_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi->create_nsx_upgrade_agent_service_action_stop: %s\n" % e)
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

# **read_nsx_upgrade_agent_service**
> NodeServiceProperties read_nsx_upgrade_agent_service()

Read NSX upgrade Agent service properties

Read NSX upgrade Agent service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX upgrade Agent service properties
    api_response = api_instance.read_nsx_upgrade_agent_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi->read_nsx_upgrade_agent_service: %s\n" % e)
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

# **read_nsx_upgrade_agent_service_status**
> NodeServiceStatusProperties read_nsx_upgrade_agent_service_status()

Read Nsx upgrade agent service status

Read Nsx upgrade agent service status

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi(swagger_client.ApiClient(configuration))

try:
    # Read Nsx upgrade agent service status
    api_response = api_instance.read_nsx_upgrade_agent_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesUpgradeAgentApi->read_nsx_upgrade_agent_service_status: %s\n" % e)
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

