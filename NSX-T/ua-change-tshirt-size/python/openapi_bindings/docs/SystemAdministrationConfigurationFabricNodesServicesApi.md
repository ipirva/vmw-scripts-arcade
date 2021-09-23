# swagger_client.SystemAdministrationConfigurationFabricNodesServicesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_node_services**](SystemAdministrationConfigurationFabricNodesServicesApi.md#list_node_services) | **GET** /node/services | List node services

# **list_node_services**
> NodeServicePropertiesListResult list_node_services()

List node services

Returns a list of all services available on the node applicance. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesApi(swagger_client.ApiClient(configuration))

try:
    # List node services
    api_response = api_instance.list_node_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesApi->list_node_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServicePropertiesListResult**](NodeServicePropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

