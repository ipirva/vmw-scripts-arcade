# swagger_client.SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vni_pool**](SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi.md#create_vni_pool) | **POST** /pools/vni-pools | Create a new VNI Pool.
[**delete_vni_pool**](SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi.md#delete_vni_pool) | **DELETE** /pools/vni-pools/{pool-id} | Delete a VNI Pool
[**list_vni_pools**](SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi.md#list_vni_pools) | **GET** /pools/vni-pools | List VNI Pools
[**read_vni_pool**](SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi.md#read_vni_pool) | **GET** /pools/vni-pools/{pool-id} | Read VNI Pool
[**update_vni_pool**](SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi.md#update_vni_pool) | **PUT** /pools/vni-pools/{pool-id} | Update a VNI Pool

# **create_vni_pool**
> VniPool create_vni_pool(body)

Create a new VNI Pool.

Creates a new VNI pool using the specified VNI pool range. The range should be non-overlapping with an existing range. If the range in payload is present or overlaps with an existing range, return code 400 with bad request and an error message is returned mentioning that the given range overlaps with an existing range. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi(swagger_client.ApiClient(configuration))
body = swagger_client.VniPool() # VniPool | 

try:
    # Create a new VNI Pool.
    api_response = api_instance.create_vni_pool(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi->create_vni_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VniPool**](VniPool.md)|  | 

### Return type

[**VniPool**](VniPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vni_pool**
> delete_vni_pool(pool_id, force=force)

Delete a VNI Pool

Deletes the given VNI pool.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi(swagger_client.ApiClient(configuration))
pool_id = 'pool_id_example' # str | VNI pool id
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete a VNI Pool
    api_instance.delete_vni_pool(pool_id, force=force)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi->delete_vni_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| VNI pool id | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vni_pools**
> VniPoolListResult list_vni_pools(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List VNI Pools

Returns information about the default and configured virtual network identifier (VNI) pools for use when building logical network segments. Each virtual network has a unique ID called a VNI. Instead of creating a new VNI each time you need a new logical switch, you can instead allocate a VNI from a VNI pool. VNI pools are sometimes called segment ID pools. Each VNI pool has a range of usable VNIs. By default, there is one pool with two ranges [5000, 65535] and [65536, 75000]. To create multiple smaller pools, specify a smaller range for each pool such as 75001-75100 and 75101-75200. The VNI range determines the maximum number of logical switches that can be created in each network segment. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List VNI Pools
    api_response = api_instance.list_vni_pools(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi->list_vni_pools: %s\n" % e)
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

[**VniPoolListResult**](VniPoolListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_vni_pool**
> VniPool read_vni_pool(pool_id)

Read VNI Pool

Returns information about the specified virtual network identifier (VNI) pool. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi(swagger_client.ApiClient(configuration))
pool_id = 'pool_id_example' # str | VNI pool ID

try:
    # Read VNI Pool
    api_response = api_instance.read_vni_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi->read_vni_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| VNI pool ID | 

### Return type

[**VniPool**](VniPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vni_pool**
> VniPool update_vni_pool(body, pool_id)

Update a VNI Pool

Updates the specified VNI pool. Modifiable parameters include description, display_name and ranges. Ranges can be added, modified or deleted. Overlapping ranges are not allowed. Only range end can be modified for any existing range. Range shrinking or deletion is not allowed if there are any allocated VNIs. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi(swagger_client.ApiClient(configuration))
body = swagger_client.VniPool() # VniPool | 
pool_id = 'pool_id_example' # str | VNI pool ID

try:
    # Update a VNI Pool
    api_response = api_instance.update_vni_pool(body, pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementVNIPoolsApi->update_vni_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VniPool**](VniPool.md)|  | 
 **pool_id** | **str**| VNI pool ID | 

### Return type

[**VniPool**](VniPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

