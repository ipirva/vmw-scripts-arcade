# swagger_client.SystemAdministrationConfigurationNSXIntelligenceFormFactorsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_intelligence_form_factors**](SystemAdministrationConfigurationNSXIntelligenceFormFactorsApi.md#list_intelligence_form_factors) | **GET** /node/intelligence/form-factors | List available NSX Intelligence appliance form factors

# **list_intelligence_form_factors**
> IntelligenceFormFactors list_intelligence_form_factors()

List available NSX Intelligence appliance form factors

Returns information about all form factors available for intelligence nodes 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceFormFactorsApi(swagger_client.ApiClient(configuration))

try:
    # List available NSX Intelligence appliance form factors
    api_response = api_instance.list_intelligence_form_factors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceFormFactorsApi->list_intelligence_form_factors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IntelligenceFormFactors**](IntelligenceFormFactors.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

