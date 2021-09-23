# swagger_client.ManagementPlaneAPIServicesDNSApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dns_forwarder_statistics**](ManagementPlaneAPIServicesDNSApi.md#get_dns_forwarder_statistics) | **GET** /dns/forwarders/{forwarder-id}/statistics | Get statistics of given dns forwarder

# **get_dns_forwarder_statistics**
> DnsForwarderStatistics get_dns_forwarder_statistics(forwarder_id)

Get statistics of given dns forwarder

Returns the statistics of the given dns forwarder specified by forwarder id. 

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
api_instance = swagger_client.ManagementPlaneAPIServicesDNSApi(swagger_client.ApiClient(configuration))
forwarder_id = 'forwarder_id_example' # str | 

try:
    # Get statistics of given dns forwarder
    api_response = api_instance.get_dns_forwarder_statistics(forwarder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIServicesDNSApi->get_dns_forwarder_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forwarder_id** | **str**|  | 

### Return type

[**DnsForwarderStatistics**](DnsForwarderStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

