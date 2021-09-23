# swagger_client.SystemAdministrationConfigurationFabricNodesFileStoreApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_from_remote_file_copy_from_remote_file**](SystemAdministrationConfigurationFabricNodesFileStoreApi.md#copy_from_remote_file_copy_from_remote_file) | **POST** /node/file-store/{file-name}?action&#x3D;copy_from_remote_file | Copy a remote file to the file store
[**copy_to_remote_file_copy_to_remote_file**](SystemAdministrationConfigurationFabricNodesFileStoreApi.md#copy_to_remote_file_copy_to_remote_file) | **POST** /node/file-store/{file-name}?action&#x3D;copy_to_remote_file | Copy file in the file store to a remote file store
[**create_file**](SystemAdministrationConfigurationFabricNodesFileStoreApi.md#create_file) | **POST** /node/file-store/{file-name} | Upload a file to the file store
[**create_remote_directory_create_remote_directory**](SystemAdministrationConfigurationFabricNodesFileStoreApi.md#create_remote_directory_create_remote_directory) | **POST** /node/file-store?action&#x3D;create_remote_directory | Create directory in remote file server
[**delete_file**](SystemAdministrationConfigurationFabricNodesFileStoreApi.md#delete_file) | **DELETE** /node/file-store/{file-name} | Delete file
[**list_files**](SystemAdministrationConfigurationFabricNodesFileStoreApi.md#list_files) | **GET** /node/file-store | List node files
[**read_file**](SystemAdministrationConfigurationFabricNodesFileStoreApi.md#read_file) | **GET** /node/file-store/{file-name}/data | Read file contents
[**read_file_properties**](SystemAdministrationConfigurationFabricNodesFileStoreApi.md#read_file_properties) | **GET** /node/file-store/{file-name} | Read file properties
[**read_file_thumbprint**](SystemAdministrationConfigurationFabricNodesFileStoreApi.md#read_file_thumbprint) | **GET** /node/file-store/{file-name}/thumbprint | Read file thumbprint
[**update_file**](SystemAdministrationConfigurationFabricNodesFileStoreApi.md#update_file) | **PUT** /node/file-store/{file-name}/data | Replace file contents

# **copy_from_remote_file_copy_from_remote_file**
> FileProperties copy_from_remote_file_copy_from_remote_file(body, file_name)

Copy a remote file to the file store

Copy a remote file to the file store. If you use scp or sftp, you must provide the remote server's SSH fingerprint. See the <i>NSX-T Administration Guide</i> for information and instructions about finding the SSH fingerprint. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesFileStoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.CopyFromRemoteFileProperties() # CopyFromRemoteFileProperties | 
file_name = 'file_name_example' # str | Destination filename

try:
    # Copy a remote file to the file store
    api_response = api_instance.copy_from_remote_file_copy_from_remote_file(body, file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesFileStoreApi->copy_from_remote_file_copy_from_remote_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyFromRemoteFileProperties**](CopyFromRemoteFileProperties.md)|  | 
 **file_name** | **str**| Destination filename | 

### Return type

[**FileProperties**](FileProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_to_remote_file_copy_to_remote_file**
> copy_to_remote_file_copy_to_remote_file(body, file_name)

Copy file in the file store to a remote file store

Copy a file in the file store to a remote server. If you use scp or sftp, you must provide the remote server's SSH fingerprint. See the <i>NSX-T Administration Guide</i> for information and instructions about finding the SSH fingerprint. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesFileStoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.CopyToRemoteFileProperties() # CopyToRemoteFileProperties | 
file_name = 'file_name_example' # str | Destination filename

try:
    # Copy file in the file store to a remote file store
    api_instance.copy_to_remote_file_copy_to_remote_file(body, file_name)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesFileStoreApi->copy_to_remote_file_copy_to_remote_file: %s\n" % e)
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

# **create_file**
> FileProperties create_file(file_name)

Upload a file to the file store

When you issue this API, the client must specify: - HTTP header Content-Type:application/octet-stream. - Request body with the contents of the file in the filestore. In the CLI, you can view the filestore with the <em>get files</em> command. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesFileStoreApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | Destination filename

try:
    # Upload a file to the file store
    api_response = api_instance.create_file(file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesFileStoreApi->create_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Destination filename | 

### Return type

[**FileProperties**](FileProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_remote_directory_create_remote_directory**
> create_remote_directory_create_remote_directory(body)

Create directory in remote file server

Create a directory on the remote remote server. Supports only SFTP. You must provide the remote server's SSH fingerprint. See the <i>NSX Administration Guide</i> for information and instructions about finding the SSH fingerprint. 

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesFileStoreApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRemoteDirectoryProperties() # CreateRemoteDirectoryProperties | 

try:
    # Create directory in remote file server
    api_instance.create_remote_directory_create_remote_directory(body)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesFileStoreApi->create_remote_directory_create_remote_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRemoteDirectoryProperties**](CreateRemoteDirectoryProperties.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(file_name)

Delete file

Delete file

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesFileStoreApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | Name of the file to delete

try:
    # Delete file
    api_instance.delete_file(file_name)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesFileStoreApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Name of the file to delete | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> FilePropertiesListResult list_files()

List node files

List node files

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesFileStoreApi(swagger_client.ApiClient(configuration))

try:
    # List node files
    api_response = api_instance.list_files()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesFileStoreApi->list_files: %s\n" % e)
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

# **read_file**
> read_file(file_name)

Read file contents

Read file contents

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesFileStoreApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | Name of the file to read

try:
    # Read file contents
    api_instance.read_file(file_name)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesFileStoreApi->read_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Name of the file to read | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_file_properties**
> FileProperties read_file_properties(file_name)

Read file properties

Read file properties

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesFileStoreApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | Name of the file to retrieve information about

try:
    # Read file properties
    api_response = api_instance.read_file_properties(file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesFileStoreApi->read_file_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Name of the file to retrieve information about | 

### Return type

[**FileProperties**](FileProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_file_thumbprint**
> FileThumbprint read_file_thumbprint(file_name)

Read file thumbprint

Read file thumbprint

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesFileStoreApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | Name of the file for which thumbprint should be computed

try:
    # Read file thumbprint
    api_response = api_instance.read_file_thumbprint(file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesFileStoreApi->read_file_thumbprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Name of the file for which thumbprint should be computed | 

### Return type

[**FileThumbprint**](FileThumbprint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file**
> FileProperties update_file(file_name)

Replace file contents

Replace file contents

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
api_instance = swagger_client.SystemAdministrationConfigurationFabricNodesFileStoreApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | Name of the file to replace

try:
    # Replace file contents
    api_response = api_instance.update_file(file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationFabricNodesFileStoreApi->update_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Name of the file to replace | 

### Return type

[**FileProperties**](FileProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

