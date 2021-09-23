# swagger_client.SystemAdministrationConfigurationFabricPoolManagementVTEPLabelPoolsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_vtep_label_pools**](SystemAdministrationConfigurationFabricPoolManagementVTEPLabelPoolsApi.md#list_vtep_label_pools) | **GET** /pools/vtep-label-pools | List virtual tunnel endpoint Label Pools
[**read_vtep_label_pool**](SystemAdministrationConfigurationFabricPoolManagementVTEPLabelPoolsApi.md#read_vtep_label_pool) | **GET** /pools/vtep-label-pools/{pool-id} | Read a virtual tunnel endpoint label pool

# **list_vtep_label_pools**
> VtepLabelPoolListResult list_vtep_label_pools(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List virtual tunnel endpoint Label Pools

Returns a list of all virtual tunnel endpoint label pools 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementVTEPLabelPoolsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List virtual tunnel endpoint Label Pools
    api_response = api_instance.list_vtep_label_pools(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementVTEPLabelPoolsApi->list_vtep_label_pools: %s\n" % e)
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

[**VtepLabelPoolListResult**](VtepLabelPoolListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_vtep_label_pool**
> VtepLabelPool read_vtep_label_pool(pool_id)

Read a virtual tunnel endpoint label pool

Returns information about the specified virtual tunnel endpoint label pool. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricPoolManagementVTEPLabelPoolsApi(swagger_client.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Virtual tunnel endpoint label pool ID

try:
    # Read a virtual tunnel endpoint label pool
    api_response = api_instance.read_vtep_label_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricPoolManagementVTEPLabelPoolsApi->read_vtep_label_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Virtual tunnel endpoint label pool ID | 

### Return type

[**VtepLabelPool**](VtepLabelPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

