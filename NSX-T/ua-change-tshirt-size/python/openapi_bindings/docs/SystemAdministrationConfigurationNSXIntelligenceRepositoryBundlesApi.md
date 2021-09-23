# swagger_client.SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_bundle_upload_cancel_upload**](SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi.md#cancel_bundle_upload_cancel_upload) | **POST** /repository/bundles/{bundle-id}?action&#x3D;cancel_upload | Cancel bundle upload
[**get_bundle_ids**](SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi.md#get_bundle_ids) | **GET** /repository/bundles | Get list of bundle-ids which are available in repository or in-progress 
[**get_bundle_upload_permissions**](SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi.md#get_bundle_upload_permissions) | **GET** /repository/bundles/upload-allowed | Checks bundle upload permissions
[**get_bundle_upload_status**](SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi.md#get_bundle_upload_status) | **GET** /repository/bundles/{bundle-id}/upload-status | Get bundle upload status
[**get_ovf_deploy_info**](SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi.md#get_ovf_deploy_info) | **GET** /repository/bundles/ovf-deploy-info | Get information of the OVF which will be getting deployed. 
[**upload_bundle_via_local_file_upload**](SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi.md#upload_bundle_via_local_file_upload) | **POST** /repository/bundles?action&#x3D;upload | Upload bundle
[**upload_bundle_via_remote_file**](SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi.md#upload_bundle_via_remote_file) | **POST** /repository/bundles | Upload bundle using remote file

# **cancel_bundle_upload_cancel_upload**
> cancel_bundle_upload_cancel_upload(bundle_id, product)

Cancel bundle upload

Cancel upload of bundle. This API works only when bundle upload is in-progress and will not work during post-processing of bundle. If bundle upload is in-progress, then the API call returns http OK response after cancelling the upload and deleting partially uploaded bundle. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi(swagger_client.ApiClient(configuration))
bundle_id = 'bundle_id_example' # str | 
product = 'product_example' # str | Name of the product

try:
    # Cancel bundle upload
    api_instance.cancel_bundle_upload_cancel_upload(bundle_id, product)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi->cancel_bundle_upload_cancel_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  | 
 **product** | **str**| Name of the product | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_ids**
> BundleIds get_bundle_ids(file_type, product)

Get list of bundle-ids which are available in repository or in-progress 

Get list of bundle-ids which are available in repository or in-progress 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi(swagger_client.ApiClient(configuration))
file_type = 'file_type_example' # str | Type of file
product = 'product_example' # str | Name of the product

try:
    # Get list of bundle-ids which are available in repository or in-progress 
    api_response = api_instance.get_bundle_ids(file_type, product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi->get_bundle_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_type** | **str**| Type of file | 
 **product** | **str**| Name of the product | 

### Return type

[**BundleIds**](BundleIds.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_upload_permissions**
> BundleUploadPermission get_bundle_upload_permissions(product)

Checks bundle upload permissions

Checks whether bundle upload is allowed on given node for given product. There are different kinds of checks for different products. Some of the checks for Intelligence product are as follows: 1. Is bundle upload-allowed on given node 2. Is bundle upload already in-progress 3. Is Intelliegnce node deployment in-progress 4. Is Intelliegnce node upgrade in-progress 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi(swagger_client.ApiClient(configuration))
product = 'product_example' # str | Name of the product

try:
    # Checks bundle upload permissions
    api_response = api_instance.get_bundle_upload_permissions(product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi->get_bundle_upload_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**| Name of the product | 

### Return type

[**BundleUploadPermission**](BundleUploadPermission.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_upload_status**
> BundleUploadStatus get_bundle_upload_status(bundle_id, product)

Get bundle upload status

Get uploaded bundle upload status

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi(swagger_client.ApiClient(configuration))
bundle_id = 'bundle_id_example' # str | 
product = 'product_example' # str | Name of the product

try:
    # Get bundle upload status
    api_response = api_instance.get_bundle_upload_status(bundle_id, product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi->get_bundle_upload_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | **str**|  | 
 **product** | **str**| Name of the product | 

### Return type

[**BundleUploadStatus**](BundleUploadStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ovf_deploy_info**
> OvfInfo get_ovf_deploy_info(product)

Get information of the OVF which will be getting deployed. 

Get information of the OVF for specified product which is present in repository and will be used to deploy new VM. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi(swagger_client.ApiClient(configuration))
product = 'product_example' # str | Name of the product

try:
    # Get information of the OVF which will be getting deployed. 
    api_response = api_instance.get_ovf_deploy_info(product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi->get_ovf_deploy_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | **str**| Name of the product | 

### Return type

[**OvfInfo**](OvfInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_bundle_via_local_file_upload**
> BundleId upload_bundle_via_local_file_upload(file, file_type, product)

Upload bundle

Upload the bundle. This call returns after upload is completed. You can check bundle processing status periodically by retrieving bundle upload-status to find out if the upload and processing is completed. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi(swagger_client.ApiClient(configuration))
file = 'file_example' # str | 
file_type = 'file_type_example' # str | Type of file
product = 'product_example' # str | Name of the product

try:
    # Upload bundle
    api_response = api_instance.upload_bundle_via_local_file_upload(file, file_type, product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi->upload_bundle_via_local_file_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **file_type** | **str**| Type of file | 
 **product** | **str**| Name of the product | 

### Return type

[**BundleId**](BundleId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_bundle_via_remote_file**
> BundleId upload_bundle_via_remote_file(body, file_type, product)

Upload bundle using remote file

Upload the bundle from remote bundle URL. The call returns after fetch is initiated. Check status by periodically retrieving bundle upload status using GET /repository/bundles/<bundle-id>/upload-status. The upload is complete when the status is SUCCESS. 

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
api_instance = swagger_client.SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RemoteBundleUrl() # RemoteBundleUrl | 
file_type = 'file_type_example' # str | Type of file
product = 'product_example' # str | Name of the product

try:
    # Upload bundle using remote file
    api_response = api_instance.upload_bundle_via_remote_file(body, file_type, product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationNSXIntelligenceRepositoryBundlesApi->upload_bundle_via_remote_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteBundleUrl**](RemoteBundleUrl.md)|  | 
 **file_type** | **str**| Type of file | 
 **product** | **str**| Name of the product | 

### Return type

[**BundleId**](BundleId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

