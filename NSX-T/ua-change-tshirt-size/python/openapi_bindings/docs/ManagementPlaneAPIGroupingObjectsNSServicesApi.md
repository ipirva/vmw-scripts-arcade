# swagger_client.ManagementPlaneAPIGroupingObjectsNSServicesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ns_service_group**](ManagementPlaneAPIGroupingObjectsNSServicesApi.md#create_ns_service_group) | **POST** /ns-service-groups | Create NSServiceGroup
[**delete_ns_service**](ManagementPlaneAPIGroupingObjectsNSServicesApi.md#delete_ns_service) | **DELETE** /ns-services/{ns-service-id} | Delete NSService
[**list_ns_services**](ManagementPlaneAPIGroupingObjectsNSServicesApi.md#list_ns_services) | **GET** /ns-services | List all NSServices
[**read_ns_service**](ManagementPlaneAPIGroupingObjectsNSServicesApi.md#read_ns_service) | **GET** /ns-services/{ns-service-id} | Read NSService
[**update_ns_service**](ManagementPlaneAPIGroupingObjectsNSServicesApi.md#update_ns_service) | **PUT** /ns-services/{ns-service-id} | Update NSService

# **create_ns_service_group**
> NSServiceGroup create_ns_service_group(body)

Create NSServiceGroup

Creates a new NSServiceGroup which can contain NSServices. A given NSServiceGroup can contain either only ether type of NSServices or only non-ether type of NSServices, i.e. an NSServiceGroup cannot contain a mix of both ether and non-ether types of NSServices. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.NSServiceGroup() # NSServiceGroup | 

try:
    # Create NSServiceGroup
    api_response = api_instance.create_ns_service_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSServicesApi->create_ns_service_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NSServiceGroup**](NSServiceGroup.md)|  | 

### Return type

[**NSServiceGroup**](NSServiceGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ns_service**
> delete_ns_service(ns_service_id, force=force)

Delete NSService

Deletes the specified NSService. By default, if the NSService is being referred in an NSServiceGroup, it can't be deleted. In such situations, pass \"force=true\" as a parameter to force delete the NSService. System defined NSServices can't be deleted using \"force\" flag. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSServicesApi(swagger_client.ApiClient(configuration))
ns_service_id = 'ns_service_id_example' # str | NSService Id
force = false # bool | Force delete the resource even if it is being used somewhere  (optional) (default to false)

try:
    # Delete NSService
    api_instance.delete_ns_service(ns_service_id, force=force)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSServicesApi->delete_ns_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_service_id** | **str**| NSService Id | 
 **force** | **bool**| Force delete the resource even if it is being used somewhere  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ns_services**
> NSServiceListResult list_ns_services(cursor=cursor, default_service=default_service, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List all NSServices

Returns paginated list of NSServices 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSServicesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
default_service = true # bool | Fetch all default NSServices (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List all NSServices
    api_response = api_instance.list_ns_services(cursor=cursor, default_service=default_service, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSServicesApi->list_ns_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **default_service** | **bool**| Fetch all default NSServices | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**NSServiceListResult**](NSServiceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ns_service**
> NSService read_ns_service(ns_service_id)

Read NSService

Returns information about the specified NSService 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSServicesApi(swagger_client.ApiClient(configuration))
ns_service_id = 'ns_service_id_example' # str | NSService Id

try:
    # Read NSService
    api_response = api_instance.read_ns_service(ns_service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSServicesApi->read_ns_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_service_id** | **str**| NSService Id | 

### Return type

[**NSService**](NSService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ns_service**
> NSService update_ns_service(body, ns_service_id)

Update NSService

Updates the specified NSService. Modifiable parameters include the description, display_name and the NSService element. The system defined NSServices can't be modified 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNSServicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.NSService() # NSService | 
ns_service_id = 'ns_service_id_example' # str | NSService Id

try:
    # Update NSService
    api_response = api_instance.update_ns_service(body, ns_service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNSServicesApi->update_ns_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NSService**](NSService.md)|  | 
 **ns_service_id** | **str**| NSService Id | 

### Return type

[**NSService**](NSService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

