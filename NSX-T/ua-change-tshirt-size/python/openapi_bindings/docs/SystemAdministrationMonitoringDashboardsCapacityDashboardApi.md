# swagger_client.SystemAdministrationMonitoringDashboardsCapacityDashboardApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_proton_capacity_thresholds**](SystemAdministrationMonitoringDashboardsCapacityDashboardApi.md#get_proton_capacity_thresholds) | **GET** /capacity/threshold | Returns warning threshold(s) set for NSX Objects.
[**get_proton_capacity_usage**](SystemAdministrationMonitoringDashboardsCapacityDashboardApi.md#get_proton_capacity_usage) | **GET** /capacity/usage | Returns capacity usage data for NSX objects
[**update_proton_capacity_thresholds**](SystemAdministrationMonitoringDashboardsCapacityDashboardApi.md#update_proton_capacity_thresholds) | **PUT** /capacity/threshold | Updates the warning threshold(s) for NSX Objects.

# **get_proton_capacity_thresholds**
> CapacityThresholdList get_proton_capacity_thresholds()

Returns warning threshold(s) set for NSX Objects.

Returns warning threshold(s) set for NSX Objects.

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
api_instance = swagger_client.SystemAdministrationMonitoringDashboardsCapacityDashboardApi(swagger_client.ApiClient(configuration))

try:
    # Returns warning threshold(s) set for NSX Objects.
    api_response = api_instance.get_proton_capacity_thresholds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringDashboardsCapacityDashboardApi->get_proton_capacity_thresholds: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CapacityThresholdList**](CapacityThresholdList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_proton_capacity_usage**
> CapacityUsageResponse get_proton_capacity_usage(category=category, cursor=cursor, force=force, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Returns capacity usage data for NSX objects

Returns capacity usage data for NSX objects

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
api_instance = swagger_client.SystemAdministrationMonitoringDashboardsCapacityDashboardApi(swagger_client.ApiClient(configuration))
category = 'category_example' # str |  (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
force = true # bool |  (optional) (default to true)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Returns capacity usage data for NSX objects
    api_response = api_instance.get_proton_capacity_usage(category=category, cursor=cursor, force=force, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringDashboardsCapacityDashboardApi->get_proton_capacity_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **force** | **bool**|  | [optional] [default to true]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**CapacityUsageResponse**](CapacityUsageResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_proton_capacity_thresholds**
> CapacityThresholdList update_proton_capacity_thresholds(body)

Updates the warning threshold(s) for NSX Objects.

Updates the warning threshold(s) for NSX Objects specified, and returns new threshold(s). Threshold list in the request must contain value for GLOBAL_DEFAULT threshold_type which represents global thresholds. 

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
api_instance = swagger_client.SystemAdministrationMonitoringDashboardsCapacityDashboardApi(swagger_client.ApiClient(configuration))
body = swagger_client.CapacityThresholdList() # CapacityThresholdList | 

try:
    # Updates the warning threshold(s) for NSX Objects.
    api_response = api_instance.update_proton_capacity_thresholds(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringDashboardsCapacityDashboardApi->update_proton_capacity_thresholds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CapacityThresholdList**](CapacityThresholdList.md)|  | 

### Return type

[**CapacityThresholdList**](CapacityThresholdList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

