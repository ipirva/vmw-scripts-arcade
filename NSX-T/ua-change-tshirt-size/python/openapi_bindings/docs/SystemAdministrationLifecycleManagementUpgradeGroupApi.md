# swagger_client.SystemAdministrationLifecycleManagementUpgradeGroupApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_upgrade_units_to_group_add_upgrade_units**](SystemAdministrationLifecycleManagementUpgradeGroupApi.md#add_upgrade_units_to_group_add_upgrade_units) | **POST** /upgrade/upgrade-unit-groups/{group-id}?action&#x3D;add_upgrade_units | Add upgrade units to specified upgrade unit group
[**create_upgrade_unit_group**](SystemAdministrationLifecycleManagementUpgradeGroupApi.md#create_upgrade_unit_group) | **POST** /upgrade/upgrade-unit-groups | Create a group
[**delete_upgrade_unit_group**](SystemAdministrationLifecycleManagementUpgradeGroupApi.md#delete_upgrade_unit_group) | **DELETE** /upgrade/upgrade-unit-groups/{group-id} | Delete the upgrade unit group
[**get_upgrade_unit_group**](SystemAdministrationLifecycleManagementUpgradeGroupApi.md#get_upgrade_unit_group) | **GET** /upgrade/upgrade-unit-groups/{group-id} | Return upgrade unit group information
[**get_upgrade_unit_group_aggregate_info**](SystemAdministrationLifecycleManagementUpgradeGroupApi.md#get_upgrade_unit_group_aggregate_info) | **GET** /upgrade/upgrade-unit-groups/aggregate-info | Return aggregate information of all upgrade unit groups
[**get_upgrade_unit_group_status**](SystemAdministrationLifecycleManagementUpgradeGroupApi.md#get_upgrade_unit_group_status) | **GET** /upgrade/upgrade-unit-groups/{group-id}/status | Get upgrade status for group
[**get_upgrade_unit_groups**](SystemAdministrationLifecycleManagementUpgradeGroupApi.md#get_upgrade_unit_groups) | **GET** /upgrade/upgrade-unit-groups | Return information of all upgrade unit groups
[**get_upgrade_unit_groups_status**](SystemAdministrationLifecycleManagementUpgradeGroupApi.md#get_upgrade_unit_groups_status) | **GET** /upgrade/upgrade-unit-groups-status | Get upgrade status for upgrade unit groups
[**reorder_upgrade_unit_group_reorder**](SystemAdministrationLifecycleManagementUpgradeGroupApi.md#reorder_upgrade_unit_group_reorder) | **POST** /upgrade/upgrade-unit-groups/{group-id}?action&#x3D;reorder | Reorder upgrade unit group
[**reorder_upgrade_unit_reorder**](SystemAdministrationLifecycleManagementUpgradeGroupApi.md#reorder_upgrade_unit_reorder) | **POST** /upgrade/upgrade-unit-groups/{group-id}/upgrade-unit/{upgrade-unit-id}?action&#x3D;reorder | Reorder an upgrade unit within the upgrade unit group
[**update_upgrade_unit_group**](SystemAdministrationLifecycleManagementUpgradeGroupApi.md#update_upgrade_unit_group) | **PUT** /upgrade/upgrade-unit-groups/{group-id} | Update the upgrade unit group

# **add_upgrade_units_to_group_add_upgrade_units**
> UpgradeUnitList add_upgrade_units_to_group_add_upgrade_units(body, group_id)

Add upgrade units to specified upgrade unit group

Add upgrade units to specified upgrade unit group. The upgrade units will be added at the end of the upgrade unit list. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpgradeUnitList() # UpgradeUnitList | 
group_id = 'group_id_example' # str | 

try:
    # Add upgrade units to specified upgrade unit group
    api_response = api_instance.add_upgrade_units_to_group_add_upgrade_units(body, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeGroupApi->add_upgrade_units_to_group_add_upgrade_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeUnitList**](UpgradeUnitList.md)|  | 
 **group_id** | **str**|  | 

### Return type

[**UpgradeUnitList**](UpgradeUnitList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upgrade_unit_group**
> UpgradeUnitGroup create_upgrade_unit_group(body)

Create a group

Create a group of upgrade units. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpgradeUnitGroup() # UpgradeUnitGroup | 

try:
    # Create a group
    api_response = api_instance.create_upgrade_unit_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeGroupApi->create_upgrade_unit_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeUnitGroup**](UpgradeUnitGroup.md)|  | 

### Return type

[**UpgradeUnitGroup**](UpgradeUnitGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_upgrade_unit_group**
> delete_upgrade_unit_group(group_id)

Delete the upgrade unit group

Delete the specified group. NOTE - A group can be deleted only if it is empty. If user tries to delete a group containing one or more upgrade units, the operation will fail and an error will be returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeGroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 

try:
    # Delete the upgrade unit group
    api_instance.delete_upgrade_unit_group(group_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeGroupApi->delete_upgrade_unit_group: %s\n" % e)
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

# **get_upgrade_unit_group**
> UpgradeUnitGroup get_upgrade_unit_group(group_id, summary=summary)

Return upgrade unit group information

Returns information about a specific upgrade unit group in the upgrade plan.  If request parameter summary is set to true, then only count of upgrade units will be returned, upgrade units list will be empty. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeGroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
summary = false # bool | Flag indicating whether to return the summary (optional) (default to false)

try:
    # Return upgrade unit group information
    api_response = api_instance.get_upgrade_unit_group(group_id, summary=summary)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeGroupApi->get_upgrade_unit_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **summary** | **bool**| Flag indicating whether to return the summary | [optional] [default to false]

### Return type

[**UpgradeUnitGroup**](UpgradeUnitGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_unit_group_aggregate_info**
> UpgradeUnitGroupAggregateInfoListResult get_upgrade_unit_group_aggregate_info(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, summary=summary, sync=sync)

Return aggregate information of all upgrade unit groups

Return information of all upgrade unit groups in the upgrade plan.  If request parameter summary is set to true, then only count of upgrade units will be returned, upgrade units list will be empty. If request parameter component type is specified, then all upgrade unit groups for that component will be returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeGroupApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which upgrade unit groups to be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
summary = false # bool | Flag indicating whether to return summary (optional) (default to false)
sync = false # bool | Synchronize before returning upgrade unit groups (optional) (default to false)

try:
    # Return aggregate information of all upgrade unit groups
    api_response = api_instance.get_upgrade_unit_group_aggregate_info(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, summary=summary, sync=sync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeGroupApi->get_upgrade_unit_group_aggregate_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type based on which upgrade unit groups to be filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **summary** | **bool**| Flag indicating whether to return summary | [optional] [default to false]
 **sync** | **bool**| Synchronize before returning upgrade unit groups | [optional] [default to false]

### Return type

[**UpgradeUnitGroupAggregateInfoListResult**](UpgradeUnitGroupAggregateInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_unit_group_status**
> UpgradeUnitStatusListResult get_upgrade_unit_group_status(group_id, cursor=cursor, has_errors=has_errors, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get upgrade status for group

Get upgrade status for upgrade units in the specified group. User can specify whether to show only the upgrade units with errors. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeGroupApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
has_errors = false # bool | Flag to indicate whether to return only upgrade units with errors (optional) (default to false)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get upgrade status for group
    api_response = api_instance.get_upgrade_unit_group_status(group_id, cursor=cursor, has_errors=has_errors, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeGroupApi->get_upgrade_unit_group_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **has_errors** | **bool**| Flag to indicate whether to return only upgrade units with errors | [optional] [default to false]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**UpgradeUnitStatusListResult**](UpgradeUnitStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_unit_groups**
> UpgradeUnitGroupListResult get_upgrade_unit_groups(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, summary=summary, sync=sync)

Return information of all upgrade unit groups

Return information of all upgrade unit groups in the upgrade plan.  If request parameter summary is set to true, then only count of upgrade units will be returned, upgrade units list will be empty. If request parameter component type is specified, then all upgrade unit groups for that component will be returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeGroupApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which upgrade unit groups to be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
summary = false # bool | Flag indicating whether to return summary (optional) (default to false)
sync = false # bool | Synchronize before returning upgrade unit groups (optional) (default to false)

try:
    # Return information of all upgrade unit groups
    api_response = api_instance.get_upgrade_unit_groups(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, summary=summary, sync=sync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeGroupApi->get_upgrade_unit_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type based on which upgrade unit groups to be filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **summary** | **bool**| Flag indicating whether to return summary | [optional] [default to false]
 **sync** | **bool**| Synchronize before returning upgrade unit groups | [optional] [default to false]

### Return type

[**UpgradeUnitGroupListResult**](UpgradeUnitGroupListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_unit_groups_status**
> UpgradeUnitGroupStatusListResult get_upgrade_unit_groups_status(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get upgrade status for upgrade unit groups

Get upgrade status for upgrade unit groups

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeGroupApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type on which the action is performed or on which the results are filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get upgrade status for upgrade unit groups
    api_response = api_instance.get_upgrade_unit_groups_status(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeGroupApi->get_upgrade_unit_groups_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type on which the action is performed or on which the results are filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**UpgradeUnitGroupStatusListResult**](UpgradeUnitGroupStatusListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder_upgrade_unit_group_reorder**
> reorder_upgrade_unit_group_reorder(body, group_id)

Reorder upgrade unit group

Reorder an upgrade unit group by placing it before/after the specified upgrade unit group. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReorderRequest() # ReorderRequest | 
group_id = 'group_id_example' # str | 

try:
    # Reorder upgrade unit group
    api_instance.reorder_upgrade_unit_group_reorder(body, group_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeGroupApi->reorder_upgrade_unit_group_reorder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReorderRequest**](ReorderRequest.md)|  | 
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reorder_upgrade_unit_reorder**
> reorder_upgrade_unit_reorder(body, group_id, upgrade_unit_id)

Reorder an upgrade unit within the upgrade unit group

Reorder an upgrade unit within the upgrade unit group by placing it before/after the specified upgrade unit 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.ReorderRequest() # ReorderRequest | 
group_id = 'group_id_example' # str | 
upgrade_unit_id = 'upgrade_unit_id_example' # str | 

try:
    # Reorder an upgrade unit within the upgrade unit group
    api_instance.reorder_upgrade_unit_reorder(body, group_id, upgrade_unit_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeGroupApi->reorder_upgrade_unit_reorder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReorderRequest**](ReorderRequest.md)|  | 
 **group_id** | **str**|  | 
 **upgrade_unit_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_upgrade_unit_group**
> UpgradeUnitGroup update_upgrade_unit_group(body, group_id)

Update the upgrade unit group

Update the specified upgrade unit group. Removal of upgrade units from the group using this is not allowed. An error will be returned in that case. Following extended_configuration is supported:  Key: upgrade_mode Supported values: maintenance_mode,in_place Default: maintenance_mode  Key: maintenance_mode_config_vsan_mode Supported values: evacuate_all_data, ensure_object_accessibility, no_action Default: ensure_object_accessibility  Key: maintenance_mode_config_evacuate_powered_off_vms Supported values: true, false Default: false  Key: rebootless_upgrade Supported values: true, false Default: true 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeGroupApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpgradeUnitGroup() # UpgradeUnitGroup | 
group_id = 'group_id_example' # str | 

try:
    # Update the upgrade unit group
    api_response = api_instance.update_upgrade_unit_group(body, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeGroupApi->update_upgrade_unit_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeUnitGroup**](UpgradeUnitGroup.md)|  | 
 **group_id** | **str**|  | 

### Return type

[**UpgradeUnitGroup**](UpgradeUnitGroup.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

