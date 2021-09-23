# swagger_client.SystemAdministrationLifecycleManagementMigrationPlanApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_migration_abort**](SystemAdministrationLifecycleManagementMigrationPlanApi.md#abort_migration_abort) | **POST** /migration/plan?action&#x3D;abort | Abort migration
[**continue_migration_continue**](SystemAdministrationLifecycleManagementMigrationPlanApi.md#continue_migration_continue) | **POST** /migration/plan?action&#x3D;continue | Continue migration
[**finish_migration_finish**](SystemAdministrationLifecycleManagementMigrationPlanApi.md#finish_migration_finish) | **POST** /migration/plan?action&#x3D;finish | Mark completion of a migration cycle
[**get_migration_plan_settings**](SystemAdministrationLifecycleManagementMigrationPlanApi.md#get_migration_plan_settings) | **GET** /migration/plan/{component_type}/settings | Get migration plan settings for the component
[**pause_migration_pause**](SystemAdministrationLifecycleManagementMigrationPlanApi.md#pause_migration_pause) | **POST** /migration/plan?action&#x3D;pause | Pause migration
[**reset_migration_plan_reset**](SystemAdministrationLifecycleManagementMigrationPlanApi.md#reset_migration_plan_reset) | **POST** /migration/plan?action&#x3D;reset | Reset migration plan to default plan
[**start_migration_start**](SystemAdministrationLifecycleManagementMigrationPlanApi.md#start_migration_start) | **POST** /migration/plan?action&#x3D;start | Start migration
[**start_rollback_migration_rollback**](SystemAdministrationLifecycleManagementMigrationPlanApi.md#start_rollback_migration_rollback) | **POST** /migration/plan?action&#x3D;rollback | Rollbabck migration
[**update_migration_plan_settings**](SystemAdministrationLifecycleManagementMigrationPlanApi.md#update_migration_plan_settings) | **PUT** /migration/plan/{component_type}/settings | Update migration plan settings for the component

# **abort_migration_abort**
> abort_migration_abort()

Abort migration

Resets all migration steps done so far, so that migration can be restarted with new setup details. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationPlanApi(swagger_client.ApiClient(configuration))

try:
    # Abort migration
    api_instance.abort_migration_abort()
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationPlanApi->abort_migration_abort: %s\n" % e)
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

# **continue_migration_continue**
> continue_migration_continue(skip=skip)

Continue migration

Continue the migration. Resumes the migration from the point where it was paused. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationPlanApi(swagger_client.ApiClient(configuration))
skip = false # bool | Skip to migration of next component. (optional) (default to false)

try:
    # Continue migration
    api_instance.continue_migration_continue(skip=skip)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationPlanApi->continue_migration_continue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **bool**| Skip to migration of next component. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finish_migration_finish**
> finish_migration_finish()

Mark completion of a migration cycle

This API marks the completion of one execution of migration workflow. This API resets internal  execution state and hence needs to be invoked before starting subsequent workflow run. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationPlanApi(swagger_client.ApiClient(configuration))

try:
    # Mark completion of a migration cycle
    api_instance.finish_migration_finish()
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationPlanApi->finish_migration_finish: %s\n" % e)
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

# **get_migration_plan_settings**
> MigrationPlanSettings get_migration_plan_settings(component_type)

Get migration plan settings for the component

Get the migration plan settings for the component. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationPlanApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | 

try:
    # Get migration plan settings for the component
    api_response = api_instance.get_migration_plan_settings(component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationPlanApi->get_migration_plan_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**|  | 

### Return type

[**MigrationPlanSettings**](MigrationPlanSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_migration_pause**
> pause_migration_pause()

Pause migration

Pause the migration. Migration will be paused after migration of all the nodes currently in progress is completed either successfully or with failure. User can make changes in the migration plan when the migration is paused. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationPlanApi(swagger_client.ApiClient(configuration))

try:
    # Pause migration
    api_instance.pause_migration_pause()
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationPlanApi->pause_migration_pause: %s\n" % e)
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

# **reset_migration_plan_reset**
> reset_migration_plan_reset(component_type)

Reset migration plan to default plan

Reset the migration plan to default plan. User has an option to change the default plan. But if after making changes, user wants to go back to the default plan, this is the way to do so. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationPlanApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type

try:
    # Reset migration plan to default plan
    api_instance.reset_migration_plan_reset(component_type)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationPlanApi->reset_migration_plan_reset: %s\n" % e)
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

# **start_migration_start**
> start_migration_start()

Start migration

Start the migration. Migration will start as per the migration plan. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationPlanApi(swagger_client.ApiClient(configuration))

try:
    # Start migration
    api_instance.start_migration_start()
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationPlanApi->start_migration_start: %s\n" % e)
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

# **start_rollback_migration_rollback**
> start_rollback_migration_rollback()

Rollbabck migration

Roll back the migration. Changes applied to target NSX will be reverted. Use the migration status API to monitor progress of roll back. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationPlanApi(swagger_client.ApiClient(configuration))

try:
    # Rollbabck migration
    api_instance.start_rollback_migration_rollback()
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationPlanApi->start_rollback_migration_rollback: %s\n" % e)
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

# **update_migration_plan_settings**
> MigrationPlanSettings update_migration_plan_settings(body, component_type)

Update migration plan settings for the component

Update the migration plan settings for the component. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationPlanApi(swagger_client.ApiClient(configuration))
body = swagger_client.MigrationPlanSettings() # MigrationPlanSettings | 
component_type = 'component_type_example' # str | 

try:
    # Update migration plan settings for the component
    api_response = api_instance.update_migration_plan_settings(body, component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationPlanApi->update_migration_plan_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrationPlanSettings**](MigrationPlanSettings.md)|  | 
 **component_type** | **str**|  | 

### Return type

[**MigrationPlanSettings**](MigrationPlanSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

