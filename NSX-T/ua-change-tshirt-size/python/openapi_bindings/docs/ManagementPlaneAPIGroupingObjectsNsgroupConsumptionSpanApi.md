# swagger_client.ManagementPlaneAPIGroupingObjectsNsgroupConsumptionSpanApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ns_service**](ManagementPlaneAPIGroupingObjectsNsgroupConsumptionSpanApi.md#create_ns_service) | **POST** /ns-services | Create NSService

# **create_ns_service**
> NSService create_ns_service(body)

Create NSService

Creates a new NSService which allows users to specify characteristics to use for matching network traffic. 

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
api_instance = swagger_client.ManagementPlaneAPIGroupingObjectsNsgroupConsumptionSpanApi(swagger_client.ApiClient(configuration))
body = swagger_client.NSService() # NSService | 

try:
    # Create NSService
    api_response = api_instance.create_ns_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPIGroupingObjectsNsgroupConsumptionSpanApi->create_ns_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NSService**](NSService.md)|  | 

### Return type

[**NSService**](NSService.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

