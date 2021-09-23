# swagger_client.ManagementPlaneAPINormalizationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_normalizations**](ManagementPlaneAPINormalizationApi.md#get_normalizations) | **GET** /normalizations | Get normalizations based on the query parameters

# **get_normalizations**
> NormalizedResourceListResult get_normalizations(preferred_normalization_type, resource_id, resource_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get normalizations based on the query parameters

Returns the list of normalized resources based on the query parameters. Id and Type of the resource on which the normalizations is to be performed, are to be specified as query parameters in the URI. The target resource types to which normalization is to be done should also be specified as query parameter. 

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
api_instance = swagger_client.ManagementPlaneAPINormalizationApi(swagger_client.ApiClient(configuration))
preferred_normalization_type = 'preferred_normalization_type_example' # str | Resource type valid for use as target in normalization API.
resource_id = 'resource_id_example' # str | Identifier of the resource on which normalization is to be performed
resource_type = 'resource_type_example' # str | Resource type valid for use as source in normalization API.
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get normalizations based on the query parameters
    api_response = api_instance.get_normalizations(preferred_normalization_type, resource_id, resource_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINormalizationApi->get_normalizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preferred_normalization_type** | **str**| Resource type valid for use as target in normalization API. | 
 **resource_id** | **str**| Identifier of the resource on which normalization is to be performed | 
 **resource_type** | **str**| Resource type valid for use as source in normalization API. | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**NormalizedResourceListResult**](NormalizedResourceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

