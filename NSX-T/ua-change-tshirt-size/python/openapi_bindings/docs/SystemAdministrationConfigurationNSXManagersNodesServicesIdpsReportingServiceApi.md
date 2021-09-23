# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_idps_reporting_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi.md#create_idps_reporting_service_action_restart) | **POST** /node/services/idps-reporting?action&#x3D;restart | Restart, start or stop the idps-reporting service
[**create_idps_reporting_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi.md#create_idps_reporting_service_action_start) | **POST** /node/services/idps-reporting?action&#x3D;start | Restart, start or stop the idps-reporting service
[**create_idps_reporting_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi.md#create_idps_reporting_service_action_stop) | **POST** /node/services/idps-reporting?action&#x3D;stop | Restart, start or stop the idps-reporting service
[**read_idps_reporting_service**](SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi.md#read_idps_reporting_service) | **GET** /node/services/idps-reporting | Read the idps-reporting service properties
[**read_idps_reporting_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi.md#read_idps_reporting_service_status) | **GET** /node/services/idps-reporting/status | Read the idps-reporting service status

# **create_idps_reporting_service_action_restart**
> NodeServiceStatusProperties create_idps_reporting_service_action_restart()

Restart, start or stop the idps-reporting service

Restart, start or stop the idps-reporting service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the idps-reporting service
    api_response = api_instance.create_idps_reporting_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi->create_idps_reporting_service_action_restart: %s\n" % e)
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

# **create_idps_reporting_service_action_start**
> NodeServiceStatusProperties create_idps_reporting_service_action_start()

Restart, start or stop the idps-reporting service

Restart, start or stop the idps-reporting service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the idps-reporting service
    api_response = api_instance.create_idps_reporting_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi->create_idps_reporting_service_action_start: %s\n" % e)
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

# **create_idps_reporting_service_action_stop**
> NodeServiceStatusProperties create_idps_reporting_service_action_stop()

Restart, start or stop the idps-reporting service

Restart, start or stop the idps-reporting service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the idps-reporting service
    api_response = api_instance.create_idps_reporting_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi->create_idps_reporting_service_action_stop: %s\n" % e)
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

# **read_idps_reporting_service**
> NodeServiceProperties read_idps_reporting_service()

Read the idps-reporting service properties

Read the idps-reporting service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read the idps-reporting service properties
    api_response = api_instance.read_idps_reporting_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi->read_idps_reporting_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeServiceProperties**](NodeServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_idps_reporting_service_status**
> NodeServiceStatusProperties read_idps_reporting_service_status()

Read the idps-reporting service status

Read the idps-reporting service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read the idps-reporting service status
    api_response = api_instance.read_idps_reporting_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesIdpsReportingServiceApi->read_idps_reporting_service_status: %s\n" % e)
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

