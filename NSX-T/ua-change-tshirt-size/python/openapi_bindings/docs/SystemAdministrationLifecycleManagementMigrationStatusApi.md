# swagger_client.SystemAdministrationLifecycleManagementMigrationStatusApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_migration_status_summary**](SystemAdministrationLifecycleManagementMigrationStatusApi.md#get_migration_status_summary) | **GET** /migration/status-summary | Get migration status summary
[**get_migration_summary**](SystemAdministrationLifecycleManagementMigrationStatusApi.md#get_migration_summary) | **GET** /migration/summary | Get migration summary

# **get_migration_status_summary**
> MigrationStatus get_migration_status_summary(component_type=component_type)

Get migration status summary

Get migration status summary

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationStatusApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | Component type based on which migration units to be filtered (optional)

try:
    # Get migration status summary
    api_response = api_instance.get_migration_status_summary(component_type=component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationStatusApi->get_migration_status_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| Component type based on which migration units to be filtered | [optional] 

### Return type

[**MigrationStatus**](MigrationStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_summary**
> MigrationSummary get_migration_summary()

Get migration summary

Get migration summary

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationStatusApi(swagger_client.ApiClient(configuration))

try:
    # Get migration summary
    api_response = api_instance.get_migration_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationStatusApi->get_migration_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MigrationSummary**](MigrationSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

