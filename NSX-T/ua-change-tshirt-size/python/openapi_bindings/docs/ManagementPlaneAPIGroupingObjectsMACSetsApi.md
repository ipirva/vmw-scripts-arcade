# swagger_client.ManagementPlaneAPIGroupingObjectsMACSetsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_mac_address**](ManagementPlaneAPIGroupingObjectsMACSetsApi.md#add_mac_address) | **POST** /mac-sets/{mac-set-id}/members | Add a MAC address to a MACSet
[**delete_mac_set**](ManagementPlaneAPIGroupingObjectsMACSetsApi.md#delete_mac_set) | **DELETE** /mac-sets/{mac-set-id} | Delete MACSet
[**get_mac_addresses**](ManagementPlaneAPIGroupingObjectsMACSetsApi.md#get_mac_addresses) | **GET** /mac-sets/{mac-set-id}/members | Get all MACAddresses in a MACSet
[**list_mac_sets**](ManagementPlaneAPIGroupingObjectsMACSetsApi.md#list_mac_sets) | **GET** /mac-sets | List MACSets
[**read_mac_set**](ManagementPlaneAPIGroupingObjectsMACSetsApi.md#read_mac_set) | **GET** /mac-sets/{mac-set-id} | Read MACSet
[**remove_mac_address**](ManagementPlaneAPIGroupingObjectsMACSetsApi.md#remove_mac_address) | **DELETE** /mac-sets/{mac-set-id}/members/{mac-address} | Remove a MAC address from given MACSet
[**update_mac_set**](ManagementPlaneAPIGroupingObjectsMACSetsApi.md#update_mac_set) | **PUT** /mac-sets/{mac-set-id} | Update MACSet

# **add_mac_address**
> MACAddressElement add_mac_address(body, mac_set_id)

Add a MAC address to a MACSet

Add an individual MAC address to a MACSet 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsMACSetsApi(swagger_client.ApiClient(configuration))
body = swagger_client.MACAddressElement() # MACAddressElement | 
mac_set_id = 'mac_set_id_example' # str | MAC Set Id

try:
    # Add a MAC address to a MACSet
    api_response = api_instance.add_mac_address(body, mac_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsMACSetsApi->add_mac_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MACAddressElement**](MACAddressElement.md)|  | 
 **mac_set_id** | **str**| MAC Set Id | 

### Return type

[**MACAddressElement**](MACAddressElement.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mac_set**
> delete_mac_set(mac_set_id, force=force)

Delete MACSet

Deletes the specified MACSet. By default, if the MACSet is added to an NSGroup, it won't be deleted. In such situations, pass \"force=true\" as query param to force delete the MACSet. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsMACSetsApi(swagger_client.ApiClient(configuration))
mac_set_id = 'mac_set_id_example' # str | MACSet Id
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete MACSet
    api_instance.delete_mac_set(mac_set_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsMACSetsApi->delete_mac_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac_set_id** | **str**| MACSet Id | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mac_addresses**
> MACAddressElementListResult get_mac_addresses(mac_set_id)

Get all MACAddresses in a MACSet

List all MAC addresses in a MACSet 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsMACSetsApi(swagger_client.ApiClient(configuration))
mac_set_id = 'mac_set_id_example' # str | MAC Set Id

try:
    # Get all MACAddresses in a MACSet
    api_response = api_instance.get_mac_addresses(mac_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsMACSetsApi->get_mac_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac_set_id** | **str**| MAC Set Id | 

### Return type

[**MACAddressElementListResult**](MACAddressElementListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mac_sets**
> MACSetListResult list_mac_sets(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List MACSets

Returns paginated list of MACSets 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsMACSetsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List MACSets
    api_response = api_instance.list_mac_sets(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsMACSetsApi->list_mac_sets: %s\n" % e)
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

[**MACSetListResult**](MACSetListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_mac_set**
> MACSet read_mac_set(mac_set_id)

Read MACSet

Returns information about the specified MACSet 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsMACSetsApi(swagger_client.ApiClient(configuration))
mac_set_id = 'mac_set_id_example' # str | MACSet Id

try:
    # Read MACSet
    api_response = api_instance.read_mac_set(mac_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsMACSetsApi->read_mac_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac_set_id** | **str**| MACSet Id | 

### Return type

[**MACSet**](MACSet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_mac_address**
> remove_mac_address(mac_set_id, mac_address)

Remove a MAC address from given MACSet

Remove an individual MAC address from a MACSet 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsMACSetsApi(swagger_client.ApiClient(configuration))
mac_set_id = 'mac_set_id_example' # str | MACSet Id
mac_address = 'mac_address_example' # str | MAC address to be removed

try:
    # Remove a MAC address from given MACSet
    api_instance.remove_mac_address(mac_set_id, mac_address)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsMACSetsApi->remove_mac_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac_set_id** | **str**| MACSet Id | 
 **mac_address** | **str**| MAC address to be removed | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mac_set**
> MACSet update_mac_set(body, mac_set_id)

Update MACSet

Updates the specified MACSet. Modifiable parameters include the description, display_name and mac_addresses. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsMACSetsApi(swagger_client.ApiClient(configuration))
body = swagger_client.MACSet() # MACSet | 
mac_set_id = 'mac_set_id_example' # str | MACSet Id

try:
    # Update MACSet
    api_response = api_instance.update_mac_set(body, mac_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsMACSetsApi->update_mac_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MACSet**](MACSet.md)|  | 
 **mac_set_id** | **str**| MACSet Id | 

### Return type

[**MACSet**](MACSet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

