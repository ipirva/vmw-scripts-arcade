# swagger_client.ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_appl_proxy_action_restart**](ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi.md#create_appl_proxy_action_restart) | **POST** /node/services/applianceproxy?action&#x3D;restart | Restart, start or stop the Appliance Proxy Service
[**create_appl_proxy_action_start**](ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi.md#create_appl_proxy_action_start) | **POST** /node/services/applianceproxy?action&#x3D;start | Restart, start or stop the Appliance Proxy Service
[**create_appl_proxy_action_stop**](ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi.md#create_appl_proxy_action_stop) | **POST** /node/services/applianceproxy?action&#x3D;stop | Restart, start or stop the Appliance Proxy Service
[**read_appl_proxy**](ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi.md#read_appl_proxy) | **GET** /node/services/applianceproxy | Read the Appliance Proxy service properties
[**read_appl_proxy_status**](ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi.md#read_appl_proxy_status) | **GET** /node/services/applianceproxy/status | Read the Appliance Proxy service status

# **create_appl_proxy_action_restart**
> NodeServiceStatusProperties create_appl_proxy_action_restart()

Restart, start or stop the Appliance Proxy Service

Restart, start or stop the Appliance Proxy Service

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
api_instance = swagger_client.ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the Appliance Proxy Service
    api_response = api_instance.create_appl_proxy_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi->create_appl_proxy_action_restart: %s\n" % e)
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

# **create_appl_proxy_action_start**
> NodeServiceStatusProperties create_appl_proxy_action_start()

Restart, start or stop the Appliance Proxy Service

Restart, start or stop the Appliance Proxy Service

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
api_instance = swagger_client.ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the Appliance Proxy Service
    api_response = api_instance.create_appl_proxy_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi->create_appl_proxy_action_start: %s\n" % e)
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

# **create_appl_proxy_action_stop**
> NodeServiceStatusProperties create_appl_proxy_action_stop()

Restart, start or stop the Appliance Proxy Service

Restart, start or stop the Appliance Proxy Service

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
api_instance = swagger_client.ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the Appliance Proxy Service
    api_response = api_instance.create_appl_proxy_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi->create_appl_proxy_action_stop: %s\n" % e)
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

# **read_appl_proxy**
> NodeServiceProperties read_appl_proxy()

Read the Appliance Proxy service properties

Read the Appliance Proxy service properties

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
api_instance = swagger_client.ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read the Appliance Proxy service properties
    api_response = api_instance.read_appl_proxy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi->read_appl_proxy: %s\n" % e)
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

# **read_appl_proxy_status**
> NodeServiceStatusProperties read_appl_proxy_status()

Read the Appliance Proxy service status

Read the Appliance Proxy service status

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
api_instance = swagger_client.ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi(swagger_client.ApiClient(configuration))

try:
    # Read the Appliance Proxy service status
    api_response = api_instance.read_appl_proxy_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPINSXComponentAdministrationApplianceManagementApi->read_appl_proxy_status: %s\n" % e)
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

