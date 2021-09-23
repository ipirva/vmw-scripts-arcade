# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_proxy_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi.md#create_proxy_service_action_restart) | **POST** /node/services/http?action&#x3D;restart | Restart the http service
[**create_proxy_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi.md#create_proxy_service_action_start) | **POST** /node/services/http?action&#x3D;start | Start the http service
[**create_proxy_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi.md#create_proxy_service_action_stop) | **POST** /node/services/http?action&#x3D;stop | Stop the http service
[**create_proxy_service_apply_certificate_action_apply_certificate**](SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi.md#create_proxy_service_apply_certificate_action_apply_certificate) | **POST** /node/services/http?action&#x3D;apply_certificate | Update http service certificate
[**read_proxy_service**](SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi.md#read_proxy_service) | **GET** /node/services/http | Read http service properties
[**read_proxy_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi.md#read_proxy_service_status) | **GET** /node/services/http/status | Read http service status
[**update_proxy_service**](SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi.md#update_proxy_service) | **PUT** /node/services/http | Update http service properties

# **create_proxy_service_action_restart**
> create_proxy_service_action_restart()

Restart the http service

Restart the http service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart the http service
    api_instance.create_proxy_service_action_restart()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi->create_proxy_service_action_restart: %s\n" % e)
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

# **create_proxy_service_action_start**
> NodeServiceStatusProperties create_proxy_service_action_start()

Start the http service

Start the http service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi(swagger_client.ApiClient(configuration))

try:
    # Start the http service
    api_response = api_instance.create_proxy_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi->create_proxy_service_action_start: %s\n" % e)
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

# **create_proxy_service_action_stop**
> create_proxy_service_action_stop()

Stop the http service

Stop the http service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi(swagger_client.ApiClient(configuration))

try:
    # Stop the http service
    api_instance.create_proxy_service_action_stop()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi->create_proxy_service_action_stop: %s\n" % e)
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

# **create_proxy_service_apply_certificate_action_apply_certificate**
> create_proxy_service_apply_certificate_action_apply_certificate(certificate_id)

Update http service certificate

Applies a security certificate to the http service. In the POST request, the CERTIFICATE_ID references a certificate created with the /api/v1/trust-management APIs. If the certificate used is a CA signed certificate,the request fails if the whole chain(leaf, intermediate, root) is not imported. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi(swagger_client.ApiClient(configuration))
certificate_id = 'certificate_id_example' # str | Certificate ID

try:
    # Update http service certificate
    api_instance.create_proxy_service_apply_certificate_action_apply_certificate(certificate_id)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi->create_proxy_service_apply_certificate_action_apply_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| Certificate ID | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_proxy_service**
> NodeHttpServiceProperties read_proxy_service()

Read http service properties

This API is deprecated.  Read the configuration of the http service by calling the GET /api/v1/cluster/api-service API. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read http service properties
    api_response = api_instance.read_proxy_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi->read_proxy_service: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeHttpServiceProperties**](NodeHttpServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_proxy_service_status**
> NodeServiceStatusProperties read_proxy_service_status()

Read http service status

Read http service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read http service status
    api_response = api_instance.read_proxy_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi->read_proxy_service_status: %s\n" % e)
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

# **update_proxy_service**
> NodeHttpServiceProperties update_proxy_service(body)

Update http service properties

This API is deprecated.  Make changes to the http service configuration by calling the PUT /api/v1/cluster/api-service API. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeHttpServiceProperties() # NodeHttpServiceProperties | 

try:
    # Update http service properties
    api_response = api_instance.update_proxy_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesHTTPServiceApi->update_proxy_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeHttpServiceProperties**](NodeHttpServiceProperties.md)|  | 

### Return type

[**NodeHttpServiceProperties**](NodeHttpServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

