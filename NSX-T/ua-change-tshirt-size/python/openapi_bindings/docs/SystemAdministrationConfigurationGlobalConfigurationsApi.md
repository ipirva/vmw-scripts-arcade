# swagger_client.SystemAdministrationConfigurationGlobalConfigurationsApi

All URIs are relative to *https://nsxmanager.your.domain/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_global_configs**](SystemAdministrationConfigurationGlobalConfigurationsApi.md#get_global_configs) | **GET** /global-configs/{config-type} | Get global configs for a config type
[**list_central_node_config_profiles**](SystemAdministrationConfigurationGlobalConfigurationsApi.md#list_central_node_config_profiles) | **GET** /configs/central-config/node-config-profiles/ | List all Central Node Config profiles
[**list_global_configs**](SystemAdministrationConfigurationGlobalConfigurationsApi.md#list_global_configs) | **GET** /global-configs | List global configurations of a NSX domain
[**read_central_node_config_profile**](SystemAdministrationConfigurationGlobalConfigurationsApi.md#read_central_node_config_profile) | **GET** /configs/central-config/node-config-profiles/{profile-id} | Read Central Node Config profile
[**resync_global_configs_resync_config**](SystemAdministrationConfigurationGlobalConfigurationsApi.md#resync_global_configs_resync_config) | **PUT** /global-configs/{config-type}?action&#x3D;resync_config | Resyncs global configurations of a config-type
[**update_central_node_config_profile**](SystemAdministrationConfigurationGlobalConfigurationsApi.md#update_central_node_config_profile) | **PUT** /configs/central-config/node-config-profiles/{node-config-profile-id} | Configure Node Config profile
[**update_global_configs**](SystemAdministrationConfigurationGlobalConfigurationsApi.md#update_global_configs) | **PUT** /global-configs/{config-type} | Update global configurations of a config type

# **get_global_configs**
> GlobalConfigs get_global_configs(config_type)

Get global configs for a config type

Returns global configurations that belong to the config type 

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
api_instance = swagger_client.SystemAdministrationConfigurationGlobalConfigurationsApi(swagger_client.ApiClient(configuration))
config_type = 'config_type_example' # str | 

try:
    # Get global configs for a config type
    api_response = api_instance.get_global_configs(config_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationGlobalConfigurationsApi->get_global_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_type** | **str**|  | 

### Return type

[**GlobalConfigs**](GlobalConfigs.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_central_node_config_profiles**
> CentralNodeConfigProfileListResult list_central_node_config_profiles()

List all Central Node Config profiles

Returns list of all Central Node Config profiles. 

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
api_instance = swagger_client.SystemAdministrationConfigurationGlobalConfigurationsApi(swagger_client.ApiClient(configuration))

try:
    # List all Central Node Config profiles
    api_response = api_instance.list_central_node_config_profiles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationGlobalConfigurationsApi->list_central_node_config_profiles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CentralNodeConfigProfileListResult**](CentralNodeConfigProfileListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_global_configs**
> GlobalConfigsListResult list_global_configs()

List global configurations of a NSX domain

Returns global configurations of a NSX domain grouped by the config types. These global configurations are valid across NSX domain for their respective types unless they are overridden by a more granular configurations. 

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
api_instance = swagger_client.SystemAdministrationConfigurationGlobalConfigurationsApi(swagger_client.ApiClient(configuration))

try:
    # List global configurations of a NSX domain
    api_response = api_instance.list_global_configs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationGlobalConfigurationsApi->list_global_configs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GlobalConfigsListResult**](GlobalConfigsListResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_central_node_config_profile**
> CentralNodeConfigProfile read_central_node_config_profile(profile_id, show_sensitive_data=show_sensitive_data)

Read Central Node Config profile

Returns properties in specified Central Node Config profile. Sensitive data (like SNMP v2c community strings) are included only if query parameter \"show_sensitive_data\" is true. 

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
api_instance = swagger_client.SystemAdministrationConfigurationGlobalConfigurationsApi(swagger_client.ApiClient(configuration))
profile_id = 'profile_id_example' # str | Central Node Config profile id
show_sensitive_data = false # bool | Show sensitive data in Central Node Config profile (optional) (default to false)

try:
    # Read Central Node Config profile
    api_response = api_instance.read_central_node_config_profile(profile_id, show_sensitive_data=show_sensitive_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationGlobalConfigurationsApi->read_central_node_config_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Central Node Config profile id | 
 **show_sensitive_data** | **bool**| Show sensitive data in Central Node Config profile | [optional] [default to false]

### Return type

[**CentralNodeConfigProfile**](CentralNodeConfigProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resync_global_configs_resync_config**
> GlobalConfigs resync_global_configs_resync_config(body, config_type)

Resyncs global configurations of a config-type

It is similar to update global configurations but this request would trigger update even if the configs are unmodified. However, the realization of the new configurations is config-type specific. Refer to config-type specific documentation for details about the configuration push state. 

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
api_instance = swagger_client.SystemAdministrationConfigurationGlobalConfigurationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GlobalConfigs() # GlobalConfigs | 
config_type = 'config_type_example' # str | 

try:
    # Resyncs global configurations of a config-type
    api_response = api_instance.resync_global_configs_resync_config(body, config_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationGlobalConfigurationsApi->resync_global_configs_resync_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GlobalConfigs**](GlobalConfigs.md)|  | 
 **config_type** | **str**|  | 

### Return type

[**GlobalConfigs**](GlobalConfigs.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_central_node_config_profile**
> CentralNodeConfigProfile update_central_node_config_profile(body, node_config_profile_id)

Configure Node Config profile

Updates properties in the specified Central Node Config profile. 

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
api_instance = swagger_client.SystemAdministrationConfigurationGlobalConfigurationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CentralNodeConfigProfile() # CentralNodeConfigProfile | 
node_config_profile_id = 'node_config_profile_id_example' # str | 

try:
    # Configure Node Config profile
    api_response = api_instance.update_central_node_config_profile(body, node_config_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationGlobalConfigurationsApi->update_central_node_config_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CentralNodeConfigProfile**](CentralNodeConfigProfile.md)|  | 
 **node_config_profile_id** | **str**|  | 

### Return type

[**CentralNodeConfigProfile**](CentralNodeConfigProfile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_global_configs**
> GlobalConfigs update_global_configs(body, config_type)

Update global configurations of a config type

Updates global configurations that belong to a config type. The request must include the updated values along with the unmodified values. The values that are updated(different) would trigger update to config-type specific state. However, the realization of the new configurations is config-type specific. Refer to config-type specific documentation for details about the config- uration push state. Policy api will overwrite the fipsGlobalConfig set using MP api. Always use https://<policyIp>/policy/api/v1/infra/global-config to update fips config- uration. 

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
api_instance = swagger_client.SystemAdministrationConfigurationGlobalConfigurationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GlobalConfigs() # GlobalConfigs | 
config_type = 'config_type_example' # str | 

try:
    # Update global configurations of a config type
    api_response = api_instance.update_global_configs(body, config_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemAdministrationConfigurationGlobalConfigurationsApi->update_global_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GlobalConfigs**](GlobalConfigs.md)|  | 
 **config_type** | **str**|  | 

### Return type

[**GlobalConfigs**](GlobalConfigs.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

