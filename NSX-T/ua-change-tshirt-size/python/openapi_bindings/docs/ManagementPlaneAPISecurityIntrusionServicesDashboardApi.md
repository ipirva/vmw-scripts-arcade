# swagger_client.ManagementPlaneAPISecurityIntrusionServicesDashboardApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_affected_users**](ManagementPlaneAPISecurityIntrusionServicesDashboardApi.md#get_affected_users) | **POST** /intrusion-services/affected-users | Get the list of the users affected for that signature
[**get_affected_vms**](ManagementPlaneAPISecurityIntrusionServicesDashboardApi.md#get_affected_vms) | **POST** /intrusion-services/affected-vms | Get the list of the VMs affected for that signature
[**get_all_ids_events**](ManagementPlaneAPISecurityIntrusionServicesDashboardApi.md#get_all_ids_events) | **POST** /intrusion-services/ids-events | Get the list of the IDS events that are detected, grouped by signature id.
[**get_ids_dashboard_summary**](ManagementPlaneAPISecurityIntrusionServicesDashboardApi.md#get_ids_dashboard_summary) | **POST** /intrusion-services/ids-summary | Get the summary of the intrusions that were detected.

# **get_affected_users**
> IdsUserList get_affected_users(body, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get the list of the users affected for that signature

Get the list of the users affected pertaining to a specific signature. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIntrusionServicesDashboardApi(swagger_client.ApiClient(configuration))
body = swagger_client.IDSEventDataRequest() # IDSEventDataRequest | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get the list of the users affected for that signature
    api_response = api_instance.get_affected_users(body, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIntrusionServicesDashboardApi->get_affected_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IDSEventDataRequest**](IDSEventDataRequest.md)|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IdsUserList**](IdsUserList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_affected_vms**
> IdsVmList get_affected_vms(body, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get the list of the VMs affected for that signature

Get the list of the VMs affected pertaining to a specific signature. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIntrusionServicesDashboardApi(swagger_client.ApiClient(configuration))
body = swagger_client.IDSEventDataRequest() # IDSEventDataRequest | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get the list of the VMs affected for that signature
    api_response = api_instance.get_affected_vms(body, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIntrusionServicesDashboardApi->get_affected_vms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IDSEventDataRequest**](IDSEventDataRequest.md)|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IdsVmList**](IdsVmList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ids_events**
> IDSEventsBySignatureResult get_all_ids_events(body)

Get the list of the IDS events that are detected, grouped by signature id.

Get the list of the IDS events that are detected with the total number of intrusions detected, their severity and the time they occurred, grouped by signature id. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIntrusionServicesDashboardApi(swagger_client.ApiClient(configuration))
body = swagger_client.IDSEventDataRequest() # IDSEventDataRequest | 

try:
    # Get the list of the IDS events that are detected, grouped by signature id.
    api_response = api_instance.get_all_ids_events(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIntrusionServicesDashboardApi->get_all_ids_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IDSEventDataRequest**](IDSEventDataRequest.md)|  | 

### Return type

[**IDSEventsBySignatureResult**](IDSEventsBySignatureResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ids_dashboard_summary**
> IDSSummaryListResult get_ids_dashboard_summary(body, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get the summary of the intrusions that were detected.

Get the summary of all the intrusions that are detected grouped by signature with details including signature name, id, severity, attack type, protocol, first and recent occurence, and affected users and VMs. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIntrusionServicesDashboardApi(swagger_client.ApiClient(configuration))
body = swagger_client.IDSEventDataRequest() # IDSEventDataRequest | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get the summary of the intrusions that were detected.
    api_response = api_instance.get_ids_dashboard_summary(body, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIntrusionServicesDashboardApi->get_ids_dashboard_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IDSEventDataRequest**](IDSEventDataRequest.md)|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**IDSSummaryListResult**](IDSSummaryListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

