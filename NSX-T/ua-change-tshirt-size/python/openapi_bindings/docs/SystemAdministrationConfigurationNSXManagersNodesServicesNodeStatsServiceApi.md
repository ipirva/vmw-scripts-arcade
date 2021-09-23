# swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_node_stats_service_action_restart**](SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi.md#create_node_stats_service_action_restart) | **POST** /node/services/node-stats?action&#x3D;restart | Restart, start or stop the NSX node-stats service
[**create_node_stats_service_action_start**](SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi.md#create_node_stats_service_action_start) | **POST** /node/services/node-stats?action&#x3D;start | Restart, start or stop the NSX node-stats service
[**create_node_stats_service_action_stop**](SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi.md#create_node_stats_service_action_stop) | **POST** /node/services/node-stats?action&#x3D;stop | Restart, start or stop the NSX node-stats service
[**read_node_stats_service**](SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi.md#read_node_stats_service) | **GET** /node/services/node-stats | Read NSX node-stats service properties
[**read_node_stats_service_status**](SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi.md#read_node_stats_service_status) | **GET** /node/services/node-stats/status | Read NSX node-stats service status

# **create_node_stats_service_action_restart**
> NodeServiceStatusProperties create_node_stats_service_action_restart()

Restart, start or stop the NSX node-stats service

Restart, start or stop the NSX node-stats service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX node-stats service
    api_response = api_instance.create_node_stats_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi->create_node_stats_service_action_restart: %s\n" % e)
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

# **create_node_stats_service_action_start**
> NodeServiceStatusProperties create_node_stats_service_action_start()

Restart, start or stop the NSX node-stats service

Restart, start or stop the NSX node-stats service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX node-stats service
    api_response = api_instance.create_node_stats_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi->create_node_stats_service_action_start: %s\n" % e)
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

# **create_node_stats_service_action_stop**
> NodeServiceStatusProperties create_node_stats_service_action_stop()

Restart, start or stop the NSX node-stats service

Restart, start or stop the NSX node-stats service

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the NSX node-stats service
    api_response = api_instance.create_node_stats_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi->create_node_stats_service_action_stop: %s\n" % e)
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

# **read_node_stats_service**
> NodeServiceProperties read_node_stats_service()

Read NSX node-stats service properties

Read NSX node-stats service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX node-stats service properties
    api_response = api_instance.read_node_stats_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi->read_node_stats_service: %s\n" % e)
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

# **read_node_stats_service_status**
> NodeServiceStatusProperties read_node_stats_service_status()

Read NSX node-stats service status

Read NSX node-stats service status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi(swagger_client.ApiClient(configuration))

try:
    # Read NSX node-stats service status
    api_response = api_instance.read_node_stats_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXManagersNodesServicesNodeStatsServiceApi->read_node_stats_service_status: %s\n" % e)
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

