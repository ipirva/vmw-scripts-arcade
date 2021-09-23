# swagger_client.SystemAdministrationConfigurationNSXIntelligenceHostApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pace_host_configuration**](SystemAdministrationConfigurationNSXIntelligenceHostApi.md#get_pace_host_configuration) | **GET** /intelligence/host-config | Get NSX-Intelligence host configuration
[**patch_pace_host_configuration**](SystemAdministrationConfigurationNSXIntelligenceHostApi.md#patch_pace_host_configuration) | **PATCH** /intelligence/host-config | Patch NSX-Intelligence host configuration
[**reset_pace_host_configuration_reset**](SystemAdministrationConfigurationNSXIntelligenceHostApi.md#reset_pace_host_configuration_reset) | **POST** /intelligence/host-config?action&#x3D;reset | Reset NSX-Intelligence host configuration

# **get_pace_host_configuration**
> IntelligenceHostConfigurationInfo get_pace_host_configuration()

Get NSX-Intelligence host configuration

Get the current NSX-Intelligence host configuration. Recommend to keep the value same for flow_data_collection_interval and context_data_collection_interval. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceHostApi(swagger_client.ApiClient(configuration))

try:
    # Get NSX-Intelligence host configuration
    api_response = api_instance.get_pace_host_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceHostApi->get_pace_host_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IntelligenceHostConfigurationInfo**](IntelligenceHostConfigurationInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pace_host_configuration**
> IntelligenceHostConfigurationInfo patch_pace_host_configuration(body)

Patch NSX-Intelligence host configuration

Patch the current NSX-Intelligence host configuration. Return error if NSX-Intelligence is not registered with NSX. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceHostApi(swagger_client.ApiClient(configuration))
body = swagger_client.IntelligenceHostConfigurationInfo() # IntelligenceHostConfigurationInfo | 

try:
    # Patch NSX-Intelligence host configuration
    api_response = api_instance.patch_pace_host_configuration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceHostApi->patch_pace_host_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntelligenceHostConfigurationInfo**](IntelligenceHostConfigurationInfo.md)|  | 

### Return type

[**IntelligenceHostConfigurationInfo**](IntelligenceHostConfigurationInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_pace_host_configuration_reset**
> IntelligenceHostConfigurationInfo reset_pace_host_configuration_reset()

Reset NSX-Intelligence host configuration

Reset NSX-Intelligence host configuration to the default setting. Clear NSX-Intelligence host configuration if NSX-Intelligence is not registered with NSX. Return the NSX-Intelligence host configuration after reset operation. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceHostApi(swagger_client.ApiClient(configuration))

try:
    # Reset NSX-Intelligence host configuration
    api_response = api_instance.reset_pace_host_configuration_reset()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceHostApi->reset_pace_host_configuration_reset: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IntelligenceHostConfigurationInfo**](IntelligenceHostConfigurationInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

