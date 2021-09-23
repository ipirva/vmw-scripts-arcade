# swagger_client.SystemAdministrationConfigurationNSXManagersAPIServicesAPIRequestBatchingApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_batch_request**](SystemAdministrationConfigurationNSXManagersAPIServicesAPIRequestBatchingApi.md#register_batch_request) | **POST** /batch | Register a Collection of API Calls at a Single End Point

# **register_batch_request**
> BatchResponse register_batch_request(body, atomic=atomic)

Register a Collection of API Calls at a Single End Point

Enables you to make multiple API requests using a single request. The batch API takes in an array of logical HTTP requests represented as JSON arrays. Each request has a method (GET, PUT, POST, or DELETE), a relative_url (the portion of the URL after https://&lt;nsx-mgr&gt;/api/), optional headers array (corresponding to HTTP headers) and an optional body (for POST and PUT requests). The batch API returns an array of logical HTTP responses represented as JSON arrays. Each response has a status code, an optional headers array and an optional body (which is a JSON-encoded string). 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersAPIServicesAPIRequestBatchingApi(swagger_client.ApiClient(configuration))
body = swagger_client.BatchRequest() # BatchRequest | 
atomic = false # bool | transactional atomicity for the batch of requests embedded in the batch list (optional) (default to false)

try:
    # Register a Collection of API Calls at a Single End Point
    api_response = api_instance.register_batch_request(body, atomic=atomic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersAPIServicesAPIRequestBatchingApi->register_batch_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchRequest**](BatchRequest.md)|  | 
 **atomic** | **bool**| transactional atomicity for the batch of requests embedded in the batch list | [optional] [default to false]

### Return type

[**BatchResponse**](BatchResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

