# swagger_client.SystemAdministrationConfigurationNSXManagersManagerModeApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_node_mode**](SystemAdministrationConfigurationNSXManagersManagerModeApi.md#change_node_mode) | **POST** /configs/node/mode | NodeMode

# **change_node_mode**
> NodeMode change_node_mode(body)

NodeMode

Currently only a switch from \"VMC_LOCAL\" to \"VMC\" is supported. Returns a new Node Mode, if the request successfuly changed it. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersManagerModeApi(swagger_client.ApiClient(configuration))
body = swagger_client.SwitchingToVmcModeParameters() # SwitchingToVmcModeParameters | 

try:
    # NodeMode
    api_response = api_instance.change_node_mode(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersManagerModeApi->change_node_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SwitchingToVmcModeParameters**](SwitchingToVmcModeParameters.md)|  | 

### Return type

[**NodeMode**](NodeMode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

