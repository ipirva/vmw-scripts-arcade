# swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_backup_config**](SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi.md#configure_backup_config) | **PUT** /cluster/backups/config | Configure backup
[**get_backup_config**](SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi.md#get_backup_config) | **GET** /cluster/backups/config | Get backup configuration
[**get_backup_history**](SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi.md#get_backup_history) | **GET** /cluster/backups/history | Get backup history
[**get_backup_overview**](SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi.md#get_backup_overview) | **GET** /cluster/backups/overview | Get all backup related information for a site
[**get_backup_status**](SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi.md#get_backup_status) | **GET** /cluster/backups/status | Get backup status
[**get_ssh_fingerprint_of_server_retrieve_ssh_fingerprint**](SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi.md#get_ssh_fingerprint_of_server_retrieve_ssh_fingerprint) | **POST** /cluster/backups?action&#x3D;retrieve_ssh_fingerprint | Get ssh fingerprint of remote(backup) server
[**request_onetime_backup_backup_to_remote**](SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi.md#request_onetime_backup_backup_to_remote) | **POST** /cluster?action&#x3D;backup_to_remote | Request one-time backup
[**request_onetime_inventory_summary_summarize_inventory_to_remote**](SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi.md#request_onetime_inventory_summary_summarize_inventory_to_remote) | **POST** /cluster?action&#x3D;summarize_inventory_to_remote | Request one-time inventory summary.

# **configure_backup_config**
> BackupConfiguration configure_backup_config(body, frame_type=frame_type, site_id=site_id)

Configure backup

Configure file server and timers for automated backup. If secret fields are omitted (password, passphrase) then use the previously set value. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))
body = swagger_client.BackupConfiguration() # BackupConfiguration | 
frame_type = 'LOCAL_LOCAL_MANAGER' # str | Frame type (optional) (default to LOCAL_LOCAL_MANAGER)
site_id = 'localhost' # str | Site ID (optional) (default to localhost)

try:
    # Configure backup
    api_response = api_instance.configure_backup_config(body, frame_type=frame_type, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi->configure_backup_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BackupConfiguration**](BackupConfiguration.md)|  | 
 **frame_type** | **str**| Frame type | [optional] [default to LOCAL_LOCAL_MANAGER]
 **site_id** | **str**| Site ID | [optional] [default to localhost]

### Return type

[**BackupConfiguration**](BackupConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_config**
> BackupConfiguration get_backup_config()

Get backup configuration

Get a configuration of a file server and timers for automated backup. Fields that contain secrets (password, passphrase) are not returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))

try:
    # Get backup configuration
    api_response = api_instance.get_backup_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi->get_backup_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BackupConfiguration**](BackupConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_history**
> BackupOperationHistory get_backup_history()

Get backup history

Get history of previous backup operations 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))

try:
    # Get backup history
    api_response = api_instance.get_backup_history()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi->get_backup_history: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BackupOperationHistory**](BackupOperationHistory.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_overview**
> BackupOverview get_backup_overview(cursor=cursor, frame_type=frame_type, included_fields=included_fields, page_size=page_size, show_backups_list=show_backups_list, site_id=site_id, sort_ascending=sort_ascending, sort_by=sort_by)

Get all backup related information for a site

Get a configuration of a file server, timers for automated backup, latest backup status, backups list for a site. Fields that contain secrets (password, passphrase) are not returned. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
frame_type = 'LOCAL_LOCAL_MANAGER' # str | Frame type (optional) (default to LOCAL_LOCAL_MANAGER)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
show_backups_list = true # bool | Need a list of backups (optional) (default to true)
site_id = 'localhost' # str | UUID of the site (optional) (default to localhost)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get all backup related information for a site
    api_response = api_instance.get_backup_overview(cursor=cursor, frame_type=frame_type, included_fields=included_fields, page_size=page_size, show_backups_list=show_backups_list, site_id=site_id, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi->get_backup_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **frame_type** | **str**| Frame type | [optional] [default to LOCAL_LOCAL_MANAGER]
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **show_backups_list** | **bool**| Need a list of backups | [optional] [default to true]
 **site_id** | **str**| UUID of the site | [optional] [default to localhost]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**BackupOverview**](BackupOverview.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_status**
> CurrentBackupOperationStatus get_backup_status()

Get backup status

Get status of active backup operations 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))

try:
    # Get backup status
    api_response = api_instance.get_backup_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi->get_backup_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentBackupOperationStatus**](CurrentBackupOperationStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssh_fingerprint_of_server_retrieve_ssh_fingerprint**
> RemoteServerFingerprint get_ssh_fingerprint_of_server_retrieve_ssh_fingerprint(body)

Get ssh fingerprint of remote(backup) server

Get SHA256 fingerprint of ECDSA key of remote server. The caller should independently verify that the key is trusted. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))
body = swagger_client.RemoteServerFingerprintRequest() # RemoteServerFingerprintRequest | 

try:
    # Get ssh fingerprint of remote(backup) server
    api_response = api_instance.get_ssh_fingerprint_of_server_retrieve_ssh_fingerprint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi->get_ssh_fingerprint_of_server_retrieve_ssh_fingerprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteServerFingerprintRequest**](RemoteServerFingerprintRequest.md)|  | 

### Return type

[**RemoteServerFingerprint**](RemoteServerFingerprint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_onetime_backup_backup_to_remote**
> request_onetime_backup_backup_to_remote(frame_type=frame_type, site_id=site_id)

Request one-time backup

Request one-time backup. The backup will be uploaded using the same server configuration as for automatic backup. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))
frame_type = 'LOCAL_LOCAL_MANAGER' # str | Frame type (optional) (default to LOCAL_LOCAL_MANAGER)
site_id = 'localhost' # str | Site ID (optional) (default to localhost)

try:
    # Request one-time backup
    api_instance.request_onetime_backup_backup_to_remote(frame_type=frame_type, site_id=site_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi->request_onetime_backup_backup_to_remote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **frame_type** | **str**| Frame type | [optional] [default to LOCAL_LOCAL_MANAGER]
 **site_id** | **str**| Site ID | [optional] [default to localhost]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_onetime_inventory_summary_summarize_inventory_to_remote**
> request_onetime_inventory_summary_summarize_inventory_to_remote()

Request one-time inventory summary.

Request one-time inventory summary. The backup will be uploaded using the same server configuration as for an automatic backup. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi(swagger_client.ApiClient(configuration))

try:
    # Request one-time inventory summary.
    api_instance.request_onetime_inventory_summary_summarize_inventory_to_remote()
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementBackupRestoreManagementBackupApi->request_onetime_inventory_summary_summarize_inventory_to_remote: %s\n" % e)
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

