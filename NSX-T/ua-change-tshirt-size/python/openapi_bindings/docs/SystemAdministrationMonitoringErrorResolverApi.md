# swagger_client.SystemAdministrationMonitoringErrorResolverApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_error_resolver_info**](SystemAdministrationMonitoringErrorResolverApi.md#get_error_resolver_info) | **GET** /error-resolver/{error_id} | Fetches metadata about the given error_id
[**list_error_resolver_info**](SystemAdministrationMonitoringErrorResolverApi.md#list_error_resolver_info) | **GET** /error-resolver | Fetches a list of metadata for all the registered error resolvers
[**resolve_error_resolve_error**](SystemAdministrationMonitoringErrorResolverApi.md#resolve_error_resolve_error) | **POST** /error-resolver?action&#x3D;resolve_error | Resolves the error

# **get_error_resolver_info**
> ErrorResolverInfo get_error_resolver_info(error_id)

Fetches metadata about the given error_id

Returns some metadata about the given error_id. This includes information of whether there is a resolver present for the given error_id and its associated user input data 

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
api_instance = swagger_client.SystemAdministrationMonitoringErrorResolverApi(swagger_client.ApiClient(configuration))
error_id = 'error_id_example' # str | 

try:
    # Fetches metadata about the given error_id
    api_response = api_instance.get_error_resolver_info(error_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringErrorResolverApi->get_error_resolver_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_id** | **str**|  | 

### Return type

[**ErrorResolverInfo**](ErrorResolverInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_error_resolver_info**
> ErrorResolverInfoList list_error_resolver_info()

Fetches a list of metadata for all the registered error resolvers

Returns a list of metadata for all the error resolvers registered. 

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
api_instance = swagger_client.SystemAdministrationMonitoringErrorResolverApi(swagger_client.ApiClient(configuration))

try:
    # Fetches a list of metadata for all the registered error resolvers
    api_response = api_instance.list_error_resolver_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringErrorResolverApi->list_error_resolver_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ErrorResolverInfoList**](ErrorResolverInfoList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_error_resolve_error**
> resolve_error_resolve_error(body)

Resolves the error

Invokes the corresponding error resolver for the given error(s) present in the payload 

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
api_instance = swagger_client.SystemAdministrationMonitoringErrorResolverApi(swagger_client.ApiClient(configuration))
body = swagger_client.ErrorResolverMetadataList() # ErrorResolverMetadataList | 

try:
    # Resolves the error
    api_instance.resolve_error_resolve_error(body)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringErrorResolverApi->resolve_error_resolve_error: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ErrorResolverMetadataList**](ErrorResolverMetadataList.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

