# swagger_client.SystemAdministrationConfigurationFabricNodesServicesNTPApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ntp_service_action_restart**](SystemAdministrationConfigurationFabricNodesServicesNTPApi.md#create_ntp_service_action_restart) | **POST** /node/services/ntp?action&#x3D;restart | Restart, start or stop the NTP service
[**create_ntp_service_action_start**](SystemAdministrationConfigurationFabricNodesServicesNTPApi.md#create_ntp_service_action_start) | **POST** /node/services/ntp?action&#x3D;start | Restart, start or stop the NTP service
[**create_ntp_service_action_stop**](SystemAdministrationConfigurationFabricNodesServicesNTPApi.md#create_ntp_service_action_stop) | **POST** /node/services/ntp?action&#x3D;stop | Restart, start or stop the NTP service
[**read_ntp_service**](SystemAdministrationConfigurationFabricNodesServicesNTPApi.md#read_ntp_service) | **GET** /node/services/ntp | Read NTP service properties
[**read_ntp_service_status**](SystemAdministrationConfigurationFabricNodesServicesNTPApi.md#read_ntp_service_status) | **GET** /node/services/ntp/status | Read NTP service status
[**update_ntp_service**](SystemAdministrationConfigurationFabricNodesServicesNTPApi.md#update_ntp_service) | **PUT** /node/services/ntp | Update NTP service properties

# **create_ntp_service_action_restart**
> NodeServiceStatusProperties create_ntp_service_action_restart()

Restart, start or stop the NTP service

Restart, start or stop the NTP service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNTPApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NTP service
    api_response = api_instance.create_ntp_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNTPApi->create_ntp_service_action_restart: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ntp_service_action_start**
> NodeServiceStatusProperties create_ntp_service_action_start()

Restart, start or stop the NTP service

Restart, start or stop the NTP service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNTPApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NTP service
    api_response = api_instance.create_ntp_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNTPApi->create_ntp_service_action_start: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ntp_service_action_stop**
> NodeServiceStatusProperties create_ntp_service_action_stop()

Restart, start or stop the NTP service

Restart, start or stop the NTP service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNTPApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NTP service
    api_response = api_instance.create_ntp_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNTPApi->create_ntp_service_action_stop: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ntp_service**
> NodeNtpServiceProperties read_ntp_service()

Read NTP service properties

Read NTP service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNTPApi(swagger_client.ApiClient(configuration))

try:
    # Read NTP service properties
    api_response = api_instance.read_ntp_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNTPApi->read_ntp_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeNtpServiceProperties**](NodeNtpServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ntp_service_status**
> NodeServiceStatusProperties read_ntp_service_status()

Read NTP service status

Read NTP service status

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNTPApi(swagger_client.ApiClient(configuration))

try:
    # Read NTP service status
    api_response = api_instance.read_ntp_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNTPApi->read_ntp_service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceStatusProperties**](NodeServiceStatusProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ntp_service**
> NodeNtpServiceProperties update_ntp_service(body)

Update NTP service properties

Update NTP service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesNTPApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeNtpServiceProperties() # NodeNtpServiceProperties | 

try:
    # Update NTP service properties
    api_response = api_instance.update_ntp_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesNTPApi->update_ntp_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeNtpServiceProperties**](NodeNtpServiceProperties.md)|  | 

### Return type

[**NodeNtpServiceProperties**](NodeNtpServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

