# swagger_client.SystemAdministrationLifecycleManagementMigrationMigrationUnitsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_migration_unit**](SystemAdministrationLifecycleManagementMigrationMigrationUnitsApi.md#get_migration_unit) | **GET** /migration/migration-units/{migration-unit-id} | Get a specific migration unit
[**get_migration_unit_aggregate_info**](SystemAdministrationLifecycleManagementMigrationMigrationUnitsApi.md#get_migration_unit_aggregate_info) | **GET** /migration/migration-units/aggregate-info | Get migration units aggregate-info
[**get_migration_units**](SystemAdministrationLifecycleManagementMigrationMigrationUnitsApi.md#get_migration_units) | **GET** /migration/migration-units | Get migration units
[**get_migration_units_stats**](SystemAdministrationLifecycleManagementMigrationMigrationUnitsApi.md#get_migration_units_stats) | **GET** /migration/migration-units-stats | Get migration units stats

# **get_migration_unit**
> MigrationUnit get_migration_unit(migration_unit_id)

Get a specific migration unit

Get a specific migration unit

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationMigrationUnitsApi(swagger_client.ApiClient(configuration))
migration_unit_id = 'migration_unit_id_example' # str | 

try:
    # Get a specific migration unit
    api_response = api_instance.get_migration_unit(migration_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationMigrationUnitsApi->get_migration_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_unit_id** | **str**|  | 

### Return type

[**MigrationUnit**](MigrationUnit.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_unit_aggregate_info**
> MigrationUnitAggregateInfoListResult get_migration_unit_aggregate_info(component_type=component_type, cursor=cursor, group_id=group_id, has_errors=has_errors, included_fields=included_fields, metadata=metadata, page_size=page_size, selection_status=selection_status, sort_ascending=sort_ascending, sort_by=sort_by)

Get migration units aggregate-info

Get migration units aggregate-info

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationMigrationUnitsApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which migration units to be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
group_id = 'group_id_example' # str | Identifier of group based on which migration units to be filtered (optional)
has_errors = false # bool | Flag to indicate whether to return only migration units with errors (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
metadata = 'metadata_example' # str | Metadata about migration unit to filter on (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
selection_status = 'ALL' # str | Flag to indicate whether to return only selected, only deselected or both type of migration units (optional) (default to ALL)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get migration units aggregate-info
    api_response = api_instance.get_migration_unit_aggregate_info(component_type=component_type, cursor=cursor, group_id=group_id, has_errors=has_errors, included_fields=included_fields, metadata=metadata, page_size=page_size, selection_status=selection_status, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationMigrationUnitsApi->get_migration_unit_aggregate_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type based on which migration units to be filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **group_id** | **str**| Identifier of group based on which migration units to be filtered | [optional] 
 **has_errors** | **bool**| Flag to indicate whether to return only migration units with errors | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **metadata** | **str**| Metadata about migration unit to filter on | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **selection_status** | **str**| Flag to indicate whether to return only selected, only deselected or both type of migration units | [optional] [default to ALL]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**MigrationUnitAggregateInfoListResult**](MigrationUnitAggregateInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_units**
> MigrationUnitListResult get_migration_units(component_type=component_type, current_version=current_version, cursor=cursor, group_id=group_id, has_warnings=has_warnings, included_fields=included_fields, metadata=metadata, migration_unit_type=migration_unit_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get migration units

Get migration units

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationMigrationUnitsApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which migration units to be filtered (optional)
current_version = 'current_version_example' # str | Current version of migration unit based on which migration units to be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
group_id = 'group_id_example' # str | UUID of group based on which migration units to be filtered (optional)
has_warnings = false # bool | Flag to indicate whether to return only migration units with warnings (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
metadata = 'metadata_example' # str | Metadata about migration unit to filter on (optional)
migration_unit_type = 'migration_unit_type_example' # str | Migration unit type based on which migration units to be filtered (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get migration units
    api_response = api_instance.get_migration_units(component_type=component_type, current_version=current_version, cursor=cursor, group_id=group_id, has_warnings=has_warnings, included_fields=included_fields, metadata=metadata, migration_unit_type=migration_unit_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationMigrationUnitsApi->get_migration_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type based on which migration units to be filtered | [optional] 
 **current_version** | **str**| Current version of migration unit based on which migration units to be filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **group_id** | **str**| UUID of group based on which migration units to be filtered | [optional] 
 **has_warnings** | **bool**| Flag to indicate whether to return only migration units with warnings | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **metadata** | **str**| Metadata about migration unit to filter on | [optional] 
 **migration_unit_type** | **str**| Migration unit type based on which migration units to be filtered | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**MigrationUnitListResult**](MigrationUnitListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_units_stats**
> MigrationUnitTypeStatsList get_migration_units_stats(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, sync=sync)

Get migration units stats

Get migration units stats

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationMigrationUnitsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
sync = false # bool | Synchronize before returning migration unit stats (optional) (default to false)

try:
    # Get migration units stats
    api_response = api_instance.get_migration_units_stats(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, sync=sync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationMigrationUnitsApi->get_migration_units_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **sync** | **bool**| Synchronize before returning migration unit stats | [optional] [default to false]

### Return type

[**MigrationUnitTypeStatsList**](MigrationUnitTypeStatsList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

