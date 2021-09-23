# swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingInterSiteForwarderApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_l2_forwarder_remote_macs**](ManagementPlaneAPINetworkingLogicalSwitchingInterSiteForwarderApi.md#get_l2_forwarder_remote_macs) | **GET** /logical-switches/{logical-switch-id}/inter-site-forwarder/site-span-info | Get L2 forwarder remote mac addresses
[**get_l2_forwarder_statistics**](ManagementPlaneAPINetworkingLogicalSwitchingInterSiteForwarderApi.md#get_l2_forwarder_statistics) | **GET** /logical-switches/{logical-switch-id}/inter-site-forwarder/statistics | Get L2 forwarder statistics
[**get_l2_forwarder_status**](ManagementPlaneAPINetworkingLogicalSwitchingInterSiteForwarderApi.md#get_l2_forwarder_status) | **GET** /logical-switches/{logical-switch-id}/inter-site-forwarder/status | Get L2 forwarder status

# **get_l2_forwarder_remote_macs**
> L2ForwarderRemoteMacs get_l2_forwarder_remote_macs(logical_switch_id)

Get L2 forwarder remote mac addresses

Returns remote mac addresses of the l2 forwarder on logical switch. It always returns realtime response. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingInterSiteForwarderApi(swagger_client.ApiClient(configuration))
logical_switch_id = 'logical_switch_id_example' # str | 

try:
    # Get L2 forwarder remote mac addresses
    api_response = api_instance.get_l2_forwarder_remote_macs(logical_switch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingInterSiteForwarderApi->get_l2_forwarder_remote_macs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_switch_id** | **str**|  | 

### Return type

[**L2ForwarderRemoteMacs**](L2ForwarderRemoteMacs.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l2_forwarder_statistics**
> L2ForwarderStatistics get_l2_forwarder_statistics(logical_switch_id)

Get L2 forwarder statistics

Returns statistics of the l2 forwarder on logical switch. It always returns realtime response. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingInterSiteForwarderApi(swagger_client.ApiClient(configuration))
logical_switch_id = 'logical_switch_id_example' # str | 

try:
    # Get L2 forwarder statistics
    api_response = api_instance.get_l2_forwarder_statistics(logical_switch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingInterSiteForwarderApi->get_l2_forwarder_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_switch_id** | **str**|  | 

### Return type

[**L2ForwarderStatistics**](L2ForwarderStatistics.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_l2_forwarder_status**
> L2ForwarderStatus get_l2_forwarder_status(logical_switch_id, source=source)

Get L2 forwarder status

Returns status per transport node of the l2 forwarder on logical switch. 

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
api_instance = swagger_client.ManagementPlaneAPINetworkingLogicalSwitchingInterSiteForwarderApi(swagger_client.ApiClient(configuration))
logical_switch_id = 'logical_switch_id_example' # str | 
source = 'source_example' # str | Data source type. (optional)

try:
    # Get L2 forwarder status
    api_response = api_instance.get_l2_forwarder_status(logical_switch_id, source=source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINetworkingLogicalSwitchingInterSiteForwarderApi->get_l2_forwarder_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_switch_id** | **str**|  | 
 **source** | **str**| Data source type. | [optional] 

### Return type

[**L2ForwarderStatus**](L2ForwarderStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

