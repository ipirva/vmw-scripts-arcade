# swagger_client.ManagementPlaneAPINetworkingVPNStatisticsIPSECSessionsSummaryApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ip_sec_vpn_session_summary**](ManagementPlaneAPINetworkingVPNStatisticsIPSECSessionsSummaryApi.md#get_ip_sec_vpn_session_summary) | **GET** /vpn/ipsec/sessions/summary | VPN session summary

# **get_ip_sec_vpn_session_summary**
> IPSecVPNSessionSummary get_ip_sec_vpn_session_summary(site_id=site_id, source=source)

VPN session summary

VPN session summary gets summary per vpn sessions and IKE session. Query parameter source supports only cached mode.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNStatisticsIPSECSessionsSummaryApi(swagger_client.ApiClient(configuration))
site_id = 'site_id_example' # str | Peer site id (optional)
source = 'source_example' # str | Data source type. (optional)

try:
    # VPN session summary
    api_response = api_instance.get_ip_sec_vpn_session_summary(site_id=site_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNStatisticsIPSECSessionsSummaryApi->get_ip_sec_vpn_session_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Peer site id | [optional] 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**IPSecVPNSessionSummary**](IPSecVPNSessionSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

