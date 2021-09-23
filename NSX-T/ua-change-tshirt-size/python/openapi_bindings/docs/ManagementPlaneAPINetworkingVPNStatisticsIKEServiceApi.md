# swagger_client.ManagementPlaneAPINetworkingVPNStatisticsIKEServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ip_sec_vpnike_service**](ManagementPlaneAPINetworkingVPNStatisticsIKEServiceApi.md#get_ip_sec_vpnike_service) | **GET** /vpn/services/{service-id}/summary | Cumulative statistics for one IKE service instance

# **get_ip_sec_vpnike_service**
> IPSecVPNIKEServiceSummary get_ip_sec_vpnike_service(service_id, source=source)

Cumulative statistics for one IKE service instance

Cumulative statistics for one IKE service instance. Query parameter source supports only cached mode.

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
api_instance = swagger_client.ManagementPlaneAPINetworkingVPNStatisticsIKEServiceApi(swagger_client.ApiClient(configuration))
service_id = 'service_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Cumulative statistics for one IKE service instance
    api_response = api_instance.get_ip_sec_vpnike_service(service_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingVPNStatisticsIKEServiceApi->get_ip_sec_vpnike_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**IPSecVPNIKEServiceSummary**](IPSecVPNIKEServiceSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

