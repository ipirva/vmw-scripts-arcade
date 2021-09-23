# swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringHealthcheckApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_manual_health_check**](ManagementPlaneAPITroubleshootingAndMonitoringHealthcheckApi.md#create_manual_health_check) | **POST** /manual-health-checks | Create a new manual health check request
[**delete_manual_health_check**](ManagementPlaneAPITroubleshootingAndMonitoringHealthcheckApi.md#delete_manual_health_check) | **DELETE** /manual-health-checks/{manual-health-check-id} | Delete an existing manual health check
[**get_manual_health_check**](ManagementPlaneAPITroubleshootingAndMonitoringHealthcheckApi.md#get_manual_health_check) | **GET** /manual-health-checks/{manual-health-check-id} | Get an existing manual health check
[**list_manual_health_checks**](ManagementPlaneAPITroubleshootingAndMonitoringHealthcheckApi.md#list_manual_health_checks) | **GET** /manual-health-checks | List manual health checks

# **create_manual_health_check**
> ManualHealthCheck create_manual_health_check(body)

Create a new manual health check request

Create a new manual health check request with essential properties. It's disallowed to create new one until the count of in-progress manual health check is less than 50. A manual health check will be deleted automatically after finished for 24 hours. 

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringHealthcheckApi(swagger_client.ApiClient(configuration))
body = swagger_client.ManualHealthCheck() # ManualHealthCheck | 

try:
    # Create a new manual health check request
    api_response = api_instance.create_manual_health_check(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringHealthcheckApi->create_manual_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManualHealthCheck**](ManualHealthCheck.md)|  | 

### Return type

[**ManualHealthCheck**](ManualHealthCheck.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_manual_health_check**
> delete_manual_health_check(manual_health_check_id)

Delete an existing manual health check

Delete an existing manual health check by ID.

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringHealthcheckApi(swagger_client.ApiClient(configuration))
manual_health_check_id = 'manual_health_check_id_example' # str | 

try:
    # Delete an existing manual health check
    api_instance.delete_manual_health_check(manual_health_check_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringHealthcheckApi->delete_manual_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_health_check_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_health_check**
> ManualHealthCheck get_manual_health_check(manual_health_check_id)

Get an existing manual health check

Get an existing manual health check by health check ID.

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringHealthcheckApi(swagger_client.ApiClient(configuration))
manual_health_check_id = 'manual_health_check_id_example' # str | 

try:
    # Get an existing manual health check
    api_response = api_instance.get_manual_health_check(manual_health_check_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringHealthcheckApi->get_manual_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_health_check_id** | **str**|  | 

### Return type

[**ManualHealthCheck**](ManualHealthCheck.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_manual_health_checks**
> ManualHealthCheckListResult list_manual_health_checks(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List manual health checks

Query manual health checks with list parameters. 

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
api_instance = swagger_client.ManagementPlaneAPITroubleshootingAndMonitoringHealthcheckApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List manual health checks
    api_response = api_instance.list_manual_health_checks(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPITroubleshootingAndMonitoringHealthcheckApi->list_manual_health_checks: %s\n" % e)
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

[**ManualHealthCheckListResult**](ManualHealthCheckListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

