# swagger_client.SystemAdministrationLifecycleManagementMigrationSetupApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nsxv_setup_details**](SystemAdministrationLifecycleManagementMigrationSetupApi.md#get_nsxv_setup_details) | **GET** /migration/setup | NSX-V setup details
[**update_nsxv_setup_details**](SystemAdministrationLifecycleManagementMigrationSetupApi.md#update_nsxv_setup_details) | **PUT** /migration/setup | NSX-V setup details

# **get_nsxv_setup_details**
> MigrationSetupInfo get_nsxv_setup_details()

NSX-V setup details

Get setup details of NSX-V to be migrated. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationSetupApi(swagger_client.ApiClient(configuration))

try:
    # NSX-V setup details
    api_response = api_instance.get_nsxv_setup_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationSetupApi->get_nsxv_setup_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MigrationSetupInfo**](MigrationSetupInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nsxv_setup_details**
> MigrationSetupInfo update_nsxv_setup_details(body)

NSX-V setup details

Provide setup details of NSX-V to be migrated. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationSetupApi(swagger_client.ApiClient(configuration))
body = swagger_client.MigrationSetupInfo() # MigrationSetupInfo | 

try:
    # NSX-V setup details
    api_response = api_instance.update_nsxv_setup_details(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationSetupApi->update_nsxv_setup_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrationSetupInfo**](MigrationSetupInfo.md)|  | 

### Return type

[**MigrationSetupInfo**](MigrationSetupInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

