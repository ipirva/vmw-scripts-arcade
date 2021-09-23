# swagger_client.SystemAdministrationSettingsProxySettingsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_proxy_config**](SystemAdministrationSettingsProxySettingsApi.md#get_proxy_config) | **GET** /proxy/config | Returns the proxy configuration
[**update_proxy_config**](SystemAdministrationSettingsProxySettingsApi.md#update_proxy_config) | **PUT** /proxy/config | Creates or updates the proxy configuration

# **get_proxy_config**
> Proxy get_proxy_config()

Returns the proxy configuration

Returns the proxy configuration.

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
api_instance = swagger_client.SystemAdministrationSettingsProxySettingsApi(swagger_client.ApiClient(configuration))

try:
    # Returns the proxy configuration
    api_response = api_instance.get_proxy_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsProxySettingsApi->get_proxy_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Proxy**](Proxy.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_proxy_config**
> Proxy update_proxy_config(body)

Creates or updates the proxy configuration

Updates or creates the proxy configuration, and returns the new configuration. 

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
api_instance = swagger_client.SystemAdministrationSettingsProxySettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Proxy() # Proxy | 

try:
    # Creates or updates the proxy configuration
    api_response = api_instance.update_proxy_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsProxySettingsApi->update_proxy_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Proxy**](Proxy.md)|  | 

### Return type

[**Proxy**](Proxy.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

