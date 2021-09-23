# swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagerConfigurationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node_mode**](SystemAdministrationConfigurationNSXManagersNodesManagerConfigurationApi.md#get_node_mode) | **GET** /node/mode | NodeMode
[**read_central_config_properties**](SystemAdministrationConfigurationNSXManagersNodesManagerConfigurationApi.md#read_central_config_properties) | **GET** /node/central-config | Read Central Config properties
[**update_central_config_properties**](SystemAdministrationConfigurationNSXManagersNodesManagerConfigurationApi.md#update_central_config_properties) | **PUT** /node/central-config | Update Central Config properties

# **get_node_mode**
> NodeMode get_node_mode()

NodeMode

Returns current Node Mode. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagerConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # NodeMode
    api_response = api_instance.get_node_mode()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesManagerConfigurationApi->get_node_mode: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeMode**](NodeMode.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_central_config_properties**
> CentralConfigProperties read_central_config_properties()

Read Central Config properties

Read Central Config properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagerConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Read Central Config properties
    api_response = api_instance.read_central_config_properties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesManagerConfigurationApi->read_central_config_properties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CentralConfigProperties**](CentralConfigProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_central_config_properties**
> CentralConfigProperties update_central_config_properties(body)

Update Central Config properties

Update Central Config properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesManagerConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.CentralConfigProperties() # CentralConfigProperties | 

try:
    # Update Central Config properties
    api_response = api_instance.update_central_config_properties(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesManagerConfigurationApi->update_central_config_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CentralConfigProperties**](CentralConfigProperties.md)|  | 

### Return type

[**CentralConfigProperties**](CentralConfigProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

