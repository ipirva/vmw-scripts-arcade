# swagger_client.SystemAdministrationConfigurationSystemPropertiesRealizationStateBarrierApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_barrier**](SystemAdministrationConfigurationSystemPropertiesRealizationStateBarrierApi.md#get_current_barrier) | **GET** /realization-state-barrier/current | Gets the current barrier number
[**get_realization_state_barrier_config**](SystemAdministrationConfigurationSystemPropertiesRealizationStateBarrierApi.md#get_realization_state_barrier_config) | **GET** /realization-state-barrier/config | Gets the realization state barrier configuration
[**increment_realization_state_barrier_increment**](SystemAdministrationConfigurationSystemPropertiesRealizationStateBarrierApi.md#increment_realization_state_barrier_increment) | **POST** /realization-state-barrier/current?action&#x3D;increment | Increments the barrier count by 1
[**update_realization_state_barrier_config**](SystemAdministrationConfigurationSystemPropertiesRealizationStateBarrierApi.md#update_realization_state_barrier_config) | **PUT** /realization-state-barrier/config | Updates the barrier configuration

# **get_current_barrier**
> CurrentRealizationStateBarrier get_current_barrier()

Gets the current barrier number

Returns the current global realization barrier number for NSX. This method has been deprecated. To track realization state, use X-NSX-REQUESTID request header instead. 

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
api_instance = swagger_client.SystemAdministrationConfigurationSystemPropertiesRealizationStateBarrierApi(swagger_client.ApiClient(configuration))

try:
    # Gets the current barrier number
    api_response = api_instance.get_current_barrier()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationSystemPropertiesRealizationStateBarrierApi->get_current_barrier: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentRealizationStateBarrier**](CurrentRealizationStateBarrier.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_realization_state_barrier_config**
> RealizationStateBarrierConfig get_realization_state_barrier_config()

Gets the realization state barrier configuration

Returns the current barrier configuration 

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
api_instance = swagger_client.SystemAdministrationConfigurationSystemPropertiesRealizationStateBarrierApi(swagger_client.ApiClient(configuration))

try:
    # Gets the realization state barrier configuration
    api_response = api_instance.get_realization_state_barrier_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationSystemPropertiesRealizationStateBarrierApi->get_realization_state_barrier_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RealizationStateBarrierConfig**](RealizationStateBarrierConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **increment_realization_state_barrier_increment**
> CurrentRealizationStateBarrier increment_realization_state_barrier_increment()

Increments the barrier count by 1

Increment the current barrier number by 1 for NSX. This method has been deprecated. To track realization state, use X-NSX-REQUESTID request header instead. 

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
api_instance = swagger_client.SystemAdministrationConfigurationSystemPropertiesRealizationStateBarrierApi(swagger_client.ApiClient(configuration))

try:
    # Increments the barrier count by 1
    api_response = api_instance.increment_realization_state_barrier_increment()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationSystemPropertiesRealizationStateBarrierApi->increment_realization_state_barrier_increment: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentRealizationStateBarrier**](CurrentRealizationStateBarrier.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_realization_state_barrier_config**
> RealizationStateBarrierConfig update_realization_state_barrier_config(body)

Updates the barrier configuration

Updates the barrier configuration having interval set in milliseconds The new interval that automatically increments the global realization number 

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
api_instance = swagger_client.SystemAdministrationConfigurationSystemPropertiesRealizationStateBarrierApi(swagger_client.ApiClient(configuration))
body = swagger_client.RealizationStateBarrierConfig() # RealizationStateBarrierConfig | 

try:
    # Updates the barrier configuration
    api_response = api_instance.update_realization_state_barrier_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationSystemPropertiesRealizationStateBarrierApi->update_realization_state_barrier_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RealizationStateBarrierConfig**](RealizationStateBarrierConfig.md)|  | 

### Return type

[**RealizationStateBarrierConfig**](RealizationStateBarrierConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

