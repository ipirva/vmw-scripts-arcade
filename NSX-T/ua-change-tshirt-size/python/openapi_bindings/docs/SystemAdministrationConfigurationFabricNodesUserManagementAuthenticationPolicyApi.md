# swagger_client.SystemAdministrationConfigurationFabricNodesUserManagementAuthenticationPolicyApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_authentication_policy_properties**](SystemAdministrationConfigurationFabricNodesUserManagementAuthenticationPolicyApi.md#read_authentication_policy_properties) | **GET** /node/aaa/auth-policy | Read node authentication policy configuration
[**update_authentication_policy_properties**](SystemAdministrationConfigurationFabricNodesUserManagementAuthenticationPolicyApi.md#update_authentication_policy_properties) | **PUT** /node/aaa/auth-policy | Update node authentication policy configuration

# **read_authentication_policy_properties**
> AuthenticationPolicyProperties read_authentication_policy_properties()

Read node authentication policy configuration

Returns information about the currently configured authentication policies on the node. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesUserManagementAuthenticationPolicyApi(swagger_client.ApiClient(configuration))

try:
    # Read node authentication policy configuration
    api_response = api_instance.read_authentication_policy_properties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesUserManagementAuthenticationPolicyApi->read_authentication_policy_properties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationPolicyProperties**](AuthenticationPolicyProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authentication_policy_properties**
> AuthenticationPolicyProperties update_authentication_policy_properties(body)

Update node authentication policy configuration

Update the currently configured authentication policy on the node. If any of api_max_auth_failures, api_failed_auth_reset_period, or api_failed_auth_lockout_period are modified, the http service is automatically restarted. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesUserManagementAuthenticationPolicyApi(swagger_client.ApiClient(configuration))
body = swagger_client.AuthenticationPolicyProperties() # AuthenticationPolicyProperties | 

try:
    # Update node authentication policy configuration
    api_response = api_instance.update_authentication_policy_properties(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesUserManagementAuthenticationPolicyApi->update_authentication_policy_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticationPolicyProperties**](AuthenticationPolicyProperties.md)|  | 

### Return type

[**AuthenticationPolicyProperties**](AuthenticationPolicyProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

