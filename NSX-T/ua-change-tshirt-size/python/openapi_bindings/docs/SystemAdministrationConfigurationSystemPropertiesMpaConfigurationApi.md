# swagger_client.SystemAdministrationConfigurationSystemPropertiesMpaConfigurationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_mpa_configuration**](SystemAdministrationConfigurationSystemPropertiesMpaConfigurationApi.md#delete_mpa_configuration) | **DELETE** /node/mpa-config | Delete MPA configuration for this node
[**read_mpa_configuration**](SystemAdministrationConfigurationSystemPropertiesMpaConfigurationApi.md#read_mpa_configuration) | **GET** /node/mpa-config | Get MPA configuration for this node
[**update_mpa_configuration**](SystemAdministrationConfigurationSystemPropertiesMpaConfigurationApi.md#update_mpa_configuration) | **PUT** /node/mpa-config | Update MPA configuration for this node

# **delete_mpa_configuration**
> delete_mpa_configuration()

Delete MPA configuration for this node

Delete the MPA configuration for this node.

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
api_instance = swagger_client.SystemAdministrationConfigurationSystemPropertiesMpaConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Delete MPA configuration for this node
    api_instance.delete_mpa_configuration()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationSystemPropertiesMpaConfigurationApi->delete_mpa_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_mpa_configuration**
> MPAConfigProperties read_mpa_configuration()

Get MPA configuration for this node

Retrieve the MPA configuration for this node to identify the Manager nodes with which this node is communicating.

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
api_instance = swagger_client.SystemAdministrationConfigurationSystemPropertiesMpaConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Get MPA configuration for this node
    api_response = api_instance.read_mpa_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationSystemPropertiesMpaConfigurationApi->read_mpa_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MPAConfigProperties**](MPAConfigProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mpa_configuration**
> MPAConfigProperties update_mpa_configuration(body)

Update MPA configuration for this node

Update the MPA configuration for this node.

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
api_instance = swagger_client.SystemAdministrationConfigurationSystemPropertiesMpaConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.MPAConfigProperties() # MPAConfigProperties | 

try:
    # Update MPA configuration for this node
    api_response = api_instance.update_mpa_configuration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationSystemPropertiesMpaConfigurationApi->update_mpa_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MPAConfigProperties**](MPAConfigProperties.md)|  | 

### Return type

[**MPAConfigProperties**](MPAConfigProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

