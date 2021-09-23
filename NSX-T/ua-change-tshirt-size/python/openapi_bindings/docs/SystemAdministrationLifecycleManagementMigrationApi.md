# swagger_client.SystemAdministrationLifecycleManagementMigrationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finalize_infra_finalize_infra**](SystemAdministrationLifecycleManagementMigrationApi.md#finalize_infra_finalize_infra) | **POST** /migration?action&#x3D;finalize_infra | Perform steps required to finalize the infra.

# **finalize_infra_finalize_infra**
> finalize_infra_finalize_infra()

Perform steps required to finalize the infra.

Perform steps that are required to finalize the infra such as remove the temporary security groups, remove other objects created temporarily for the migration. 

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementMigrationApi(swagger_client.ApiClient(configuration))

try:
    # Perform steps required to finalize the infra.
    api_instance.finalize_infra_finalize_infra()
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementMigrationApi->finalize_infra_finalize_infra: %s\n" % e)
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

