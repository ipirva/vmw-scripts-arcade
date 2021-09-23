# swagger_client.SystemAdministrationConfigurationNSXManagersHardeningMandatoryAccessControlApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node_mandatory_access_control**](SystemAdministrationConfigurationNSXManagersHardeningMandatoryAccessControlApi.md#get_node_mandatory_access_control) | **GET** /node/hardening-policy/mandatory-access-control | Gets the enable status for Mandatory Access Control
[**get_node_mandatory_access_control_report**](SystemAdministrationConfigurationNSXManagersHardeningMandatoryAccessControlApi.md#get_node_mandatory_access_control_report) | **GET** /node/hardening-policy/mandatory-access-control/report | Get the report for Mandatory Access Control
[**set_node_mandatory_access_control**](SystemAdministrationConfigurationNSXManagersHardeningMandatoryAccessControlApi.md#set_node_mandatory_access_control) | **PUT** /node/hardening-policy/mandatory-access-control | Enable or disable  Mandatory Access Control

# **get_node_mandatory_access_control**
> MandatoryAccessControlProperties get_node_mandatory_access_control()

Gets the enable status for Mandatory Access Control

Gets the enable status for Mandatory Access Control

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersHardeningMandatoryAccessControlApi(swagger_client.ApiClient(configuration))

try:
    # Gets the enable status for Mandatory Access Control
    api_response = api_instance.get_node_mandatory_access_control()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersHardeningMandatoryAccessControlApi->get_node_mandatory_access_control: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MandatoryAccessControlProperties**](MandatoryAccessControlProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_mandatory_access_control_report**
> get_node_mandatory_access_control_report()

Get the report for Mandatory Access Control

Get the report for Mandatory Access Control

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersHardeningMandatoryAccessControlApi(swagger_client.ApiClient(configuration))

try:
    # Get the report for Mandatory Access Control
    api_instance.get_node_mandatory_access_control_report()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersHardeningMandatoryAccessControlApi->get_node_mandatory_access_control_report: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_node_mandatory_access_control**
> MandatoryAccessControlProperties set_node_mandatory_access_control(body)

Enable or disable  Mandatory Access Control

Enable or disable  Mandatory Access Control

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersHardeningMandatoryAccessControlApi(swagger_client.ApiClient(configuration))
body = swagger_client.MandatoryAccessControlProperties() # MandatoryAccessControlProperties | 

try:
    # Enable or disable  Mandatory Access Control
    api_response = api_instance.set_node_mandatory_access_control(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersHardeningMandatoryAccessControlApi->set_node_mandatory_access_control: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MandatoryAccessControlProperties**](MandatoryAccessControlProperties.md)|  | 

### Return type

[**MandatoryAccessControlProperties**](MandatoryAccessControlProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

