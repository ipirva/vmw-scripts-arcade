# swagger_client.ManagementPlaneAPIGroupingObjectsIPSetsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_remove_ip_address**](ManagementPlaneAPIGroupingObjectsIPSetsApi.md#add_remove_ip_address) | **POST** /ip-sets/{ip-set-id} | Add a IP address to a IPSet
[**create_mac_set**](ManagementPlaneAPIGroupingObjectsIPSetsApi.md#create_mac_set) | **POST** /mac-sets | Create MACSet
[**delete_ip_set**](ManagementPlaneAPIGroupingObjectsIPSetsApi.md#delete_ip_set) | **DELETE** /ip-sets/{ip-set-id} | Delete IPSet
[**get_ip_addresses**](ManagementPlaneAPIGroupingObjectsIPSetsApi.md#get_ip_addresses) | **GET** /ip-sets/{ip-set-id}/members | Get all IPAddresses in a IPSet
[**list_ip_sets**](ManagementPlaneAPIGroupingObjectsIPSetsApi.md#list_ip_sets) | **GET** /ip-sets | List IPSets
[**read_ip_set**](ManagementPlaneAPIGroupingObjectsIPSetsApi.md#read_ip_set) | **GET** /ip-sets/{ip-set-id} | Read IPSet
[**update_ip_set**](ManagementPlaneAPIGroupingObjectsIPSetsApi.md#update_ip_set) | **PUT** /ip-sets/{ip-set-id} | Update IPSet

# **add_remove_ip_address**
> IPAddressElement add_remove_ip_address(body, action, ip_set_id)

Add a IP address to a IPSet

Add/Remove an individual IP address to an IPSet 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsIPSetsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPAddressElement() # IPAddressElement | 
action = 'action_example' # str | Specifies addition or removal action
ip_set_id = 'ip_set_id_example' # str | IP Set Id

try:
    # Add a IP address to a IPSet
    api_response = api_instance.add_remove_ip_address(body, action, ip_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsIPSetsApi->add_remove_ip_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPAddressElement**](IPAddressElement.md)|  | 
 **action** | **str**| Specifies addition or removal action | 
 **ip_set_id** | **str**| IP Set Id | 

### Return type

[**IPAddressElement**](IPAddressElement.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mac_set**
> MACSet create_mac_set(body)

Create MACSet

Creates a new MACSet that can group individual MAC addresses. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsIPSetsApi(swagger_client.ApiClient(configuration))
body = swagger_client.MACSet() # MACSet | 

try:
    # Create MACSet
    api_response = api_instance.create_mac_set(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsIPSetsApi->create_mac_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MACSet**](MACSet.md)|  | 

### Return type

[**MACSet**](MACSet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_set**
> delete_ip_set(ip_set_id, force=force)

Delete IPSet

Deletes the specified IPSet.  By default, if the IPSet is added to an NSGroup, it won't be deleted. In such situations, pass \"force=true\" as query param to force delete the IPSet. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsIPSetsApi(swagger_client.ApiClient(configuration))
ip_set_id = 'ip_set_id_example' # str | IPSet Id
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete IPSet
    api_instance.delete_ip_set(ip_set_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsIPSetsApi->delete_ip_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_set_id** | **str**| IPSet Id | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_addresses**
> IPAddressElementListResult get_ip_addresses(ip_set_id)

Get all IPAddresses in a IPSet

List all IP addresses in a IPSet 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsIPSetsApi(swagger_client.ApiClient(configuration))
ip_set_id = 'ip_set_id_example' # str | IP Set Id

try:
    # Get all IPAddresses in a IPSet
    api_response = api_instance.get_ip_addresses(ip_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsIPSetsApi->get_ip_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_set_id** | **str**| IP Set Id | 

### Return type

[**IPAddressElementListResult**](IPAddressElementListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_sets**
> IPSetListResult list_ip_sets(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List IPSets

Returns paginated list of IPSets 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsIPSetsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List IPSets
    api_response = api_instance.list_ip_sets(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsIPSetsApi->list_ip_sets: %s\n" % e)
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

[**IPSetListResult**](IPSetListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ip_set**
> IPSet read_ip_set(ip_set_id)

Read IPSet

Returns information about the specified IPSet 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsIPSetsApi(swagger_client.ApiClient(configuration))
ip_set_id = 'ip_set_id_example' # str | IPSet Id

try:
    # Read IPSet
    api_response = api_instance.read_ip_set(ip_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsIPSetsApi->read_ip_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_set_id** | **str**| IPSet Id | 

### Return type

[**IPSet**](IPSet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_set**
> IPSet update_ip_set(body, ip_set_id)

Update IPSet

Updates the specified IPSet. Modifiable parameters include description, display_name and ip_addresses. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsIPSetsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IPSet() # IPSet | 
ip_set_id = 'ip_set_id_example' # str | IPSet Id

try:
    # Update IPSet
    api_response = api_instance.update_ip_set(body, ip_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsIPSetsApi->update_ip_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPSet**](IPSet.md)|  | 
 **ip_set_id** | **str**| IPSet Id | 

### Return type

[**IPSet**](IPSet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

