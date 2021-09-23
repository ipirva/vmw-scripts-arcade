# swagger_client.SystemAdministrationLifecycleManagementMigrationFeedbackApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_recommended_value_in_feedback_accept_recommended**](SystemAdministrationLifecycleManagementMigrationFeedbackApi.md#accept_recommended_value_in_feedback_accept_recommended) | **POST** /migration/feedback-response?action&#x3D;accept-recommended | Accept default action for feedbacks
[**get_feedback_requests**](SystemAdministrationLifecycleManagementMigrationFeedbackApi.md#get_feedback_requests) | **GET** /migration/feedback-requests | NSX-V feedback details
[**get_feedback_summary**](SystemAdministrationLifecycleManagementMigrationFeedbackApi.md#get_feedback_summary) | **GET** /migration/feedback-summary | Feedback request summary
[**get_grouped_feedback_requests**](SystemAdministrationLifecycleManagementMigrationFeedbackApi.md#get_grouped_feedback_requests) | **GET** /migration/grouped-feedback-requests | NSX-V feedback details
[**update_feedback_response**](SystemAdministrationLifecycleManagementMigrationFeedbackApi.md#update_feedback_response) | **PUT** /migration/feedback-response | Migration feedback response

# **accept_recommended_value_in_feedback_accept_recommended**
> accept_recommended_value_in_feedback_accept_recommended()

Accept default action for feedbacks

Pick default resolution for all feedback items. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationFeedbackApi(swagger_client.ApiClient(configuration))

try:
    # Accept default action for feedbacks
    api_instance.accept_recommended_value_in_feedback_accept_recommended()
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationFeedbackApi->accept_recommended_value_in_feedback_accept_recommended: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feedback_requests**
> MigrationFeedbackRequestListResult get_feedback_requests(category=category, cursor=cursor, hash=hash, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, state=state, sub_category=sub_category)

NSX-V feedback details

Get feedback details of NSX-V to be migrated. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationFeedbackApi(swagger_client.ApiClient(configuration))
category = 'category_example' # str | Category on which feedback request should be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
hash = 'hash_example' # str | Hash based on which feedback request should be filtered (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
state = 'ALL' # str | Filter based on current state of the feedback request (optional) (default to ALL)
sub_category = 'sub_category_example' # str | Sub category based on which feedback request should be filtered (optional)

try:
    # NSX-V feedback details
    api_response = api_instance.get_feedback_requests(category=category, cursor=cursor, hash=hash, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, state=state, sub_category=sub_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationFeedbackApi->get_feedback_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Category on which feedback request should be filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **hash** | **str**| Hash based on which feedback request should be filtered | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **state** | **str**| Filter based on current state of the feedback request | [optional] [default to ALL]
 **sub_category** | **str**| Sub category based on which feedback request should be filtered | [optional] 

### Return type

[**MigrationFeedbackRequestListResult**](MigrationFeedbackRequestListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feedback_summary**
> MigrationFeedbackSummaryListResult get_feedback_summary(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Feedback request summary

Get feedback summary of NSX-V to be migrated. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationFeedbackApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Feedback request summary
    api_response = api_instance.get_feedback_summary(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationFeedbackApi->get_feedback_summary: %s\n" % e)
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

[**MigrationFeedbackSummaryListResult**](MigrationFeedbackSummaryListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grouped_feedback_requests**
> GroupedMigrationFeedbackRequestListResult get_grouped_feedback_requests(category=category, cursor=cursor, hash=hash, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, state=state, sub_category=sub_category)

NSX-V feedback details

Get feedback details of NSX-V to be migrated, grouped by feedback type. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationFeedbackApi(swagger_client.ApiClient(configuration))
category = 'category_example' # str | Category on which feedback request should be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
hash = 'hash_example' # str | Hash based on which feedback request should be filtered (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
state = 'ALL' # str | Filter based on current state of the feedback request (optional) (default to ALL)
sub_category = 'sub_category_example' # str | Sub category based on which feedback request should be filtered (optional)

try:
    # NSX-V feedback details
    api_response = api_instance.get_grouped_feedback_requests(category=category, cursor=cursor, hash=hash, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, state=state, sub_category=sub_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationFeedbackApi->get_grouped_feedback_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**| Category on which feedback request should be filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **hash** | **str**| Hash based on which feedback request should be filtered | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **state** | **str**| Filter based on current state of the feedback request | [optional] [default to ALL]
 **sub_category** | **str**| Sub category based on which feedback request should be filtered | [optional] 

### Return type

[**GroupedMigrationFeedbackRequestListResult**](GroupedMigrationFeedbackRequestListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_feedback_response**
> update_feedback_response(body)

Migration feedback response

Provide response for feedback queries needed for migration. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationFeedbackApi(swagger_client.ApiClient(configuration))
body = swagger_client.MigrationFeedbackResponseList() # MigrationFeedbackResponseList | 

try:
    # Migration feedback response
    api_instance.update_feedback_response(body)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationFeedbackApi->update_feedback_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrationFeedbackResponseList**](MigrationFeedbackResponseList.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

