# swagger_client.SystemAdministrationSettingsCustomerExperienceImprovementTelemetryApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_telemetry_agreement**](SystemAdministrationSettingsCustomerExperienceImprovementTelemetryApi.md#get_telemetry_agreement) | **GET** /telemetry/agreement | Returns telemetry agreement information
[**get_telemetry_config**](SystemAdministrationSettingsCustomerExperienceImprovementTelemetryApi.md#get_telemetry_config) | **GET** /telemetry/config | Returns the telemetry configuration
[**update_telemetry_agreement**](SystemAdministrationSettingsCustomerExperienceImprovementTelemetryApi.md#update_telemetry_agreement) | **PUT** /telemetry/agreement | Set telemetry agreement information
[**update_telemetry_config**](SystemAdministrationSettingsCustomerExperienceImprovementTelemetryApi.md#update_telemetry_config) | **PUT** /telemetry/config | Creates or updates the telemetry configuration

# **get_telemetry_agreement**
> TelemetryAgreement get_telemetry_agreement()

Returns telemetry agreement information

Returns telemetry agreement information.

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
api_instance = swagger_client.SystemAdministrationSettingsCustomerExperienceImprovementTelemetryApi(swagger_client.ApiClient(configuration))

try:
    # Returns telemetry agreement information
    api_response = api_instance.get_telemetry_agreement()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCustomerExperienceImprovementTelemetryApi->get_telemetry_agreement: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TelemetryAgreement**](TelemetryAgreement.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_telemetry_config**
> TelemetryConfig get_telemetry_config()

Returns the telemetry configuration

Returns the telemetry configuration.

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
api_instance = swagger_client.SystemAdministrationSettingsCustomerExperienceImprovementTelemetryApi(swagger_client.ApiClient(configuration))

try:
    # Returns the telemetry configuration
    api_response = api_instance.get_telemetry_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCustomerExperienceImprovementTelemetryApi->get_telemetry_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TelemetryConfig**](TelemetryConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_telemetry_agreement**
> TelemetryAgreement update_telemetry_agreement(body)

Set telemetry agreement information

Set telemetry agreement information.

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
api_instance = swagger_client.SystemAdministrationSettingsCustomerExperienceImprovementTelemetryApi(swagger_client.ApiClient(configuration))
body = swagger_client.TelemetryAgreement() # TelemetryAgreement | 

try:
    # Set telemetry agreement information
    api_response = api_instance.update_telemetry_agreement(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCustomerExperienceImprovementTelemetryApi->update_telemetry_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TelemetryAgreement**](TelemetryAgreement.md)|  | 

### Return type

[**TelemetryAgreement**](TelemetryAgreement.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_telemetry_config**
> TelemetryConfig update_telemetry_config(body)

Creates or updates the telemetry configuration

Updates or creates the telemetry configuration, and returns the new configuration. 

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
api_instance = swagger_client.SystemAdministrationSettingsCustomerExperienceImprovementTelemetryApi(swagger_client.ApiClient(configuration))
body = swagger_client.TelemetryConfig() # TelemetryConfig | 

try:
    # Creates or updates the telemetry configuration
    api_response = api_instance.update_telemetry_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationSettingsCustomerExperienceImprovementTelemetryApi->update_telemetry_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TelemetryConfig**](TelemetryConfig.md)|  | 

### Return type

[**TelemetryConfig**](TelemetryConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

