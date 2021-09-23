# swagger_client.ManagementPlaneAPINetworkingVPNStatisticsIKESessionsStatusApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ip_sec_vpnike_session_status**](ManagementPlaneAPINetworkingVPNStatisticsIKESessionsStatusApi.md#get_ip_sec_vpnike_session_status) | **GET** /vpn/ipsec/sessions/{session-id}/status | Get IPSec VPN IKE session status

# **get_ip_sec_vpnike_session_status**
> IPSecVPNSessionStatus get_ip_sec_vpnike_session_status(session_id, source=source)

Get IPSec VPN IKE session status

List status of IPSec session. Query parameter source supports both realtime and cached mode.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNStatisticsIKESessionsStatusApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get IPSec VPN IKE session status
    api_response = api_instance.get_ip_sec_vpnike_session_status(session_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNStatisticsIKESessionsStatusApi->get_ip_sec_vpnike_session_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**IPSecVPNSessionStatus**](IPSecVPNSessionStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

