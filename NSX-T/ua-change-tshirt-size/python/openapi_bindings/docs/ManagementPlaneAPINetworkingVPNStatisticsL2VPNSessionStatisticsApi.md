# swagger_client.ManagementPlaneAPINetworkingVPNStatisticsL2VPNSessionStatisticsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_l2_vpn_session_statistics**](ManagementPlaneAPINetworkingVPNStatisticsL2VPNSessionStatisticsApi.md#get_l2_vpn_session_statistics) | **GET** /vpn/l2vpn/sessions/{session-id}/statistics | Get L2VPN session statistics

# **get_l2_vpn_session_statistics**
> L2VPNSessionStatistics get_l2_vpn_session_statistics(session_id, source=source)

Get L2VPN session statistics

Get statistics of a L2VPN session. Query parameter source=realtime is the only supported source.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNStatisticsL2VPNSessionStatisticsApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get L2VPN session statistics
    api_response = api_instance.get_l2_vpn_session_statistics(session_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNStatisticsL2VPNSessionStatisticsApi->get_l2_vpn_session_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**L2VPNSessionStatistics**](L2VPNSessionStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

