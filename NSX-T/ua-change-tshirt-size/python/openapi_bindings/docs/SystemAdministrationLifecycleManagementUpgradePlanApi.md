# swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_pre_upgrade_checks_abort_pre_upgrade_checks**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#abort_pre_upgrade_checks_abort_pre_upgrade_checks) | **POST** /upgrade?action&#x3D;abort_pre_upgrade_checks | Abort pre-upgrade checks
[**continue_upgrade_continue**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#continue_upgrade_continue) | **POST** /upgrade/plan?action&#x3D;continue | Continue upgrade
[**execute_post_upgrade_checks_execute_post_upgrade_checks**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#execute_post_upgrade_checks_execute_post_upgrade_checks) | **POST** /upgrade/{component-type}?action&#x3D;execute_post_upgrade_checks | Execute post-upgrade checks
[**execute_pre_upgrade_checks_execute_pre_upgrade_checks**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#execute_pre_upgrade_checks_execute_pre_upgrade_checks) | **POST** /upgrade?action&#x3D;execute_pre_upgrade_checks | Execute pre-upgrade checks
[**get_all_pre_upgrade_checks_in_csv_format_csv**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#get_all_pre_upgrade_checks_in_csv_format_csv) | **GET** /upgrade/pre-upgrade-checks?format&#x3D;csv | Returns pre-upgrade checks in csv format
[**get_pre_upgrade_check_failures**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#get_pre_upgrade_check_failures) | **GET** /upgrade/pre-upgrade-checks/failures | Get Pre-upgrade Check Failures
[**get_upgrade_checks_info**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#get_upgrade_checks_info) | **GET** /upgrade/upgrade-checks-info | Returns information about upgrade checks
[**get_upgrade_plan_settings**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#get_upgrade_plan_settings) | **GET** /upgrade/plan/{component_type}/settings | Get upgrade plan settings for the component
[**pause_upgrade_pause**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#pause_upgrade_pause) | **POST** /upgrade/plan?action&#x3D;pause | Pause upgrade
[**reset_upgrade_plan_reset**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#reset_upgrade_plan_reset) | **POST** /upgrade/plan?action&#x3D;reset | Reset upgrade plan to default plan
[**stage_upgrade_stage_upgrade**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#stage_upgrade_stage_upgrade) | **POST** /upgrade/plan?action&#x3D;stage-upgrade | Stage the upgrade bits
[**start_upgrade_start**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#start_upgrade_start) | **POST** /upgrade/plan?action&#x3D;start | Start upgrade
[**update_upgrade_plan_settings**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#update_upgrade_plan_settings) | **PUT** /upgrade/plan/{component_type}/settings | Update upgrade plan settings for the component
[**upgrade_selected_units_upgrade_selected_units**](SystemAdministrationLifecycleManagementUpgradePlanApi.md#upgrade_selected_units_upgrade_selected_units) | **POST** /upgrade/plan?action&#x3D;upgrade_selected_units | Upgrade selected units

# **abort_pre_upgrade_checks_abort_pre_upgrade_checks**
> abort_pre_upgrade_checks_abort_pre_upgrade_checks()

Abort pre-upgrade checks

Aborts execution of pre-upgrade checks if already in progress. Halts the execution of checks awaiting execution at this point and makes best-effort attempts to stop checks already in execution. Returns without action if execution of pre-upgrade checks is not in progress. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))

try:
    # Abort pre-upgrade checks
    api_instance.abort_pre_upgrade_checks_abort_pre_upgrade_checks()
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->abort_pre_upgrade_checks_abort_pre_upgrade_checks: %s\n" % e)
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

# **continue_upgrade_continue**
> continue_upgrade_continue(component_type=component_type, skip=skip)

Continue upgrade

Continue the upgrade. Resumes the upgrade from the point where it was paused. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component to upgrade. (optional)
skip = false # bool | Skip to upgrade of next component. (optional) (default to false)

try:
    # Continue upgrade
    api_instance.continue_upgrade_continue(component_type=component_type, skip=skip)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->continue_upgrade_continue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component to upgrade. | [optional] 
 **skip** | **bool**| Skip to upgrade of next component. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_post_upgrade_checks_execute_post_upgrade_checks**
> execute_post_upgrade_checks_execute_post_upgrade_checks(component_type)

Execute post-upgrade checks

Run pre-defined checks to identify issues after upgrade of a component. The results of the checks are added to the respective upgrade units aggregate-info. The progress and status of post-upgrade checks is part of aggregate-info of individual upgrade unit groups. Returns HTTP status 500 with error code 30953 if execution of post-upgrade checks is already in progress. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | 

try:
    # Execute post-upgrade checks
    api_instance.execute_post_upgrade_checks_execute_post_upgrade_checks(component_type)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->execute_post_upgrade_checks_execute_post_upgrade_checks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_pre_upgrade_checks_execute_pre_upgrade_checks**
> execute_pre_upgrade_checks_execute_pre_upgrade_checks(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Execute pre-upgrade checks

Run pre-defined checks to identify potential issues which can be encountered during an upgrade or can cause an upgrade to fail. The results of the checks are added to the respective upgrade units aggregate-info. The progress and status of operation is part of upgrade status summary of individual components. Returns HTTP status 500 with error code 30953 if execution of pre-upgrade checks is already in progress. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type on which the action is performed or on which the results are filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Execute pre-upgrade checks
    api_instance.execute_pre_upgrade_checks_execute_pre_upgrade_checks(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->execute_pre_upgrade_checks_execute_pre_upgrade_checks: %s\n" % e)
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

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_pre_upgrade_checks_in_csv_format_csv**
> UpgradeCheckCsvListResult get_all_pre_upgrade_checks_in_csv_format_csv()

Returns pre-upgrade checks in csv format

Returns pre-upgrade checks in csv format 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))

try:
    # Returns pre-upgrade checks in csv format
    api_response = api_instance.get_all_pre_upgrade_checks_in_csv_format_csv()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->get_all_pre_upgrade_checks_in_csv_format_csv: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UpgradeCheckCsvListResult**](UpgradeCheckCsvListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pre_upgrade_check_failures**
> UpgradeCheckFailureListResult get_pre_upgrade_check_failures(component_type=component_type, cursor=cursor, filter_text=filter_text, included_fields=included_fields, origin_type=origin_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)

Get Pre-upgrade Check Failures

Get failures resulting from the last execution of pre-upgrade checks. If the execution of checks is in progress, the response has the list of failures observed so far. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
filter_text = 'filter_text_example' # str | Filter text (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
origin_type = 'origin_type_example' # str | Type of origin of failure (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)
type = 'type_example' # str | Status of the upgrade check (optional)

try:
    # Get Pre-upgrade Check Failures
    api_response = api_instance.get_pre_upgrade_check_failures(component_type=component_type, cursor=cursor, filter_text=filter_text, included_fields=included_fields, origin_type=origin_type, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->get_pre_upgrade_check_failures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **filter_text** | **str**| Filter text | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **origin_type** | **str**| Type of origin of failure | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 
 **type** | **str**| Status of the upgrade check | [optional] 

### Return type

[**UpgradeCheckFailureListResult**](UpgradeCheckFailureListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_checks_info**
> ComponentUpgradeChecksInfoListResult get_upgrade_checks_info(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Returns information about upgrade checks

Returns information of pre-upgrade and post-upgrade checks. If request parameter component type is specified, then returns information about all pre-upgrade and post-upgrade for the component. Otherwise returns information of checks across all component types. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which upgrade checks are to be filtered (optional)
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Returns information about upgrade checks
    api_response = api_instance.get_upgrade_checks_info(component_type=component_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->get_upgrade_checks_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type based on which upgrade checks are to be filtered | [optional] 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ComponentUpgradeChecksInfoListResult**](ComponentUpgradeChecksInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_plan_settings**
> UpgradePlanSettings get_upgrade_plan_settings(component_type)

Get upgrade plan settings for the component

Get the upgrade plan settings for the component. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | 

try:
    # Get upgrade plan settings for the component
    api_response = api_instance.get_upgrade_plan_settings(component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->get_upgrade_plan_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**|  | 

### Return type

[**UpgradePlanSettings**](UpgradePlanSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_upgrade_pause**
> pause_upgrade_pause()

Pause upgrade

Pause the upgrade. Upgrade will be paused after upgrade of all the nodes currently in progress is completed either successfully or with failure. User can make changes in the upgrade plan when the upgrade is paused. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))

try:
    # Pause upgrade
    api_instance.pause_upgrade_pause()
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->pause_upgrade_pause: %s\n" % e)
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

# **reset_upgrade_plan_reset**
> reset_upgrade_plan_reset(component_type)

Reset upgrade plan to default plan

Reset the upgrade plan to default plan. User has an option to change the default plan. But if after making changes, user wants to go back to the default plan, this is the way to do so. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type

try:
    # Reset upgrade plan to default plan
    api_instance.reset_upgrade_plan_reset(component_type)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->reset_upgrade_plan_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stage_upgrade_stage_upgrade**
> stage_upgrade_stage_upgrade(component_type=component_type)

Stage the upgrade bits

This will stage the upgrade bits so that upgrade can be driven from outside NSX upgrade-coordinator. If component type is not provided as a request parameter then upgrade staging will be performed on all the components. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type (optional)

try:
    # Stage the upgrade bits
    api_instance.stage_upgrade_stage_upgrade(component_type=component_type)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->stage_upgrade_stage_upgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_upgrade_start**
> start_upgrade_start()

Start upgrade

Start the upgrade. Upgrade will start as per the upgrade plan. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))

try:
    # Start upgrade
    api_instance.start_upgrade_start()
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->start_upgrade_start: %s\n" % e)
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

# **update_upgrade_plan_settings**
> UpgradePlanSettings update_upgrade_plan_settings(body, component_type)

Update upgrade plan settings for the component

Update the upgrade plan settings for the component. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpgradePlanSettings() # UpgradePlanSettings | 
component_type = 'component_type_example' # str | 

try:
    # Update upgrade plan settings for the component
    api_response = api_instance.update_upgrade_plan_settings(body, component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->update_upgrade_plan_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradePlanSettings**](UpgradePlanSettings.md)|  | 
 **component_type** | **str**|  | 

### Return type

[**UpgradePlanSettings**](UpgradePlanSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_selected_units_upgrade_selected_units**
> upgrade_selected_units_upgrade_selected_units(body)

Upgrade selected units

Upgrades, Resumes the upgrade of a selected set of units. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradePlanApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpgradeUnitList() # UpgradeUnitList | 

try:
    # Upgrade selected units
    api_instance.upgrade_selected_units_upgrade_selected_units(body)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradePlanApi->upgrade_selected_units_upgrade_selected_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeUnitList**](UpgradeUnitList.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

