# swagger_client.SystemAdministrationLifecycleManagementMigrationStatsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_migration_data**](SystemAdministrationLifecycleManagementMigrationStatsApi.md#download_migration_data) | **GET** /migration/data/download | Download migration data
[**get_logical_construct_migration_stats**](SystemAdministrationLifecycleManagementMigrationStatsApi.md#get_logical_construct_migration_stats) | **GET** /migration/logical-constructs/stats | Get migration stats for logical constructs phase
[**get_migration_data_info**](SystemAdministrationLifecycleManagementMigrationStatsApi.md#get_migration_data_info) | **GET** /migration/data | Get Migration Data Info.

# **download_migration_data**
> download_migration_data(file_type)

Download migration data

Download the data needed for migration. The call returns after Download is completed. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationStatsApi(swagger_client.ApiClient(configuration))
file_type = 'file_type_example' # str | Type of the Migration data file that needs to be downloaded.

try:
    # Download migration data
    api_instance.download_migration_data(file_type)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationStatsApi->download_migration_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_type** | **str**| Type of the Migration data file that needs to be downloaded. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_construct_migration_stats**
> LogicalConstructMigrationStatsListResult get_logical_construct_migration_stats(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get migration stats for logical constructs phase

Get migration stats for logical constructs phase. This API can be polled for getting runtime progress of the migration from source to target.

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationStatsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get migration stats for logical constructs phase
    api_response = api_instance.get_logical_construct_migration_stats(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationStatsApi->get_logical_construct_migration_stats: %s\n" % e)
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

[**LogicalConstructMigrationStatsListResult**](LogicalConstructMigrationStatsListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_data_info**
> MigrationDataInfo get_migration_data_info(file_type)

Get Migration Data Info.

Get information about the requested Migration Data file.

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationStatsApi(swagger_client.ApiClient(configuration))
file_type = 'file_type_example' # str | Type of the Migration data file for which info is needed.

try:
    # Get Migration Data Info.
    api_response = api_instance.get_migration_data_info(file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationStatsApi->get_migration_data_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_type** | **str**| Type of the Migration data file for which info is needed. | 

### Return type

[**MigrationDataInfo**](MigrationDataInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

