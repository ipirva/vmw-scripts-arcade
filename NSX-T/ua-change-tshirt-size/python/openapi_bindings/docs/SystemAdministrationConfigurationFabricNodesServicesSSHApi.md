# swagger_client.SystemAdministrationConfigurationFabricNodesServicesSSHApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ssh_service_action_notify_mpa_restart**](SystemAdministrationConfigurationFabricNodesServicesSSHApi.md#create_ssh_service_action_notify_mpa_restart) | **POST** /node/services/ssh/notify_mpa?action&#x3D;restart | Restart, start or stop the ssh service
[**create_ssh_service_action_notify_mpa_start**](SystemAdministrationConfigurationFabricNodesServicesSSHApi.md#create_ssh_service_action_notify_mpa_start) | **POST** /node/services/ssh/notify_mpa?action&#x3D;start | Restart, start or stop the ssh service
[**create_ssh_service_action_notify_mpa_stop**](SystemAdministrationConfigurationFabricNodesServicesSSHApi.md#create_ssh_service_action_notify_mpa_stop) | **POST** /node/services/ssh/notify_mpa?action&#x3D;stop | Restart, start or stop the ssh service
[**create_ssh_service_action_restart**](SystemAdministrationConfigurationFabricNodesServicesSSHApi.md#create_ssh_service_action_restart) | **POST** /node/services/ssh?action&#x3D;restart | Restart, start or stop the ssh service
[**create_ssh_service_action_start**](SystemAdministrationConfigurationFabricNodesServicesSSHApi.md#create_ssh_service_action_start) | **POST** /node/services/ssh?action&#x3D;start | Restart, start or stop the ssh service
[**create_ssh_service_action_stop**](SystemAdministrationConfigurationFabricNodesServicesSSHApi.md#create_ssh_service_action_stop) | **POST** /node/services/ssh?action&#x3D;stop | Restart, start or stop the ssh service
[**create_ssh_service_remove_host_fingerprint_action_remove_host_fingerprint**](SystemAdministrationConfigurationFabricNodesServicesSSHApi.md#create_ssh_service_remove_host_fingerprint_action_remove_host_fingerprint) | **POST** /node/services/ssh?action&#x3D;remove_host_fingerprint | Remove a host&#x27;s fingerprint from known hosts file
[**read_ssh_service**](SystemAdministrationConfigurationFabricNodesServicesSSHApi.md#read_ssh_service) | **GET** /node/services/ssh | Read ssh service properties
[**read_ssh_service_status**](SystemAdministrationConfigurationFabricNodesServicesSSHApi.md#read_ssh_service_status) | **GET** /node/services/ssh/status | Read ssh service status
[**update_ssh_service**](SystemAdministrationConfigurationFabricNodesServicesSSHApi.md#update_ssh_service) | **PUT** /node/services/ssh | Update ssh service properties

# **create_ssh_service_action_notify_mpa_restart**
> NodeServiceStatusProperties create_ssh_service_action_notify_mpa_restart()

Restart, start or stop the ssh service

Restart, start or stop the ssh service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSSHApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the ssh service
    api_response = api_instance.create_ssh_service_action_notify_mpa_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSSHApi->create_ssh_service_action_notify_mpa_restart: %s\n" % e)
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

# **create_ssh_service_action_notify_mpa_start**
> NodeServiceStatusProperties create_ssh_service_action_notify_mpa_start()

Restart, start or stop the ssh service

Restart, start or stop the ssh service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSSHApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the ssh service
    api_response = api_instance.create_ssh_service_action_notify_mpa_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSSHApi->create_ssh_service_action_notify_mpa_start: %s\n" % e)
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

# **create_ssh_service_action_notify_mpa_stop**
> NodeServiceStatusProperties create_ssh_service_action_notify_mpa_stop()

Restart, start or stop the ssh service

Restart, start or stop the ssh service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSSHApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the ssh service
    api_response = api_instance.create_ssh_service_action_notify_mpa_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSSHApi->create_ssh_service_action_notify_mpa_stop: %s\n" % e)
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

# **create_ssh_service_action_restart**
> NodeServiceStatusProperties create_ssh_service_action_restart()

Restart, start or stop the ssh service

Restart, start or stop the ssh service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSSHApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the ssh service
    api_response = api_instance.create_ssh_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSSHApi->create_ssh_service_action_restart: %s\n" % e)
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

# **create_ssh_service_action_start**
> NodeServiceStatusProperties create_ssh_service_action_start()

Restart, start or stop the ssh service

Restart, start or stop the ssh service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSSHApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the ssh service
    api_response = api_instance.create_ssh_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSSHApi->create_ssh_service_action_start: %s\n" % e)
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

# **create_ssh_service_action_stop**
> NodeServiceStatusProperties create_ssh_service_action_stop()

Restart, start or stop the ssh service

Restart, start or stop the ssh service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSSHApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the ssh service
    api_response = api_instance.create_ssh_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSSHApi->create_ssh_service_action_stop: %s\n" % e)
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

# **create_ssh_service_remove_host_fingerprint_action_remove_host_fingerprint**
> create_ssh_service_remove_host_fingerprint_action_remove_host_fingerprint(body)

Remove a host's fingerprint from known hosts file

Remove a host's fingerprint from known hosts file

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSSHApi(swagger_client.ApiClient(configuration))
body = swagger_client.KnownHostParameter() # KnownHostParameter | 

try:
    # Remove a host's fingerprint from known hosts file
    api_instance.create_ssh_service_remove_host_fingerprint_action_remove_host_fingerprint(body)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSSHApi->create_ssh_service_remove_host_fingerprint_action_remove_host_fingerprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KnownHostParameter**](KnownHostParameter.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ssh_service**
> NodeSshServiceProperties read_ssh_service()

Read ssh service properties

Read ssh service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSSHApi(swagger_client.ApiClient(configuration))

try:
    # Read ssh service properties
    api_response = api_instance.read_ssh_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSSHApi->read_ssh_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSshServiceProperties**](NodeSshServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ssh_service_status**
> NodeServiceStatusProperties read_ssh_service_status()

Read ssh service status

Read ssh service status

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSSHApi(swagger_client.ApiClient(configuration))

try:
    # Read ssh service status
    api_response = api_instance.read_ssh_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSSHApi->read_ssh_service_status: %s\n" % e)
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

# **update_ssh_service**
> NodeSshServiceProperties update_ssh_service(body)

Update ssh service properties

Update ssh service properties. If the start_on_boot property is updated to true, existing ssh sessions if any are stopped and the ssh service is restarted.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSSHApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeSshServiceProperties() # NodeSshServiceProperties | 

try:
    # Update ssh service properties
    api_response = api_instance.update_ssh_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSSHApi->update_ssh_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeSshServiceProperties**](NodeSshServiceProperties.md)|  | 

### Return type

[**NodeSshServiceProperties**](NodeSshServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

