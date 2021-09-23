# swagger_client.SystemAdministrationLifecycleManagementUpgradeUpgradeUnitsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_upgrade_unit**](SystemAdministrationLifecycleManagementUpgradeUpgradeUnitsApi.md#get_upgrade_unit) | **GET** /upgrade/upgrade-units/{upgrade-unit-id} | Get a specific upgrade unit
[**get_upgrade_unit_aggregate_info**](SystemAdministrationLifecycleManagementUpgradeUpgradeUnitsApi.md#get_upgrade_unit_aggregate_info) | **GET** /upgrade/upgrade-units/aggregate-info | Get upgrade units aggregate-info
[**get_upgrade_units**](SystemAdministrationLifecycleManagementUpgradeUpgradeUnitsApi.md#get_upgrade_units) | **GET** /upgrade/upgrade-units | Get upgrade units
[**get_upgrade_units_stats**](SystemAdministrationLifecycleManagementUpgradeUpgradeUnitsApi.md#get_upgrade_units_stats) | **GET** /upgrade/upgrade-units-stats | Get upgrade units stats

# **get_upgrade_unit**
> UpgradeUnit get_upgrade_unit(upgrade_unit_id)

Get a specific upgrade unit

Get a specific upgrade unit

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeUpgradeUnitsApi(swagger_client.ApiClient(configuration))
upgrade_unit_id = 'upgrade_unit_id_example' # str | 

try:
    # Get a specific upgrade unit
    api_response = api_instance.get_upgrade_unit(upgrade_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeUpgradeUnitsApi->get_upgrade_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade_unit_id** | **str**|  | 

### Return type

[**UpgradeUnit**](UpgradeUnit.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_unit_aggregate_info**
> UpgradeUnitAggregateInfoListResult get_upgrade_unit_aggregate_info(component_type=component_type, cursor=cursor, group_id=group_id, has_errors=has_errors, included_fields=included_fields, metadata=metadata, page_size=page_size, selection_status=selection_status, sort_ascending=sort_ascending, sort_by=sort_by, upgrade_unit_display_name=upgrade_unit_display_name)

Get upgrade units aggregate-info

Get upgrade units aggregate-info

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeUpgradeUnitsApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which upgrade units to be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
group_id = 'group_id_example' # str | Identifier of group based on which upgrade units to be filtered (optional)
has_errors = false # bool | Flag to indicate whether to return only upgrade units with errors (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
metadata = 'metadata_example' # str | Metadata about upgrade unit to filter on (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
selection_status = 'ALL' # str | Flag to indicate whether to return only selected, only deselected or both type of upgrade units (optional) (default to ALL)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
upgrade_unit_display_name = 'upgrade_unit_display_name_example' # str | Display name of upgrade unit (optional)

try:
    # Get upgrade units aggregate-info
    api_response = api_instance.get_upgrade_unit_aggregate_info(component_type=component_type, cursor=cursor, group_id=group_id, has_errors=has_errors, included_fields=included_fields, metadata=metadata, page_size=page_size, selection_status=selection_status, sort_ascending=sort_ascending, sort_by=sort_by, upgrade_unit_display_name=upgrade_unit_display_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeUpgradeUnitsApi->get_upgrade_unit_aggregate_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type based on which upgrade units to be filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **group_id** | **str**| Identifier of group based on which upgrade units to be filtered | [optional] 
 **has_errors** | **bool**| Flag to indicate whether to return only upgrade units with errors | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **metadata** | **str**| Metadata about upgrade unit to filter on | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **selection_status** | **str**| Flag to indicate whether to return only selected, only deselected or both type of upgrade units | [optional] [default to ALL]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **upgrade_unit_display_name** | **str**| Display name of upgrade unit | [optional] 

### Return type

[**UpgradeUnitAggregateInfoListResult**](UpgradeUnitAggregateInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_units**
> UpgradeUnitListResult get_upgrade_units(component_type=component_type, current_version=current_version, cursor=cursor, group_id=group_id, has_warnings=has_warnings, included_fields=included_fields, metadata=metadata, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, upgrade_unit_type=upgrade_unit_type)

Get upgrade units

Get upgrade units

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeUpgradeUnitsApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which upgrade units to be filtered (optional)
current_version = 'current_version_example' # str | Current version of upgrade unit based on which upgrade units to be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
group_id = 'group_id_example' # str | UUID of group based on which upgrade units to be filtered (optional)
has_warnings = false # bool | Flag to indicate whether to return only upgrade units with warnings (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
metadata = 'metadata_example' # str | Metadata about upgrade unit to filter on (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
upgrade_unit_type = 'upgrade_unit_type_example' # str | Upgrade unit type based on which upgrade units to be filtered (optional)

try:
    # Get upgrade units
    api_response = api_instance.get_upgrade_units(component_type=component_type, current_version=current_version, cursor=cursor, group_id=group_id, has_warnings=has_warnings, included_fields=included_fields, metadata=metadata, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, upgrade_unit_type=upgrade_unit_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeUpgradeUnitsApi->get_upgrade_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type based on which upgrade units to be filtered | [optional] 
 **current_version** | **str**| Current version of upgrade unit based on which upgrade units to be filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **group_id** | **str**| UUID of group based on which upgrade units to be filtered | [optional] 
 **has_warnings** | **bool**| Flag to indicate whether to return only upgrade units with warnings | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **metadata** | **str**| Metadata about upgrade unit to filter on | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **upgrade_unit_type** | **str**| Upgrade unit type based on which upgrade units to be filtered | [optional] 

### Return type

[**UpgradeUnitListResult**](UpgradeUnitListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_units_stats**
> UpgradeUnitTypeStatsList get_upgrade_units_stats(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, sync=sync)

Get upgrade units stats

Get upgrade units stats

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeUpgradeUnitsApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
sync = false # bool | Synchronize before returning upgrade unit stats (optional) (default to false)

try:
    # Get upgrade units stats
    api_response = api_instance.get_upgrade_units_stats(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, sync=sync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeUpgradeUnitsApi->get_upgrade_units_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **sync** | **bool**| Synchronize before returning upgrade unit stats | [optional] [default to false]

### Return type

[**UpgradeUnitTypeStatsList**](UpgradeUnitTypeStatsList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

