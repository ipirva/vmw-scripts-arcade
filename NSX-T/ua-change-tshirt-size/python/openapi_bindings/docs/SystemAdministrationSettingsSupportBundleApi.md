# swagger_client.SystemAdministrationSettingsSupportBundleApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collect_support_bundles_collect**](SystemAdministrationSettingsSupportBundleApi.md#collect_support_bundles_collect) | **POST** /administration/support-bundles?action&#x3D;collect | Collect support bundles from registered cluster and fabric nodes
[**delete_support_bundles_async_response_delete_async_response**](SystemAdministrationSettingsSupportBundleApi.md#delete_support_bundles_async_response_delete_async_response) | **POST** /administration/support-bundles?action&#x3D;delete_async_response | Delete existing support bundles waiting to be downloaded

# **collect_support_bundles_collect**
> SupportBundleResult collect_support_bundles_collect(body, override_async_response=override_async_response, require_delete_or_override_async_response=require_delete_or_override_async_response)

Collect support bundles from registered cluster and fabric nodes

Collect support bundles from registered cluster and fabric nodes.

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
api_instance = swagger_client.SystemAdministrationSettingsSupportBundleApi(swagger_client.ApiClient(configuration))
body = swagger_client.SupportBundleRequest() # SupportBundleRequest | 
override_async_response = false # bool | Override any existing support bundle async response (optional) (default to false)
require_delete_or_override_async_response = false # bool | Suppress auto-deletion of generated support bundle (optional) (default to false)

try:
    # Collect support bundles from registered cluster and fabric nodes
    api_response = api_instance.collect_support_bundles_collect(body, override_async_response=override_async_response, require_delete_or_override_async_response=require_delete_or_override_async_response)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsSupportBundleApi->collect_support_bundles_collect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupportBundleRequest**](SupportBundleRequest.md)|  | 
 **override_async_response** | **bool**| Override any existing support bundle async response | [optional] [default to false]
 **require_delete_or_override_async_response** | **bool**| Suppress auto-deletion of generated support bundle | [optional] [default to false]

### Return type

[**SupportBundleResult**](SupportBundleResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_support_bundles_async_response_delete_async_response**
> delete_support_bundles_async_response_delete_async_response()

Delete existing support bundles waiting to be downloaded

Delete existing support bundles waiting to be downloaded.

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
api_instance = swagger_client.SystemAdministrationSettingsSupportBundleApi(swagger_client.ApiClient(configuration))

try:
    # Delete existing support bundles waiting to be downloaded
    api_instance.delete_support_bundles_async_response_delete_async_response()
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsSupportBundleApi->delete_support_bundles_async_response_delete_async_response: %s\n" % e)
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

