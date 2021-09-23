# swagger_client.ManagementPlaneAPISecurityServiceConfigurationApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_config**](ManagementPlaneAPISecurityServiceConfigurationApi.md#create_service_config) | **POST** /service-configs | Create service config
[**delete_service_config**](ManagementPlaneAPISecurityServiceConfigurationApi.md#delete_service_config) | **DELETE** /service-configs/{config-set-id} | Delete Service Config
[**effective_profiles**](ManagementPlaneAPISecurityServiceConfigurationApi.md#effective_profiles) | **GET** /service-configs/effective-profiles | Get Effective Profiles for an Entity
[**list_service_configs**](ManagementPlaneAPISecurityServiceConfigurationApi.md#list_service_configs) | **GET** /service-configs | List service configs
[**read_service_config**](ManagementPlaneAPISecurityServiceConfigurationApi.md#read_service_config) | **GET** /service-configs/{config-set-id} | Read Service Config
[**service_config_batch_operation**](ManagementPlaneAPISecurityServiceConfigurationApi.md#service_config_batch_operation) | **POST** /service-configs/batch | Creates/Updates service configs sent in batch request
[**update_service_config**](ManagementPlaneAPISecurityServiceConfigurationApi.md#update_service_config) | **PUT** /service-configs/{config-set-id} | Update service config

# **create_service_config**
> ServiceConfig create_service_config(body)

Create service config

Creates a new service config that can group profiles and configs 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServiceConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceConfig() # ServiceConfig | 

try:
    # Create service config
    api_response = api_instance.create_service_config(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServiceConfigurationApi->create_service_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceConfig**](ServiceConfig.md)|  | 

### Return type

[**ServiceConfig**](ServiceConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_config**
> delete_service_config(config_set_id)

Delete Service Config

Deletes the specified service config 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServiceConfigurationApi(swagger_client.ApiClient(configuration))
config_set_id = 'config_set_id_example' # str | service Ccnfig Id

try:
    # Delete Service Config
    api_instance.delete_service_config(config_set_id)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServiceConfigurationApi->delete_service_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_set_id** | **str**| service Ccnfig Id | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **effective_profiles**
> EffectiveProfileListResult effective_profiles(resource_id, resource_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)

Get Effective Profiles for an Entity

Returns the effective profiles applied to the specified Resource. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServiceConfigurationApi(swagger_client.ApiClient(configuration))
resource_id = 'resource_id_example' # str | The resource for which the effective profiles are to be fetched
resource_type = 'resource_type_example' # str | Valid Resource type in effective profiles API
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # Get Effective Profiles for an Entity
    api_response = api_instance.effective_profiles(resource_id, resource_type, cursor=cursor, included_fields=included_fields, page_size=page_size, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServiceConfigurationApi->effective_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The resource for which the effective profiles are to be fetched | 
 **resource_type** | **str**| Valid Resource type in effective profiles API | 
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**EffectiveProfileListResult**](EffectiveProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_configs**
> ServiceConfigListResult list_service_configs(cursor=cursor, included_fields=included_fields, page_size=page_size, profile_type=profile_type, sort_ascending=sort_ascending, sort_by=sort_by)

List service configs

List of all service configs. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServiceConfigurationApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Opaque cursor to be used for getting next page of records (supplied by current result page) (optional)
included_fields = 'included_fields_example' # str | Comma separated list of fields that should be included in query result (optional)
page_size = 1000 # int | Maximum number of results to return in this page (server may return fewer) (optional) (default to 1000)
profile_type = 'profile_type_example' # str | Fetch ServiceConfig for the given attribute profile_type (optional)
sort_ascending = true # bool |  (optional)
sort_by = 'sort_by_example' # str | Field by which records are sorted (optional)

try:
    # List service configs
    api_response = api_instance.list_service_configs(cursor=cursor, included_fields=included_fields, page_size=page_size, profile_type=profile_type, sort_ascending=sort_ascending, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServiceConfigurationApi->list_service_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Opaque cursor to be used for getting next page of records (supplied by current result page) | [optional] 
 **included_fields** | **str**| Comma separated list of fields that should be included in query result | [optional] 
 **page_size** | **int**| Maximum number of results to return in this page (server may return fewer) | [optional] [default to 1000]
 **profile_type** | **str**| Fetch ServiceConfig for the given attribute profile_type | [optional] 
 **sort_ascending** | **bool**|  | [optional] 
 **sort_by** | **str**| Field by which records are sorted | [optional] 

### Return type

[**ServiceConfigListResult**](ServiceConfigListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_service_config**
> ServiceConfig read_service_config(config_set_id)

Read Service Config

Returns information about the specified Service Config. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServiceConfigurationApi(swagger_client.ApiClient(configuration))
config_set_id = 'config_set_id_example' # str | Service Config Id

try:
    # Read Service Config
    api_response = api_instance.read_service_config(config_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServiceConfigurationApi->read_service_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_set_id** | **str**| Service Config Id | 

### Return type

[**ServiceConfig**](ServiceConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_config_batch_operation**
> ServiceConfigListResult service_config_batch_operation(body)

Creates/Updates service configs sent in batch request

Creates/Updates new service configs sent in batch request. This API returns ALL the service configs that are created/updated. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServiceConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceConfigList() # ServiceConfigList | 

try:
    # Creates/Updates service configs sent in batch request
    api_response = api_instance.service_config_batch_operation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServiceConfigurationApi->service_config_batch_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceConfigList**](ServiceConfigList.md)|  | 

### Return type

[**ServiceConfigListResult**](ServiceConfigListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_config**
> ServiceConfig update_service_config(body, config_set_id)

Update service config

Updates the specified ServiceConfig. 

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
api_instance = swagger_client.ManagementPlaneAPISecurityServiceConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.ServiceConfig() # ServiceConfig | 
config_set_id = 'config_set_id_example' # str | service config Id

try:
    # Update service config
    api_response = api_instance.update_service_config(body, config_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementPlaneAPISecurityServiceConfigurationApi->update_service_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceConfig**](ServiceConfig.md)|  | 
 **config_set_id** | **str**| service config Id | 

### Return type

[**ServiceConfig**](ServiceConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

