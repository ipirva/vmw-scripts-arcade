# swagger_client.SystemAdministrationConfigurationFabricNodesLogsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_node_logs**](SystemAdministrationConfigurationFabricNodesLogsApi.md#list_node_logs) | **GET** /node/logs | List available node logs
[**read_node_log**](SystemAdministrationConfigurationFabricNodesLogsApi.md#read_node_log) | **GET** /node/logs/{log-name} | Read node log properties
[**read_node_log_data**](SystemAdministrationConfigurationFabricNodesLogsApi.md#read_node_log_data) | **GET** /node/logs/{log-name}/data | Read node log contents

# **list_node_logs**
> NodeLogPropertiesListResult list_node_logs()

List available node logs

Returns the number of log files and lists the log files that reside on the NSX virtual appliance. The list includes the filename, file size, and last-modified time in milliseconds since epoch (1 January 1970) for each log file. Knowing the last-modified time with millisecond accuracy since epoch is helpful when you are comparing two times, such as the time of a POST request and the end time on a server. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesLogsApi(swagger_client.ApiClient(configuration))

try:
    # List available node logs
    api_response = api_instance.list_node_logs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesLogsApi->list_node_logs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeLogPropertiesListResult**](NodeLogPropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_log**
> NodeLogProperties read_node_log(log_name)

Read node log properties

For a single specified log file, lists the filename, file size, and last-modified time. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesLogsApi(swagger_client.ApiClient(configuration))
log_name = 'log_name_example' # str | Name of log file to read properties

try:
    # Read node log properties
    api_response = api_instance.read_node_log(log_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesLogsApi->read_node_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_name** | **str**| Name of log file to read properties | 

### Return type

[**NodeLogProperties**](NodeLogProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_node_log_data**
> read_node_log_data(log_name)

Read node log contents

For a single specified log file, returns the content of the log file. This method supports byte-range requests. To request just a portion of a log file, supply an HTTP Range header, e.g. \"Range: bytes=<start>-<end>\". <end> is optional, and, if omitted, the file contents from start to the end of the file are returned.' 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesLogsApi(swagger_client.ApiClient(configuration))
log_name = 'log_name_example' # str | Name of log to read

try:
    # Read node log contents
    api_instance.read_node_log_data(log_name)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesLogsApi->read_node_log_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_name** | **str**| Name of log to read | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

