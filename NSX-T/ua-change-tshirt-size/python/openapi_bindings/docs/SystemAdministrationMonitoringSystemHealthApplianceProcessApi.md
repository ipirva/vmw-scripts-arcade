# swagger_client.SystemAdministrationMonitoringSystemHealthApplianceProcessApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**show_all_appliance_latency_data**](SystemAdministrationMonitoringSystemHealthApplianceProcessApi.md#show_all_appliance_latency_data) | **GET** /systemhealth/appliances/latency/status | Show the details of latency status for all appliances
[**show_all_appliance_process_data**](SystemAdministrationMonitoringSystemHealthApplianceProcessApi.md#show_all_appliance_process_data) | **GET** /systemhealth/appliances/process/status | Show the details of process status in all appliances.
[**show_appliance_latency_data**](SystemAdministrationMonitoringSystemHealthApplianceProcessApi.md#show_appliance_latency_data) | **GET** /systemhealth/appliances/{appliance-id}/latency/status | Show the details of process status in given appliance
[**show_appliance_process_data**](SystemAdministrationMonitoringSystemHealthApplianceProcessApi.md#show_appliance_process_data) | **GET** /systemhealth/appliances/{appliance-id}/process/status | Show the details of process status in given appliance

# **show_all_appliance_latency_data**
> ApplianceLatencyListResult show_all_appliance_latency_data(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Show the details of latency status for all appliances

Show the details of latency status in all appliances. 

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthApplianceProcessApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Show the details of latency status for all appliances
    api_response = api_instance.show_all_appliance_latency_data(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthApplianceProcessApi->show_all_appliance_latency_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ApplianceLatencyListResult**](ApplianceLatencyListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_all_appliance_process_data**
> ApplianceProcessListResult show_all_appliance_process_data(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Show the details of process status in all appliances.

Show the details of process status in all appliances. 

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthApplianceProcessApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Show the details of process status in all appliances.
    api_response = api_instance.show_all_appliance_process_data(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthApplianceProcessApi->show_all_appliance_process_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ApplianceProcessListResult**](ApplianceProcessListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_appliance_latency_data**
> ApplianceLatencyData show_appliance_latency_data(appliance_id)

Show the details of process status in given appliance

Show the details of process status in given appliance. 

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthApplianceProcessApi(swagger_client.ApiClient(configuration))
appliance_id = 'appliance_id_example' # str | 

try:
    # Show the details of process status in given appliance
    api_response = api_instance.show_appliance_latency_data(appliance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthApplianceProcessApi->show_appliance_latency_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_id** | **str**|  | 

### Return type

[**ApplianceLatencyData**](ApplianceLatencyData.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_appliance_process_data**
> ApplianceProcessData show_appliance_process_data(appliance_id)

Show the details of process status in given appliance

Show the details of process status in given appliance. The appliance id can be obtained by below APIs.   1. /api/v1/cluster/nodes   2. /api/v1/systemhealth/appliances/process/status 

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
api_instance = swagger_client.SystemAdministrationMonitoringSystemHealthApplianceProcessApi(swagger_client.ApiClient(configuration))
appliance_id = 'appliance_id_example' # str | 

try:
    # Show the details of process status in given appliance
    api_response = api_instance.show_appliance_process_data(appliance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringSystemHealthApplianceProcessApi->show_appliance_process_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_id** | **str**|  | 

### Return type

[**ApplianceProcessData**](ApplianceProcessData.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

