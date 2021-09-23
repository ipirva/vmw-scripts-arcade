# swagger_client.SystemAdministrationSettingsUserManagementUsersApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_user_info**](SystemAdministrationSettingsUserManagementUsersApi.md#get_current_user_info) | **GET** /aaa/user-info | Get the name and role information of the user.

# **get_current_user_info**
> UserInfo get_current_user_info()

Get the name and role information of the user.

This API will return the name and role information of the user invoking this API request. This API is available for all NSX users no matter their authentication method (Local account, VIDM, LDAP etc). The permissions parameter of the NsxRole has been deprecated. 

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementUsersApi(swagger_client.ApiClient(configuration))

try:
    # Get the name and role information of the user.
    api_response = api_instance.get_current_user_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementUsersApi->get_current_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

