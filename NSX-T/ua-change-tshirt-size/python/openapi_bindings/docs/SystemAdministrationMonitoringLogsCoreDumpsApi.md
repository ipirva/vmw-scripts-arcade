# swagger_client.SystemAdministrationMonitoringLogsCoreDumpsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_core_dump_to_remote_file_copy_to_remote_file**](SystemAdministrationMonitoringLogsCoreDumpsApi.md#copy_core_dump_to_remote_file_copy_to_remote_file) | **POST** /node/core-dumps/{file-name}?action&#x3D;copy_to_remote_file | Copy system generated core dump file to a remote file store
[**list_core_dumps**](SystemAdministrationMonitoringLogsCoreDumpsApi.md#list_core_dumps) | **GET** /node/core-dumps | List system core dumps

# **copy_core_dump_to_remote_file_copy_to_remote_file**
> copy_core_dump_to_remote_file_copy_to_remote_file(body, file_name)

Copy system generated core dump file to a remote file store

Copy system generated core dump file to a remote server. If you use scp or sftp, you must provide the remote server's SSH fingerprint. See the <i>NSX-T Administration Guide</i> for information and instructions about finding the SSH fingerprint. 

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
api_instance = swagger_client.SystemAdministrationMonitoringLogsCoreDumpsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CopyToRemoteFileProperties() # CopyToRemoteFileProperties | 
file_name = 'file_name_example' # str | Destination filename

try:
    # Copy system generated core dump file to a remote file store
    api_instance.copy_core_dump_to_remote_file_copy_to_remote_file(body, file_name)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringLogsCoreDumpsApi->copy_core_dump_to_remote_file_copy_to_remote_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyToRemoteFileProperties**](CopyToRemoteFileProperties.md)|  | 
 **file_name** | **str**| Destination filename | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_core_dumps**
> FilePropertiesListResult list_core_dumps()

List system core dumps

List system core dumps

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
api_instance = swagger_client.SystemAdministrationMonitoringLogsCoreDumpsApi(swagger_client.ApiClient(configuration))

try:
    # List system core dumps
    api_response = api_instance.list_core_dumps()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationMonitoringLogsCoreDumpsApi->list_core_dumps: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FilePropertiesListResult**](FilePropertiesListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

