# swagger_client.SystemAdministrationConfigurationFabricNodesServicesSNMPApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snmp_service_action_restart**](SystemAdministrationConfigurationFabricNodesServicesSNMPApi.md#create_snmp_service_action_restart) | **POST** /node/services/snmp?action&#x3D;restart | Restart, start or stop the SNMP service
[**create_snmp_service_action_start**](SystemAdministrationConfigurationFabricNodesServicesSNMPApi.md#create_snmp_service_action_start) | **POST** /node/services/snmp?action&#x3D;start | Restart, start or stop the SNMP service
[**create_snmp_service_action_stop**](SystemAdministrationConfigurationFabricNodesServicesSNMPApi.md#create_snmp_service_action_stop) | **POST** /node/services/snmp?action&#x3D;stop | Restart, start or stop the SNMP service
[**read_snmp_service**](SystemAdministrationConfigurationFabricNodesServicesSNMPApi.md#read_snmp_service) | **GET** /node/services/snmp | Read SNMP service properties
[**read_snmp_service_status**](SystemAdministrationConfigurationFabricNodesServicesSNMPApi.md#read_snmp_service_status) | **GET** /node/services/snmp/status | Read SNMP service status
[**read_snmpv3_engine_id**](SystemAdministrationConfigurationFabricNodesServicesSNMPApi.md#read_snmpv3_engine_id) | **GET** /node/services/snmp/v3-engine-id | Read SNMP V3 Engine ID
[**update_snmp_service**](SystemAdministrationConfigurationFabricNodesServicesSNMPApi.md#update_snmp_service) | **PUT** /node/services/snmp | Update SNMP service properties
[**update_snmpv3_engine_id**](SystemAdministrationConfigurationFabricNodesServicesSNMPApi.md#update_snmpv3_engine_id) | **PUT** /node/services/snmp/v3-engine-id | Update SNMP V3 Engine ID

# **create_snmp_service_action_restart**
> NodeServiceStatusProperties create_snmp_service_action_restart()

Restart, start or stop the SNMP service

Restart, start or stop the SNMP service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSNMPApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the SNMP service
    api_response = api_instance.create_snmp_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSNMPApi->create_snmp_service_action_restart: %s\n" % e)
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

# **create_snmp_service_action_start**
> NodeServiceStatusProperties create_snmp_service_action_start()

Restart, start or stop the SNMP service

Restart, start or stop the SNMP service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSNMPApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the SNMP service
    api_response = api_instance.create_snmp_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSNMPApi->create_snmp_service_action_start: %s\n" % e)
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

# **create_snmp_service_action_stop**
> NodeServiceStatusProperties create_snmp_service_action_stop()

Restart, start or stop the SNMP service

Restart, start or stop the SNMP service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSNMPApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the SNMP service
    api_response = api_instance.create_snmp_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSNMPApi->create_snmp_service_action_stop: %s\n" % e)
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

# **read_snmp_service**
> NodeSnmpServiceProperties read_snmp_service(show_sensitive_data=show_sensitive_data)

Read SNMP service properties

Read SNMP service properties.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSNMPApi(swagger_client.ApiClient(configuration))
show_sensitive_data = false # bool | Show SNMP sensitive data or not (optional) (default to false)

try:
    # Read SNMP service properties
    api_response = api_instance.read_snmp_service(show_sensitive_data=show_sensitive_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSNMPApi->read_snmp_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_sensitive_data** | **bool**| Show SNMP sensitive data or not | [optional] [default to false]

### Return type

[**NodeSnmpServiceProperties**](NodeSnmpServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_snmp_service_status**
> NodeServiceStatusProperties read_snmp_service_status()

Read SNMP service status

Read SNMP service status

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSNMPApi(swagger_client.ApiClient(configuration))

try:
    # Read SNMP service status
    api_response = api_instance.read_snmp_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSNMPApi->read_snmp_service_status: %s\n" % e)
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

# **read_snmpv3_engine_id**
> NodeSnmpV3EngineID read_snmpv3_engine_id()

Read SNMP V3 Engine ID

Read SNMP V3 Engine ID

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSNMPApi(swagger_client.ApiClient(configuration))

try:
    # Read SNMP V3 Engine ID
    api_response = api_instance.read_snmpv3_engine_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSNMPApi->read_snmpv3_engine_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSnmpV3EngineID**](NodeSnmpV3EngineID.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snmp_service**
> NodeSnmpServiceProperties update_snmp_service(body)

Update SNMP service properties

Update SNMP service properties.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSNMPApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeSnmpServiceProperties() # NodeSnmpServiceProperties | 

try:
    # Update SNMP service properties
    api_response = api_instance.update_snmp_service(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSNMPApi->update_snmp_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeSnmpServiceProperties**](NodeSnmpServiceProperties.md)|  | 

### Return type

[**NodeSnmpServiceProperties**](NodeSnmpServiceProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snmpv3_engine_id**
> NodeSnmpV3EngineID update_snmpv3_engine_id(body)

Update SNMP V3 Engine ID

Update SNMP V3 Engine ID

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSNMPApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeSnmpV3EngineID() # NodeSnmpV3EngineID | 

try:
    # Update SNMP V3 Engine ID
    api_response = api_instance.update_snmpv3_engine_id(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSNMPApi->update_snmpv3_engine_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeSnmpV3EngineID**](NodeSnmpV3EngineID.md)|  | 

### Return type

[**NodeSnmpV3EngineID**](NodeSnmpV3EngineID.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

