# swagger_client.ManagementPlaneAPISecurityIntrusionServicesIdsProfilesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ids_profile**](ManagementPlaneAPISecurityIntrusionServicesIdsProfilesApi.md#get_ids_profile) | **GET** /intrusion-services/profiles/{ids-profile-id} | Get IDSProfile

# **get_ids_profile**
> IDSProfile get_ids_profile(ids_profile_id)

Get IDSProfile

Returns information about the specified IDSProfile. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityIntrusionServicesIdsProfilesApi(swagger_client.ApiClient(configuration))
ids_profile_id = 'ids_profile_id_example' # str | IDSProfile Id

try:
    # Get IDSProfile
    api_response = api_instance.get_ids_profile(ids_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityIntrusionServicesIdsProfilesApi->get_ids_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids_profile_id** | **str**| IDSProfile Id | 

### Return type

[**IDSProfile**](IDSProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

