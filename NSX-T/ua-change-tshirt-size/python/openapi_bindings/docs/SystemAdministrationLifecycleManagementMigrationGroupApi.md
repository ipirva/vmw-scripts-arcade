# swagger_client.SystemAdministrationLifecycleManagementMigrationGroupApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_migration_units_to_group_add_migration_units**](SystemAdministrationLifecycleManagementMigrationGroupApi.md#add_migration_units_to_group_add_migration_units) | **POST** /migration/migration-unit-groups/{group-id}?action&#x3D;add_migration_units | Add migration units to specified migration unit group
[**create_migration_unit_group**](SystemAdministrationLifecycleManagementMigrationGroupApi.md#create_migration_unit_group) | **POST** /migration/migration-unit-groups | Create a group
[**delete_migration_unit_group**](SystemAdministrationLifecycleManagementMigrationGroupApi.md#delete_migration_unit_group) | **DELETE** /migration/migration-unit-groups/{group-id} | Delete the migration unit group
[**get_migration_unit_group**](SystemAdministrationLifecycleManagementMigrationGroupApi.md#get_migration_unit_group) | **GET** /migration/migration-unit-groups/{group-id} | Return migration unit group information
[**get_migration_unit_group_aggregate_info**](SystemAdministrationLifecycleManagementMigrationGroupApi.md#get_migration_unit_group_aggregate_info) | **GET** /migration/migration-unit-groups/aggregate-info | Return aggregate information of all migration unit groups
[**get_migration_unit_group_status**](SystemAdministrationLifecycleManagementMigrationGroupApi.md#get_migration_unit_group_status) | **GET** /migration/migration-unit-groups/{group-id}/status | Get migration status for group
[**get_migration_unit_groups**](SystemAdministrationLifecycleManagementMigrationGroupApi.md#get_migration_unit_groups) | **GET** /migration/migration-unit-groups | Return information of all migration unit groups
[**get_migration_unit_groups_status**](SystemAdministrationLifecycleManagementMigrationGroupApi.md#get_migration_unit_groups_status) | **GET** /migration/migration-unit-groups-status | Get migration status for migration unit groups
[**reorder_migration_unit_group_reorder**](SystemAdministrationLifecycleManagementMigrationGroupApi.md#reorder_migration_unit_group_reorder) | **POST** /migration/migration-unit-groups/{group-id}?action&#x3D;reorder | Reorder migration unit group
[**reorder_migration_unit_reorder**](SystemAdministrationLifecycleManagementMigrationGroupApi.md#reorder_migration_unit_reorder) | **POST** /migration/migration-unit-groups/{group-id}/migration-unit/{migration-unit-id}?action&#x3D;reorder | Reorder an migration unit within the migration unit group
[**update_migration_unit_group**](SystemAdministrationLifecycleManagementMigrationGroupApi.md#update_migration_unit_group) | **PUT** /migration/migration-unit-groups/{group-id} | Update the migration unit group

# **add_migration_units_to_group_add_migration_units**
> MigrationUnitList add_migration_units_to_group_add_migration_units(body, group_id)

Add migration units to specified migration unit group

Add migration units to specified migration unit group. The migration units will be added at the end of the migration unit list. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.MigrationUnitList() # MigrationUnitList | 
group_id = 'group_id_example' # str | 

try:
    # Add migration units to specified migration unit group
    api_response = api_instance.add_migration_units_to_group_add_migration_units(body, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationGroupApi->add_migration_units_to_group_add_migration_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrationUnitList**](MigrationUnitList.md)|  | 
 **group_id** | **str**|  | 

### Return type

[**MigrationUnitList**](MigrationUnitList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_migration_unit_group**
> MigrationUnitGroup create_migration_unit_group(body)

Create a group

Create a group of migration units. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.MigrationUnitGroup() # MigrationUnitGroup | 

try:
    # Create a group
    api_response = api_instance.create_migration_unit_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationGroupApi->create_migration_unit_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrationUnitGroup**](MigrationUnitGroup.md)|  | 

### Return type

[**MigrationUnitGroup**](MigrationUnitGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_migration_unit_group**
> delete_migration_unit_group(group_id)

Delete the migration unit group

Delete the specified group. NOTE - A group can be deleted only if it is empty. If user tries to delete a group containing one or more migration units, the operation will fail and an error will be returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationGroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 

try:
    # Delete the migration unit group
    api_instance.delete_migration_unit_group(group_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationGroupApi->delete_migration_unit_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_unit_group**
> MigrationUnitGroup get_migration_unit_group(group_id, summary=summary)

Return migration unit group information

Returns information about a specific migration unit group in the migration plan.  If request parameter summary is set to true, then only count of migration units will be returned, migration units list will be empty. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationGroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
summary = false # bool | Flag indicating whether to return the summary (optional) (default to false)

try:
    # Return migration unit group information
    api_response = api_instance.get_migration_unit_group(group_id, summary=summary)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationGroupApi->get_migration_unit_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **summary** | **bool**| Flag indicating whether to return the summary | [optional] [default to false]

### Return type

[**MigrationUnitGroup**](MigrationUnitGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_unit_group_aggregate_info**
> MigrationUnitGroupAggregateInfoListResult get_migration_unit_group_aggregate_info(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, summary=summary, sync=sync)

Return aggregate information of all migration unit groups

Return information of all migration unit groups in the migration plan.  If request parameter summary is set to true, then only count of migration units will be returned, migration units list will be empty. If request parameter component type is specified, then all migration unit groups for that component will be returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationGroupApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which migration unit groups to be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
summary = false # bool | Flag indicating whether to return summary (optional) (default to false)
sync = false # bool | Synchronize before returning migration unit groups (optional) (default to false)

try:
    # Return aggregate information of all migration unit groups
    api_response = api_instance.get_migration_unit_group_aggregate_info(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, summary=summary, sync=sync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationGroupApi->get_migration_unit_group_aggregate_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type based on which migration unit groups to be filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **summary** | **bool**| Flag indicating whether to return summary | [optional] [default to false]
 **sync** | **bool**| Synchronize before returning migration unit groups | [optional] [default to false]

### Return type

[**MigrationUnitGroupAggregateInfoListResult**](MigrationUnitGroupAggregateInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_unit_group_status**
> MigrationUnitStatusListResult get_migration_unit_group_status(group_id, cursor=cursor, has_errors=has_errors, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get migration status for group

Get migration status for migration units in the specified group. User can specify whether to show only the migration units with errors. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationGroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
has_errors = false # bool | Flag to indicate whether to return only migration units with errors (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get migration status for group
    api_response = api_instance.get_migration_unit_group_status(group_id, cursor=cursor, has_errors=has_errors, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationGroupApi->get_migration_unit_group_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **has_errors** | **bool**| Flag to indicate whether to return only migration units with errors | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**MigrationUnitStatusListResult**](MigrationUnitStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_unit_groups**
> MigrationUnitGroupListResult get_migration_unit_groups(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, summary=summary, sync=sync)

Return information of all migration unit groups

Return information of all migration unit groups in the migration plan.  If request parameter summary is set to true, then only count of migration units will be returned, migration units list will be empty. If request parameter component type is specified, then all migration unit groups for that component will be returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationGroupApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which migration unit groups to be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
summary = false # bool | Flag indicating whether to return summary (optional) (default to false)
sync = false # bool | Synchronize before returning migration unit groups (optional) (default to false)

try:
    # Return information of all migration unit groups
    api_response = api_instance.get_migration_unit_groups(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, summary=summary, sync=sync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationGroupApi->get_migration_unit_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type based on which migration unit groups to be filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **summary** | **bool**| Flag indicating whether to return summary | [optional] [default to false]
 **sync** | **bool**| Synchronize before returning migration unit groups | [optional] [default to false]

### Return type

[**MigrationUnitGroupListResult**](MigrationUnitGroupListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_unit_groups_status**
> MigrationUnitGroupStatusListResult get_migration_unit_groups_status(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get migration status for migration unit groups

Get migration status for migration unit groups

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationGroupApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which migration unit groups to be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get migration status for migration unit groups
    api_response = api_instance.get_migration_unit_groups_status(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationGroupApi->get_migration_unit_groups_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type based on which migration unit groups to be filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**MigrationUnitGroupStatusListResult**](MigrationUnitGroupStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder_migration_unit_group_reorder**
> reorder_migration_unit_group_reorder(body, group_id)

Reorder migration unit group

Reorder an migration unit group by placing it before/after the specified migration unit group. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReorderMigrationRequest() # ReorderMigrationRequest | 
group_id = 'group_id_example' # str | 

try:
    # Reorder migration unit group
    api_instance.reorder_migration_unit_group_reorder(body, group_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationGroupApi->reorder_migration_unit_group_reorder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReorderMigrationRequest**](ReorderMigrationRequest.md)|  | 
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder_migration_unit_reorder**
> reorder_migration_unit_reorder(body, group_id, migration_unit_id)

Reorder an migration unit within the migration unit group

Reorder an migration unit within the migration unit group by placing it before/after the specified migration unit 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReorderMigrationRequest() # ReorderMigrationRequest | 
group_id = 'group_id_example' # str | 
migration_unit_id = 'migration_unit_id_example' # str | 

try:
    # Reorder an migration unit within the migration unit group
    api_instance.reorder_migration_unit_reorder(body, group_id, migration_unit_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationGroupApi->reorder_migration_unit_reorder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReorderMigrationRequest**](ReorderMigrationRequest.md)|  | 
 **group_id** | **str**|  | 
 **migration_unit_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_migration_unit_group**
> MigrationUnitGroup update_migration_unit_group(body, group_id)

Update the migration unit group

Update the specified migration unit group. Removal of migration units from the group using this is not allowed. An error will be returned in that case. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.MigrationUnitGroup() # MigrationUnitGroup | 
group_id = 'group_id_example' # str | 

try:
    # Update the migration unit group
    api_response = api_instance.update_migration_unit_group(body, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationGroupApi->update_migration_unit_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrationUnitGroup**](MigrationUnitGroup.md)|  | 
 **group_id** | **str**|  | 

### Return type

[**MigrationUnitGroup**](MigrationUnitGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

