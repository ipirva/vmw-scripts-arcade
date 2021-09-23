# swagger_client.SystemAdministrationConfigurationFabricNodesServicesSyslogApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_syslog_service_action_restart**](SystemAdministrationConfigurationFabricNodesServicesSyslogApi.md#create_syslog_service_action_restart) | **POST** /node/services/syslog?action&#x3D;restart | Restart, start or stop the syslog service
[**create_syslog_service_action_start**](SystemAdministrationConfigurationFabricNodesServicesSyslogApi.md#create_syslog_service_action_start) | **POST** /node/services/syslog?action&#x3D;start | Restart, start or stop the syslog service
[**create_syslog_service_action_stop**](SystemAdministrationConfigurationFabricNodesServicesSyslogApi.md#create_syslog_service_action_stop) | **POST** /node/services/syslog?action&#x3D;stop | Restart, start or stop the syslog service
[**delete_node_syslog_exporter**](SystemAdministrationConfigurationFabricNodesServicesSyslogApi.md#delete_node_syslog_exporter) | **DELETE** /node/services/syslog/exporters/{exporter-name} | Delete node syslog exporter
[**delete_node_syslog_exporter_all**](SystemAdministrationConfigurationFabricNodesServicesSyslogApi.md#delete_node_syslog_exporter_all) | **DELETE** /node/services/syslog/exporters | Delete all node syslog exporters
[**list_node_syslog_exporters**](SystemAdministrationConfigurationFabricNodesServicesSyslogApi.md#list_node_syslog_exporters) | **GET** /node/services/syslog/exporters | List node syslog exporters
[**post_node_syslog_exporter**](SystemAdministrationConfigurationFabricNodesServicesSyslogApi.md#post_node_syslog_exporter) | **POST** /node/services/syslog/exporters | Add node syslog exporter
[**read_node_syslog_exporter**](SystemAdministrationConfigurationFabricNodesServicesSyslogApi.md#read_node_syslog_exporter) | **GET** /node/services/syslog/exporters/{exporter-name} | Read node syslog exporter
[**read_syslog_service**](SystemAdministrationConfigurationFabricNodesServicesSyslogApi.md#read_syslog_service) | **GET** /node/services/syslog | Read syslog service properties
[**read_syslog_service_status**](SystemAdministrationConfigurationFabricNodesServicesSyslogApi.md#read_syslog_service_status) | **GET** /node/services/syslog/status | Read syslog service status
[**verify_node_syslog_exporter_verify**](SystemAdministrationConfigurationFabricNodesServicesSyslogApi.md#verify_node_syslog_exporter_verify) | **POST** /node/services/syslog/exporters?action&#x3D;verify | Verify node syslog exporter

# **create_syslog_service_action_restart**
> NodeServiceStatusProperties create_syslog_service_action_restart()

Restart, start or stop the syslog service

Restart, start or stop the syslog service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSyslogApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the syslog service
    api_response = api_instance.create_syslog_service_action_restart()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSyslogApi->create_syslog_service_action_restart: %s\n" % e)
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

# **create_syslog_service_action_start**
> NodeServiceStatusProperties create_syslog_service_action_start()

Restart, start or stop the syslog service

Restart, start or stop the syslog service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSyslogApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the syslog service
    api_response = api_instance.create_syslog_service_action_start()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSyslogApi->create_syslog_service_action_start: %s\n" % e)
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

# **create_syslog_service_action_stop**
> NodeServiceStatusProperties create_syslog_service_action_stop()

Restart, start or stop the syslog service

Restart, start or stop the syslog service

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSyslogApi(swagger_client.ApiClient(configuration))

try:
    # Restart, start or stop the syslog service
    api_response = api_instance.create_syslog_service_action_stop()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSyslogApi->create_syslog_service_action_stop: %s\n" % e)
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

# **delete_node_syslog_exporter**
> delete_node_syslog_exporter(exporter_name)

Delete node syslog exporter

Removes a specified rule from the collection of syslog exporter rules. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSyslogApi(swagger_client.ApiClient(configuration))
exporter_name = 'exporter_name_example' # str | Name of syslog exporter to delete

try:
    # Delete node syslog exporter
    api_instance.delete_node_syslog_exporter(exporter_name)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSyslogApi->delete_node_syslog_exporter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exporter_name** | **str**| Name of syslog exporter to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_syslog_exporter_all**
> delete_node_syslog_exporter_all()

Delete all node syslog exporters

Removes all syslog exporter rules. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSyslogApi(swagger_client.ApiClient(configuration))

try:
    # Delete all node syslog exporters
    api_instance.delete_node_syslog_exporter_all()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSyslogApi->delete_node_syslog_exporter_all: %s\n" % e)
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

# **list_node_syslog_exporters**
> NodeSyslogExporterPropertiesListResult list_node_syslog_exporters()

List node syslog exporters

Returns the collection of registered syslog exporter rules, if any. The rules specify the collector IP address and port, and the protocol to use. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSyslogApi(swagger_client.ApiClient(configuration))

try:
    # List node syslog exporters
    api_response = api_instance.list_node_syslog_exporters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSyslogApi->list_node_syslog_exporters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeSyslogExporterPropertiesListResult**](NodeSyslogExporterPropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_node_syslog_exporter**
> NodeSyslogExporterProperties post_node_syslog_exporter(body)

Add node syslog exporter

Adds a rule for exporting syslog information to a specified server. The required parameters are the rule name (exporter_name); severity level (emerg, alert, crit, and so on); transmission protocol (TCP or UDP); and server IP address or hostname. The optional parameters are the syslog port number, which can be 1 through 65,535 (514, by default); facility level to use when logging messages to syslog (kern, user, mail, and so on); and message IDs (msgids), which identify the types of messages to export. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSyslogApi(swagger_client.ApiClient(configuration))
body = swagger_client.NodeSyslogExporterProperties() # NodeSyslogExporterProperties | 

try:
    # Add node syslog exporter
    api_response = api_instance.post_node_syslog_exporter(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSyslogApi->post_node_syslog_exporter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeSyslogExporterProperties**](NodeSyslogExporterProperties.md)|  | 

### Return type

[**NodeSyslogExporterProperties**](NodeSyslogExporterProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_syslog_exporter**
> NodeSyslogExporterProperties read_node_syslog_exporter(exporter_name)

Read node syslog exporter

Returns information about a specific syslog collection point.

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSyslogApi(swagger_client.ApiClient(configuration))
exporter_name = 'exporter_name_example' # str | Name of syslog exporter

try:
    # Read node syslog exporter
    api_response = api_instance.read_node_syslog_exporter(exporter_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSyslogApi->read_node_syslog_exporter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exporter_name** | **str**| Name of syslog exporter | 

### Return type

[**NodeSyslogExporterProperties**](NodeSyslogExporterProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_syslog_service**
> NodeServiceProperties read_syslog_service()

Read syslog service properties

Read syslog service properties

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSyslogApi(swagger_client.ApiClient(configuration))

try:
    # Read syslog service properties
    api_response = api_instance.read_syslog_service()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSyslogApi->read_syslog_service: %s\n" % e)
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

# **read_syslog_service_status**
> NodeServiceStatusProperties read_syslog_service_status()

Read syslog service status

Read syslog service status

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSyslogApi(swagger_client.ApiClient(configuration))

try:
    # Read syslog service status
    api_response = api_instance.read_syslog_service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSyslogApi->read_syslog_service_status: %s\n" % e)
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

# **verify_node_syslog_exporter_verify**
> verify_node_syslog_exporter_verify()

Verify node syslog exporter

Collect iptables rules needed for all existing syslog exporters and verify if the existing iptables rules are the same. If not, remove the stale rules and add the new rules to make sure all exporters work properly. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesServicesSyslogApi(swagger_client.ApiClient(configuration))

try:
    # Verify node syslog exporter
    api_instance.verify_node_syslog_exporter_verify()
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesServicesSyslogApi->verify_node_syslog_exporter_verify: %s\n" % e)
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

