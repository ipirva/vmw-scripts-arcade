# swagger_client.SystemAdministrationMonitoringLatencyProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_latency_stat_profile**](SystemAdministrationMonitoringLatencyProfilesApi.md#create_latency_stat_profile) | **POST** /latency-profiles | Create a new latency profile
[**delete_latency_stat_profile**](SystemAdministrationMonitoringLatencyProfilesApi.md#delete_latency_stat_profile) | **DELETE** /latency-profiles/{latency-profile-id} | Delete an existing latency profile
[**list_latency_profiles**](SystemAdministrationMonitoringLatencyProfilesApi.md#list_latency_profiles) | **GET** /latency-profiles | List latency profiles
[**read_latency_stat_profile**](SystemAdministrationMonitoringLatencyProfilesApi.md#read_latency_stat_profile) | **GET** /latency-profiles/{latency-profile-id} | Get an existing latency profile configuration
[**update_latency_profile**](SystemAdministrationMonitoringLatencyProfilesApi.md#update_latency_profile) | **PUT** /latency-profiles/{latency-profile-id} | Update an existing latency profile

# **create_latency_stat_profile**
> LatencyStatProfile create_latency_stat_profile(body)

Create a new latency profile

Create a new latency profile

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
api_instance = swagger_client.SystemAdministrationMonitoringLatencyProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.LatencyStatProfile() # LatencyStatProfile | 

try:
    # Create a new latency profile
    api_response = api_instance.create_latency_stat_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringLatencyProfilesApi->create_latency_stat_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LatencyStatProfile**](LatencyStatProfile.md)|  | 

### Return type

[**LatencyStatProfile**](LatencyStatProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_latency_stat_profile**
> delete_latency_stat_profile(latency_profile_id)

Delete an existing latency profile

Delete an existing latency profile

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
api_instance = swagger_client.SystemAdministrationMonitoringLatencyProfilesApi(swagger_client.ApiClient(configuration))
latency_profile_id = 'latency_profile_id_example' # str | 

try:
    # Delete an existing latency profile
    api_instance.delete_latency_stat_profile(latency_profile_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringLatencyProfilesApi->delete_latency_stat_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latency_profile_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_latency_profiles**
> LatencyStatProfileListResult list_latency_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List latency profiles

List latency profiles

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
api_instance = swagger_client.SystemAdministrationMonitoringLatencyProfilesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List latency profiles
    api_response = api_instance.list_latency_profiles(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringLatencyProfilesApi->list_latency_profiles: %s\n" % e)
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

[**LatencyStatProfileListResult**](LatencyStatProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_latency_stat_profile**
> LatencyStatProfile read_latency_stat_profile(latency_profile_id)

Get an existing latency profile configuration

Get an existing latency profile configuration

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
api_instance = swagger_client.SystemAdministrationMonitoringLatencyProfilesApi(swagger_client.ApiClient(configuration))
latency_profile_id = 'latency_profile_id_example' # str | 

try:
    # Get an existing latency profile configuration
    api_response = api_instance.read_latency_stat_profile(latency_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringLatencyProfilesApi->read_latency_stat_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latency_profile_id** | **str**|  | 

### Return type

[**LatencyStatProfile**](LatencyStatProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_latency_profile**
> LatencyStatProfile update_latency_profile(body, latency_profile_id)

Update an existing latency profile

Update an existing latency profile

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
api_instance = swagger_client.SystemAdministrationMonitoringLatencyProfilesApi(swagger_client.ApiClient(configuration))
body = swagger_client.LatencyStatProfile() # LatencyStatProfile | 
latency_profile_id = 'latency_profile_id_example' # str | 

try:
    # Update an existing latency profile
    api_response = api_instance.update_latency_profile(body, latency_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringLatencyProfilesApi->update_latency_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LatencyStatProfile**](LatencyStatProfile.md)|  | 
 **latency_profile_id** | **str**|  | 

### Return type

[**LatencyStatProfile**](LatencyStatProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

