# swagger_client.ManagementPlaneAPINetworkingVPNStatisticsL2VPNRemoteMACSApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_l2_vpn_session_remote_macs_for_ls**](ManagementPlaneAPINetworkingVPNStatisticsL2VPNRemoteMACSApi.md#get_l2_vpn_session_remote_macs_for_ls) | **GET** /vpn/l2vpn/sessions/{session-id}/remote-mac | Get L2VPN session remote mac for logical switch

# **get_l2_vpn_session_remote_macs_for_ls**
> L2VPNSessionRemoteMacs get_l2_vpn_session_remote_macs_for_ls(session_id, logical_switch_id=logical_switch_id)

Get L2VPN session remote mac for logical switch

Get L2VPN session remote mac for logical switch.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNStatisticsL2VPNRemoteMACSApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | 
logical_switch_id = 'logical_switch_id_example' # str | logical switch identifier (optional)

try:
    # Get L2VPN session remote mac for logical switch
    api_response = api_instance.get_l2_vpn_session_remote_macs_for_ls(session_id, logical_switch_id=logical_switch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNStatisticsL2VPNRemoteMACSApi->get_l2_vpn_session_remote_macs_for_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **logical_switch_id** | **str**| logical switch identifier | [optional] 

### Return type

[**L2VPNSessionRemoteMacs**](L2VPNSessionRemoteMacs.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

