# swagger_client.SystemAdministrationConfigurationNSXManagersManagerConfigurationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_management_config**](SystemAdministrationConfigurationNSXManagersManagerConfigurationApi.md#read_management_config) | **GET** /configs/management | Read NSX Management nodes global configuration.
[**update_management_config**](SystemAdministrationConfigurationNSXManagersManagerConfigurationApi.md#update_management_config) | **PUT** /configs/management | Update NSX Management nodes global configuration

# **read_management_config**
> ManagementConfig read_management_config()

Read NSX Management nodes global configuration.

Returns the NSX Management nodes global configuration. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersManagerConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX Management nodes global configuration.
    api_response = api_instance.read_management_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersManagerConfigurationApi->read_management_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ManagementConfig**](ManagementConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_management_config**
> ManagementConfig update_management_config(body)

Update NSX Management nodes global configuration

Modifies the NSX Management nodes global configuration.

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersManagerConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.ManagementConfig() # ManagementConfig | 

try:
    # Update NSX Management nodes global configuration
    api_response = api_instance.update_management_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersManagerConfigurationApi->update_management_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManagementConfig**](ManagementConfig.md)|  | 

### Return type

[**ManagementConfig**](ManagementConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

