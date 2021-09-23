# swagger_client.ManagementPlaneAPINetworkingVPNStatisticsIPSECResetSessionsStatisticsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_ip_sec_vpn_session_statistics_reset**](ManagementPlaneAPINetworkingVPNStatisticsIPSECResetSessionsStatisticsApi.md#reset_ip_sec_vpn_session_statistics_reset) | **POST** /vpn/ipsec/sessions/{session-id}/statistics?action&#x3D;reset | Reset the statistics of the given VPN session

# **reset_ip_sec_vpn_session_statistics_reset**
> reset_ip_sec_vpn_session_statistics_reset(session_id)

Reset the statistics of the given VPN session

Reset the statistics of the given VPN session.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNStatisticsIPSECResetSessionsStatisticsApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 

try:
    # Reset the statistics of the given VPN session
    api_instance.reset_ip_sec_vpn_session_statistics_reset(session_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNStatisticsIPSECResetSessionsStatisticsApi->reset_ip_sec_vpn_session_statistics_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

