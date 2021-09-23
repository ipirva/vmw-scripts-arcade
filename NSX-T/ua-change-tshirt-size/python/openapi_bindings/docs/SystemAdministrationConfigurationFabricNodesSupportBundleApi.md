# swagger_client.SystemAdministrationConfigurationFabricNodesSupportBundleApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_node_support_bundle**](SystemAdministrationConfigurationFabricNodesSupportBundleApi.md#read_node_support_bundle) | **GET** /node/support-bundle | Read node support bundle

# **read_node_support_bundle**
> read_node_support_bundle(all=all)

Read node support bundle

Read node support bundle

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesSupportBundleApi(swagger_client.ApiClient(configuration))
all = false # bool | Include all files (optional) (default to false)

try:
    # Read node support bundle
    api_instance.read_node_support_bundle(all=all)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesSupportBundleApi->read_node_support_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| Include all files | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

