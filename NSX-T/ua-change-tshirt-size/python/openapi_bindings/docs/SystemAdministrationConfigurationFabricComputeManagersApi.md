# swagger_client.SystemAdministrationConfigurationFabricComputeManagersApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_compute_manager**](SystemAdministrationConfigurationFabricComputeManagersApi.md#add_compute_manager) | **POST** /fabric/compute-managers | Register compute manager with NSX
[**delete_compute_manager**](SystemAdministrationConfigurationFabricComputeManagersApi.md#delete_compute_manager) | **DELETE** /fabric/compute-managers/{compute-manager-id} | Unregister a compute manager
[**get_compute_manager_state**](SystemAdministrationConfigurationFabricComputeManagersApi.md#get_compute_manager_state) | **GET** /fabric/compute-managers/{compute-manager-id}/state | Get the realized state of a compute manager
[**get_inventory_config**](SystemAdministrationConfigurationFabricComputeManagersApi.md#get_inventory_config) | **GET** /configs/inventory | Return inventory configuration
[**list_compute_managers**](SystemAdministrationConfigurationFabricComputeManagersApi.md#list_compute_managers) | **GET** /fabric/compute-managers | Return the List of Compute managers
[**read_compute_manager**](SystemAdministrationConfigurationFabricComputeManagersApi.md#read_compute_manager) | **GET** /fabric/compute-managers/{compute-manager-id} | Return compute manager Information
[**read_compute_manager_status**](SystemAdministrationConfigurationFabricComputeManagersApi.md#read_compute_manager_status) | **GET** /fabric/compute-managers/{compute-manager-id}/status | Return runtime status information for a compute manager
[**update_compute_manager**](SystemAdministrationConfigurationFabricComputeManagersApi.md#update_compute_manager) | **PUT** /fabric/compute-managers/{compute-manager-id} | Update compute manager

# **add_compute_manager**
> ComputeManager add_compute_manager(body)

Register compute manager with NSX

Registers compute manager with NSX. Inventory service will collect data from the registered compute manager 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeManagersApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComputeManager() # ComputeManager | 

try:
    # Register compute manager with NSX
    api_response = api_instance.add_compute_manager(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeManagersApi->add_compute_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComputeManager**](ComputeManager.md)|  | 

### Return type

[**ComputeManager**](ComputeManager.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_compute_manager**
> delete_compute_manager(compute_manager_id)

Unregister a compute manager

Unregisters a specified compute manager 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeManagersApi(swagger_client.ApiClient(configuration))
compute_manager_id = 'compute_manager_id_example' # str | 

try:
    # Unregister a compute manager
    api_instance.delete_compute_manager(compute_manager_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeManagersApi->delete_compute_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_manager_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compute_manager_state**
> ConfigurationState get_compute_manager_state(compute_manager_id)

Get the realized state of a compute manager

Get the realized state of a compute manager

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeManagersApi(swagger_client.ApiClient(configuration))
compute_manager_id = 'compute_manager_id_example' # str | 

try:
    # Get the realized state of a compute manager
    api_response = api_instance.get_compute_manager_state(compute_manager_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeManagersApi->get_compute_manager_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_manager_id** | **str**|  | 

### Return type

[**ConfigurationState**](ConfigurationState.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_config**
> InventoryConfig get_inventory_config()

Return inventory configuration

Supports retrieving following configuration of inventory module 1. Soft limit on number of compute managers that can be registered. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeManagersApi(swagger_client.ApiClient(configuration))

try:
    # Return inventory configuration
    api_response = api_instance.get_inventory_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeManagersApi->get_inventory_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InventoryConfig**](InventoryConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compute_managers**
> ComputeManagerListResult list_compute_managers(cursor=cursor, included_fields=included_fields, origin_type=origin_type, page_size=page_size, server=server, sort_ascending=sort_ascending, sort_by=sort_by)

Return the List of Compute managers

Returns information about all compute managers.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeManagersApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
origin_type = 'origin_type_example' # str | Compute manager type like vCenter (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
server = 'server_example' # str | IP address or hostname of compute manager (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Return the List of Compute managers
    api_response = api_instance.list_compute_managers(cursor=cursor, included_fields=included_fields, origin_type=origin_type, page_size=page_size, server=server, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeManagersApi->list_compute_managers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **origin_type** | **str**| Compute manager type like vCenter | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **server** | **str**| IP address or hostname of compute manager | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ComputeManagerListResult**](ComputeManagerListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_compute_manager**
> ComputeManager read_compute_manager(compute_manager_id)

Return compute manager Information

Returns information about a specific compute manager

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeManagersApi(swagger_client.ApiClient(configuration))
compute_manager_id = 'compute_manager_id_example' # str | 

try:
    # Return compute manager Information
    api_response = api_instance.read_compute_manager(compute_manager_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeManagersApi->read_compute_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_manager_id** | **str**|  | 

### Return type

[**ComputeManager**](ComputeManager.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_compute_manager_status**
> ComputeManagerStatus read_compute_manager_status(compute_manager_id)

Return runtime status information for a compute manager

Returns connection and version information about a compute manager 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeManagersApi(swagger_client.ApiClient(configuration))
compute_manager_id = 'compute_manager_id_example' # str | 

try:
    # Return runtime status information for a compute manager
    api_response = api_instance.read_compute_manager_status(compute_manager_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeManagersApi->read_compute_manager_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_manager_id** | **str**|  | 

### Return type

[**ComputeManagerStatus**](ComputeManagerStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_compute_manager**
> ComputeManager update_compute_manager(body, compute_manager_id)

Update compute manager

Updates a specified compute manager 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricComputeManagersApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComputeManager() # ComputeManager | 
compute_manager_id = 'compute_manager_id_example' # str | 

try:
    # Update compute manager
    api_response = api_instance.update_compute_manager(body, compute_manager_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricComputeManagersApi->update_compute_manager: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComputeManager**](ComputeManager.md)|  | 
 **compute_manager_id** | **str**|  | 

### Return type

[**ComputeManager**](ComputeManager.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

