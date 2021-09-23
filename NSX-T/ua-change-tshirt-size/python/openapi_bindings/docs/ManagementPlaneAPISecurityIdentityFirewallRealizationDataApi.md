# swagger_client.ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nsgroup_vm_details**](ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi.md#get_nsgroup_vm_details) | **GET** /idfw/nsgroup-vm-details/{group-id} | Get all IDFW NSGroup VM details for a given NSGroup
[**get_system_stats**](ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi.md#get_system_stats) | **GET** /idfw/system-stats | Get IDFW system statistics data
[**get_user_stats**](ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi.md#get_user_stats) | **GET** /idfw/user-stats/{user-id} | Get IDFW user login events for a given user
[**get_vm_stats**](ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi.md#get_vm_stats) | **GET** /idfw/vm-stats/{vm-ext-id} | Get IDFW user login events for a given VM
[**list_user_sessions**](ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi.md#list_user_sessions) | **GET** /idfw/user-session-data | Get user session data

# **get_nsgroup_vm_details**
> IdfwNsgroupVmDetailListResult get_nsgroup_vm_details(group_id)

Get all IDFW NSGroup VM details for a given NSGroup

Get all Identity Firewall NSGroup VM details for a given NSGroup.

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 

try:
    # Get all IDFW NSGroup VM details for a given NSGroup
    api_response = api_instance.get_nsgroup_vm_details(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi->get_nsgroup_vm_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

[**IdfwNsgroupVmDetailListResult**](IdfwNsgroupVmDetailListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_stats**
> IdfwSystemStats get_system_stats()

Get IDFW system statistics data

Get IDFW system statistics data.

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi(swagger_client.ApiClient(configuration))

try:
    # Get IDFW system statistics data
    api_response = api_instance.get_system_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi->get_system_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdfwSystemStats**](IdfwSystemStats.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_stats**
> IdfwUserStats get_user_stats(user_id)

Get IDFW user login events for a given user

Get IDFW user login events for a given user (all active plus up to 5 most recent archived entries). 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Get IDFW user login events for a given user
    api_response = api_instance.get_user_stats(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi->get_user_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**IdfwUserStats**](IdfwUserStats.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vm_stats**
> IdfwVmStats get_vm_stats(vm_ext_id)

Get IDFW user login events for a given VM

Get IDFW user login events for a given VM (all active plus up to 5 most recent archived entries). 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi(swagger_client.ApiClient(configuration))
vm_ext_id = 'vm_ext_id_example' # str | 

try:
    # Get IDFW user login events for a given VM
    api_response = api_instance.get_vm_stats(vm_ext_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi->get_vm_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_ext_id** | **str**|  | 

### Return type

[**IdfwVmStats**](IdfwVmStats.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_sessions**
> IdfwUserSessionDataAndMappings list_user_sessions()

Get user session data

Get user session data.

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
api_instance = swagger_client.ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi(swagger_client.ApiClient(configuration))

try:
    # Get user session data
    api_response = api_instance.list_user_sessions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIdentityFirewallRealizationDataApi->list_user_sessions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdfwUserSessionDataAndMappings**](IdfwUserSessionDataAndMappings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

