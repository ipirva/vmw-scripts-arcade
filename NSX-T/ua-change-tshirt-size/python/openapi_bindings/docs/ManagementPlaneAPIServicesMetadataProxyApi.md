# swagger_client.ManagementPlaneAPIServicesMetadataProxyApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metadata_proxy_statistics**](ManagementPlaneAPIServicesMetadataProxyApi.md#get_metadata_proxy_statistics) | **GET** /md-proxies/{proxy-id}/statistics | Get Metadata Proxy statistics with given proxy id

# **get_metadata_proxy_statistics**
> MetadataProxyStatistics get_metadata_proxy_statistics(proxy_id, logical_switch_id=logical_switch_id, source=source)

Get Metadata Proxy statistics with given proxy id

Returns the statistics of the given metatada proxy. If no logical switch is provided, all staticstics of all the logical switches the proxy was attached will be returned. 

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
api_instance = swagger_client.ManagementPlaneAPIServicesMetadataProxyApi(swagger_client.ApiClient(configuration))
proxy_id = 'proxy_id_example' # str | 
logical_switch_id = 'logical_switch_id_example' # str | The uuid of logical switch (optional)
source = 'source_example' # str | Data source type. (optional)

try:
    # Get Metadata Proxy statistics with given proxy id
    api_response = api_instance.get_metadata_proxy_statistics(proxy_id, logical_switch_id=logical_switch_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIServicesMetadataProxyApi->get_metadata_proxy_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxy_id** | **str**|  | 
 **logical_switch_id** | **str**| The uuid of logical switch | [optional] 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**MetadataProxyStatistics**](MetadataProxyStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

