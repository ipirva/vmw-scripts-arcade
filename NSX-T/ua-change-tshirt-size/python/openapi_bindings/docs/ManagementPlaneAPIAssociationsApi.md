# swagger_client.ManagementPlaneAPIAssociationsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_associations**](ManagementPlaneAPIAssociationsApi.md#get_associations) | **GET** /associations | Get ResourceReference objects to which the given resource belongs to 

# **get_associations**
> AssociationListResult get_associations(associated_resource_type, resource_id, resource_type, cursor=cursor, fetch_ancestors=fetch_ancestors, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get ResourceReference objects to which the given resource belongs to 

Returns information about resources that are associated with the given resource. Id and type of the resource for which associated resources are to be fetched are to be specified as query parameter in the URI. Resource type of the associated resources must be specified as query parameter. 

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
api_instance = swagger_client.ManagementPlaneAPIAssociationsApi(swagger_client.ApiClient(configuration))
associated_resource_type = 'associated_resource_type_example' # str | Resource type valid for use as target in association API
resource_id = 'resource_id_example' # str | The resource for which associated resources are to be fetched
resource_type = 'resource_type_example' # str | Resource type valid for use as source in association API
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
fetch_ancestors = false # bool | Fetch complete list of associated resources considering containment and nesting  (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get ResourceReference objects to which the given resource belongs to 
    api_response = api_instance.get_associations(associated_resource_type, resource_id, resource_type, cursor=cursor, fetch_ancestors=fetch_ancestors, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIAssociationsApi->get_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **associated_resource_type** | **str**| Resource type valid for use as target in association API | 
 **resource_id** | **str**| The resource for which associated resources are to be fetched | 
 **resource_type** | **str**| Resource type valid for use as source in association API | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **fetch_ancestors** | **bool**| Fetch complete list of associated resources considering containment and nesting  | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**AssociationListResult**](AssociationListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

