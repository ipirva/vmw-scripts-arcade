# swagger_client.SystemAdministrationMonitoringHealthChecksApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_automatic_health_check**](SystemAdministrationMonitoringHealthChecksApi.md#get_automatic_health_check) | **GET** /automatic-health-checks/transport-zones/{transport-zone-id} | Get an automatic health check
[**get_automatic_health_check_toggle**](SystemAdministrationMonitoringHealthChecksApi.md#get_automatic_health_check_toggle) | **GET** /automatic-health-check-toggle | Get automatic health check toggle
[**list_automatic_health_checks**](SystemAdministrationMonitoringHealthChecksApi.md#list_automatic_health_checks) | **GET** /automatic-health-checks | List automatic health checks
[**update_automatic_health_check_toggle**](SystemAdministrationMonitoringHealthChecksApi.md#update_automatic_health_check_toggle) | **PUT** /automatic-health-check-toggle | Update automatic health check toggle

# **get_automatic_health_check**
> AutomaticHealthCheck get_automatic_health_check(transport_zone_id)

Get an automatic health check

Get health check performed by system automatically for specific transport zone. 

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
api_instance = swagger_client.SystemAdministrationMonitoringHealthChecksApi(swagger_client.ApiClient(configuration))
transport_zone_id = 'transport_zone_id_example' # str | 

try:
    # Get an automatic health check
    api_response = api_instance.get_automatic_health_check(transport_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringHealthChecksApi->get_automatic_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_zone_id** | **str**|  | 

### Return type

[**AutomaticHealthCheck**](AutomaticHealthCheck.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_automatic_health_check_toggle**
> AutomaticHealthCheckToggle get_automatic_health_check_toggle()

Get automatic health check toggle

Get detailed info for automatic health check toggle.

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
api_instance = swagger_client.SystemAdministrationMonitoringHealthChecksApi(swagger_client.ApiClient(configuration))

try:
    # Get automatic health check toggle
    api_response = api_instance.get_automatic_health_check_toggle()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringHealthChecksApi->get_automatic_health_check_toggle: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AutomaticHealthCheckToggle**](AutomaticHealthCheckToggle.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_automatic_health_checks**
> AutomaticHealthCheckListResult list_automatic_health_checks(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List automatic health checks

Query automatic health checks with list parameters. 

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
api_instance = swagger_client.SystemAdministrationMonitoringHealthChecksApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List automatic health checks
    api_response = api_instance.list_automatic_health_checks(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringHealthChecksApi->list_automatic_health_checks: %s\n" % e)
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

[**AutomaticHealthCheckListResult**](AutomaticHealthCheckListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_automatic_health_check_toggle**
> AutomaticHealthCheckToggle update_automatic_health_check_toggle(body)

Update automatic health check toggle

Change status of automatic health check toggle to enabled/disabled.

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
api_instance = swagger_client.SystemAdministrationMonitoringHealthChecksApi(swagger_client.ApiClient(configuration))
body = swagger_client.AutomaticHealthCheckToggle() # AutomaticHealthCheckToggle | 

try:
    # Update automatic health check toggle
    api_response = api_instance.update_automatic_health_check_toggle(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringHealthChecksApi->update_automatic_health_check_toggle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AutomaticHealthCheckToggle**](AutomaticHealthCheckToggle.md)|  | 

### Return type

[**AutomaticHealthCheckToggle**](AutomaticHealthCheckToggle.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

