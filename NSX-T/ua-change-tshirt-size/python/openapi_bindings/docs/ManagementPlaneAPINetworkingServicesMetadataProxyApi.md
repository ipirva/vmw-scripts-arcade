# swagger_client.ManagementPlaneAPINetworkingServicesMetadataProxyApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata_proxy**](ManagementPlaneAPINetworkingServicesMetadataProxyApi.md#create_metadata_proxy) | **POST** /md-proxies | Create a metadata proxy
[**delete_metadata_proxy**](ManagementPlaneAPINetworkingServicesMetadataProxyApi.md#delete_metadata_proxy) | **DELETE** /md-proxies/{proxy-id} | Delete a metadata proxy
[**get_metadata_proxy_status**](ManagementPlaneAPINetworkingServicesMetadataProxyApi.md#get_metadata_proxy_status) | **GET** /md-proxies/{proxy-id}/{logical-switch-id}/status | Get Metadata Proxy status with given proxy id and attached logical switch.
[**list_metadata_proxy**](ManagementPlaneAPINetworkingServicesMetadataProxyApi.md#list_metadata_proxy) | **GET** /md-proxies | Get a paginated list of metadata proxies
[**read_metadata_proxy**](ManagementPlaneAPINetworkingServicesMetadataProxyApi.md#read_metadata_proxy) | **GET** /md-proxies/{proxy-id} | Get a metadata proxy
[**update_metadata_proxy**](ManagementPlaneAPINetworkingServicesMetadataProxyApi.md#update_metadata_proxy) | **PUT** /md-proxies/{proxy-id} | Update a metadata proxy

# **create_metadata_proxy**
> MetadataProxy create_metadata_proxy(body)

Create a metadata proxy

Create a metadata proxy

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesMetadataProxyApi(swagger_client.ApiClient(configuration))
body = swagger_client.MetadataProxy() # MetadataProxy | 

try:
    # Create a metadata proxy
    api_response = api_instance.create_metadata_proxy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesMetadataProxyApi->create_metadata_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataProxy**](MetadataProxy.md)|  | 

### Return type

[**MetadataProxy**](MetadataProxy.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata_proxy**
> delete_metadata_proxy(proxy_id)

Delete a metadata proxy

Delete a metadata proxy

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesMetadataProxyApi(swagger_client.ApiClient(configuration))
proxy_id = 'proxy_id_example' # str | 

try:
    # Delete a metadata proxy
    api_instance.delete_metadata_proxy(proxy_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesMetadataProxyApi->delete_metadata_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxy_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_proxy_status**
> MetadataProxyStatus get_metadata_proxy_status(proxy_id, logical_switch_id)

Get Metadata Proxy status with given proxy id and attached logical switch.

Returns the status of the given metadata proxy and attached logical switch. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesMetadataProxyApi(swagger_client.ApiClient(configuration))
proxy_id = 'proxy_id_example' # str | 
logical_switch_id = 'logical_switch_id_example' # str | 

try:
    # Get Metadata Proxy status with given proxy id and attached logical switch.
    api_response = api_instance.get_metadata_proxy_status(proxy_id, logical_switch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesMetadataProxyApi->get_metadata_proxy_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxy_id** | **str**|  | 
 **logical_switch_id** | **str**|  | 

### Return type

[**MetadataProxyStatus**](MetadataProxyStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metadata_proxy**
> MetadataProxyListResult list_metadata_proxy(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get a paginated list of metadata proxies

Get a paginated list of metadata proxies

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesMetadataProxyApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get a paginated list of metadata proxies
    api_response = api_instance.list_metadata_proxy(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesMetadataProxyApi->list_metadata_proxy: %s\n" % e)
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

[**MetadataProxyListResult**](MetadataProxyListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_metadata_proxy**
> MetadataProxy read_metadata_proxy(proxy_id)

Get a metadata proxy

Get a metadata proxy

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesMetadataProxyApi(swagger_client.ApiClient(configuration))
proxy_id = 'proxy_id_example' # str | 

try:
    # Get a metadata proxy
    api_response = api_instance.read_metadata_proxy(proxy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesMetadataProxyApi->read_metadata_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxy_id** | **str**|  | 

### Return type

[**MetadataProxy**](MetadataProxy.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_proxy**
> MetadataProxy update_metadata_proxy(body, proxy_id)

Update a metadata proxy

Update a metadata proxy

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
api_instance = swagger_client.ManagementPlaneAPINetworkingServicesMetadataProxyApi(swagger_client.ApiClient(configuration))
body = swagger_client.MetadataProxy() # MetadataProxy | 
proxy_id = 'proxy_id_example' # str | 

try:
    # Update a metadata proxy
    api_response = api_instance.update_metadata_proxy(body, proxy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingServicesMetadataProxyApi->update_metadata_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetadataProxy**](MetadataProxy.md)|  | 
 **proxy_id** | **str**|  | 

### Return type

[**MetadataProxy**](MetadataProxy.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

