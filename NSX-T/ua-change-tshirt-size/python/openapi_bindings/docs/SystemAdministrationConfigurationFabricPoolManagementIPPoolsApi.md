# swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_or_release_from_ip_pool**](SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi.md#allocate_or_release_from_ip_pool) | **POST** /pools/ip-pools/{pool-id} | Allocate or Release an IP Address from a Pool
[**create_ip_pool**](SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi.md#create_ip_pool) | **POST** /pools/ip-pools | Create an IP Pool
[**delete_ip_pool**](SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi.md#delete_ip_pool) | **DELETE** /pools/ip-pools/{pool-id} | Delete an IP Pool
[**list_ip_pool_allocations**](SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi.md#list_ip_pool_allocations) | **GET** /pools/ip-pools/{pool-id}/allocations | List IP Pool Allocations
[**list_ip_pools**](SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi.md#list_ip_pools) | **GET** /pools/ip-pools | List IP Pools
[**read_ip_pool**](SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi.md#read_ip_pool) | **GET** /pools/ip-pools/{pool-id} | Read IP Pool
[**update_ip_pool**](SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi.md#update_ip_pool) | **PUT** /pools/ip-pools/{pool-id} | Update an IP Pool

# **allocate_or_release_from_ip_pool**
> AllocationIpAddress allocate_or_release_from_ip_pool(body, action, pool_id)

Allocate or Release an IP Address from a Pool

Allocates or releases an IP address from the specified IP pool. To allocate an address, include ?action=ALLOCATE in the request and \"allocation_id\":null in the request body. When the request is successful, the response is \"allocation_id\": \"<ip-address>\", where <ip-address> is an IP address from the specified pool. To release an IP address (return it back to the pool), include ?action=RELEASE in the request and \"allocation_id\":<ip-address> in the request body, where <ip-address> is the address to be released. When the request is successful, the response is NULL. Tags, display_name and description attributes are not supported for AllocationIpAddress in this release. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AllocationIpAddress() # AllocationIpAddress | 
action = 'action_example' # str | Specifies allocate or release action
pool_id = 'pool_id_example' # str | IP pool ID

try:
    # Allocate or Release an IP Address from a Pool
    api_response = api_instance.allocate_or_release_from_ip_pool(body, action, pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi->allocate_or_release_from_ip_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AllocationIpAddress**](AllocationIpAddress.md)|  | 
 **action** | **str**| Specifies allocate or release action | 
 **pool_id** | **str**| IP pool ID | 

### Return type

[**AllocationIpAddress**](AllocationIpAddress.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ip_pool**
> IpPool create_ip_pool(body)

Create an IP Pool

Creates a new IPv4 or IPv6 address pool. Required parameters are allocation_ranges and cidr. Optional parameters are display_name, description, dns_nameservers, dns_suffix, and gateway_ip. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpPool() # IpPool | 

try:
    # Create an IP Pool
    api_response = api_instance.create_ip_pool(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi->create_ip_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpPool**](IpPool.md)|  | 

### Return type

[**IpPool**](IpPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_pool**
> delete_ip_pool(pool_id, force=force)

Delete an IP Pool

Deletes the specified IP address pool. By default, if the IpPool is used in other configurations (such as transport node template), it won't be deleted. In such situations, pass \"force=true\" as query param to force delete the IpPool

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi(swagger_client.ApiClient(configuration))
pool_id = 'pool_id_example' # str | IP pool ID
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete an IP Pool
    api_instance.delete_ip_pool(pool_id, force=force)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi->delete_ip_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| IP pool ID | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_pool_allocations**
> AllocationIpAddressListResult list_ip_pool_allocations(pool_id)

List IP Pool Allocations

Returns information about which addresses have been allocated from a specified IP address pool. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi(swagger_client.ApiClient(configuration))
pool_id = 'pool_id_example' # str | IP pool ID

try:
    # List IP Pool Allocations
    api_response = api_instance.list_ip_pool_allocations(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi->list_ip_pool_allocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| IP pool ID | 

### Return type

[**AllocationIpAddressListResult**](AllocationIpAddressListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_pools**
> IpPoolListResult list_ip_pools(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List IP Pools

Returns information about the configured IP address pools. Information includes the display name and description of the pool and the details of each of the subnets in the pool, including the DNS servers, allocation ranges, gateway, and CIDR subnet address. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List IP Pools
    api_response = api_instance.list_ip_pools(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi->list_ip_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IpPoolListResult**](IpPoolListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ip_pool**
> IpPool read_ip_pool(pool_id)

Read IP Pool

Returns information about the specified IP address pool.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi(swagger_client.ApiClient(configuration))
pool_id = 'pool_id_example' # str | IP pool ID

try:
    # Read IP Pool
    api_response = api_instance.read_ip_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi->read_ip_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| IP pool ID | 

### Return type

[**IpPool**](IpPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_pool**
> IpPool update_ip_pool(body, pool_id)

Update an IP Pool

Modifies the specified IP address pool. Modifiable parameters include the description, display_name, and all subnet information. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IpPool() # IpPool | 
pool_id = 'pool_id_example' # str | IP pool ID

try:
    # Update an IP Pool
    api_response = api_instance.update_ip_pool(body, pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementIPPoolsApi->update_ip_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpPool**](IpPool.md)|  | 
 **pool_id** | **str**| IP pool ID | 

### Return type

[**IpPool**](IpPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

