# swagger_client.SystemAdministrationConfigurationFabricNodesSettingsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_node_processes**](SystemAdministrationConfigurationFabricNodesSettingsApi.md#list_node_processes) | **GET** /node/processes | List node processes
[**read_appliance_node_status**](SystemAdministrationConfigurationFabricNodesSettingsApi.md#read_appliance_node_status) | **GET** /node/status | Read node status
[**read_node_process**](SystemAdministrationConfigurationFabricNodesSettingsApi.md#read_node_process) | **GET** /node/processes/{process-id} | Read node process
[**read_node_properties**](SystemAdministrationConfigurationFabricNodesSettingsApi.md#read_node_properties) | **GET** /node | Read node properties
[**read_node_version**](SystemAdministrationConfigurationFabricNodesSettingsApi.md#read_node_version) | **GET** /node/version | Read node version
[**restart_or_shutdown_node_restart**](SystemAdministrationConfigurationFabricNodesSettingsApi.md#restart_or_shutdown_node_restart) | **POST** /node?action&#x3D;restart | Restart or shutdown node
[**restart_or_shutdown_node_shutdown**](SystemAdministrationConfigurationFabricNodesSettingsApi.md#restart_or_shutdown_node_shutdown) | **POST** /node?action&#x3D;shutdown | Restart or shutdown node
[**set_node_time_set_system_time**](SystemAdministrationConfigurationFabricNodesSettingsApi.md#set_node_time_set_system_time) | **POST** /node?action&#x3D;set_system_time | Set the node system time
[**update_appliance_node_status_clear_bootup_error**](SystemAdministrationConfigurationFabricNodesSettingsApi.md#update_appliance_node_status_clear_bootup_error) | **POST** /node/status?action&#x3D;clear_bootup_error | Update node status
[**update_node_properties**](SystemAdministrationConfigurationFabricNodesSettingsApi.md#update_node_properties) | **PUT** /node | Update node properties

# **list_node_processes**
> NodeProcessPropertiesListResult list_node_processes()

List node processes

Returns the number of processes and information about each process. Process information includes 1) mem_resident, which is roughly equivalent to the amount of RAM, in bytes, currently used by the process, 2) parent process ID (ppid), 3) process name, 4) process up time in milliseconds, 5) mem_used, wich is the amount of virtual memory used by the process, in bytes, 6) process start time, in milliseconds since epoch, 7) process ID (pid), 8) CPU time, both user and the system, consumed by the process in milliseconds. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesSettingsApi(swagger_client.ApiClient(configuration))

try:
    # List node processes
    api_response = api_instance.list_node_processes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesSettingsApi->list_node_processes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeProcessPropertiesListResult**](NodeProcessPropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_appliance_node_status**
> NodeStatusProperties read_appliance_node_status()

Read node status

Returns information about the node appliance's file system, CPU, memory, disk usage, and uptime. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesSettingsApi(swagger_client.ApiClient(configuration))

try:
    # Read node status
    api_response = api_instance.read_appliance_node_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesSettingsApi->read_appliance_node_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeStatusProperties**](NodeStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_process**
> NodeProcessProperties read_node_process(process_id)

Read node process

Returns information for a specified process ID (pid).

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesSettingsApi(swagger_client.ApiClient(configuration))
process_id = 'process_id_example' # str | ID of process to read

try:
    # Read node process
    api_response = api_instance.read_node_process(process_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesSettingsApi->read_node_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| ID of process to read | 

### Return type

[**NodeProcessProperties**](NodeProcessProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_properties**
> NodeProperties read_node_properties()

Read node properties

Returns information about the NSX appliance. Information includes release number, time zone, system time, kernel version, message of the day (motd), and host name. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesSettingsApi(swagger_client.ApiClient(configuration))

try:
    # Read node properties
    api_response = api_instance.read_node_properties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesSettingsApi->read_node_properties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeProperties**](NodeProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_version**
> NodeVersion read_node_version()

Read node version

Read node version

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesSettingsApi(swagger_client.ApiClient(configuration))

try:
    # Read node version
    api_response = api_instance.read_node_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesSettingsApi->read_node_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeVersion**](NodeVersion.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_or_shutdown_node_restart**
> restart_or_shutdown_node_restart()

Restart or shutdown node

Restarts or shuts down the NSX appliance.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesSettingsApi(swagger_client.ApiClient(configuration))

try:
    # Restart or shutdown node
    api_instance.restart_or_shutdown_node_restart()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesSettingsApi->restart_or_shutdown_node_restart: %s\n" % e)
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

# **restart_or_shutdown_node_shutdown**
> restart_or_shutdown_node_shutdown()

Restart or shutdown node

Restarts or shuts down the NSX appliance.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesSettingsApi(swagger_client.ApiClient(configuration))

try:
    # Restart or shutdown node
    api_instance.restart_or_shutdown_node_shutdown()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesSettingsApi->restart_or_shutdown_node_shutdown: %s\n" % e)
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

# **set_node_time_set_system_time**
> set_node_time_set_system_time(body)

Set the node system time

Set the node system time to the given time in UTC in the RFC3339 format 'yyyy-mm-ddThh:mm:ssZ'. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesSettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeTime() # NodeTime | 

try:
    # Set the node system time
    api_instance.set_node_time_set_system_time(body)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesSettingsApi->set_node_time_set_system_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeTime**](NodeTime.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_node_status_clear_bootup_error**
> NodeStatusProperties update_appliance_node_status_clear_bootup_error()

Update node status

Clear node bootup status 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesSettingsApi(swagger_client.ApiClient(configuration))

try:
    # Update node status
    api_response = api_instance.update_appliance_node_status_clear_bootup_error()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesSettingsApi->update_appliance_node_status_clear_bootup_error: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeStatusProperties**](NodeStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_properties**
> NodeProperties update_node_properties(body)

Update node properties

Modifies NSX appliance properties. Modifiable properties include the timezone, message of the day (motd), and hostname. The NSX appliance node_version, system_time, and kernel_version are read only and cannot be modified with this method. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesSettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeProperties() # NodeProperties | 

try:
    # Update node properties
    api_response = api_instance.update_node_properties(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesSettingsApi->update_node_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeProperties**](NodeProperties.md)|  | 

### Return type

[**NodeProperties**](NodeProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

