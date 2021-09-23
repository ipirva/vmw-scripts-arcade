# swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advance_cluster_restore_advance**](SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi.md#advance_cluster_restore_advance) | **POST** /cluster/restore?action&#x3D;advance | Advance any suspended restore operation
[**cancel_cluster_restore_cancel**](SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi.md#cancel_cluster_restore_cancel) | **POST** /cluster/restore?action&#x3D;cancel | Cancel any running restore operation
[**configure_restore_config**](SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi.md#configure_restore_config) | **PUT** /cluster/restore/config | Deprecated. Configure Restore SFTP server credentials
[**get_restore_config**](SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi.md#get_restore_config) | **GET** /cluster/restore/config | Deprecated. Get Restore configuration
[**initiate_cluster_restore_start**](SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi.md#initiate_cluster_restore_start) | **POST** /cluster/restore?action&#x3D;start | Initiate a restore operation
[**list_cluster_backup_timestamps**](SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi.md#list_cluster_backup_timestamps) | **GET** /cluster/restore/backuptimestamps | List timestamps of all available Cluster Backups.
[**list_restore_instruction_resources**](SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi.md#list_restore_instruction_resources) | **GET** /cluster/restore/instruction-resources | List resources for a given instruction, to be shown to/executed by users. 
[**query_cluster_restore_status**](SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi.md#query_cluster_restore_status) | **GET** /cluster/restore/status | Query Restore Request Status
[**retry_cluster_restore_retry**](SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi.md#retry_cluster_restore_retry) | **POST** /cluster/restore?action&#x3D;retry | Retry any failed restore operation
[**suspend_cluster_restore_suspend**](SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi.md#suspend_cluster_restore_suspend) | **POST** /cluster/restore?action&#x3D;suspend | Suspend any running restore operation

# **advance_cluster_restore_advance**
> ClusterRestoreStatus advance_cluster_restore_advance(body)

Advance any suspended restore operation

Advance any currently suspended restore operation. The operation might have been suspended because (1) the user had suspended it previously, or (2) the operation is waiting for user input, to be provided as a part of the POST request body. This operation is only valid when a GET cluster/restore/status returns a status with value SUSPENDED. Otherwise, a 409 response is returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.AdvanceClusterRestoreRequest() # AdvanceClusterRestoreRequest | 

try:
    # Advance any suspended restore operation
    api_response = api_instance.advance_cluster_restore_advance(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi->advance_cluster_restore_advance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdvanceClusterRestoreRequest**](AdvanceClusterRestoreRequest.md)|  | 

### Return type

[**ClusterRestoreStatus**](ClusterRestoreStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_cluster_restore_cancel**
> ClusterRestoreStatus cancel_cluster_restore_cancel()

Cancel any running restore operation

This operation is only valid when a restore is in suspended state. The UI user can cancel any restore operation when the restore is suspended either due to an error, or for a user input. The API user would need to monitor the progression of a restore by calling periodically \"/api/v1/cluster/restore/status\" API. The response object (ClusterRestoreStatus), contains a field \"endpoints\". The API user can cancel the restore process if 'cancel' action is shown in the endpoint field. This operation is only valid when a GET cluster/restore/status returns a status with value SUSPENDED. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi(swagger_client.ApiClient(configuration))

try:
    # Cancel any running restore operation
    api_response = api_instance.cancel_cluster_restore_cancel()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi->cancel_cluster_restore_cancel: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterRestoreStatus**](ClusterRestoreStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_restore_config**
> RestoreConfiguration configure_restore_config(body)

Deprecated. Configure Restore SFTP server credentials

Deprecated. Please use API /cluster/backups/config, to configure remote file server(where backed-up files are stored) details during restore. In older versions - Configure file server where the backed-up files used for the Restore operation are available. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.RestoreConfiguration() # RestoreConfiguration | 

try:
    # Deprecated. Configure Restore SFTP server credentials
    api_response = api_instance.configure_restore_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi->configure_restore_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RestoreConfiguration**](RestoreConfiguration.md)|  | 

### Return type

[**RestoreConfiguration**](RestoreConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_restore_config**
> RestoreConfiguration get_restore_config()

Deprecated. Get Restore configuration

Deprecated. Please use API /cluster/backups/config, to get remote file server(where backuped-up files are stored) details durign restore. In older versions - Get configuration information for the file server used to store backed-up files. Fields that contain secrets (password, passphrase) are not returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi(swagger_client.ApiClient(configuration))

try:
    # Deprecated. Get Restore configuration
    api_response = api_instance.get_restore_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi->get_restore_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RestoreConfiguration**](RestoreConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_cluster_restore_start**
> ClusterRestoreStatus initiate_cluster_restore_start(body)

Initiate a restore operation

Start the restore of an NSX cluster, from some previously backed-up configuration. This operation is only valid when a GET cluster/restore/status returns a status with value NOT_STARTED. Otherwise, a 409 response is returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.InitiateClusterRestoreRequest() # InitiateClusterRestoreRequest | 

try:
    # Initiate a restore operation
    api_response = api_instance.initiate_cluster_restore_start(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi->initiate_cluster_restore_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InitiateClusterRestoreRequest**](InitiateClusterRestoreRequest.md)|  | 

### Return type

[**ClusterRestoreStatus**](ClusterRestoreStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_backup_timestamps**
> ClusterBackupInfoListResult list_cluster_backup_timestamps(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List timestamps of all available Cluster Backups.

Returns timestamps for all backup files that are available on the SFTP server. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List timestamps of all available Cluster Backups.
    api_response = api_instance.list_cluster_backup_timestamps(cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi->list_cluster_backup_timestamps: %s\n" % e)
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

[**ClusterBackupInfoListResult**](ClusterBackupInfoListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_restore_instruction_resources**
> ActionableResourceListResult list_restore_instruction_resources(instruction_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

List resources for a given instruction, to be shown to/executed by users. 

For restore operations requiring user input e.g. performing an action, accepting/rejecting an action, etc. the information to be conveyed to users is provided in this call. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi(swagger_client.ApiClient(configuration))
instruction_id = 'instruction_id_example' # str | Id of the instruction set whose instructions are to be returned
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List resources for a given instruction, to be shown to/executed by users. 
    api_response = api_instance.list_restore_instruction_resources(instruction_id, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi->list_restore_instruction_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instruction_id** | **str**| Id of the instruction set whose instructions are to be returned | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ActionableResourceListResult**](ActionableResourceListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_cluster_restore_status**
> ClusterRestoreStatus query_cluster_restore_status(restore_component=restore_component)

Query Restore Request Status

Returns status information for the specified NSX cluster restore request. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi(swagger_client.ApiClient(configuration))
restore_component = 'LOCAL_MANAGER' # str |  (optional) (default to LOCAL_MANAGER)

try:
    # Query Restore Request Status
    api_response = api_instance.query_cluster_restore_status(restore_component=restore_component)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi->query_cluster_restore_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restore_component** | **str**|  | [optional] [default to LOCAL_MANAGER]

### Return type

[**ClusterRestoreStatus**](ClusterRestoreStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_cluster_restore_retry**
> ClusterRestoreStatus retry_cluster_restore_retry()

Retry any failed restore operation

Retry any currently in-progress, failed restore operation. Only the last step of the multi-step restore operation would have failed,and only that step is retried. This operation is only valid when a GET cluster/restore/status returns a status with value FAILED. Otherwise, a 409 response is returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi(swagger_client.ApiClient(configuration))

try:
    # Retry any failed restore operation
    api_response = api_instance.retry_cluster_restore_retry()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi->retry_cluster_restore_retry: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterRestoreStatus**](ClusterRestoreStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_cluster_restore_suspend**
> ClusterRestoreStatus suspend_cluster_restore_suspend()

Suspend any running restore operation

Suspend any currently running restore operation. The restore operation is made up of a number of steps. When this call is issued, any currently running step is allowed to finish (successfully or with errors), and the next step (and therefore the entire restore operation) is suspended until a subsequent resume or cancel call is issued. This operation is only valid when a GET cluster/restore/status returns a status with value RUNNING. Otherwise, a 409 response is returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi(swagger_client.ApiClient(configuration))

try:
    # Suspend any running restore operation
    api_response = api_instance.suspend_cluster_restore_suspend()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementRestoreApi->suspend_cluster_restore_suspend: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterRestoreStatus**](ClusterRestoreStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

