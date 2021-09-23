# swagger_client.SystemAdministrationLifecycleManagementUpgradeHistoryApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_upgrade_history**](SystemAdministrationLifecycleManagementUpgradeHistoryApi.md#get_upgrade_history) | **GET** /upgrade/history | Get upgrade history

# **get_upgrade_history**
> UpgradeHistoryList get_upgrade_history()

Get upgrade history

Get upgrade history

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
api_instance = swagger_client.SystemAdministrationLifecycleManagementUpgradeHistoryApi(swagger_client.ApiClient(configuration))

try:
    # Get upgrade history
    api_response = api_instance.get_upgrade_history()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationLifecycleManagementUpgradeHistoryApi->get_upgrade_history: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UpgradeHistoryList**](UpgradeHistoryList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

