# swagger_client.SystemAdministrationSettingsUserManagementAccessTokenApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_registration_token**](SystemAdministrationSettingsUserManagementAccessTokenApi.md#create_registration_token) | **POST** /aaa/registration-token | Create registration access token
[**delete_registration_token**](SystemAdministrationSettingsUserManagementAccessTokenApi.md#delete_registration_token) | **DELETE** /aaa/registration-token/{token} | Delete registration access token
[**get_registration_token**](SystemAdministrationSettingsUserManagementAccessTokenApi.md#get_registration_token) | **GET** /aaa/registration-token/{token} | Get registration access token

# **create_registration_token**
> RegistrationToken create_registration_token()

Create registration access token

The privileges of the registration token will be the same as the caller.

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementAccessTokenApi(swagger_client.ApiClient(configuration))

try:
    # Create registration access token
    api_response = api_instance.create_registration_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementAccessTokenApi->create_registration_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RegistrationToken**](RegistrationToken.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registration_token**
> delete_registration_token(token)

Delete registration access token

Delete registration access token

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementAccessTokenApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | Registration token

try:
    # Delete registration access token
    api_instance.delete_registration_token(token)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementAccessTokenApi->delete_registration_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Registration token | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_token**
> RegistrationToken get_registration_token(token)

Get registration access token

Get registration access token

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
api_instance = swagger_client.SystemAdministrationSettingsUserManagementAccessTokenApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | Registration token

try:
    # Get registration access token
    api_response = api_instance.get_registration_token(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsUserManagementAccessTokenApi->get_registration_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Registration token | 

### Return type

[**RegistrationToken**](RegistrationToken.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

