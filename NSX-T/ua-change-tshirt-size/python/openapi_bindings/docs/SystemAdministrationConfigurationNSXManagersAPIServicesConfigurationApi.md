# swagger_client.SystemAdministrationConfigurationNSXManagersAPIServicesConfigurationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_service_config**](SystemAdministrationConfigurationNSXManagersAPIServicesConfigurationApi.md#get_api_service_config) | **GET** /cluster/api-service | Read API service properties
[**update_api_service_config**](SystemAdministrationConfigurationNSXManagersAPIServicesConfigurationApi.md#update_api_service_config) | **PUT** /cluster/api-service | Update API service properties

# **get_api_service_config**
> ApiServiceConfig get_api_service_config()

Read API service properties

Read the configuration of the NSX API service. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersAPIServicesConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Read API service properties
    api_response = api_instance.get_api_service_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersAPIServicesConfigurationApi->get_api_service_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiServiceConfig**](ApiServiceConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_service_config**
> ApiServiceConfig update_api_service_config(body)

Update API service properties

Read the configuration of the NSX API service. Changes are applied to all nodes in the cluster. The API service on each node will restart after it is updated using this API. There may be a delay of up to a minute or so between the time this API call completes and when the new configuration goes into effect.

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersAPIServicesConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiServiceConfig() # ApiServiceConfig | 

try:
    # Update API service properties
    api_response = api_instance.update_api_service_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersAPIServicesConfigurationApi->update_api_service_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiServiceConfig**](ApiServiceConfig.md)|  | 

### Return type

[**ApiServiceConfig**](ApiServiceConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

